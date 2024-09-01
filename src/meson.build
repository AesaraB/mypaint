# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later
# version.

# /src/meson.build

# Configure config.py
brushlib_ver = brushlib_dep.name()

## brushes_dir
opt_brushes_dir = get_option('brushes_dir')
if opt_brushes_dir != ''
  brushes_dir = opt_brushes_dir
  if not fs.is_dir(brushes_dir)
    error('Supplied brushes_dir does not exist!')
  endif
  if fs.is_absolute(brushes_dir)
    warning('Supplied brush directory path is not relative')
  endif
else
  brushes_dir = brushes_dep.get_pkgconfig_variable('brushesdir')
endif

## libmypaint_locale_dir
opt_libmypaint_locale_dir = get_option('libmypaint_locale_dir')
opt_libmypaint_locale_pkgconfig = get_option('libmypaint_locale_pkgconfig')
brushlib_prefix = brushlib_dep.get_pkgconfig_variable('prefix')

if (not opt_libmypaint_locale_pkgconfig) and (opt_libmypaint_locale_dir == '')
  libmypaint_locale_dir = 'None'
elif opt_libmypaint_locale_pkgconfig and (opt_libmypaint_locale_dir != '')
  error('Both libmypaint_locale_dir and libmypaint_locale_pkgconfig active, use only one of these.')
elif opt_libmypaint_locale_pkgconfig
  libmypaint_locale_dir = brushlib_prefix + '/share/locale'
  if not fs.is_dir(libmypaint_locale_dir)
    error('pkg-config provides non-extant libmypaint locale dir!')
  endif
  libmypaint_locale_dir = '\'' + libmypaint_locale_dir + '\''
else
  if not fs.is_dir(opt_libmypaint_locale_dir)
    error('Supplied libmypaint_locale_dir does not exist!')
  endif
  libmypaint_locale_dir = '\'' + opt_libmypaint_locale_dir + '\''
endif

## Supported locales
opt_translation_threshold = get_option('translation_threshold').to_string()
supported_locales = run_command(linguas_cmd, ['../data/po/', opt_translation_threshold], check: true).stdout().strip()

# Configure the file
conf = configuration_data()
conf.set('brushes_dir', brushes_dir)
conf.set('brushlib_ver', brushlib_ver)
conf.set('libmypaint_locale_dir', libmypaint_locale_dir)
conf.set('supported_locales', supported_locales)

configure_file(
  encoding : 'utf-8',
  input : 'config.py.in',
  output : 'config.py',
  install_dir : purelibdir + '/lib',
  configuration : conf)
