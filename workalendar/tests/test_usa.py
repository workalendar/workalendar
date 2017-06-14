# -*- coding: utf-8 -*-
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.usa import (UnitedStates, Alabama, Florida, Arkansas,
                             Alaska, Arizona, California, Colorado,
                             Connecticut, Delaware, Georgia, Hawaii,
                             Indiana, Illinois, Idaho, Iowa, Kansas, Kentucky,
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

    def test_federal_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # New Year
        self.assertIn(date(2013, 1, 21), holidays)  # Martin Luther King
        self.assertIn(date(2013, 2, 18), holidays)  # Washington's bday
        self.assertIn(date(2013, 5, 27), holidays)  # Memorial day
        self.assertIn(date(2013, 7, 4), holidays)  # Nation day
        self.assertIn(date(2013, 9, 2), holidays)  # Labour day
        self.assertIn(date(2013, 10, 14), holidays)  # Colombus
        self.assertIn(date(2013, 11, 11), holidays)  # Armistice
        self.assertIn(date(2013, 11, 28), holidays)  # Thanskgiving
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas

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

    def test_federal_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)   # New Year
        self.assertIn(date(2014, 1, 20), holidays)  # Martin Luther King
        self.assertIn(date(2014, 2, 17), holidays)  # Washington's bday
        self.assertIn(date(2014, 5, 26), holidays)  # Memorial day
        self.assertIn(date(2014, 7, 4), holidays)  # Nation day
        self.assertIn(date(2014, 9, 1), holidays)  # Labour day
        self.assertIn(date(2014, 10, 13), holidays)  # Colombus
        self.assertIn(date(2014, 11, 11), holidays)  # Armistice
        self.assertIn(date(2014, 11, 27), holidays)  # Thanskgiving
        self.assertIn(date(2014, 12, 25), holidays)  # XMas

    def test_federal_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)   # New Year
        self.assertIn(date(2015, 1, 19), holidays)  # Martin Luther King
        self.assertIn(date(2015, 2, 16), holidays)  # Washington's bday
        self.assertIn(date(2015, 5, 25), holidays)  # Memorial day
        self.assertIn(date(2015, 7, 4), holidays)   # Nation day
        self.assertIn(date(2015, 9, 7), holidays)  # Labour day
        self.assertIn(date(2015, 10, 12), holidays)  # Colombus
        self.assertIn(date(2015, 11, 11), holidays)  # Armistice
        self.assertIn(date(2015, 11, 26), holidays)  # Thanskgiving
        self.assertIn(date(2015, 12, 25), holidays)  # XMas


class AlabamaTest(UnitedStatesTest):
    cal_class = Alabama

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 28), holidays)
        self.assertIn(date(2014, 6, 2), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 6, 1), holidays)
        self.assertIn(date(2015, 7, 3), holidays)

    def test_state_year_2010(self):
        holidays = self.cal.holidays_set(2010)
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


class AlaskaTest(UnitedStatesTest):
    cal_class = Alaska

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 31), holidays)
        self.assertIn(date(2014, 10, 17), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 30), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 10, 19), holidays)


class ArizonaTest(UnitedStatesTest):
    cal_class = Arizona

    # NOTE: Arizona only has federal holidays.
    def test_state_year_2015(self):
        # FIXME: tests for floating holidays
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)


class ArkansasTest(UnitedStatesTest):
    cal_class = Arkansas

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 12, 24), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 12, 24), holidays)

    def test_christmas_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 12, 23), holidays)
        self.assertIn(date(2016, 12, 26), holidays)

    def test_christmas_2010(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 12, 23), holidays)
        self.assertIn(date(2010, 12, 24), holidays)


class CaliforniaTest(UnitedStatesTest):
    cal_class = California

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 31), holidays)  # Cesar Chavez Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 31), holidays)  # Cesar Chavez Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class ColoradoTest(UnitedStatesTest):
    cal_class = Colorado

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 31), holidays)  # Cesar Chavez Day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 31), holidays)   # Cesar Chavez Day


class ConnecticutTest(UnitedStatesTest):
    cal_class = Connecticut

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)
        self.assertIn(date(2014, 4, 18), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)


class DelawareTest(UnitedStatesTest):
    cal_class = Delaware

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class FloridaTest(UnitedStatesTest):
    cal_class = Florida

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class GeorgiaTest(UnitedStatesTest):
    cal_class = Georgia

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 28), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 26), holidays)  # Washington bday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)  # Washington bday


class HawaiiTest(UnitedStatesTest):
    cal_class = Hawaii
    # NOTE: Hawaii only has federal holidays


class IdahoTest(UnitedStatesTest):
    cal_class = Idaho

    # NOTE: Arizona only has federal holidays.
    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)


