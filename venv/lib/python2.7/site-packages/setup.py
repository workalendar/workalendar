#!/usr/bin/env python

from distutils.core import setup
import calverter

setup(name = 'pyCalverter',
      version = '1.6.1',
      description = 'Python Calendar Converter',
      author = 'Mehdi Bayazee',
      author_email = 'bayazee@gmail.com',
      url = 'https://bitbucket.org/bayazee/pycalverter/overview',
      package_dir = {},
      packages = [""],
      py_modules = ["calverter"],
      license='GPL v2',
      classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Environment :: Plugins',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Developers',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Software Development :: Localization',
      'Topic :: Utilities',
      ]

     )
