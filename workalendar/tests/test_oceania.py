from datetime import date

from workalendar.tests import GenericCalendarTest
from workalendar.oceania import (
    Australia,
    AustralianCapitalTerritory,
    NewSouthWales,
    NorthernTerritory,
    Queensland,
    SouthAustralia,
    Tasmania,
    Hobart,
    Victoria,
    WesternAustralia,
    MarshallIslands,
    NewZealand
)


class AustraliaTest(GenericCalendarTest):
    cal_class = Australia

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 1, 28), holidays)  # Australia day shift
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 3, 29), holidays)  # Good Friday
        self.assertIn(date(2013, 4, 25), holidays)
        self.assertIn(date(2013, 12, 25), holidays)

    def test_new_year_shift(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 2), holidays)  # 1st was a sunday

    def test_anzac_shift(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 4, 26), holidays)

    def test_oceania_shift_2016(self):
        holidays = self.cal.holidays_set(2016)
        # Christmas day is on sunday in 2016
        # Boxing day is on 26th
        self.assertIn(date(2016, 12, 26), holidays)
        # Boxing day shift on 27th
        self.assertIn(date(2016, 12, 27), holidays)

    def test_oceania_shift_2009(self):
        holidays = self.cal.holidays_set(2009)
        # Boxing day is on saturday in 2009
        # Boxing day is on 26th
        self.assertIn(date(2009, 12, 26), holidays)
        # Boxing day shift on 28th
        self.assertIn(date(2009, 12, 28), holidays)


class AustraliaCapitalTerritoryTest(AustraliaTest):
    cal_class = AustralianCapitalTerritory

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 11), holidays)
        self.assertIn(date(2013, 3, 30), holidays)  # Easter Saturday
        self.assertIn(date(2013, 4, 1), holidays)  # Easter Monday
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 9, 30), holidays)  # Family & Community day
        self.assertIn(date(2013, 10, 7), holidays)  # Labour day october
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day

    def test_family_community_day_before_2007(self):
        # There were no Family and Community day before 2007
        for year in range(1970, 2007):
            self.assertIsNone(self.cal.get_family_community_day(year))
            holidays = self.cal.holidays(year)
            holidays = dict(holidays)
            labels = holidays.values()
            self.assertNotIn(self.cal._family_community_label, labels)

    def test_family_community_day_2007_2017_presence(self):
        # Family & Community day was included [2007 -> 2017]
        for year in range(2007, 2018):
            self.assertIsNotNone(self.cal.get_family_community_day(year))
            holidays = self.cal.holidays(year)
            holidays = dict(holidays)
            labels = holidays.values()
            self.assertIn(self.cal._family_community_label, labels)

    def test_family_community_day_after_2017(self):
        # Starting of 2018 this day would no longer exist
        for year in range(2018, date.today().year + 1):
            self.assertIsNone(self.cal.get_family_community_day(year))
            holidays = self.cal.holidays(year)
            holidays = dict(holidays)
            labels = holidays.values()
            print(labels)
            self.assertNotIn(self.cal._family_community_label, labels)

    def test_reconciliation_day(self):
        reconciliation_day = self.cal.get_reconciliation_day(2017)
        self.assertIsNone(reconciliation_day)

        reconciliation_day = self.cal.get_reconciliation_day(2018)
        self.assertEqual(reconciliation_day, (date(2018, 5, 28),
                                              "Reconciliation Day Shift"))

        reconciliation_day = self.cal.get_reconciliation_day(2019)
        self.assertEqual(reconciliation_day, (date(2019, 5, 27),
                                              "Reconciliation Day"))


class NewSouthWalesTest(AustraliaTest):
    cal_class = NewSouthWales

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 30), holidays)  # Good friday
        self.assertIn(date(2013, 3, 31), holidays)  # Easter Sunday
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 10, 7), holidays)  # Labour day october
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day

    def test_anzac_shift(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 4, 26), holidays)

        # We don't shift if ANZAC day falls on a Saturday
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 25), holidays)


class NorthernTerritoryTest(AustraliaTest):
    cal_class = NorthernTerritory

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 30), holidays)  # Easter Saturday
        self.assertIn(date(2013, 5, 6), holidays)  # May Day
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 8, 5), holidays)  # Picnic day
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day

    def test_anzac_shift(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 4, 26), holidays)

        # We don't shift if ANZAC day falls on a Saturday
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 25), holidays)


class QueenslandTest(AustraliaTest):
    cal_class = Queensland

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 30), holidays)  # Easter Saturday
        self.assertIn(date(2013, 5, 6), holidays)  # May's labour day
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day

    def test_anzac_shift(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 4, 26), holidays)

        # We don't shift if ANZAC day falls on a Saturday
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 25), holidays)


class SouthAustraliaTest(AustraliaTest):
    cal_class = SouthAustralia

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 11), holidays)  # Adelaide's cup
        self.assertIn(date(2013, 3, 30), holidays)  # Easter Saturday
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 10, 7), holidays)  # Labour day october
        self.assertIn(date(2013, 12, 26), holidays)  # Proclamation day

    def test_anzac_shift(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 4, 26), holidays)

        # We don't shift if ANZAC day falls on a Saturday
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 25), holidays)


class TasmaniaTest(AustraliaTest):
    cal_class = Tasmania

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 11), holidays)  # Eight hours day
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day
        self.assertIn(date(2013, 4, 25), holidays)  # ANZAC day

    def test_anzac_shift(self):
        # We don't shift
        holidays = self.cal.holidays_set(2010)
        self.assertNotIn(date(2010, 4, 26), holidays)


class NonHobartTest(TasmaniaTest):
    def test_tasmania_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 11, 4), holidays)  # Recreation Day


class HobartTest(TasmaniaTest):
    cal_class = Hobart

    def test_hobart_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 2, 11), holidays)  # Royal Hobart Regatta
        # Recreation day not in Hobart
        self.assertNotIn(date(2013, 11, 4), holidays)  # Recreation Day


class VictoriaTest(AustraliaTest):
    cal_class = Victoria

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 11), holidays)  # Labours day in march
        self.assertIn(date(2013, 3, 30), holidays)  # Easter Saturday
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 11, 5), holidays)  # Melbourne's cup
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day
        self.assertIn(date(2013, 4, 25), holidays)  # ANZAC day

    def test_anzac_shift(self):
        # We don't shift
        holidays = self.cal.holidays_set(2010)
        self.assertNotIn(date(2010, 4, 26), holidays)


class WesternAustraliaTest(AustraliaTest):
    cal_class = WesternAustralia

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 4), holidays)  # Labours day in march
        self.assertIn(date(2013, 6, 3), holidays)  # Western Australia Day
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day
        # It is not possible to surely compute Queen's Birthday holiday in
        # The western Australia territory, since it's based on the Governor
        # Decision (it is typically the last Monday of September or the first
        # Monday of October)


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

    def test_new_year_shift(self):
        holidays = self.cal.holidays_set(2012)
        # New Years was on a sunday
        # Day After New Years is on the 2nd
        self.assertIn(date(2012, 1, 2), holidays)
        # New Years Shift is on the 3rd
        self.assertIn(date(2012, 1, 3), holidays)

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
