# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# /src/lib/compiled/meson.build

# Basic declarations
swig = find_program('swig', required: true)
pkgconfig = find_program('pkg-config', required: true)
numpy_include = '-I' + run_command(numpy_include_cmd, check: true).stdout().strip()

# Platform stuff
opt_set_rpath = get_option('set_rpath')
rpath_os = ['linux', 'freebsd', 'netbsd', 'openbsd']

if opt_set_rpath
  if (rpath_os.contains(host_os))
    error('Testing') #TODO
  else
    error('Option set_rpath is active but host machine not linux/bsd')
  endif
  # The directories in runtime_library_dirs will be added to the linker
  # args as '-Wl,-R{dirs}' This _should_ be compatible with the --rpath=
  # build_ext option
  #for ext in self.extensions:
      #rt_libs = uniq(ext.library_dirs + ext.runtime_library_dirs)
      # Retain original list reference, just in case
      #ext.runtime_library_dirs[:] = rt_libs
endif

# swig configuration

## Check command version and set python opts accordingly
# Returns: "\nSWIG Version 4.1.1\n\nCompiled with ..."
swig_version_cmd = run_command(swig, ['-version'], check: true)
swig_version = swig_version_cmd.stdout().split('\n')[1].split()[2].strip()
if swig_version.version_compare('<4.1.0')
  mypaintlib_swig_args = [swig, '-python', '-py3']
else
  mypaintlib_swig_args = [swig, '-python']
endif

## Other
mypaintlib_swig_args += ['-Wall', '-c++']
mypaintlib_swig_args += ['-DNO_TESTS'] # FIXME: Building against the new shared lib, omit old test code

## Extensions
mypaintlib_swig_args += [numpy_include]
dep_cflags = run_command(pkgconfig, dep_names, ['--cflags-only-I'], check: true).stdout().strip().split()
mypaintlib_swig_args += dep_cflags

# Run swig
mypaintlib_swig = custom_target(
  'mypaintlib.py',
  input: ['mypaintlib.i'],
  output:  ['mypaintlib.py', 'mypaintlib_wrap.cpp'],
  command: [mypaintlib_swig_args, '-o', '@OUTPUT1@', '@INPUT0@'],
  install: true,
  install_dir: ['lib/mypaint/lib', false],
  )

# Shared library configuration
mypaintlib_compile_args = [
  numpy_include,
  '--std=c++11',
  '-Wall',
  '-Wno-sign-compare',
  '-Wno-write-strings',
  '-D_POSIX_C_SOURCE=200809L',
  '-DNO_TESTS',  # FIXME: we're building against shared libmypaint now
  '-g']  # always include symbols, for profiling
mypaintlib_link_args = []

## Operating system
if host_os == 'darwin'
  mypaintlib_compile_args += ['-D_DARWIN_C_SOURCE']
endif

mypaintlib_sources = [
  mypaintlib_swig[1],
  'gdkpixbuf2numpy.cpp',
  'pixops.cpp',
  'fastpng.cpp',
  'brushsettings.cpp',
  'fill/fill_common.cpp',
  'fill/fill_constants.cpp',
  'fill/floodfill.cpp',
  'fill/gap_closing_fill.cpp',
  'fill/gap_detection.cpp',
  'fill/blur.cpp',
  'fill/morphology.cpp']

# Build shared library
shared_library('_mypaintlib',
  sources: mypaintlib_sources,
  cpp_args: mypaintlib_compile_args,
  link_args: mypaintlib_link_args,
  dependencies: [dep_list, python_dep],
  link_depends: mypaintlib_swig,
  install: true,
  install_dir: 'lib/mypaint/lib')
