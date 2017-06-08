# coding=utf-8
from datetime import date
from collections import Counter

from workalendar.tests import GenericCalendarTest
from workalendar.europe import Austria
from workalendar.europe import Bulgaria
from workalendar.europe import Belgium
from workalendar.europe import Croatia
from workalendar.europe import Cyprus
from workalendar.europe import CzechRepublic
from workalendar.europe import Denmark
from workalendar.europe import Slovakia
from workalendar.europe import Finland
from workalendar.europe import Estonia
from workalendar.europe import Sweden
from workalendar.europe import France, FranceAlsaceMoselle
from workalendar.europe import Greece
from workalendar.europe import Hungary
from workalendar.europe import Iceland
from workalendar.europe import Ireland
from workalendar.europe import Italy
from workalendar.europe import Latvia
from workalendar.europe import Luxembourg
from workalendar.europe import Malta
from workalendar.europe import Netherlands
from workalendar.europe import Norway
from workalendar.europe import Poland
from workalendar.europe import Portugal
from workalendar.europe import Romania
from workalendar.europe import Spain, Catalonia
from workalendar.europe import Slovenia
from workalendar.europe import Switzerland, Vaud
from workalendar.europe import UnitedKingdom
from workalendar.europe import UnitedKingdomNorthernIreland
from workalendar.europe import EuropeanCentralBank
from workalendar.europe import (Germany, BadenWurttemberg, Bavaria, Berlin,
                                Brandenburg, Bremen, Hamburg, Hesse,
                                MecklenburgVorpommern, LowerSaxony,
                                NorthRhineWestphalia, RhinelandPalatinate,
                                Saarland, Saxony, SaxonyAnhalt,
                                SchleswigHolstein, Thuringia)


class AustriaTest(GenericCalendarTest):
    cal_class = Austria

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # New Years day
        self.assertIn(date(2016, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2016, 3, 28), holidays)  # easter monday
        self.assertIn(date(2016, 5, 1), holidays)  # National Holiday
        self.assertIn(date(2016, 5, 5), holidays)  # Ascension Day
        self.assertIn(date(2016, 5, 16), holidays)  # Whit monday
        self.assertIn(date(2016, 5, 26), holidays)  # Corpus Christi
        self.assertIn(date(2016, 8, 15), holidays)  # Assumption
        self.assertIn(date(2016, 10, 26), holidays)  # national day again
        self.assertIn(date(2016, 11, 1), holidays)  # all saints
        self.assertIn(date(2016, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2016, 12, 25), holidays)  # Xmas
        self.assertIn(date(2016, 12, 26), holidays)  # St Stephens


class BulgariaTest(GenericCalendarTest):
    cal_class = Bulgaria

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)   # New Year's Day
        self.assertIn(date(2016, 3, 3), holidays)   # Liberation Day
        self.assertIn(date(2016, 3, 27), holidays)   # Easter Sun
        self.assertIn(date(2016, 3, 28), holidays)   # Easter Mon
        self.assertIn(date(2016, 5, 1), holidays)   # International Workers'
        self.assertIn(date(2016, 5, 6), holidays)   # St George's Day
        self.assertIn(date(2016, 5, 24), holidays)   # St Cyril & Methodius
        self.assertIn(date(2016, 9, 6), holidays)   # Unification Day
        self.assertIn(date(2016, 9, 22), holidays)   # Independence Day
        self.assertIn(date(2016, 12, 24), holidays)   # Christmas Eve
        self.assertIn(date(2016, 12, 25), holidays)   # Christmas 1
        self.assertIn(date(2016, 12, 26), holidays)   # Christmas 2
        # Non-attendance day for schools, otherwise a working day.
        self.assertNotIn(date(2016, 11, 1), holidays)   # National Awakening


class CroatiaTest(GenericCalendarTest):
    cal_class = Croatia

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)   # New Year's Day Nova Godin
        self.assertIn(date(2016, 1, 6), holidays)   # Epiphany Bogojavljenje,
        self.assertIn(date(2016, 3, 27), holidays)  # Easter Sunday Uskrs i us
        self.assertIn(date(2016, 3, 28), holidays)  # Easter Monday
        self.assertIn(date(2016, 5, 1), holidays)   # Intl Workers' Day Međunar
        self.assertIn(date(2016, 5, 26), holidays)  # Corpus Christi Tijelovo
        self.assertIn(date(2016, 6, 22), holidays)  # Anti-Fascist Day Dan anti
        self.assertIn(date(2016, 6, 25), holidays)  # Statehood Day 	Dan drž
        self.assertIn(date(2016, 8, 5), holidays)   # Victory & Homeland Thanks
        self.assertIn(date(2016, 8, 15), holidays)  # Assumption of Mary 	Vel
        self.assertIn(date(2016, 10, 8), holidays)  # Independence Day Dan neov
        self.assertIn(date(2016, 11, 1), holidays)  # All Saints' Day Dan svih
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas Božić
        self.assertIn(date(2016, 12, 26), holidays)  # St. Stephen's Day Prvi d


