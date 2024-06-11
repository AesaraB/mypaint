# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# /src/meson.build

brushlib_ver = brushlib_dep.version()

conf = configuration_data()
conf.set('mypaint_brushdir', 'brushdir')
conf.set('libmypaint_version', brushlib_ver)
conf.set('libmypaint_locale_dir', 'self.get_libmypaint_locale_dir()')
conf.set('supported_locales', 'locstring')

configure_file(
  input : 'config.py.in',
  output : 'config.py',
  configuration : conf)
