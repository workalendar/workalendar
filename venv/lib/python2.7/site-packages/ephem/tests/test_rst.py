#!/usr/bin/env python

import doctest
import unittest
import os.path
import sys
import time
from glob import glob

def load_tests(loader, tests, pattern):

    # Force time zone to EST/EDT to make localtime tests work.
    os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
    time.tzset()

    # The different floating-point formatting rules in 2.6 and prior
    # ruin our doctests.

    tests = []

    if sys.version_info >= (2, 7):
        tests.extend([
            doctest.DocFileSuite('../doc/%s' % os.path.basename(path))
            for path in glob(os.path.dirname(__file__) + '/../doc/*.rst')
            if os.path.split(path)[-1] != 'index.rst'
            # skips time-dependent doctest in index.rst
            ])

    return unittest.TestSuite(tests)