class Cyprus(GenericCalendarTest):
    cal_class = Cyprus

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)    # New Year's Day
        self.assertIn(date(2017, 1, 6), holidays)    # Epiphany
        self.assertIn(date(2017, 2, 27), holidays)   # Green Monday
        self.assertIn(date(2017, 3, 25), holidays)   # Greek Independence Day
        self.assertIn(date(2017, 4, 1), holidays)    # Cyprus National Holiday
        self.assertIn(date(2017, 4, 14), holidays)   # Good Friday (Orthodox)
        self.assertIn(date(2017, 4, 17), holidays)   # Easter Monday (Orthodox)
        self.assertIn(date(2017, 4, 18), holidays)   # Easter Tues banks only
        self.assertIn(date(2017, 5, 1), holidays)    # Labour Day/May Day
        self.assertIn(date(2017, 6, 5), holidays)    # Orthodox Pentecost Mon
        self.assertIn(date(2017, 7, 15), holidays)   # Assumption
        self.assertIn(date(2017, 10, 1), holidays)   # Cyprus Independence Day
        self.assertIn(date(2017, 10, 28), holidays)  # Ochi Day
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2017, 12, 26), holidays)  # Boxing Day


class CzechRepublicTest(GenericCalendarTest):
    cal_class = CzechRepublic

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

    def test_year_good_friday(self):
        # Good Friday not yet a holiday before 2016
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 4, 3), holidays)
        # Good friday will be a holiday as of 2016
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 3, 25), holidays)


class DenmarkTest(GenericCalendarTest):
    cal_class = Denmark

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)    # nytaarsdag
        self.assertIn(date(2015, 3, 29), holidays)   # palmesoendag
        self.assertIn(date(2015, 4, 2), holidays)    # skaertaarsdag
        self.assertIn(date(2015, 4, 3), holidays)    # langfredag
        self.assertIn(date(2015, 4, 5), holidays)    # paaskedag
        self.assertIn(date(2015, 4, 6), holidays)    # 2. paaskedag
        self.assertIn(date(2015, 5, 1), holidays)    # st bededag
        self.assertIn(date(2015, 5, 14), holidays)   # kristi himmelfart
        self.assertIn(date(2015, 5, 24), holidays)   # pinsedag
        self.assertIn(date(2015, 5, 25), holidays)   # 2. pinsedag
        self.assertIn(date(2015, 6, 5), holidays)    # grundlovsdag
        self.assertIn(date(2015, 12, 24), holidays)  # juleaftensdag
        self.assertIn(date(2015, 12, 25), holidays)  # juledag
        self.assertIn(date(2015, 12, 26), holidays)  # 2. juledag
        self.assertIn(date(2015, 12, 31), holidays)  # nytaarsaften


class SlovakiaTest(GenericCalendarTest):
    cal_class = Slovakia

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 1, 6), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 8), holidays)
        self.assertIn(date(2013, 7, 5), holidays)
        self.assertIn(date(2013, 8, 29), holidays)
        self.assertIn(date(2013, 9, 1), holidays)
        self.assertIn(date(2013, 9, 15), holidays)
        self.assertIn(date(2013, 11, 1), holidays)
        self.assertIn(date(2013, 11, 17), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)

    def test_removed_duplicate(self):
        holidays = self.cal.holidays(2017)
        counter = Counter(day for day, label in holidays)
        # Only one "all saints"
        self.assertEqual(counter[date(2017, 11, 1)], 1)
        # Only one "XMas eve"
        self.assertEqual(counter[date(2017, 12, 24)], 1)
        # De-duplicate, XMas day was configured twice.
        # Refs #205.
        self.assertEqual(counter[date(2017, 12, 25)], 1)
        # Only one St Stephen
        self.assertEqual(counter[date(2017, 12, 25)], 1)


