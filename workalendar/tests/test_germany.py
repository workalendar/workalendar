from datetime import date
from unittest import TestCase

from workalendar.tests import GenericCalendarTest
from workalendar.europe import (Germany, BadenWurttemberg, Bavaria, Berlin,
                                Brandenburg, Bremen, Hamburg, Hesse,
                                MecklenburgVorpommern, LowerSaxony,
                                NorthRhineWestphalia, RhinelandPalatinate,
                                Saarland, Saxony, SaxonyAnhalt,
                                SchleswigHolstein, Thuringia)


class ReformationFlagTest(TestCase):
    def test_flags_reformation_day(self):
        klasses = (
            BadenWurttemberg, Bavaria, Berlin, Brandenburg, Bremen, Hamburg,
            Hesse, MecklenburgVorpommern, LowerSaxony, NorthRhineWestphalia,
            RhinelandPalatinate, Saarland, Saxony, SaxonyAnhalt,
            SchleswigHolstein, Thuringia
        )
        for klass in klasses:
            if klass in (Bremen, Hamburg, LowerSaxony, SchleswigHolstein):
                self.assertTrue(klass.include_reformation_day_2018)
            else:
                self.assertFalse(klass.include_reformation_day_2018)


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
        if self.cal.include_reformation_day(2015):
            self.assertIn(date(2015, 10, 31), holidays)
        else:
            self.assertNotIn(date(2015, 10, 31), holidays)

        # But in the year 2017, it's included for the whole country
        holidays = self.cal.holidays_set(2017)
        self.assertTrue(self.cal.include_reformation_day(2017))
        self.assertIn(date(2017, 10, 31), holidays)

        # In 2018, Four more states have added it:
        # Bremen, Hamburg, Lower Saxony and Schleswig-Holstein
        holidays = self.cal.holidays_set(2018)
        if self.cal.include_reformation_day(2018):
            self.assertIn(date(2018, 10, 31), holidays)
        else:
            self.assertNotIn(date(2018, 10, 31), holidays)


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

    def test_extra_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertNotIn(date(2018, 3, 8), holidays)
        self.assertNotIn(date(2018, 5, 8), holidays)

    def test_extra_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 3, 8), holidays)
        self.assertNotIn(date(2019, 5, 8), holidays)

    def test_extra_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 3, 8), holidays)
        self.assertIn(date(2020, 5, 8), holidays)

    def test_extra_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 3, 8), holidays)
        self.assertNotIn(date(2021, 5, 8), holidays)


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
