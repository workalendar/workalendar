from datetime import date

from . import GenericCalendarTest
from ..oceania import MarshallIslands, NewZealand


class MarshallIslandsTest(GenericCalendarTest):
    cal_class = MarshallIslands

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 3, 3), holidays)  # Remembrance day
        self.assertIn(date(2013, 3, 29), holidays)  # (good friday)
        self.assertIn(date(2013, 5, 1), holidays)  # constitution day
        self.assertIn(date(2013, 7, 5), holidays)  # Fishermens
        self.assertIn(date(2013, 9, 6), holidays)  # labour day
        self.assertIn(date(2013, 9, 27), holidays)  # Manit Day
        self.assertIn(date(2013, 11, 17), holidays)  # presidents day
        self.assertIn(date(2013, 12, 6), holidays)  # gospel day
        self.assertIn(date(2013, 12, 25), holidays)  # Xmas
        self.assertIn(date(2013, 12, 31), holidays)  # new year's eve


class NewZealandTest(GenericCalendarTest):
    cal_class = NewZealand

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2018, 1, 2), holidays)  # Day after New Year's Day
        self.assertIn(date(2018, 2, 6), holidays)  # Waitangi Day
        self.assertIn(date(2018, 3, 30), holidays)  # Good Friday
        self.assertIn(date(2018, 4, 2), holidays)  # Easter Monday
        self.assertIn(date(2018, 4, 25), holidays)  # ANZAC Day
        self.assertIn(date(2018, 6, 4), holidays)  # Queen's Birthday
        self.assertIn(date(2018, 10, 22), holidays)  # Labour Day
        self.assertIn(date(2018, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2018, 12, 26), holidays)  # Boxing Day

    def test_new_year_shift_on_sunday(self):
        holidays = self.cal.holidays_set(2012)
        # New Years was on a SUN
        # Day After New Years is on the 2nd
        self.assertIn(date(2012, 1, 2), holidays)
        # New Years Shift is on the 3rd
        self.assertIn(date(2012, 1, 3), holidays)
        # No shift of a shift
        self.assertNotIn(date(2012, 1, 4), holidays)

    def test_new_year_shift_on_saturday(self):
        holidays = self.cal.holidays_set(2022)
        # New Years is on a SAT
        # The day after is still a holiday
        self.assertIn(date(2022, 1, 2), holidays)
        # The shift is on the MON, 3rd
        self.assertIn(date(2022, 1, 3), holidays)
        # And there's a shift of the shift
        self.assertIn(date(2022, 1, 4), holidays)

    def test_anzac_shift(self):
        holidays = self.cal.holidays_set(2010)
        # 25th was a sunday
        # ANZAC Day is on 25th
        self.assertIn(date(2010, 4, 25), holidays)
        # ANZAC Day Shift is on 26th
        self.assertIn(date(2010, 4, 26), holidays)

    def test_waitangi_shift(self):
        holidays = self.cal.holidays_set(2016)
        # 6th was a saturday
        # Waitangi Day is on 6th
        self.assertIn(date(2016, 2, 6), holidays)
        # Waitangi Day Shift is on 7th
        self.assertIn(date(2016, 2, 8), holidays)

    def test_oceania_shift_2016(self):
        holidays = self.cal.holidays_set(2016)
        # Christmas day is on sunday in 2016
        # Boxing day is on 26th
        self.assertIn(date(2016, 12, 26), holidays)
        # Christmas day shift on 27th
        self.assertIn(date(2016, 12, 27), holidays)

    def test_oceania_shift_2009(self):
        holidays = self.cal.holidays_set(2009)
        # Boxing day is on saturday in 2009
        # Boxing day is on 26th
        self.assertIn(date(2009, 12, 26), holidays)
        # Boxing day shift on 28th
        self.assertIn(date(2009, 12, 28), holidays)
