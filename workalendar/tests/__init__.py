from datetime import date
from unittest import TestCase

from workalendar.core import Calendar


class GenericCalendarTest(TestCase):

    cal_class = Calendar

    def setUp(self):
        self.year = date.today().year
        self.cal = self.cal_class()
