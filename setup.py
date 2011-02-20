#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
    have_Cython = True
except ImportError:
    print "Warning: Cython could not be imported.  Will use slower version."
    have_Cython = False

if have_Cython:
    Cython_args = {
        "cmdclass" : {'build_ext': build_ext},
        "ext_modules" : [Extension("pacal.bary_interp", ["pacal/bary_interp.pyx"])],
        #"ext_modules" : [Extension("pacal.bary_interp", ["pacal/bary_interp.pyx"], include_dirs=["c:/Python27/Lib/site-packages/numpy/core/include/"])],
        }
else:
    Cython_args = {}
    
setup(
    name='PaCal',
    version='0.99',
    description ='PaCal - ProbAbilistic CALculator',
    author='Szymon Jaroszewicz, Marcin Korzen',
    author_email='s.jaroszewicz@itl.waw.pl, mkorzen@wi.zut.edu.pl',
    license='GNU General Public License V.3 or later',
    url='http://pacal.sf.net',
    long_description=open('README.txt').read(),
    requires=['Python (>=2.6,<3.0)', 'numpy (>=1.3)', 'matplotlib (>=0.99)', 'Cython'],

    packages=['pacal', 'pacal.examples', 'pacal.examples.springer_book'],
    **Cython_args
)
