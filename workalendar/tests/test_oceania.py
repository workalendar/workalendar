from datetime import date

from workalendar.tests import GenericCalendarTest
from workalendar.oceania import AustraliaCalendar


class AustraliaCalendarTest(GenericCalendarTest):
    cal_class = AustraliaCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 4, 25), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
