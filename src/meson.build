# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# /src/meson.build

# Configure config.py.in
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

## Configure the file
main_config = configuration_data()
main_config.set('brushes_dir', brushes_dir)
main_config.set('brushlib_ver', brushlib_ver)
main_config.set('libmypaint_locale_dir', libmypaint_locale_dir)
main_config.set('supported_locales', supported_locales)

configure_file(
  encoding : 'utf-8',
  input : 'config.py.in',
  output : 'config.py',
  configuration : main_config,
  install_dir : purelibdir + '/lib')

# Configure binaries
python_path = python.path()
rel_bindir = fs.relative_to(bindir, bindir) # This is literally pointless, but it mimics the distutils' behaviour
rel_datadir = fs.relative_to(datadir, bindir)
rel_includedir = fs.relative_to(includedir, bindir)
rel_platlibdir = fs.relative_to(platlibdir, bindir)
rel_purelibdir = fs.relative_to(purelibdir, bindir)

binary_config = configuration_data()
binary_config.set('python_path', '!' + python_path) # prepend the '!' to make the comment a shebang
binary_config.set('os_bindir', rel_bindir)
binary_config.set('os_datadir', rel_datadir)
binary_config.set('os_includedir', rel_includedir)
binary_config.set('platlibdir', rel_platlibdir)
binary_config.set('purelibdir', rel_purelibdir)

# mypaint.py.in
configure_file(
  encoding : 'utf-8',
  input : 'mypaint.py.in',
  output : 'mypaint',
  configuration : binary_config,
  install_dir : bindir,
  install_mode: 'rwxr-xr-x')

# mypaint-ora-thumbnailer.py.in
configure_file(
  encoding : 'utf-8',
  input : 'mypaint-ora-thumbnailer.py.in',
  output : 'mypaint-ora-thumbnailer',
  configuration : binary_config,
  install_dir : bindir,
  install_mode: 'rwxr-xr-x')
