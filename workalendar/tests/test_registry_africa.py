# -*- coding: utf-8 -*-
from unittest import TestCase
from datetime import date
from workalendar.tests import GenericCalendarTest

from workalendar.africa import (
    Algeria,
    Benin,
    IvoryCoast,
    Madagascar,
    SaoTomeAndPrincipe,
    SouthAfrica,
)

from workalendar.registry import registry


class RegistryAfrica(TestCase):
    def test_africa(self):
        classes = (v for k, v in registry.region_registry.items())
        classes = list(classes)
        self.assertIn(Algeria, classes)
        self.assertIn(Benin, classes)
        self.assertIn(IvoryCoast, classes)
        self.assertIn(Madagascar, classes)
        self.assertIn(SaoTomeAndPrincipe, classes)
        self.assertIn(SouthAfrica, classes)


class SouthAfricaTest(GenericCalendarTest):
    cal_class = SouthAfrica

    def test_south_africa_2019(self):
        holidays = self.cal.holidays_set(2019)

        # variable days
        self.assertIn(date(2019, 5, 8), holidays)  # 2019 National Elections
        self.assertNotIn(date(2017, 5, 8), holidays)