class SwedenTest(GenericCalendarTest):
    cal_class = Sweden

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # may day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 19), holidays)  # pentecost
        self.assertIn(date(2013, 6, 6), holidays)  # national day
        self.assertIn(date(2013, 6, 21), holidays)  # midsummer eve
        self.assertIn(date(2013, 6, 22), holidays)  # midsummer day
        self.assertIn(date(2013, 11, 2), holidays)  # all saints
        self.assertIn(date(2013, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2013, 12, 25), holidays)  # xmas day
        self.assertIn(date(2013, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2013, 12, 31), holidays)  # new year's eve

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # new year
        self.assertIn(date(2014, 1, 6), holidays)  # epiphany
        self.assertIn(date(2014, 4, 18), holidays)  # good friday
        self.assertIn(date(2014, 4, 20), holidays)  # easter sunday
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 5, 1), holidays)  # may day
        self.assertIn(date(2014, 5, 29), holidays)  # ascension
        self.assertIn(date(2014, 6, 6), holidays)  # national day
        self.assertIn(date(2014, 6, 8), holidays)  # pentecost
        self.assertIn(date(2014, 6, 20), holidays)  # midsummer eve
        self.assertIn(date(2014, 6, 21), holidays)  # midsummer day
        self.assertIn(date(2014, 11, 1), holidays)  # all saints
        self.assertIn(date(2014, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2014, 12, 25), holidays)  # xmas day
        self.assertIn(date(2014, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2014, 12, 31), holidays)  # new year's eve

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # new year
        self.assertIn(date(2015, 1, 6), holidays)  # epiphany
        self.assertIn(date(2015, 4, 3), holidays)  # good friday
        self.assertIn(date(2015, 4, 5), holidays)  # easter sunday
        self.assertIn(date(2015, 4, 6), holidays)  # easter monday
        self.assertIn(date(2015, 5, 1), holidays)  # may day
        self.assertIn(date(2015, 5, 14), holidays)  # ascension
        self.assertIn(date(2015, 5, 24), holidays)  # pentecost
        self.assertIn(date(2015, 6, 6), holidays)  # national day
        self.assertIn(date(2015, 6, 19), holidays)  # midsummer eve
        self.assertIn(date(2015, 6, 20), holidays)  # midsummer day
        self.assertIn(date(2015, 10, 31), holidays)  # all saints
        self.assertIn(date(2015, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2015, 12, 25), holidays)  # xmas day
        self.assertIn(date(2015, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2015, 12, 31), holidays)  # new year's eve

    def test_pentecost(self):
        holidays = self.cal.holidays(2015)
        self.assertIn((date(2015, 5, 24), 'Pentecost'), holidays)


class FinlandTest(GenericCalendarTest):
    cal_class = Finland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # may day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 19), holidays)  # pentecost
        self.assertIn(date(2013, 6, 21), holidays)  # midsummer eve
        self.assertIn(date(2013, 6, 22), holidays)  # midsummer day
        self.assertIn(date(2013, 11, 2), holidays)  # all saints (special)
        self.assertIn(date(2013, 12, 6), holidays)  # Independence day
        self.assertIn(date(2013, 12, 24), holidays)  # XMas eve
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # St Stephens

    def test_year_2014(self):
        # testing the special rule variable holidays
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 20), holidays)  # midsummer eve
        self.assertIn(date(2014, 6, 21), holidays)  # midsummer day
        self.assertIn(date(2014, 11, 1), holidays)  # all saints (special)


class FranceTest(GenericCalendarTest):

    cal_class = France

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


class FranceAlsaceMoselleTest(FranceTest):
    cal_class = FranceAlsaceMoselle

    def test_year_2013(self):
        super(FranceAlsaceMoselleTest, self).test_year_2013()
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 29), holidays)  # Good friday
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day

    def test_working_days(self):
        super(FranceAlsaceMoselleTest, self).test_working_days()

    def test_business_days_computations(self):
        super(FranceAlsaceMoselleTest, self) \
            .test_business_days_computations()


class GreeceTest(GenericCalendarTest):
    cal_class = Greece

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 18), holidays)  # Clean monday
        # Annunciation & Independence day
        self.assertIn(date(2013, 3, 25), holidays)
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 5, 3), holidays)  # good friday
        self.assertIn(date(2013, 5, 5), holidays)  # easter
        self.assertIn(date(2013, 5, 6), holidays)  # easter monday
        self.assertIn(date(2013, 6, 23), holidays)  # pentecost sunday
        self.assertIn(date(2013, 6, 24), holidays)  # whit monday
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 10, 28), holidays)  # Ochi Day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # Glorifying mother of God


class HungaryTest(GenericCalendarTest):
    cal_class = Hungary

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 15), holidays)  # national day
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 5, 19), holidays)  # Whit sunday
        self.assertIn(date(2013, 5, 20), holidays)  # Whit monday
        self.assertIn(date(2013, 8, 20), holidays)  # St Stephen's day
        self.assertIn(date(2013, 10, 23), holidays)  # national day (again?)
        self.assertIn(date(2013, 11, 1), holidays)  # all saints
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # Second day of XMas

    def test_year_good_friday(self):
        # Since the year 2017, Good Friday is a non-working day un Hungary
        # Refs #203
        holidays = self.cal.holidays_set(2016)
        good_friday_2016 = date(2016, 3, 25)
        self.assertNotIn(good_friday_2016, holidays)
        # 2017
        holidays = self.cal.holidays_set(2017)
        good_friday_2017 = date(2017, 4, 14)
        self.assertIn(good_friday_2017, holidays)


