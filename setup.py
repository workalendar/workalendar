#!/usr/bin/env python

import setuptools

setuptools.setup(
    requires=[
        'pyluach',
    ],
    tests_require=[
        'pandas',
        'pytest-cov',
        'pytest-flake8',
    ],
)

if __name__ == "__main__":
    setuptools.setup(use_scm_version=True)