class IllinoisTest(UnitedStatesTest):
    cal_class = Illinois

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class IndianaTest(UnitedStatesTest):
    cal_class = Indiana

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 26), holidays)  # Washington bday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)  # Washington bday


class IowaTest(UnitedStatesTest):
    cal_class = Iowa

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class KansasTest(UnitedStatesTest):
    cal_class = Kansas

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class KentuckyTest(UnitedStatesTest):
    cal_class = Kentucky

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 26), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 26), holidays)


class LouisianaTest(UnitedStatesTest):
    cal_class = Louisiana

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 4), holidays)
        self.assertIn(date(2014, 4, 18), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 17), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)


class MaineTest(UnitedStatesTest):
    cal_class = Maine

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 20), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class MarylandTest(UnitedStatesTest):
    cal_class = Maryland

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class MassachusettsTest(UnitedStatesTest):
    cal_class = Massachusetts

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 21), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 20), holidays)
        self.assertIn(date(2015, 7, 3), holidays)


class MichiganTest(UnitedStatesTest):
    cal_class = Michigan

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 31), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 31), holidays)


class MinnesotaTest(UnitedStatesTest):
    cal_class = Minnesota

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class MississippiTest(UnitedStatesTest):
    cal_class = Mississippi

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 28), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class MissouriTest(UnitedStatesTest):
    cal_class = Missouri

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)
        self.assertIn(date(2014, 5, 8), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 5, 8), holidays)
        self.assertIn(date(2015, 7, 3), holidays)


class MontanaTest(UnitedStatesTest):
    cal_class = Montana

    # NOTE: Montana has only federal holidays
    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)


class NebraskaTest(UnitedStatesTest):
    cal_class = Nebraska

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 25), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 24), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class NevadaTest(UnitedStatesTest):
    cal_class = Nevada

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 10, 30), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class NewHampshireTest(UnitedStatesTest):
    cal_class = NewHampshire

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class NewJerseyTest(UnitedStatesTest):
    cal_class = NewJersey

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)


class NewMexicoTest(UnitedStatesTest):
    cal_class = NewMexico

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class NewYorkTest(UnitedStatesTest):
    cal_class = NewYork

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)
        self.assertIn(date(2015, 7, 3), holidays)


class NorthCarolinaTest(UnitedStatesTest):
    cal_class = NorthCarolina

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class NorthDakotaTest(UnitedStatesTest):
    cal_class = NorthDakota

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)


class OhioTest(UnitedStatesTest):
    cal_class = Ohio

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 12, 1), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 12, 1), holidays)


class OklahomaTest(UnitedStatesTest):
    cal_class = Oklahoma

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)


class OregonTest(UnitedStatesTest):
    cal_class = Oregon

    # NOTE: Oregon has only the federal holidays
    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)


class PennsylvaniaTest(UnitedStatesTest):
    cal_class = Pennsylvania

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class RhodeIslandTest(UnitedStatesTest):
    cal_class = RhodeIsland

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 8, 11), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 8, 10), holidays)


class SouthCarolinaTest(UnitedStatesTest):
    cal_class = SouthCarolina

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 9), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 5, 10), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class SouthDakotaTest(UnitedStatesTest):
    cal_class = SouthDakota

    # NOTE: South Dakota only has federal holidays.
    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)


class TennesseeTest(UnitedStatesTest):
    cal_class = Tennessee

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class TexasTest(UnitedStatesTest):
    cal_class = Texas

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 19), holidays)
        self.assertIn(date(2014, 3, 2), holidays)
        self.assertIn(date(2014, 3, 31), holidays)  # Cesar Chavez Day
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 8, 27), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 2), holidays)
        self.assertIn(date(2015, 3, 31), holidays)  # Cesar Chavez Day
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 21), holidays)
        self.assertIn(date(2015, 6, 19), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 8, 27), holidays)


class UtahTest(UnitedStatesTest):
    cal_class = Utah

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 7, 24), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 7, 24), holidays)


class VermontTest(UnitedStatesTest):
    cal_class = Vermont

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 4), holidays)
        self.assertIn(date(2014, 8, 15), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 3), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 8, 17), holidays)


class VirginiaTest(UnitedStatesTest):
    cal_class = Virginia

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 17), holidays)
        self.assertIn(date(2014, 11, 26), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 16), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 25), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class WashingtonTest(UnitedStatesTest):
    cal_class = Washington

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class WestVirginiaTest(UnitedStatesTest):
    cal_class = WestVirginia

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 20), holidays)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 31), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 20), holidays)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 31), holidays)


class WisconsinTest(UnitedStatesTest):
    cal_class = Wisconsin

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)
        self.assertIn(date(2014, 12, 31), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)
        self.assertIn(date(2015, 12, 31), holidays)


class WyomingTest(UnitedStatesTest):
    cal_class = Wyoming

    # NOTE: Wyoming has only federal holidays
    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
