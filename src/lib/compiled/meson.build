# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# /src/lib/compiled/meson.build

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
swig = find_program('swig', required: true)

## Check command version and set python opts accordingly
# Returns: "\nSWIG Version 4.1.1\n\nCompiled with ..."
swig_version_cmd = run_command(swig, ['-version'], check: true)
swig_version = swig_version_cmd.stdout().split('\n')[1].split()[2].strip()
if swig_version.version_compare('<4.1.0')
  swig_cmd = [swig, '-python', '-py3']
else
  swig_cmd = [swig, '-python']
endif

## Other
swig_cmd += ['-Wall', '-c++']
# FIXME: Building against the new shared lib, omit old test code
swig_cmd += ['-DNO_TESTS']

## Extensions
### Numpy
numpy_include = run_command(numpy_include_cmd, check: true).stdout()
swig_cmd += ['-I' + numpy_include]

### Other extensions
pkgconfig_cmd = find_program('pkg-config', required: true)
dep_cflags = run_command(pkgconfig_cmd, dep_names, ['--cflags-only-I'], check: true).stdout()
swig_cmd += dep_cflags

# Run swig
mypaintlib_swig = custom_target(
  'mypaintlib.py',
  input: ['mypaintlib.i'],
  output:  ['mypaintlib.py', 'mypaintlib_wrap.cpp'],
  command: swig_cmd + ['-o', '@OUTPUT1@', '@INPUT0@'],
  install: true,
  install_dir: ['lib/mypaint/lib', false],
  )

# Other configuration
extra_compile_args = [
  '--std=c++11',
  '-Wall',
  '-Wno-sign-compare',
  '-Wno-write-strings',
  '-D_POSIX_C_SOURCE=200809L',
  '-DNO_TESTS',  # FIXME: we're building against shared libmypaint now
  '-g']  # always include symbols, for profiling

## Operating system
if host_os == 'darwin'
  extra_compile_args += ['-D_DARWIN_C_SOURCE']
elif rpath_os.contains(host_os)
  # Look up libraries dependencies relative to the library.
  extra_compile_args += ['-Wl,-z,origin','-Wl,-rpath,$ORIGIN']
endif
