# -*- coding: utf-8 -*-
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.usa import (UnitedStates, Alabama, Florida, Arkansas,
                             Alaska, Arizona, California, Colorado,
                             Connecticut, Delaware, Georgia, Indiana,
                             Illinois, Idaho, Iowa, Kansas, Kentucky,
                             Louisiana, Maine, Maryland, Massachusetts,
                             Minnesota, Michigan, Mississippi, Missouri,
                             Montana, Nebraska, Nevada, NewHampshire,
                             NewJersey, NewMexico, NewYork, NorthCarolina,
                             NorthDakota, Ohio, Oklahoma, Oregon, Pennsylvania,
                             RhodeIsland, SouthCarolina, SouthDakota,
                             Tennessee, Texas, Utah, Vermont, Virginia,
                             Washington, WestVirginia, Wisconsin, Wyoming)


class UnitedStatesTest(GenericCalendarTest):
    cal_class = UnitedStates

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
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
        self.assertTrue(UnitedStates.is_presidential_year(2012))
        self.assertFalse(UnitedStates.is_presidential_year(2013))
        self.assertFalse(UnitedStates.is_presidential_year(2014))
        self.assertFalse(UnitedStates.is_presidential_year(2015))
        self.assertTrue(UnitedStates.is_presidential_year(2016))

    def test_inauguration_day(self):
        holidays = self.cal.holidays_set(2008)
        self.assertNotIn(date(2008, 1, 20), holidays)
        holidays = self.cal.holidays_set(2009)
        self.assertIn(date(2009, 1, 20), holidays)
        # case when inauguration day is a sunday
        holidays = self.cal.holidays_set(1985)
        self.assertNotIn(date(1985, 1, 20), holidays)
        self.assertIn(date(1985, 1, 21), holidays)


class AlabamaTest(GenericCalendarTest):
    cal_class = Alabama

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 28), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 6, 2), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 6, 1), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)

    def test_year_2010(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 1, 1), holidays)
        self.assertIn(date(2010, 1, 18), holidays)
        self.assertIn(date(2010, 2, 15), holidays)
        self.assertIn(date(2010, 4, 26), holidays)
        self.assertIn(date(2010, 5, 31), holidays)
        self.assertIn(date(2010, 6, 7), holidays)
        self.assertIn(date(2010, 7, 5), holidays)
        self.assertIn(date(2010, 9, 6), holidays)
        self.assertIn(date(2010, 10, 11), holidays)
        self.assertIn(date(2010, 11, 11), holidays)
        self.assertIn(date(2010, 11, 25), holidays)
        self.assertIn(date(2010, 12, 24), holidays)
        self.assertIn(date(2010, 12, 31), holidays)


class AlaskaTest(GenericCalendarTest):
    cal_class = Alaska

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 3, 31), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 17), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 3, 30), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 19), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class ArizonaTest(GenericCalendarTest):
    cal_class = Arizona

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class ArkansasTest(GenericCalendarTest):
    cal_class = Arkansas

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)

    def test_christmas_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 12, 23), holidays)
        self.assertIn(date(2016, 12, 26), holidays)

    def test_christmas_2010(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 12, 23), holidays)
        self.assertIn(date(2010, 12, 24), holidays)


class CaliforniaTest(GenericCalendarTest):
    cal_class = California

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 3, 31), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 3, 31), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class ColoradoTest(GenericCalendarTest):
    cal_class = Colorado

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 3, 31), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 3, 31), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class ConnecticutTest(GenericCalendarTest):
    cal_class = Connecticut

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 12), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 12), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class DelawareTest(GenericCalendarTest):
    cal_class = Delaware

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class FloridaTest(GenericCalendarTest):
    cal_class = Florida

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class GeorgiaTest(GenericCalendarTest):
    cal_class = Georgia

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 4, 28), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 24), holidays)


class HawaiiTest(GenericCalendarTest):
    pass


class IdahoTest(GenericCalendarTest):
    cal_class = Idaho

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class IllinoisTest(GenericCalendarTest):
    cal_class = Illinois

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 12), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 12), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class IndianaTest(GenericCalendarTest):
    cal_class = Indiana

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 24), holidays)


