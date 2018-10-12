# -*- coding: utf-8 -*-
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.africa import (
    Algeria,
    Angola,
    Benin,
    IvoryCoast,
    Madagascar,
    SaoTomeAndPrincipe,
    SouthAfrica,
)
from workalendar.core import MON, FRI
from workalendar.exceptions import CalendarError


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

    def test_before_1910(self):
        with self.assertRaises(CalendarError):
            self.cal.holidays_set(1909)

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 3, 21), holidays)  # human rights day
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
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

    def test_easter_monday(self):
        # 1910-1979, Easter Monday label was "Easter Monday"
        holidays = self.cal.holidays(1979)
        easter_monday_1979 = date(1979, 4, 16)
        holidays_dates = [item[0] for item in holidays]
        self.assertEqual(holidays_dates.count(easter_monday_1979), 1, holidays)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[easter_monday_1979], "Easter Monday")

        # From 1980 to "now", it's Family Day
        holidays = self.cal.holidays(1980)
        # Since the Founders' day is a Sunday, the same date appears twice
        # The second one is a substitute
        holidays = [item for item in holidays
                    if item[1] != "Founder's Day substitute"]
        easter_monday_1980 = date(1980, 4, 7)
        holidays_dates = [item[0] for item in holidays]
        self.assertEqual(holidays_dates.count(easter_monday_1980), 1, holidays)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[easter_monday_1980], "Family Day")

    def test_april_6th(self):
        # 1951, no April 6th
        holidays = self.cal.holidays(1951)
        holidays_dates = [item[0] for item in holidays]
        april_6th = date(1951, 4, 6)
        self.assertNotIn(april_6th, holidays_dates, holidays)

        # 1952-1973, it was named Van Riebeeck's day
        holidays = self.cal.holidays(1952)
        holidays_dates = [item[0] for item in holidays]
        april_6th = date(1952, 4, 6)
        self.assertIn(april_6th, holidays_dates, holidays)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[april_6th], "Van Riebeeck's Day")

        # 1974: No April 6th
        holidays = self.cal.holidays(1974)
        holidays_dates = [item[0] for item in holidays]
        april_6th = date(1974, 4, 6)
        self.assertNotIn(april_6th, holidays_dates, holidays)

        # 1980-1994, it became Founder's day
        holidays = self.cal.holidays(1980)
        holidays_dates = [item[0] for item in holidays]
        april_6th = date(1980, 4, 6)
        self.assertIn(april_6th, holidays_dates, holidays)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[april_6th], "Founder's Day")

        # 1995, no April 6th
        holidays = self.cal.holidays(1995)
        holidays_dates = [item[0] for item in holidays]
        april_6th = date(1995, 4, 6)
        self.assertNotIn(april_6th, holidays_dates, holidays)

    def test_workers_day(self):
        # No Workers' day before 1987
        holidays = self.cal.holidays(1986)
        holidays_labels = [item[1] for item in holidays]
        self.assertNotIn("Workers' Day", holidays_labels, holidays)

        # 1987-1989: 1st Friday in May
        holidays = self.cal.holidays(1987)
        holidays_dates = [item[0] for item in holidays]
        first_friday_may = self.cal.get_nth_weekday_in_month(1987, 5, FRI)
        self.assertIn(first_friday_may, holidays_dates)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[first_friday_may], "Workers' Day")

        # 1990-1994: No Workers' day
        holidays = self.cal.holidays(1990)
        holidays_labels = [item[1] for item in holidays]
        self.assertNotIn("Workers' Day", holidays_labels, holidays)

        # as of 1995: Workers' day is on May 1st
        holidays = self.cal.holidays(1995)
        holidays_dates = [item[0] for item in holidays]
        first_may = date(1995, 5, 1)
        self.assertIn(first_may, holidays_dates)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[first_may], "Workers' Day")

    def test_ascension_day(self):
        # Before 1993 (included), Ascension day was a holiday
        holidays = self.cal.holidays(1993)
        holidays_dates = [item[0] for item in holidays]
        ascension_1993 = self.cal.get_ascension_thursday(1993)
        self.assertIn(ascension_1993, holidays_dates)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[ascension_1993], "Ascension Day")

        # After 1993, no more Ascension day
        holidays = self.cal.holidays(1994)
        holidays_dates = [item[0] for item in holidays]
        ascension_1994 = self.cal.get_ascension_thursday(1994)
        self.assertNotIn(ascension_1994, holidays_dates)

    def test_victoria_empire_day(self):
        # 1910–1951: 24 May is Victoria Day / Empire Day
        holidays = self.cal.holidays(1951)
        holidays_dates = [item[0] for item in holidays]
        may_24th_1951 = date(1951, 5, 24)
        self.assertIn(may_24th_1951, holidays_dates, holidays)
        holidays_dict = dict(holidays)
        self.assertEqual(
            holidays_dict[may_24th_1951], "Victoria Day / Empire Day")

        # 1952-present, no Victoria / Empire day
        holidays = self.cal.holidays(1952)
        holidays_dates = [item[0] for item in holidays]
        may_24th_1952 = date(1952, 5, 24)
        self.assertNotIn(may_24th_1952, holidays_dates, holidays)

    def test_may_31st(self):
        # 1910-1960, it's Union Day
        holidays = self.cal.holidays(1960)
        holidays_dates = [item[0] for item in holidays]
        may_31st_1960 = date(1960, 5, 31)
        self.assertIn(may_31st_1960, holidays_dates, holidays)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[may_31st_1960], "Union Day")

        # 1961-1993, it's Republic Day
        holidays = self.cal.holidays(1993)
        holidays_dates = [item[0] for item in holidays]
        may_31st_1993 = date(1993, 5, 31)
        self.assertIn(may_31st_1993, holidays_dates, holidays)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[may_31st_1993], "Republic Day")

        # As of 1994, no more may 31st
        holidays = self.cal.holidays(1994)
        holidays_dates = [item[0] for item in holidays]
        may_31st_1994 = date(1994, 5, 31)
        self.assertNotIn(may_31st_1994, holidays_dates, holidays)

    def test_queens_birthday(self):
        # Before 1952, no Queens Birthday
        holidays = self.cal.holidays(1951)
        holidays_dates = [item[0] for item in holidays]
        july_2nd_monday = self.cal.get_nth_weekday_in_month(1951, 7, MON, 2)
        self.assertNotIn(july_2nd_monday, holidays_dates)

        # 1952–1960: 2nd Monday in July is Queen's Birthday
        for year in (1952, 1959, 1960):  # interval of the years
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            july_2nd_monday = self.cal.get_nth_weekday_in_month(
                year, 7, MON, 2)
            self.assertIn(july_2nd_monday, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(
                holidays_dict[july_2nd_monday],
                "Queen's Birthday"
            )

        # After 1961, no more Queen's Birthday
        for year in (1961, 1962, 2008, 2018):  # interval of the years
            holidays = self.cal.holidays(year)
            holidays_labels = [item[1] for item in holidays]
            self.assertNotIn("Queen's Birthday", holidays_labels)

    def test_womens_day_label(self):
        holidays = self.cal.holidays(2018)
        womens_day = date(2018, 8, 9)
        holidays_dict = dict(holidays)
        self.assertEqual(
            holidays_dict[womens_day],
            "National Women's Day"
        )

    def test_family_day_in_july(self):
        # Before 1961, no Family day in July
        holidays = self.cal.holidays(1960)
        holidays_dates = [item[0] for item in holidays]
        family_day = date(1960, 7, 10)
        self.assertNotIn(family_day, holidays_dates)

        # From 1961 to 1973, Family day is on July 10th
        for year in (1961, 1970, 1973):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            family_day = date(year, 7, 10)
            self.assertIn(family_day, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(holidays_dict[family_day], "Family Day")

        # As of 1974, no more
        for year in (1974, 1980, 1990, 2018):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            family_day = date(year, 7, 10)
            self.assertNotIn(family_day, holidays_dates)

    def test_king_birthday(self):
        # From 1910 to 1951, 1st Monday in August
        for year in (1910, 1935, 1951):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            king_birthday = self.cal.get_nth_weekday_in_month(year, 8, MON)
            self.assertIn(king_birthday, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(holidays_dict[king_birthday], "King's Birthday")

        # Not after 1952
        for year in (1952, 1960, 1990, 2018):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            king_birthday = self.cal.get_nth_weekday_in_month(year, 8, MON)
            self.assertNotIn(king_birthday, holidays_dates)

    def test_settlers_day(self):
        # Before 1952, no settler's day
        holidays = self.cal.holidays(1951)
        holidays_dates = [item[0] for item in holidays]
        settlers_day = self.cal.get_nth_weekday_in_month(1951, 9, MON)
        self.assertNotIn(settlers_day, holidays_dates)

        # From 1952 to 1979, 1st Monday in August
        for year in (1952, 1960, 1952, 1979):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            settlers_day = self.cal.get_nth_weekday_in_month(year, 9, MON)
            self.assertIn(settlers_day, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(holidays_dict[settlers_day], "Settlers' Day")

        # Not after 1979
        for year in (1980, 1990, 2018):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            settlers_day = self.cal.get_nth_weekday_in_month(year, 9, MON)
            self.assertNotIn(settlers_day, holidays_dates)

    def test_kruger_day(self):
        # Not before 1952
        holidays = self.cal.holidays(1951)
        holidays_dates = [item[0] for item in holidays]
        kruger_day = date(1951, 10, 10)
        self.assertNotIn(kruger_day, holidays_dates)

        # Kruger Day was on October 10th 1952-1993
        for year in (1952, 1960, 1952, 1979, 1993):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            kruger_day = date(year, 10, 10)
            self.assertIn(kruger_day, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(holidays_dict[kruger_day], "Kruger Day")

        # As of 1994, not anymore
        for year in (1994, 2000, 2018):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            kruger_day = date(year, 10, 10)
            self.assertNotIn(kruger_day, holidays_dates)

    def test_december_16th(self):
        # from 1910 to 1951, it's "Dingaan's Day"
        for year in (1910, 1930, 1951):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            december_16th = date(year, 12, 16)
            self.assertIn(december_16th, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(holidays_dict[december_16th], "Dingaan's Day")

        # from 1952 to 1979 it's the "Day of the Covenant"
        for year in (1952, 1960, 1979):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            december_16th = date(year, 12, 16)
            self.assertIn(december_16th, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(
                holidays_dict[december_16th], "Day of the Covenant")

        # from 1980 to 1994 it's the "Day of the Vow"
        # NOTE: wikipedia states it starts at year 1979, but that would mean
        # there were two labels on the same year, which would be wrong.
        # We may wait to see if this error is fixed one day.
        for year in (1980, 1990, 1994):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            december_16th = date(year, 12, 16)
            self.assertIn(december_16th, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(
                holidays_dict[december_16th], "Day of the Vow")

        # As of 1995, it's the "Day of Reconciliation"
        for year in (1995, 2000, 2010, 2018):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            december_16th = date(year, 12, 16)
            self.assertIn(december_16th, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(
                holidays_dict[december_16th], "Day of Reconciliation")

    def test_december_26th(self):
        # from 1910 to 1979, it's "Boxing Day"
        # Year 1910 is excluded, since Christmas was on a Sunday, and shift
        # rules apply
        for year in (1911, 1930, 1951, 1979):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            december_26th = date(year, 12, 26)
            self.assertIn(december_26th, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(holidays_dict[december_26th], "Boxing Day", year)

        # As of 1980, it's "Day of Goodwill"
        for year in (1980, 1990, 1995, 2000, 2018):
            holidays = self.cal.holidays(year)
            holidays_dates = [item[0] for item in holidays]
            december_26th = date(year, 12, 26)
            self.assertIn(december_26th, holidays_dates)
            holidays_dict = dict(holidays)
            self.assertEqual(holidays_dict[december_26th], "Day of Goodwill")

    def test_special_1999(self):
        # National and provincial government elections – 2 June 1999
        holidays = self.cal.holidays_set(1999)
        self.assertIn(date(1999, 6, 2), holidays)
        # December 31st was a "Y2K" holiday
        self.assertIn(date(1999, 12, 31), holidays)

    def test_special_2000(self):
        holidays = self.cal.holidays_set(2000)
        # Holiday added to celebrate Y2K
        self.assertIn(date(2000, 1, 2), holidays)
        # Shift day because Jan 2nd was a sunday
        self.assertIn(date(2000, 1, 3), holidays)

    def test_special_2004(self):
        # National and provincial government elections – 14 April 2004
        holidays = self.cal.holidays_set(2004)
        self.assertIn(date(2004, 4, 14), holidays)

    def test_special_2006(self):
        # Local government elections – 1 March 2006
        holidays = self.cal.holidays_set(2006)
        self.assertIn(date(2006, 3, 1), holidays)

    def test_special_2008(self):
        # 2 May 2008 was declared a public holiday when Human Rights Day
        # and Good Friday coincided on 21 March 2008.
        holidays = self.cal.holidays_set(2008)
        self.assertIn(date(2008, 5, 2), holidays)

    def test_special_2009(self):
        # National and provincial government elections – 22 April 2009
        holidays = self.cal.holidays_set(2009)
        self.assertIn(date(2009, 4, 22), holidays)

    def test_special_2011(self):
        # Local government elections – 18 May 2011
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 5, 18), holidays)
        # 27 December 2011 was declared a holiday by president Motlanthe
        self.assertIn(date(2011, 12, 27), holidays)

    def test_special_2014(self):
        # National and provincial government elections – 7 May 2014
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 7), holidays)

    def test_special_2016(self):
        # Local government elections – 3 August 2016
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 8, 3), holidays)


class MadagascarTest(GenericCalendarTest):
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


class AngolaTest(GenericCalendarTest):
    cal_class = Angola

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        # Dia de Ano Novo – 1 de Janeiro
        self.assertIn(date(2018, 1, 1), holidays)  # Ano Novo
        # Dia do Inicio da Luta Armada – 4 de Fevereiro
        self.assertIn(date(2018, 2, 4), holidays)
        # Dia do Carnaval – 13 de Fevereiro
        self.assertIn(date(2018, 2, 13), holidays)  # Entrudo
        # Dia Internacional da Mulher – 8 de Março
        self.assertIn(date(2018, 3, 8), holidays)
        # Dia da Paz – 4 de Abril
        self.assertIn(date(2018, 4, 4), holidays)  # Dia da Paz
        # Sexta Feira Santa – 30 de Março
        self.assertIn(date(2018, 3, 30), holidays)  # Sexta-Feira Santa
        # Páscoa – 01 de Abril
        self.assertIn(date(2018, 4, 1), holidays)  # Domingo de Páscoa
        # Dia Internacional do Trabalhador – 1 de Maio
        self.assertIn(date(2018, 5, 1), holidays)  # Dia do Trabalhador
        # Dia do Fundador da Nação e do Herói Nacional – 17 de Setembro
        self.assertIn(date(2018, 9, 17), holidays)
        # Dia dos Finados – 2 de Novembro
        # Dia da Independência Nacional – 11 de Novembro
        self.assertIn(date(2018, 11, 11), holidays)
        # Dia do Natal – 25 de Dezembro
        self.assertIn(date(2018, 12, 25), holidays)  # Natal