class MaltaTest(GenericCalendarTest):
    """Rollover rules changed in 2005"""
    cal_class = Malta

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # National Holidays
        self.assertIn(date(2017, 3, 31), holidays)  # Jum il-Ħelsien
        self.assertIn(date(2017, 6, 7), holidays)  # Sette Giugno
        self.assertIn(date(2017, 9, 8), holidays)  # Jum il-Vitorja
        self.assertIn(date(2017, 9, 21), holidays)  # Jum l-Indipendenza
        self.assertIn(date(2017, 12, 13), holidays)  # Jum ir-Repubblika
        # Public Holidays
        self.assertIn(date(2017, 1, 1), holidays)  # L-Ewwel tas-Sena
        self.assertIn(date(2017, 2, 10), holidays)  # Nawfraġju ta' San Pawl
        self.assertIn(date(2017, 3, 19), holidays)  # San Ġużepp
        self.assertIn(date(2017, 4, 14), holidays)  # Il-Ġimgħa l-Kbira
        self.assertIn(date(2017, 5, 1), holidays)  # Jum il-Ħaddiem
        self.assertIn(date(2017, 6, 29), holidays)  # L-Imnarja
        self.assertIn(date(2017, 8, 15), holidays)  # Santa Marija
        self.assertIn(date(2017, 12, 8), holidays)  # Il-Kunċizzjoni
        self.assertIn(date(2017, 12, 25), holidays)  # Il-Milied


class NorwayTest(GenericCalendarTest):
    cal_class = Norway

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 3, 28), holidays)   # maundy thursday
        self.assertIn(date(2013, 3, 29), holidays)   # good friday
        self.assertIn(date(2013, 3, 31), holidays)   # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)   # easter monday
        self.assertIn(date(2013, 5, 1), holidays)   # labour day
        self.assertIn(date(2013, 5, 17), holidays)   # constitution day
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 19), holidays)  # Pentecost
        self.assertIn(date(2013, 5, 20), holidays)  # Whit monday
        self.assertIn(date(2013, 12, 25), holidays)  # Xmas
        self.assertIn(date(2013, 12, 26), holidays)  # St Stephens


class PolandTest(GenericCalendarTest):
    cal_class = Poland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # New Year
        self.assertIn(date(2013, 1, 6), holidays)  # Trzech Kroli
        self.assertIn(date(2013, 3, 31), holidays)  # Easter Sunday
        self.assertIn(date(2013, 4, 1), holidays)  # Easter Monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labor Day
        self.assertIn(date(2013, 5, 3), holidays)  # Constitution Day
        self.assertIn(date(2013, 5, 19), holidays)  # Pentecost
        self.assertIn(date(2013, 5, 30), holidays)  # Corpus Christi
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 11, 1), holidays)  # All Saints' Day
        self.assertIn(date(2013, 11, 11), holidays)  # Independence Day
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day


class IcelandTest(GenericCalendarTest):
    cal_class = Iceland

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
        self.assertIn(date(2013, 12, 31), holidays)


class IrelandTest(GenericCalendarTest):
    cal_class = Ireland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # Tue New Year's Day
        self.assertIn(date(2013, 3, 17), holidays)   # Sun St Patricks day
        self.assertIn(date(2013, 3, 18), holidays)   # Mon St Patricks shift
        self.assertIn(date(2013, 4, 1), holidays)    # Mon Easter Monday
        self.assertIn(date(2013, 5, 6), holidays)    # Mon May day
        self.assertIn(date(2013, 6, 3), holidays)    # Mon June Holiday
        self.assertIn(date(2013, 8, 5), holidays)    # Mon August Holiday
        self.assertIn(date(2013, 10, 28), holidays)  # Mon October Holiday
        self.assertIn(date(2013, 12, 25), holidays)  # Wed Christmas
        self.assertIn(date(2013, 12, 26), holidays)  # Thu St Stepehen's

    def test_shift_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)    # new year day
        self.assertIn(date(2012, 1, 2), holidays)    # new year day shift

    def test_shift_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 12, 25), holidays)  # Christmas it's sunday
        self.assertIn(date(2011, 12, 26), holidays)  # Xmas day shift
        self.assertIn(date(2011, 12, 27), holidays)  # St Stephen's day shift

    def test_shift_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas it's friday
        self.assertIn(date(2015, 12, 26), holidays)  # St. Stephen's day Sat
        self.assertIn(date(2015, 12, 28), holidays)  # St. Stephen's day shift

    def test_whit_mon(self):
        holidays_1972 = self.cal.holidays_set(1972)
        holidays_1973 = self.cal.holidays_set(1973)
        # holidays_1974 = self.cal.holidays_set(1974) Overlaps with June Hol
        holidays_1975 = self.cal.holidays_set(1975)
        self.assertIn(date(1972, 5, 22), holidays_1972)     # Whit Monday
        self.assertIn(date(1973, 6, 11), holidays_1973)
        # self.assertNotIn(date(1974, 6, 3), holidays_1974) # Overlaps Jun Hol
        self.assertNotIn(date(1975, 5, 19), holidays_1975)  # No Whit Monday

    def test_may_day(self):
        holidays_1993 = self.cal.holidays_set(1993)
        holidays_1994 = self.cal.holidays_set(1994)
        holidays_1995 = self.cal.holidays_set(1995)
        self.assertNotIn(date(1993, 5, 1), holidays_1993)  # No May Day
        self.assertIn(date(1994, 5, 2), holidays_1994)     # May Day
        self.assertIn(date(1995, 5, 1), holidays_1995)

    def test_october_holiday(self):
        holidays_1976 = self.cal.holidays_set(1976)
        holidays_1977 = self.cal.holidays_set(1977)
        holidays_1978 = self.cal.holidays_set(1978)
        self.assertNotIn(date(1976, 10, 25), holidays_1976)  # No October Hol
        self.assertIn(date(1977, 10, 31), holidays_1977)     # October Hol
        self.assertIn(date(1978, 10, 30), holidays_1978)


