from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name='frccontrol',
	  ext_modules=[
    Extension('frccontrol',
              sources=['frccontrol/ctrlutil.pyx', 'frccontrol/kalmd.pyx', 'frccontrol/lqr.pyx', 'frccontrol/models.pyx', 'frccontrol/profiles.pyx', 'frccontrol/system.pyx'],
              # extra_compile_args=['-c -o'],
              language='c++')
    ],
	cmdclass = {'build_ext': build_ext})
