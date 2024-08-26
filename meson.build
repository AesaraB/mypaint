# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# /meson.build

project('MyPaint', 'cpp',
  version : 'v2.1.0',
  default_options : ['warning_level=3', 'cpp_std=c++14'])

# Build machine info
host_os = host_machine.system()
host_cpu_family = host_machine.cpu_family()

# Modules
## Python
py_mod = import('python')
py_deps = ['cairo','gettext','gi','numpy', 'polib']
py = py_mod.find_installation('python3', modules: py_deps)
## Filesystem
fs = import('fs')

# Dependencies
python_dep = py.dependency(embed: true)
## First party dependencies
brushlib_dep = dependency('libmypaint-2.0')
brushes_dep = dependency('mypaint-brushes-2.0')

## Third party dependencies
cairo_dep = dependency('cairo', version: '>=1.4')
lcms2_dep = dependency('lcms2')
libpng_dep = dependency('libpng')
librsvg_dep = dependency('librsvg-2.0')
json_dep = dependency('json-c')
### GTK
gtk_dep = dependency('gtk+-3.0', version: '>=3.12')
glib_dep = dependency('glib-2.0')
gobject_dep = dependency('gobject-2.0')
pygobject_dep = dependency('pygobject-3.0')

## Array of extension deps
dep_list = [brushlib_dep, pygobject_dep, glib_dep, libpng_dep, lcms2_dep, gtk_dep, brushes_dep]
dep_names = []
foreach dep : dep_list
  dep_names += dep.name()
endforeach

# Helper commands
linguas_cmd = find_program('build-aux/meson/get_locales.py', required: true)
numpy_include_cmd = find_program('build-aux/meson/numpy_include.py', required: true)

# Configure
subdir('src') # Configuration and main executable
subdir('src/lib_ext') # Swig
subdir('src/lib_pure') # Python library scripts
subdir('src/gui') # Python GUI scripts