class ItalyTest(GenericCalendarTest):
    cal_class = Italy

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new years day
        self.assertIn(date(2013, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 4, 25), holidays)  # liberation day
        self.assertIn(date(2013, 5, 1), holidays)  # workers day
        self.assertIn(date(2013, 6, 2), holidays)  # Republic day
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 11, 1), holidays)  # all saints
        self.assertIn(date(2013, 12, 8), holidays)  # immaculate Conception
        self.assertIn(date(2013, 12, 25), holidays)  # christmas
        self.assertIn(date(2013, 12, 26), holidays)  # San Stefano


class LatviaTest(GenericCalendarTest):

    cal_class = Latvia

    def test_year_2017(self):
        """
        https://www.bank.lv/en/about-us/public-holidays-in-latvia
        """
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2017, 4, 14), holidays)  # Easter 14 and 17 april
        self.assertIn(date(2017, 4, 16), holidays)  # Easter 14 and 17 april
        self.assertIn(date(2017, 4, 17), holidays)  # Easter 14 and 17 april
        self.assertIn(date(2017, 5, 1), holidays)  # Labour Day, C
        self.assertIn(date(2017, 5, 4), holidays)  # Restoration of Independe
        self.assertIn(date(2017, 6, 23), holidays)  # Midsummer Day
        self.assertIn(date(2017, 6, 24), holidays)  # St. John's Day
        self.assertIn(date(2017, 11, 18), holidays)  # Proclamation
        self.assertIn(date(2017, 11, 20), holidays)  # Proclamation Observed
        self.assertIn(date(2017, 12, 24), holidays)  # Christmas
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas
        self.assertIn(date(2017, 12, 26), holidays)  # Christmas
        self.assertIn(date(2017, 12, 31), holidays)  # New Year's Eve

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 5, 6), holidays)  # Restoration Day Observed


class LuxembourgTest(GenericCalendarTest):

    cal_class = Luxembourg

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)   # new year
        self.assertIn(date(2016, 3, 28), holidays)   # easter
        self.assertIn(date(2016, 5, 1), holidays)   # labour day
        self.assertIn(date(2016, 5, 5), holidays)   # Ascension
        self.assertIn(date(2016, 5, 16), holidays)  # Pentecote
        self.assertIn(date(2016, 6, 23), holidays)  # Luxembourg National Day
        self.assertIn(date(2016, 8, 15), holidays)  # Assomption
        self.assertIn(date(2016, 11, 1), holidays)  # Toussaint
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas
        self.assertIn(date(2016, 12, 26), holidays)  # St. Stephen´s Day


class NetherlandsTest(GenericCalendarTest):

    cal_class = Netherlands

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)   # New Year
        self.assertIn(date(2015, 4, 3), holidays)   # Good friday
        self.assertIn(date(2015, 4, 5), holidays)   # Easter Sunday
        self.assertIn(date(2015, 4, 6), holidays)   # Easter Monday
        self.assertIn(date(2015, 4, 27), holidays)  # King's Day
        self.assertIn(date(2015, 5, 5), holidays)   # Liberation Day
        self.assertIn(date(2015, 5, 14), holidays)  # Ascension
        self.assertIn(date(2015, 5, 24), holidays)  # whit sunday
        self.assertIn(date(2015, 5, 25), holidays)  # whit monday
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas
        self.assertIn(date(2015, 12, 26), holidays)  # St. Stephen´s Day

    def test_year_2025(self):
        """ In 2025 King's Day is on 26 April """
        holidays = self.cal.holidays_set(2025)
        self.assertIn(date(2025, 4, 26), holidays)   # King's Day

    def test_year_1990(self):
        """ In 1990 Queen's day was on 30 April """
        holidays = self.cal.holidays_set(1990)
        self.assertIn(date(1990, 4, 30), holidays)   # Queen's Day

    def test_new_years_eve(self):
        # For some reason, the new year's eve was added to the list of fixed
        # holidays. It appears it's not a holiday
        holidays = self.cal.holidays_set(2016)
        self.assertNotIn(date(2016, 12, 31), holidays)


