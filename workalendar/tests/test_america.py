from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.america import UnitedStatesCalendar


class UnitedStatesCalendarTest(GenericCalendarTest):

    cal_class = UnitedStatesCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 7, 4), holidays)  # Nation day
        self.assertIn(date(2013, 11, 11), holidays)  # Armistice
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas
        # Variable days
        self.assertIn(date(2013, 1, 21), holidays)  # Martin Luther King
        self.assertIn(date(2013, 2, 18), holidays)  # Washington's bday
        self.assertIn(date(2013, 5, 27), holidays)  # Memorial day
        self.assertIn(date(2013, 9, 2), holidays)  # Labour day
        self.assertIn(date(2013, 10, 14), holidays)  # Colombus
        self.assertIn(date(2013, 11, 28), holidays)  # Thanskgiving

    def test_presidential_year(self):
        self.assertTrue(UnitedStatesCalendar.is_presidential_year(2012))
        self.assertFalse(UnitedStatesCalendar.is_presidential_year(2013))
        self.assertFalse(UnitedStatesCalendar.is_presidential_year(2014))
        self.assertFalse(UnitedStatesCalendar.is_presidential_year(2015))
        self.assertTrue(UnitedStatesCalendar.is_presidential_year(2016))

    def test_inauguration_day(self):
        holidays = self.cal.holidays(2008)
        self.assertNotIn(date(2008, 1, 20), holidays)
        holidays = self.cal.holidays(2009)
        self.assertIn(date(2009, 1, 20), holidays)
        # case when inauguration day is a sunday
        holidays = self.cal.holidays(1985)
        self.assertNotIn(date(1985, 1, 20), holidays)
        self.assertIn(date(1985, 1, 21), holidays)
