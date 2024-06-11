# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# /src/meson.build

brushes_dir = brushes_dep.get_pkgconfig_variable('brushesdir')
brushlib_ver = brushlib_dep.name()

conf = configuration_data()
conf.set('brushes_dir', brushes_dir)
conf.set('brushlib_ver', brushlib_ver)
conf.set('libmypaint_locale_dir', 'self.get_libmypaint_locale_dir()')
conf.set('supported_locales', 'locstring')

configure_file(
  input : 'config.py.in',
  output : 'config.py',
  encoding : 'utf-8',
  configuration : conf)