class Romania(GenericCalendarTest):
    cal_class = Romania

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # Anul Nou New Year's Day
        self.assertIn(date(2017, 1, 2), holidays)  # Anul Nou Day after New Yr
        self.assertIn(date(2017, 1, 24), holidays)  # Unirea Principatelor Rom
        self.assertIn(date(2017, 4, 14), holidays)  # Orthodox Good Fri
        self.assertIn(date(2017, 4, 16), holidays)  # Orthodox Easter Sun
        self.assertIn(date(2017, 4, 17), holidays)  # Orthodox Easter Mon
        self.assertIn(date(2017, 5, 1), holidays)  # Ziua Muncii Labour Day
        self.assertIn(date(2017, 6, 1), holidays)  # Ziua Copilului Children's
        self.assertIn(date(2017, 6, 4), holidays)  # Pentecost
        self.assertIn(date(2017, 6, 5), holidays)  # Whit Monday
        self.assertIn(date(2017, 8, 15), holidays)  # Adormirea Maicii Domnului
        self.assertIn(date(2017, 11, 30), holidays)  # Sfântul Andrei St. Andre
        self.assertIn(date(2017, 12, 1), holidays)  # Ziua Națională/Marea Unir
        self.assertIn(date(2017, 12, 25), holidays)  # Crăciunul Christmas
        self.assertIn(date(2017, 12, 26), holidays)  # Crăciunul Christmas


class UnitedKingdomTest(GenericCalendarTest):
    cal_class = UnitedKingdom

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year day
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 6), holidays)  # Early May Bank Holiday
        self.assertIn(date(2013, 5, 27), holidays)  # Spring Bank Holiday
        self.assertIn(date(2013, 8, 26), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day

    def test_shift_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)  # new year day
        self.assertIn(date(2012, 1, 2), holidays)  # new year day shift

    def test_shift_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 12, 25), holidays)  # Christmas it's sunday
        self.assertIn(date(2011, 12, 26), holidays)  # XMas day shift
        self.assertIn(date(2011, 12, 27), holidays)  # Boxing day shift

    def test_shift_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas it's friday
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing day it's saturday
        self.assertIn(date(2015, 12, 28), holidays)  # Boxing day shift


class UnitedKingdomNorthernIrelandTest(UnitedKingdomTest):
    cal_class = UnitedKingdomNorthernIreland

    def test_regional_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 17), holidays)  # St Patrick's day
        self.assertIn(date(2013, 3, 18), holidays)  # St Patrick's sub
        self.assertIn(date(2013, 7, 12), holidays)  # Battle of the Boyne

    def test_regional_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 7, 12), holidays)  # Battle of the Boyne
        self.assertIn(date(2014, 7, 14), holidays)  # Battle of the Boyne sub


class EuropeanCentralBankTest(GenericCalendarTest):
    cal_class = EuropeanCentralBank

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # New year's day
        self.assertIn(date(2014, 4, 18), holidays)  # Good friday
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 5, 1), holidays)  # Labour day
        self.assertIn(date(2014, 12, 25), holidays)  # XMas
        self.assertIn(date(2014, 12, 26), holidays)  # St Stephen


class BelgiumTest(GenericCalendarTest):
    cal_class = Belgium

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 7, 21), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 11, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 21), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class GermanyTest(GenericCalendarTest):
    cal_class = Germany

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 10, 3), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 10, 3), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)

    def test_year_reformation_day(self):
        # Reformation Day is included each year in:
        # Brandenburg, MecklenburgVorpommern, Saxony, SaxonyAnhalt & Thuringia
        holidays = self.cal.holidays_set(2015)
        if self.cal.include_reformation_day:
            self.assertIn(date(2015, 10, 31), holidays)
        else:
            self.assertNotIn(date(2015, 10, 31), holidays)
        # But in the year 2017, it's included for the whole country
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 31), holidays)


class BadenWurttembergTest(GermanyTest):
    cal_class = BadenWurttemberg

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 6), holidays)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 6), holidays)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class BavariaTest(GenericCalendarTest):
    cal_class = Bavaria

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 6), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 10, 3), holidays)
        self.assertIn(date(2014, 11, 1), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 6), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 10, 3), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class BerlinTest(GermanyTest):
    cal_class = Berlin


