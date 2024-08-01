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
librsvg_dep = dependency('librsvg-2.0')
json_dep = dependency('json-c')
### GTK
gtk_dep = dependency('gtk+-3.0', version: '>=3.12')
glib_dep = dependency('glib-2.0')
gobject_dep = dependency('gobject-2.0')
pygobject_dep = dependency('pygobject-3.0')

# Configure config.py
brushes_dir = brushes_dep.get_pkgconfig_variable('brushesdir')
brushlib_ver = brushlib_dep.name()

conf = configuration_data()
conf.set('brushes_dir', brushes_dir)
conf.set('brushlib_ver', brushlib_ver)
conf.set('libmypaint_locale_dir', 'self.get_libmypaint_locale_dir()')
conf.set('supported_locales', 'locstring')

configure_file(
  encoding : 'utf-8',
  input : 'src/config.py.in',
  output : 'config.py',
  install_dir : 'lib/mypaint/lib',
  configuration : conf)

# Setup python
install_subdir('src/gui', install_dir : 'lib/mypaint/gui', strip_directory : true)
install_subdir('src/lib/python', install_dir : 'lib/mypaint/lib', strip_directory : true)

# Build
#subdir('src/lib') # Swig
## Extensions

## Options
# swig_opts=mypaintlib_swig_opts,
# **mypaintlib_opts

# Install
#install_subdir('src/gui', install_dir : 'mypaint')
