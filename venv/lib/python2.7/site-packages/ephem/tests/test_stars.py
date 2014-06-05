#!/usr/bin/env python

import unittest
from ephem import star

class StarTests(unittest.TestCase):
    def test_Fomalhaut(self):
        s = star('Fomalhaut')
        self.assertEqual(s.name, 'Fomalhaut')
        self.assertRaises(RuntimeError, getattr, s, 'ra')

    def test_Fomalhaut_compute(self):
        s = star('Fomalhaut')
        s.compute()
        self.assertEqual(s.name, 'Fomalhaut')
        self.assertEqual(str(s._ra), '22:57:38.80')

    def test_Fomalhaut_autocompute(self):
        s = star('Fomalhaut', '1971/1/1')
        self.assertEqual(s.name, 'Fomalhaut')
        self.assertEqual(str(s._ra), '22:57:38.80')

    def test_unknown_star(self):
        self.assertRaises(KeyError, star, 'Alpha Centauri')
