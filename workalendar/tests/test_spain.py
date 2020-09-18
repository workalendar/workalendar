from datetime import date

from . import GenericCalendarTest
from ..europe import Spain, Catalonia


class SpainTest(GenericCalendarTest):
    cal_class = Spain

    def test_common_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)    # New Year
        self.assertIn(date(2015, 1, 6), holidays)    # Epiphany
        self.assertIn(date(2015, 4, 3), holidays)    # Good Friday
        self.assertIn(date(2015, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2015, 8, 15), holidays)   # Assumption
        self.assertIn(date(2015, 10, 12), holidays)  # Nation Day
        self.assertIn(date(2015, 11, 1), holidays)   # All Saints
        self.assertIn(date(2015, 12, 6), holidays)   # Dia de la Constitución
        self.assertIn(date(2015, 12, 8), holidays)   # Immaculate conception
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas

    def test_common_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)    # New Year
        self.assertIn(date(2016, 1, 6), holidays)    # Epiphany
        self.assertIn(date(2016, 3, 25), holidays)   # Good Friday
        self.assertIn(date(2016, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2016, 8, 15), holidays)   # Assumption
        self.assertIn(date(2016, 10, 12), holidays)  # Nation Day
        self.assertIn(date(2016, 11, 1), holidays)   # All Saints
        self.assertIn(date(2016, 12, 6), holidays)   # Dia de la Constitución
        self.assertIn(date(2016, 12, 8), holidays)   # Immaculate conception
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "Día del trabajador")


class CataloniaTest(SpainTest):
    cal_class = Catalonia

    def test_region_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 6), holidays)  # Easter Monday
        self.assertIn(date(2015, 6, 24), holidays)  # San Joan
        # Diada nacional de Catalunya
        self.assertIn(date(2015, 9, 11), holidays)
        self.assertIn(date(2015, 12, 26), holidays)  # Sant Esteve

    def test_region_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 3, 28), holidays)  # Easter Monday
        self.assertIn(date(2016, 6, 24), holidays)  # San Joan
        # Diada nacional de Catalunya
        self.assertIn(date(2016, 9, 11), holidays)
        self.assertIn(date(2016, 12, 26), holidays)  # Sant Esteve

    def test_boxing_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(holidays[date(2020, 12, 26)], "Sant Esteve")
