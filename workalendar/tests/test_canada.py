from datetime import date
from . import GenericCalendarTest
from ..core import MON
from ..america.canada import (
    Canada, Ontario, Quebec, BritishColumbia, Alberta, Saskatchewan, Manitoba,
    NewBrunswick, NovaScotia, PrinceEdwardIsland, Newfoundland, Yukon,
    NorthwestTerritories, Nunavut
)


class CanadaTest(GenericCalendarTest):
    cal_class = Canada

    def test_holidays_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 1, 3), holidays)
        self.assertIn(date(2011, 7, 1), holidays)
        self.assertIn(date(2011, 9, 5), holidays)
        self.assertIn(date(2011, 12, 26), holidays)

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)  # New years shift
        self.assertIn(date(2012, 7, 2), holidays)  # Canada day shift
        self.assertIn(date(2012, 9, 3), holidays)  # Labour day
        self.assertIn(date(2012, 12, 25), holidays)

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertNotIn(date(2013, 3, 29), holidays)  # Good Friday not in QC
        self.assertNotIn(date(2013, 4, 1), holidays)  # Easter Monday QC only
        self.assertIn(date(2013, 7, 1), holidays)
        self.assertIn(date(2013, 9, 2), holidays)
        self.assertIn(date(2013, 12, 25), holidays)

    def test_holidays_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 2), holidays)


class OntarioTest(GenericCalendarTest):
    cal_class = Ontario

    def test_holidays_2010(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 12, 27), holidays)  # Christmas day shift
        self.assertIn(date(2010, 12, 28), holidays)  # Boxing day shift

    def test_holidays_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 1, 3), holidays)
        self.assertIn(date(2011, 2, 21), holidays)  # Family Day Ontario
        self.assertIn(date(2011, 4, 22), holidays)  # Good Friday
        self.assertNotIn(date(2011, 4, 25), holidays)  # Easter Monday
        self.assertIn(date(2011, 5, 23), holidays)  # Victoria Day
        self.assertIn(date(2011, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2011, 8, 1), holidays)  # Civic holiday
        self.assertIn(date(2011, 9, 5), holidays)  # Labour Day
        self.assertIn(date(2011, 10, 10), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2011, 12, 26), holidays)
        self.assertIn(date(2011, 12, 27), holidays)  # Boxing day shift

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertIn(date(2012, 2, 20), holidays)  # Family Day Ontario
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertIn(date(2012, 12, 26), holidays)  # Boxing day


class QuebecTest(GenericCalendarTest):
    cal_class = Quebec

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertNotIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 6, 24), holidays)  # St Jean Baptise
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day


class BritishColumbiaTest(GenericCalendarTest):
    cal_class = BritishColumbia

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        # Family Day BC was not set in 2012
        self.assertNotIn(date(2012, 2, 13), holidays)

        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 8, 6), holidays)  # BC Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day

    def test_family_day(self):
        # From 2013 to 2018, Family Day was on 2nd MON of February
        for year in range(2013, 2019):
            holidays = dict(self.cal.holidays(year))
            day = self.cal.get_nth_weekday_in_month(year, 2, MON, 2)
            self.assertIn(day, holidays)
            self.assertEqual(holidays[day], "Family Day")

        # As of 2019, it happens on 3rd MON of February
        for year in (2019, 2020, 2021):
            holidays = dict(self.cal.holidays(year))
            day = self.cal.get_nth_weekday_in_month(year, 2, MON, 3)
            self.assertIn(day, holidays)
            self.assertEqual(holidays[day], "Family Day")


class AlbertaTest(GenericCalendarTest):
    cal_class = Alberta

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertIn(date(2012, 2, 20), holidays)  # Family Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertNotIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day


class SaskatchewanTest(GenericCalendarTest):
    cal_class = Saskatchewan

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertIn(date(2012, 2, 20), holidays)  # Family Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2012, 11, 12), holidays)  # Remembrance Day (Shift)
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day


class ManitobaTest(GenericCalendarTest):
    cal_class = Manitoba

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertIn(date(2012, 2, 20), holidays)  # Louis Riel Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertNotIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertNotIn(date(2012, 11, 12), holidays)  # Remembrance Day Shift
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertNotIn(date(2012, 12, 26), holidays)  # Boxing day


class NewBrunswickTest(GenericCalendarTest):
    cal_class = NewBrunswick

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertNotIn(date(2012, 2, 20), holidays)  # Family Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertNotIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertNotIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertNotIn(date(2012, 11, 12), holidays)  # Remembrance Day Shift
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertNotIn(date(2012, 12, 26), holidays)  # Boxing day


class NovaScotiaTest(GenericCalendarTest):
    cal_class = NovaScotia

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertNotIn(date(2012, 2, 20), holidays)  # Family Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertNotIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertNotIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertNotIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2012, 11, 12), holidays)  # Remembrance Day Shift
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertNotIn(date(2012, 12, 26), holidays)  # Boxing day

    def test_holidays_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 16), holidays)  # Viola Desmond day


class PrinceEdwardIslandTest(GenericCalendarTest):
    cal_class = PrinceEdwardIsland

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertIn(date(2012, 2, 20), holidays)  # Islander Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertNotIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertNotIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertNotIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2012, 11, 12), holidays)  # Remembrance Day Shift
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertNotIn(date(2012, 12, 26), holidays)  # Boxing day


class NewfoundlandTest(GenericCalendarTest):
    cal_class = Newfoundland

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 29), holidays)  # Good Friday
        self.assertNotIn(date(2013, 4, 1), holidays)  # Easter Monday
        self.assertIn(date(2013, 7, 1), holidays)
        self.assertIn(date(2013, 9, 2), holidays)
        self.assertIn(date(2013, 12, 25), holidays)


class YukonTest(GenericCalendarTest):
    cal_class = Yukon

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertNotIn(date(2012, 2, 20), holidays)  # Family Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertNotIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertIn(date(2012, 8, 20), holidays)  # Discovery Day
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertNotIn(date(2012, 11, 12), holidays)  # Remembrance Day Shift
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertNotIn(date(2012, 12, 26), holidays)  # Boxing day


class NorthwestTerritoriesTest(GenericCalendarTest):
    cal_class = NorthwestTerritories

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertNotIn(date(2012, 2, 20), holidays)  # Family Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertNotIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertIn(date(2012, 6, 21), holidays)  # National Aboriginal Day
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2012, 11, 12), holidays)  # Remembrance Day Shift
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertNotIn(date(2012, 12, 26), holidays)  # Boxing day


class NunavutTests(GenericCalendarTest):
    cal_class = Nunavut

    def test_holidays_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)
        self.assertNotIn(date(2012, 2, 20), holidays)  # Family Day
        self.assertIn(date(2012, 4, 6), holidays)  # Good Friday
        self.assertNotIn(date(2012, 4, 9), holidays)  # Easter Monday
        self.assertIn(date(2012, 5, 21), holidays)  # Victoria Day
        self.assertIn(date(2012, 7, 1), holidays)  # Canada Day
        self.assertIn(date(2012, 9, 3), holidays)  # Labour Day
        self.assertIn(date(2012, 7, 9), holidays)  # Nunavut Day
        self.assertNotIn(date(2012, 8, 6), holidays)  # Civic Holiday
        self.assertNotIn(date(2012, 6, 21), holidays)  # Nat. Aboriginal Day
        self.assertIn(date(2012, 10, 8), holidays)  # Canadian Thanksgiving
        self.assertIn(date(2012, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2012, 11, 12), holidays)  # Remembrance Day Shift
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas day
        self.assertNotIn(date(2012, 12, 26), holidays)  # Boxing day
