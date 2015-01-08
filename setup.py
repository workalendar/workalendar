#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from os.path import join, dirname, abspath
import sys

import setuptools

PY2 = sys.version_info[0] == 2


def read_relative_file(filename):
    """Returns contents of the given file, whose path is supposed relative
    to this module."""
    path = join(dirname(abspath(__file__)), filename)
    with io.open(path, encoding='utf-8') as f:
        return f.read()

NAME = 'calendra'
DESCRIPTION = 'Worldwide holidays and working days helper and toolkit.'
REQUIREMENTS = [
    'python-dateutil',
    'lunardate',
    'pytz',
    'pyCalverter',
]

if PY2:
    REQUIREMENTS.append('pyephem')
else:
    REQUIREMENTS.append('ephem')

params = dict(
    name=NAME,
    description=DESCRIPTION,
    packages=['calendra'],
    use_vcs_version=True,
    long_description=read_relative_file('README.rst'),
    author='Jason R. Coombs',
    author_email='jaraco@jaraco.com',
    url='https://github.com/jaraco/calendra',
    license='MIT License',
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    setup_requires=[
        'hgtools>=5',
        'pytest-runner>=2.2.1',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-pep8',
    ],
)

if __name__ == '__main__':
    setuptools.setup(**params)
