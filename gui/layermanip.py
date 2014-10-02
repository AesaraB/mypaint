# This file is part of MyPaint.
# Copyright (C) 2014 by Andrew Chadwick <a.t.chadwick@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or


"""Modes for moving layers around on the canvas"""

## Imports

import gtk2compat
import gui.mode
import lib.command

import gobject
import gtk
from gtk import gdk
from gettext import gettext as _


## Class defs


class LayerMoveMode (gui.mode.ScrollableModeMixin,
                     gui.mode.DragMode):
    """Moving a layer interactively

    MyPaint is tile-based, and tiles must align between layers.
    Therefore moving layers involves copying data around. This is slow
    for very large layers, so the work is broken into chunks and
    processed in the idle phase of the GUI for greater responsiveness.

    """

    ## API properties and informational methods

    ACTION_NAME = 'LayerMoveMode'

    pointer_behavior = gui.mode.Behavior.CHANGE_VIEW
    scroll_behavior = gui.mode.Behavior.CHANGE_VIEW

    @classmethod
    def get_name(cls):
        return _(u"Move Layer")


    def get_usage(self):
        return _(u"Move the current layer")


    @property
    def active_cursor(self):
        cursor_name = "cursor_hand_closed"
        if not self._move_possible:
            cursor_name = "cursor_forbidden_everywhere"
        return self.doc.app.cursors.get_action_cursor(
            self.ACTION_NAME, cursor_name)

    @property
    def inactive_cursor(self):
        cursor_name = "cursor_hand_open"
        if not self._move_possible:
            cursor_name = "cursor_forbidden_everywhere"
        return self.doc.app.cursors.get_action_cursor(
            self.ACTION_NAME, cursor_name)

    unmodified_persist = True
    permitted_switch_actions = set([
        'RotateViewMode', 'ZoomViewMode', 'PanViewMode',
    ] + gui.mode.BUTTON_BINDING_ACTIONS)


    ## Initialization

    def __init__(self, **kwds):
        super(LayerMoveMode, self).__init__(**kwds)
        self._cmd = None
        self._drag_update_idler_srcid = None
        self.final_modifiers = 0
        self._move_possible = False
        self._drag_tdw = None
        self._drag_model = None


    ## Layer stacking API

    def enter(self, **kwds):
        super(LayerMoveMode, self).enter(**kwds)
        self.final_modifiers = self.initial_modifiers
        rootstack = self.doc.model.layer_stack
        rootstack.current_path_updated += self._update_cursors
        rootstack.layer_properties_changed += self._update_cursors
        self._update_cursors()

    def leave(self, **kwds):
        if self._cmd is not None:
            while self._finalize_move_idler():
                pass
        rootstack = self.doc.model.layer_stack
        rootstack.current_path_updated -= self._update_cursors
        rootstack.layer_properties_changed -= self._update_cursors
        return super(LayerMoveMode, self).leave(**kwds)

    def checkpoint(self, **kwds):
        """Commits any pending work to the command stack"""
        if self._cmd is not None:
            while self._finalize_move_idler():
                pass
        return super(LayerMoveMode, self).checkpoint(**kwds)


    ## Drag-mode API

    def drag_start_cb(self, tdw, event):
        """Drag initialization"""
        if self._cmd is None:
            model = tdw.doc
            layer_path = model.layer_stack.current_path
            x0, y0 = tdw.display_to_model(self.start_x, self.start_y)
            cmd = lib.command.MoveLayer(model, layer_path, x0, y0)
            self._cmd = cmd
            self._drag_tdw = tdw
            self._drag_model = model
        return super(LayerMoveMode, self).drag_start_cb(tdw, event)

    def drag_update_cb(self, tdw, event, dx, dy):
        """UI and model updates during a drag"""
        assert self._cmd is not None
        assert tdw is self._drag_tdw
        x, y = tdw.display_to_model(event.x, event.y)
        self._cmd.move_to(x, y)
        if self._drag_update_idler_srcid is None:
            idler = self._drag_update_idler
            self._drag_update_idler_srcid = gobject.idle_add(idler)

        return super(LayerMoveMode, self).drag_update_cb(tdw, event, dx, dy)

    def _drag_update_idler(self):
        """Processes tile moves in chunks as a background idler"""
        # Might have exited, in which case leave() will have cleaned up
        if self._cmd is None:
            self._drag_update_idler_srcid = None
            return False
        # Terminate if asked. Assume the asker will clean up.
        if self._drag_update_idler_srcid is None:
            return False
        # Process some tile moves, and carry on if there's more to do
        if self._cmd.process_move():
            return True
        self._drag_update_idler_srcid = None
        return False

    def drag_stop_cb(self):
        """UI and model updates at the end of a drag"""
        # Stop the update idler running on its next scheduling
        self._drag_update_idler_srcid = None
        # This will leave a non-cleaned-up move if one is still active,
        # so finalize it in its own idle routine.
        if self._cmd is not None:
            # Arrange for the background work to be done, and look busy
            tdw = self._drag_tdw
            tdw.set_sensitive(False)
            tdw.set_override_cursor(gdk.Cursor(gdk.WATCH))
            self.final_modifiers = self.current_modifiers()
            gobject.idle_add(self._finalize_move_idler)
        else:
            # Still need cleanup for tracking state, cursors etc.
            self._drag_cleanup()
        return super(LayerMoveMode, self).drag_stop_cb()

    def _finalize_move_idler(self):
        """Finalizes everything in chunks once the drag's finished"""
        if self._cmd is None:
            return False  # something else cleaned up
        while self._cmd.process_move():
            return True
        model = self._drag_model
        cmd = self._cmd
        tdw = self._drag_tdw
        self._cmd = None
        self._drag_tdw = None
        self._drag_model = None
        self._update_cursors()
        tdw.set_sensitive(True)
        model.do(cmd)
        self._drag_cleanup()
        return False


    ## Helpers

    def _update_cursors(self, *_ignored):
        """Update the main canvas's cursors based on the model"""
        layer = self.doc.model.layer_stack.current
        self._move_possible = layer.visible and not layer.locked
        self.doc.tdw.set_override_cursor(self.inactive_cursor)

    def _drag_cleanup(self):
        """Final cleanup after any drag is complete"""
        if self._drag_tdw:
            self._update_cursors()  # update may have been deferred
        self._drag_tdw = None
        self._drag_model = None
        self._cmd = None
        if not self.doc:
            return
        if self is self.doc.modes.top:
            if self.initial_modifiers:
                if (self.final_modifiers & self.initial_modifiers) == 0:
                    self.doc.modes.pop()
            else:
                self.doc.modes.pop()

