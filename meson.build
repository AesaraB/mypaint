project('MyPaint', 'cpp',
  version : 'v2.1.0',
  default_options : ['warning_level=3', 'cpp_std=c++14'])

fs = import('fs')

install_subdir('src/gui', install_dir : 'mypaint')

# Extensions
#        [
#            'lib/mypaintlib.i',
#            'lib/gdkpixbuf2numpy.cpp',
#            'lib/pixops.cpp',
#            'lib/fastpng.cpp',
#            'lib/brushsettings.cpp',
#            'lib/fill/fill_common.cpp',
#            'lib/fill/fill_constants.cpp',
#            'lib/fill/floodfill.cpp',
#            'lib/fill/gap_closing_fill.cpp',
#            'lib/fill/gap_detection.cpp',
#            'lib/fill/blur.cpp',
#            'lib/fill/morphology.cpp',
#        ],
#        swig_opts=mypaintlib_swig_opts,
#        **mypaintlib_opts

#
#    mypaintlib_swig_opts = ['-Wall', '-noproxydel', '-c++']
#    mypaintlib_swig_opts.extend([
#        "-I" + d
#        for d in mypaintlib_opts["include_dirs"]
#    ])
#    # FIXME: building against the new shared lib, omit old test code
#    mypaintlib_swig_opts.extend(['-DNO_TESTS'])
