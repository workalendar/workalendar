#!/usr/bin/env python

import setuptools

setuptools.setup(
    requires=[
        'pyluach',
    ]
)

if __name__ == "__main__":
    setuptools.setup(use_scm_version=True)
