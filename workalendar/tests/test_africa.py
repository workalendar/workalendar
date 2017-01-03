# -*- coding: utf-8 -*-
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.africa import Benin, Algeria
from workalendar.africa import SouthAfrica, IvoryCoast
from workalendar.africa import SaoTomeAndPrincipe, Madagascar
from workalendar.core import MON


class AlgeriaTest(GenericCalendarTest):
    cal_class = Algeria

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # New year
        self.assertIn(date(2013, 1, 24), holidays)   # Milad un Nabi
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 7, 5), holidays)  # Independence day
        self.assertIn(date(2013, 8, 8), holidays)  # Eid ul-fitr
        self.assertIn(date(2013, 10, 15), holidays)  # Eid el-ada
        self.assertIn(date(2013, 11, 1), holidays)  # Anniversary revolution
        self.assertIn(date(2013, 11, 5), holidays)  # New Year
        self.assertIn(date(2013, 11, 14), holidays)  # Ashura


class BeninTest(GenericCalendarTest):
    cal_class = Benin

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 20), holidays)   # Whit Monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 8, 1), holidays)  # Independence Day
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 10, 26), holidays)  # Armed Forces Day
        self.assertIn(date(2013, 11, 1), holidays)  # All Saints Day
        self.assertIn(date(2013, 11, 30), holidays)  # National Day
        self.assertIn(date(2013, 12, 25), holidays)  # christmas
        # Variable Muslim days
        self.assertIn(date(2013, 1, 24), holidays)  # Milad un Nabi
        self.assertIn(date(2013, 10, 15), holidays)  # Tabaski
        self.assertIn(date(2013, 8, 8), holidays)  # Eid al-Fitr


class SouthAfricaTest(GenericCalendarTest):
    cal_class = SouthAfrica

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 3, 21), holidays)  # human rights day
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 1), holidays)  # Easter monday / Family day
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

#    def test_pre_1994(self):
#        pass
#
#    def test_pre_1995(self):
#        pass

    def test_special_1999(self):
        # National and provincial government elections – 2 June 1999[8]
        holidays = self.cal.holidays_set(1999)
        self.assertIn(date(1999, 6, 2), holidays)

    def test_special_2000(self):
        holidays = self.cal.holidays_set(2000)
        self.assertIn(date(2000, 1, 2), holidays)
        self.assertIn(date(2000, 1, 3), holidays)

    def test_special_2004(self):
        # National and provincial government elections – 14 April 2004[9]
        holidays = self.cal.holidays_set(2004)
        self.assertIn(date(2004, 4, 14), holidays)

    def test_special_2006(self):
        # Local government elections – 1 March 2006[10]
        holidays = self.cal.holidays_set(2006)
        self.assertIn(date(2006, 3, 1), holidays)

    def test_special_2008(self):
        # 2 May 2008 was declared a public holiday when Human Rights Day
        # and Good Friday coincided on 21 March 2008.
        holidays = self.cal.holidays_set(2008)
        self.assertIn(date(2008, 5, 2), holidays)

    def test_special_2009(self):
        # National and provincial government elections – 22 April 2009[11]
        holidays = self.cal.holidays_set(2009)
        self.assertIn(date(2009, 4, 22), holidays)

    def test_special_2011(self):
        # Local government elections – 18 May 2011[12]
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 5, 18), holidays)
        # 27 December 2011 was declared a holiday by president Motlanthe
        self.assertIn(date(2011, 12, 27), holidays)

    def test_special_2014(self):
        # National and provincial government elections – 7 May 2014[13]
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 7), holidays)

    def test_special_2016(self):
        # Local government elections – 3 August 2016[14]
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 8, 3), holidays)

    def test_historical_1973(self):
        # Ascension Day	1910–1993
        holidays = self.cal.holidays_set(1973)
        self.assertIn(self.cal.get_ascension_thursday(1973), holidays)

    def test_historical_1974(self):
        holidays = self.cal.holidays_set(1974)
        # 6 April	Van Riebeeck's Day / Founder's Day
        self.assertIn(date(1974, 4, 6), holidays)
        # 31 May	Union Day / Republic Day
        self.assertIn(date(1974, 5, 31), holidays)
        # 10 July	Family Day	1961–1974
        self.assertIn(date(1974, 7, 10), holidays)
        # 1st Monday in September	Settlers' Day	1952–1979
        self.assertIn(self.cal.get_nth_weekday_in_month(1974, 9, MON, 1),
                      holidays)
        # 10 October	Kruger Day	1952–1993
        self.assertIn(date(1974, 10, 10), holidays)

    def test_historical_empire(self):
        holidays = self.cal.holidays_set(1951)
        # 24 May	Victoria Day / Empire Day	1910–1951
        self.assertIn(date(1951, 5, 24), holidays)

    def test_queens_birthday(self):
        # 2nd Monday in July	Queen's Birthday	1952–1960
        holidays = self.cal.holidays_set(1960)
        self.assertIn(date(1960, 5, 2), holidays)


class Madagascar(GenericCalendarTest):
    cal_class = Madagascar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 3, 29), holidays)  # martyrs day
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 20), holidays)  # whit monday
        self.assertIn(date(2013, 6, 26), holidays)  # independence day
        self.assertIn(date(2013, 8, 15), holidays)  # assumption
        self.assertIn(date(2013, 11, 1), holidays)  # all saints
        self.assertIn(date(2013, 12, 25), holidays)  # XMas


class IvoryCoastTest(GenericCalendarTest):
    cal_class = IvoryCoast

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 20), holidays)  # whit monday
        self.assertIn(date(2013, 8, 7), holidays)  # Independence day
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 11, 1), holidays)  # All saints
        self.assertIn(date(2013, 11, 15), holidays)  # National peace day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        # Muslim days
        self.assertIn(date(2013, 1, 25), holidays)  # Mawlid al-Nabi
        # Laylat al-Qadr is not computable
        # self.assertIn(date(2013, 8, 3), holidays)
        self.assertIn(date(2013, 8, 8), holidays)  # End of ramadan
        self.assertIn(date(2013, 10, 15), holidays)  # Feast of sacrifice


class SaoTomeAndPrincipeTest(GenericCalendarTest):
    cal_class = SaoTomeAndPrincipe

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 2, 3), holidays)  # Martyrs' day
        self.assertIn(date(2013, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2013, 7, 12), holidays)  # Independence Day
        self.assertIn(date(2013, 9, 6), holidays)  # Armed Forces Day
        self.assertIn(date(2013, 9, 30), holidays)  # Agricultural Reform Day
        self.assertIn(date(2013, 11, 1), holidays)  # All saints
        self.assertIn(date(2013, 12, 21), holidays)  # São Tomé Day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
