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
system_os = host_machine.system()

# Modules
## Python
py_mod = import('python')
py_deps = ['cairo','gettext','gi','numpy']
py = py_mod.find_installation('python3', modules: py_deps)

# Dependencies
python_dep = py.dependency()
## First party dependencies
brushlib_dep = dependency('libmypaint-2.0')
brushes_dep = dependency('mypaint-brushes-2.0')

## Third party dependencies
cairo_dep = dependency('cairo', version: '>=1.4')
lcms2_dep = dependency('lcms2')
libpng_dep = dependency('libpng')
json_dep = dependency('json-c')
### GTK
gtk_dep = dependency('gtk+-3.0', version: '>=3.12')
glib_dep = dependency('glib-2.0')
gobject_dep = dependency('gobject-2.0')
pygobject_dep = dependency('pygobject-3.0')

# Build
subdir('src') # config.py.in
#subdir('src/lib') # Swig
## Extensions

## Options
# swig_opts=mypaintlib_swig_opts,
# **mypaintlib_opts

# Install
#install_subdir('src/gui', install_dir : 'mypaint')
