from distutils.core import setup
from Cython.Build import cythonize

setup(name='frccontrol',
      ext_modules=cythonize("frccontrol/*.pyx"),
	  language='c++')