class IowaTest(GenericCalendarTest):
    cal_class = Iowa

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class KansasTest(GenericCalendarTest):
    cal_class = Kansas

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class KentuckyTest(GenericCalendarTest):
    cal_class = Kentucky

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class LouisianaTest(GenericCalendarTest):
    cal_class = Louisiana

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 3, 4), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 17), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class MaineTest(GenericCalendarTest):
    cal_class = Maine

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 20), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class MarylandTest(GenericCalendarTest):
    cal_class = Maryland

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class MassachusettsTest(GenericCalendarTest):
    cal_class = Massachusetts

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 20), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class MichiganTest(GenericCalendarTest):
    cal_class = Michigan

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 31), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 31), holidays)


class MinnesotaTest(GenericCalendarTest):
    cal_class = Minnesota

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class MississippiTest(GenericCalendarTest):
    cal_class = Mississippi

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 28), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class MissouriTest(GenericCalendarTest):
    cal_class = Missouri

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 12), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 8), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 8), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class MontanaTest(GenericCalendarTest):
    cal_class = Montana

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class NebraskaTest(GenericCalendarTest):
    cal_class = Nebraska

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 25), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 24), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class NevadaTest(GenericCalendarTest):
    cal_class = Nevada

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 31), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 30), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class NewHampshireTest(GenericCalendarTest):
    cal_class = NewHampshire

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class NewJerseyTest(GenericCalendarTest):
    cal_class = NewJersey

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class NewMexicoTest(GenericCalendarTest):
    cal_class = NewMexico

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class NewYorkTest(GenericCalendarTest):
    cal_class = NewYork

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 12), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 12), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class NorthCarolinaTest(GenericCalendarTest):
    cal_class = NorthCarolina

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class NorthDakotaTest(GenericCalendarTest):
    cal_class = NorthDakota

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class OhioTest(GenericCalendarTest):
    cal_class = Ohio

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 1), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class OklahomaTest(GenericCalendarTest):
    cal_class = Oklahoma

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class OregonTest(GenericCalendarTest):
    cal_class = Oregon

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class Pennsylvania(GenericCalendarTest):
    cal_class = Pennsylvania

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class RhodeIslandTest(GenericCalendarTest):
    cal_class = RhodeIsland

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 8, 11), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 8, 10), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class SouthCarolinaTest(GenericCalendarTest):
    cal_class = SouthCarolina

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 9), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 10), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class SouthDakotaTest(GenericCalendarTest):
    cal_class = SouthDakota

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class TennesseeTest(GenericCalendarTest):
    cal_class = Tennessee

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class TexasTest(GenericCalendarTest):
    cal_class = Texas

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 19), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 3, 2), holidays)
        self.assertIn(date(2014, 3, 31), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 8, 27), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 3, 2), holidays)
        self.assertIn(date(2015, 3, 31), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 21), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 6, 19), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 8, 27), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class UtahTest(GenericCalendarTest):
    cal_class = Utah

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 7, 24), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 7, 24), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class VermontTest(GenericCalendarTest):
    cal_class = Vermont

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 3, 4), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 3, 3), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 8, 17), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class VirginiaTest(GenericCalendarTest):
    cal_class = Virginia

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 17), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 26), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 16), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 25), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class WashingtonTest(GenericCalendarTest):
    cal_class = Washington

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class WestVirginiaTest(GenericCalendarTest):
    cal_class = WestVirginia

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 6, 20), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 10, 13), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 31), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 6, 20), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 31), holidays)


class WisconsinTest(GenericCalendarTest):
    cal_class = Wisconsin

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 11, 28), holidays)
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 31), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 11, 27), holidays)
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 31), holidays)


class WyomingTest(GenericCalendarTest):
    cal_class = Wyoming

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 20), holidays)
        self.assertIn(date(2014, 2, 17), holidays)
        self.assertIn(date(2014, 5, 26), holidays)
        self.assertIn(date(2014, 7, 4), holidays)
        self.assertIn(date(2014, 9, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 11, 27), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 19), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 9, 7), holidays)
        self.assertIn(date(2015, 11, 11), holidays)
        self.assertIn(date(2015, 11, 26), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
