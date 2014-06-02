#!/usr/bin/env python

from ephem import Observer
from unittest import TestCase

class ObserverTests(TestCase):
    def test_lon_can_also_be_called_long(self):
        o = Observer()
        o.lon = 3.0
        self.assertEqual(o.long, 3.0)
        o.long = 6.0
        self.assertEqual(o.lon, 6.0)

    def test_pressure_at_sea_level(self):
        o = Observer()
        o.elevation = 0
        o.compute_pressure()
        self.assertEqual(o.pressure, 1013.25)

    def test_pressure_at_11km(self):
        o = Observer()
        o.elevation = 11e3
        o.compute_pressure()
        assert 226.31 < o.pressure < 226.33
