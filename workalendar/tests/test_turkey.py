from datetime import date
from unittest import TestCase

from workalendar.tests import GenericCalendarTest
from workalendar.europe.turkey import Turkey


class TurkeyTest(GenericCalendarTest):
    cal_class = Turkey

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 23), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 19), holidays)
        self.assertIn(date(2014, 7, 15), holidays)
        self.assertIn(date(2014, 8, 30), holidays)
        self.assertIn(date(2014, 9, 29), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 23), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 19), holidays)
        self.assertIn(date(2015, 7, 15), holidays)
        self.assertIn(date(2015, 8, 30), holidays)
        self.assertIn(date(2015, 9, 29), holidays)
