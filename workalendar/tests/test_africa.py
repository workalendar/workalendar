from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.africa import SouthAfricaCalendar


class SouthAfricaCalendarTest(GenericCalendarTest):

    cal_class = SouthAfricaCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 3, 21), holidays)  # human rights day
        # good friday, becoming family day
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 27), holidays)  # freedom day
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 6, 16), holidays)  # youth day
        self.assertIn(date(2013, 6, 17), holidays)  # youth day - shift
        self.assertIn(date(2013, 8, 9), holidays)  # national women's day
        self.assertIn(date(2013, 9, 24), holidays)  # heritage day
        self.assertIn(date(2013, 12, 16), holidays)  # day of reconciliation
        self.assertIn(date(2013, 12, 25), holidays)  # christmas
        self.assertIn(date(2013, 12, 26), holidays)  # day of goodwill

    def test_year_2014(self):
        # test shifting
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 27), holidays)  # freedom day
        self.assertIn(date(2014, 4, 28), holidays)  # freedom day sub
