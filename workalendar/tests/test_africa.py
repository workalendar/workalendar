from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.africa import BeninCalendar, AlgeriaCalendar
from workalendar.africa import SouthAfricaCalendar


class AlgeriaCalendarTest(GenericCalendarTest):
    cal_class = AlgeriaCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # New year
        self.assertIn(date(2013, 1, 24), holidays)   # Milad un Nabi
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 7, 5), holidays)  # Independance day
        self.assertIn(date(2013, 8, 8), holidays)  # Eid ul-fitr
        self.assertIn(date(2013, 10, 15), holidays)  # Eid el-ada
        self.assertIn(date(2013, 11, 1), holidays)  # Anniversary revolution
        self.assertIn(date(2013, 11, 5), holidays)  # New Year
        self.assertIn(date(2013, 11, 14), holidays)  # Ashura


class BeninCalendarTest(GenericCalendarTest):
    cal_class = BeninCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 20), holidays)   # Whit Monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 8, 1), holidays)  # Independance Day
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 10, 26), holidays)  # Armed Forces Day
        self.assertIn(date(2013, 11, 1), holidays)  # All Saints Day
        self.assertIn(date(2013, 11, 30), holidays)  # National Day
        self.assertIn(date(2013, 12, 25), holidays)  # christmas
        # Variable Muslim days
        self.assertIn(date(2013, 1, 24), holidays)  # Milad un Nabi
        self.assertIn(date(2013, 10, 15), holidays)  # Tabaski
        self.assertIn(date(2013, 8, 8), holidays)  # Eid al-Fitr


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
