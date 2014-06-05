#!/usr/bin/env python

import unittest, time
from datetime import datetime

from ephem import Date, localtime

# Determine whether dates behave reasonably.

class DateTests(unittest.TestCase):
    def setUp(self):
        self.date = Date('2004/09/04 00:17:15.8')

    def test_date_constructor(self):

        def construct_and_compare(args1, args2):
            d1, d2 = Date(*args1), Date(*args2)
            self.assert_(-1e-15 < (d1 / d2 - 1) < 1e-15,
                         'dates not equal:\n %r = date%r\n %r = date%r'
                         % (d1.tuple(), args1, d2.tuple(), args2))

        std = ('2004/09/04 00:17:15.8',)
        pairs = [
            [std, ('2004.67489614324023472',)],
            [std, ('   2004.67489614324023472 ',)],
            [std, ('2004/9/4.0119884259259257',)],
            [std, (' 2004/9/4.0119884259259257  ',)],
            [std, ('2004/9/4 0.28772222222222221',)],
            [std, (' 2004/9/4 0.28772222222222221 ',)],
            [std, ('2004/9/4 0:17.263333333333332',)],
            [std, ('    2004/9/4 0:17.263333333333332  ',)],
            [std, ('2004/9/4 0:17:15.8',)],
            [std, ('  2004/9/4 0:17:15.8 ',)],
            [std, ('  2004-9-4 0:17:15.8 ',)],
            [('2004',), ((2004,),)],
            [('  2004 ',), ((2004,),)],
            [('2004/09',), ((2004, 9),)],
            [(' 2004/09  ',), ((2004, 9),)],
            [std, ((2004, 9, 4.0119884259259257),)],
            [std, ((2004, 9, 4, 0.28772222222222221),)],
            [std, ((2004, 9, 4, 0, 17.263333333333332),)],
            [std, ((2004, 9, 4, 0, 17, 15.8),)],
            [std, (datetime(2004, 9, 4, 0, 17, 15, 800000),)],
            ]
        for args1, args2 in pairs:
            construct_and_compare(args1, args2)
            if len(args2) == 1 and type(args2[0]) is str:
                construct_and_compare(args1, ( '  %s  ' % args2[0] ,))

    def test_date_string_value(self):
        self.assertEqual(str(self.date), '2004/9/4 00:17:15')

    def test_date_triple_value(self):
        self.assertEqual(self.date.triple(), (2004, 9, 4.0119884259256651))

    def test_date_tuple_value(self):
        self.assertEqual(self.date.tuple(),
                         (2004, 9, 4, 0, 17, 15.799999977461994))

    def test_localtime_modern(self):
        if time.timezone == 18000: # test only works in Eastern time zone
            self.assertEqual(localtime(Date('2009/6/23 8:47')),
                             datetime(2009, 6, 23, 4, 47, 0, 1))

    # I am commenting this out for now because I am not sure that I can
    # fix it without either writing an entirely new time module for
    # PyEphem, or making PyEphem depend on another Python module - which
    # would be its first-ever external dependency.

    def OFF_test_localtime_premodern(self):
        if time.timezone == 18000: # test only works in Eastern time zone
            self.assertEqual(localtime(Date('1531/8/24 2:49')),
                             datetime(1957, 10, 4, 15, 28, 34, 4))
