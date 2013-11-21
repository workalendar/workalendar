#!/usr/bin/env python
#-*- coding: utf-8 -*-
from os.path import join, dirname, abspath

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA


def read_relative_file(filename):
    """Returns contents of the given file, whose path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()

if __name__ == '__main__':
    setup(
        name='workalendar',
        packages=['workalendar'],
        version='0.0.1',
        description='Worldwide holidays and workdays computational toolkit.',
        long_description=read_relative_file('README.rst'),
        author='Bruno Bord',
        author_email='bruno.bord@novapost.fr',
        url='https://github.com/novapost/workalendar',
        license='MIT License',
        include_package_data=True,
        install_requires=['python-dateutil'],
        zip_safe=False,
        classifiers=(
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
        )
    )
