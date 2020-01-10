import warnings
from datetime import date
from unittest import TestCase

from ..core import Calendar


class GenericCalendarTest(TestCase):
    cal_class = Calendar

    def setUp(self):
        super().setUp()
        warnings.simplefilter('ignore')
        self.year = date.today().year
        self.cal = self.cal_class()
