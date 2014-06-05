# -*- coding: utf-8 -*-

import unittest, ephem

tle_lines = (
    'ISS (ZARYA)             ',
    '1 25544U 98067A   09119.77864163  .00009789  00000-0  76089-4 0  7650',
    '2 25544  51.6397 195.1243 0008906 304.8273 151.9344 15.72498628598335',
    )

class SatelliteTests(unittest.TestCase):
    def setUp(self):
        self.iss = ephem.readtle(*tle_lines)
        self.atlanta = ephem.city('Atlanta')

    def test_normal_methods(self):
        for which in ['previous', 'next']:
            for event in ['transit', 'antitransit', 'rising', 'setting']:
                method_name = which + '_' + event
                method = getattr(self.atlanta, method_name)
                self.assertRaises(TypeError, method, self.iss)

    def test_next_pass(self):
        iss = self.iss
        self.atlanta.date = '2009/4/30'
        rt, raz, tt, talt, st, saz = self.atlanta.next_pass(iss)

        # Calsky says (using EST, and probably a different horizon):
        #  Rise(invis.)  1h02m17s  --.-mag  az:192.0° SSW
        #  Culmination   1h06m39s  --.-mag  az:128.2° SE   h:16.0°
        #  Set (invis.)  1h11m04s  --.-m  az: 64.9° ENE

        self.assertAlmostEqual(ephem.Date('2009/4/30 5:02:17'), rt, 3)
        self.assertAlmostEqual(ephem.Date('2009/4/30 5:06:39'), tt, 3)
        self.assertAlmostEqual(ephem.Date('2009/4/30 5:11:04'), st, 3)

        self.assertAlmostEqual(ephem.degrees('192.0'), raz, 1)
        self.assertAlmostEqual(ephem.degrees('16.0'), talt, 1)
        self.assertAlmostEqual(ephem.degrees('64.9'), saz, 1)