class BrandenburgTest(GenericCalendarTest):
    cal_class = Brandenburg

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 20), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 10, 3), holidays)
        self.assertIn(date(2014, 10, 31), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 5), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 10, 3), holidays)
        self.assertIn(date(2015, 10, 31), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class BremenTest(GermanyTest):
    cal_class = Bremen


class HamburgTest(GermanyTest):
    cal_class = Hamburg


class HesseTest(GermanyTest):
    cal_class = Hesse

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)


class MecklenburgVorpommernTest(GermanyTest):
    cal_class = MecklenburgVorpommern

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 10, 31), holidays)


class LowerSaxonyTest(GermanyTest):
    cal_class = LowerSaxony


class NorthRhineWestphaliaTest(GermanyTest):
    cal_class = NorthRhineWestphalia

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class RhinelandPalatinateTest(GermanyTest):
    cal_class = RhinelandPalatinate

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class SaarlandTest(GermanyTest):
    cal_class = Saarland

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class SaxonyTest(GermanyTest):
    cal_class = Saxony

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 19), holidays)
        self.assertIn(date(2014, 10, 31), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 11, 18), holidays)
        self.assertIn(date(2015, 10, 31), holidays)

    def test_extra_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 11, 16), holidays)
        self.assertNotIn(date(2016, 11, 23), holidays)
        self.assertIn(date(2016, 10, 31), holidays)


class SaxonyAnhaltTest(GermanyTest):
    cal_class = SaxonyAnhalt

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)
        self.assertIn(date(2014, 1, 6), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 10, 31), holidays)
        self.assertIn(date(2015, 1, 6), holidays)


class SchleswigHolsteinTest(GermanyTest):
    cal_class = SchleswigHolstein


class ThuringiaTest(GermanyTest):
    cal_class = Thuringia

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 10, 31), holidays)


class PortugalTest(GenericCalendarTest):
    cal_class = Portugal

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # Ano Novo
        self.assertIn(date(2015, 2, 17), holidays)  # Entrudo
        self.assertIn(date(2015, 4, 3), holidays)  # Sexta-Feira Santa
        self.assertIn(date(2015, 4, 5), holidays)  # Domingo de Páscoa
        self.assertIn(date(2015, 4, 25), holidays)  # Dia da Liberdade
        self.assertIn(date(2015, 5, 1), holidays)  # Dia do Trabalhador
        self.assertIn(date(2015, 6, 10), holidays)  # Dia de Portugal
        self.assertIn(date(2015, 8, 15), holidays)  # Assunção de Nossa Senhora
        self.assertIn(date(2015, 12, 8), holidays)  # Imaculada Conceição
        self.assertIn(date(2015, 12, 25), holidays)  # Natal

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # Ano Novo
        self.assertIn(date(2016, 2, 9), holidays)  # Entrudo
        self.assertIn(date(2016, 3, 25), holidays)  # Sexta-Feira Santa
        self.assertIn(date(2016, 3, 27), holidays)  # Domingo de Páscoa
        self.assertIn(date(2016, 4, 25), holidays)  # Dia da Liberdade
        self.assertIn(date(2016, 5, 1), holidays)  # Dia do Trabalhador
        self.assertIn(date(2016, 6, 10), holidays)  # Dia de Portugal
        self.assertIn(date(2016, 8, 15), holidays)  # Assunção de Nossa Senhora
        self.assertIn(date(2016, 12, 8), holidays)  # Imaculada Conceição
        self.assertIn(date(2016, 12, 25), holidays)  # Natal


class SpainTest(GenericCalendarTest):
    cal_class = Spain

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 6), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 12, 8), holidays)
        self.assertIn(date(2015, 12, 25), holidays)

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 1, 6), holidays)
        self.assertIn(date(2016, 3, 25), holidays)
        self.assertIn(date(2016, 8, 15), holidays)
        self.assertIn(date(2016, 10, 12), holidays)
        self.assertIn(date(2016, 11, 1), holidays)
        self.assertIn(date(2016, 12, 6), holidays)
        self.assertIn(date(2016, 12, 8), holidays)


class CataloniaTest(GenericCalendarTest):
    cal_class = Catalonia

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 6), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 6, 24), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 9, 11), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 6), holidays)
        self.assertIn(date(2015, 12, 8), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 1, 6), holidays)
        self.assertIn(date(2016, 3, 25), holidays)
        self.assertIn(date(2016, 3, 28), holidays)
        self.assertIn(date(2016, 6, 24), holidays)
        self.assertIn(date(2016, 8, 15), holidays)
        self.assertIn(date(2016, 9, 11), holidays)
        self.assertIn(date(2016, 10, 12), holidays)
        self.assertIn(date(2016, 11, 1), holidays)
        self.assertIn(date(2016, 12, 6), holidays)
        self.assertIn(date(2016, 12, 8), holidays)
        self.assertIn(date(2016, 12, 25), holidays)
        self.assertIn(date(2016, 12, 26), holidays)


