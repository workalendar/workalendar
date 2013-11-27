from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.europe import FranceCalendar, CzechRepublicCalendar
from workalendar.europe import IcelandCalendar


class CzechRepublicCalendarTest(GenericCalendarTest):
    cal_class = CzechRepublicCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 8), holidays)
        self.assertIn(date(2013, 7, 5), holidays)
        self.assertIn(date(2013, 7, 6), holidays)
        self.assertIn(date(2013, 9, 28), holidays)
        self.assertIn(date(2013, 10, 28), holidays)
        self.assertIn(date(2013, 11, 17), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)


class FranceCalendarTest(GenericCalendarTest):

    cal_class = FranceCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 4, 1), holidays)   # easter
        self.assertIn(date(2013, 5, 1), holidays)   # labour day
        self.assertIn(date(2013, 5, 8), holidays)   # 39-45
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 20), holidays)  # Pentecote
        self.assertIn(date(2013, 7, 14), holidays)  # Nation day
        self.assertIn(date(2013, 8, 15), holidays)  # Assomption
        self.assertIn(date(2013, 11, 1), holidays)  # Toussaint
        self.assertIn(date(2013, 11, 11), holidays)  # Armistice
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas

    def test_working_days(self):
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 1)))  # holiday
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 5)))  # saturday
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 6)))  # sunday
        self.assertTrue(self.cal.is_working_day(date(2013, 1, 7)))   # monday

    def test_business_days_computations(self):
        day = date(2013, 10, 30)
        self.assertEquals(
            self.cal.add_working_days(day, 0), date(2013, 10, 30))
        self.assertEquals(
            self.cal.add_working_days(day, 1), date(2013, 10, 31))
        self.assertEquals(self.cal.add_working_days(day, 2), date(2013, 11, 4))
        self.assertEquals(self.cal.add_working_days(day, 3), date(2013, 11, 5))


class IcelandCalendarTest(GenericCalendarTest):
    cal_class = IcelandCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 28), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 4, 25), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 9), holidays)
        self.assertIn(date(2013, 5, 20), holidays)
        self.assertIn(date(2013, 6, 17), holidays)
        self.assertIn(date(2013, 8, 5), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)
