#!/usr/bin/env python
#-*- coding: utf-8 -*-
from os.path import join, dirname, abspath
import sys

PY2 = sys.version_info[0] == 2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA


def read_relative_file(filename):
    """Returns contents of the given file, whose path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()

NAME = 'workalendar'
DESCRIPTION = 'Worldwide holidays and working days helper and toolkit.'
REQUIREMENTS = [
    'python-dateutil',
    'lunardate',
    'pytz',
    'pyCalverter',
]
__VERSION__ = '0.3-dev'

if PY2:
    REQUIREMENTS.append('pyephem')
else:
    REQUIREMENTS.append('ephem')

params = dict(
    name=NAME,
    description=DESCRIPTION,
    packages=['workalendar'],
    version=__VERSION__,
    long_description=read_relative_file('README.rst'),
    author='Bruno Bord',
    author_email='bruno.bord@novapost.fr',
    url='https://github.com/novapost/workalendar',
    license='MIT License',
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)

if __name__ == '__main__':
    setup(**params)
