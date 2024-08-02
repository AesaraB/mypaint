# This file is part of MyPaint.
# Copyright (C) 2024 the MyPaint project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# /src/lib/meson.build


### Run swig

mypaintlib_clib = py.extension_module(
  '_mypaintlib',
  mypaintlib_swig[1],
  dependencies : [python_dep],
  include_directories: [incdir, internal_incdir],
  link_with: [libccan],
  install: true,
  subdir: 'libnvme',
  )


### Swig Flags
# mypaintlib_swig_opts.extend([
#   "-I" + d
#   for d in mypaintlib_opts["include_dirs"]
# ])