class SloveniaTest(GenericCalendarTest):
    cal_class = Slovenia

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 2, 8), holidays)
        self.assertIn(date(2015, 4, 5), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 2), holidays)
        self.assertIn(date(2015, 5, 24), holidays)
        self.assertIn(date(2015, 6, 25), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 10, 31), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 2, 8), holidays)
        self.assertIn(date(2016, 3, 27), holidays)
        self.assertIn(date(2016, 3, 28), holidays)
        self.assertIn(date(2016, 4, 27), holidays)
        self.assertIn(date(2016, 5, 1), holidays)
        self.assertIn(date(2016, 5, 2), holidays)
        self.assertIn(date(2016, 5, 15), holidays)
        self.assertIn(date(2016, 6, 25), holidays)
        self.assertIn(date(2016, 8, 15), holidays)
        self.assertIn(date(2016, 10, 31), holidays)
        self.assertIn(date(2016, 11, 1), holidays)
        self.assertIn(date(2016, 12, 25), holidays)
        self.assertIn(date(2016, 12, 26), holidays)

    def test_january_second(self):
        # From 1955 until May 2012, when the National Assembly of Slovenia
        # passed the Public Finance Balance Act, 2 January was a work-free day.
        # It has been re-introduced in 2017.
        # Source - Wikipedia
        # https://en.wikipedia.org/wiki/Public_holidays_in_Slovenia

        # Before 1955...
        holidays = self.cal.holidays_set(1953)
        self.assertNotIn(date(1953, 1, 2), holidays)
        holidays = self.cal.holidays_set(1954)
        self.assertNotIn(date(1953, 1, 2), holidays)
        # Ranging from 1955 to 2012
        for year in range(1955, 2013):
            holidays = self.cal.holidays_set(year)
            self.assertIn(date(year, 1, 2), holidays)

        # As of 2012, it was no more
        for year in range(2013, 2017):
            holidays = self.cal.holidays_set(year)
            self.assertNotIn(date(year, 1, 2), holidays)

        # In 2017, january 2nd became a state holiday
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 2), holidays)


class SwitzerlandTest(GenericCalendarTest):
    cal_class = Switzerland

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 2), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 5), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 24), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 8, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 1, 2), holidays)
        self.assertIn(date(2016, 3, 25), holidays)
        self.assertIn(date(2016, 3, 28), holidays)
        self.assertIn(date(2016, 5, 1), holidays)
        self.assertIn(date(2016, 5, 5), holidays)
        self.assertIn(date(2016, 5, 15), holidays)
        self.assertIn(date(2016, 5, 16), holidays)
        self.assertIn(date(2016, 8, 1), holidays)
        self.assertIn(date(2016, 12, 25), holidays)
        self.assertIn(date(2016, 12, 26), holidays)


class VaudTest(GenericCalendarTest):
    cal_class = Vaud

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 9, 19), holidays)
        self.assertNotIn(date(2016, 5, 1), holidays)
        self.assertNotIn(date(2016, 12, 26), holidays)

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 9, 18), holidays)
        self.assertNotIn(date(2017, 5, 1), holidays)
        self.assertNotIn(date(2017, 12, 26), holidays)


class EstoniaTest(GenericCalendarTest):
    cal_class = Estonia

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # new year
        self.assertIn(date(2015, 2, 24), holidays)  # independence day
        self.assertIn(date(2015, 4, 3), holidays)  # good friday
        self.assertIn(date(2015, 4, 5), holidays)  # easter sunday
        self.assertIn(date(2015, 5, 1), holidays)  # spring day
        self.assertIn(date(2015, 5, 24), holidays)  # pentecost
        self.assertIn(date(2015, 6, 23), holidays)  # victory day
        self.assertIn(date(2015, 6, 24), holidays)  # midsummer day
        self.assertIn(date(2015, 8, 20), holidays)  # restoration of independ.
        self.assertIn(date(2015, 12, 24), holidays)  # XMas eve
        self.assertIn(date(2015, 12, 25), holidays)  # XMas
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing day

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # new year
        self.assertIn(date(2016, 2, 24), holidays)  # independence day
        self.assertIn(date(2016, 3, 25), holidays)  # good friday
        self.assertIn(date(2016, 3, 27), holidays)  # easter sunday
        self.assertIn(date(2016, 5, 1), holidays)  # spring day
        self.assertIn(date(2016, 5, 15), holidays)  # pentecost
        self.assertIn(date(2016, 6, 23), holidays)  # victory day
        self.assertIn(date(2016, 6, 24), holidays)  # midsummer day
        self.assertIn(date(2016, 8, 20), holidays)  # restoration of independ.
        self.assertIn(date(2016, 12, 24), holidays)  # XMas eve
        self.assertIn(date(2016, 12, 25), holidays)  # XMas
        self.assertIn(date(2016, 12, 26), holidays)  # Boxing day
