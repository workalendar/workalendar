from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.europe import FranceCalendar


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

    def test_workdays(self):
        self.assertFalse(self.cal.is_workday(date(2013, 1, 1)))  # holiday
        self.assertFalse(self.cal.is_workday(date(2013, 1, 5)))  # saturday
        self.assertFalse(self.cal.is_workday(date(2013, 1, 6)))  # sunday
        self.assertTrue(self.cal.is_workday(date(2013, 1, 7)))   # monday

    def test_business_days_computations(self):
        day = date(2013, 10, 30)
        self.assertEquals(self.cal.add_workdays(day, 0), date(2013, 10, 30))
        self.assertEquals(self.cal.add_workdays(day, 1), date(2013, 10, 31))
        self.assertEquals(self.cal.add_workdays(day, 2), date(2013, 11, 4))
        self.assertEquals(self.cal.add_workdays(day, 3), date(2013, 11, 5))
