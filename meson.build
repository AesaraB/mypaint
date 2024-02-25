project('MyPaint', 'cpp',
  version : 'v2.1.0',
  default_options : ['warning_level=3', 'cpp_std=c++14'])

# Dependencies
## First party dependencies
brushlib_dep = dependency('libmypaint-2.0')
brush_dep = dependency('mypaint-brushes-2.0')

## Third party dependencies
python_dep = dependency('python3', version : '>=2.7.4')

### GTK
gtk_dep = dependency('gtk+-3.0', version: '>=3.12')
gobject_dep = dependency('gobject-2.0')
pygobject_dep = dependency('pygobject-3.0')
glib_dep = dependency('glib-2.0')

## Other
libpng_dep = dependency('libpng')
lcms2_dep = dependency('lcms2')
cairo_dep = dependency('cairo', version: '>=1.4')
json_dep = dependency('json-c')

# Install
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
