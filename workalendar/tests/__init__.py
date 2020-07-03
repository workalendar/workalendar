import warnings
from datetime import date
from unittest import TestCase

from ..core import Calendar


class CoreCalendarTest(TestCase):
    cal_class = Calendar

    def setUp(self):
        super().setUp()
        self.year = date.today().year
        self.cal = self.cal_class()


class GenericCalendarTest(CoreCalendarTest):
    test_include_january_1st = True

    def setUp(self):
        super().setUp()
        warnings.simplefilter('ignore')

    def test_weekend_days(self):
        class_name = self.cal_class.__name__
        if class_name in ('Calendar',):
            return
        try:
            self.cal.get_weekend_days()
        except NotImplementedError:
            assert False, (self.cal, class_name)

    def test_january_1st(self):
        class_name = self.cal_class.__name__
        if class_name in ('Calendar',):
            return
        holidays = self.cal.holidays_set(self.year)
        if self.test_include_january_1st:
            self.assertIn(date(self.year, 1, 1), holidays)
        else:
            self.assertNotIn(date(self.year, 1, 1), holidays)
