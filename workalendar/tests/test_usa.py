# -*- coding: utf-8 -*-
from unittest import skip, skipIf
from datetime import date
import sys
import warnings

from workalendar.tests import GenericCalendarTest
from workalendar.usa import (
    UnitedStates,
    Alabama, AlabamaBaldwinCounty, AlabamaMobileCounty, AlabamaPerryCounty,
    Arkansas, Alaska, Arizona,
    # California and others
    California, CaliforniaEducation, CaliforniaBerkeley,
    CaliforniaSanFrancisco, CaliforniaWestHollywood,
    # Florida and others
    Florida, FloridaLegal, FloridaCircuitCourts, FloridaMiamiDade,
    Colorado, Connecticut, Delaware, DistrictOfColumbia, Georgia, Hawaii,
    Indiana, Illinois, Idaho, Iowa, Kansas, Kentucky, Louisiana, Maine,
    Maryland, Massachusetts, Minnesota, Michigan, Mississippi, Missouri,
    Montana, Nebraska, Nevada, NewHampshire, NewJersey, NewMexico, NewYork,
    NorthCarolina, NorthDakota, Ohio, Oklahoma, Oregon, Pennsylvania,
    RhodeIsland, SouthCarolina, SouthDakota, Tennessee, TexasBase, Texas,
    Utah, Vermont, Virginia, Washington, WestVirginia, Wisconsin, Wyoming,
    # Other territories, cities...
    AmericanSamoa, ChicagoIllinois, Guam, SuffolkCountyMassachusetts,
)

PY2 = sys.version_info[0] == 2


class UnitedStatesTest(GenericCalendarTest):
    cal_class = UnitedStates

    def test_martin_luther_king_day(self):
        # All States observe this day, but it started in 1985 only.
        holidays = self.cal.holidays_set(2013)
        mlk_day = self.cal.get_martin_luther_king_date(2013)
        self.assertEqual(date(2013, 1, 21), mlk_day)
        self.assertIn(mlk_day, holidays)

        holidays = self.cal.holidays_set(2014)
        mlk_day = self.cal.get_martin_luther_king_date(2014)
        self.assertEqual(date(2014, 1, 20), mlk_day)
        self.assertIn(mlk_day, holidays)

        # Shifted in 2015
        holidays = self.cal.holidays_set(2015)
        mlk_day = self.cal.get_martin_luther_king_date(2015)
        self.assertEqual(date(2015, 1, 19), mlk_day)
        self.assertIn(mlk_day, holidays)

        # Let's get into the past
        holidays = self.cal.holidays_set(1986)
        mlk_day = self.cal.get_martin_luther_king_date(1986)
        self.assertEqual(date(1986, 1, 20), mlk_day)
        self.assertIn(mlk_day, holidays)

        holidays = self.cal.holidays_set(1985)
        mlk_day = self.cal.get_martin_luther_king_date(1985)
        self.assertEqual(date(1985, 1, 21), mlk_day)
        self.assertIn(mlk_day, holidays)

        # No MLK Day before 1985
        # 3rd Monday of January was the 16th
        holidays = self.cal.holidays_set(1984)
        self.assertNotIn(date(1984, 1, 16), holidays)
        with self.assertRaises(ValueError):
            self.cal.get_martin_luther_king_date(1984)

    def test_mlk_label(self):
        _, label = self.cal.get_martin_luther_king_day(2017)
        self.assertEqual(label, "Birthday of Martin Luther King, Jr.")

    def test_federal_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # New Year
        self.assertIn(date(2013, 5, 27), holidays)  # Memorial day
        self.assertIn(date(2013, 7, 4), holidays)  # Nation day
        self.assertIn(date(2013, 9, 2), holidays)  # Labour day
        self.assertIn(date(2013, 11, 11), holidays)  # Armistice
        self.assertIn(date(2013, 11, 28), holidays)  # Thanskgiving
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas

    def test_presidential_year(self):
        self.assertTrue(UnitedStates.is_presidential_year(2012))
        self.assertFalse(UnitedStates.is_presidential_year(2013))
        self.assertFalse(UnitedStates.is_presidential_year(2014))
        self.assertFalse(UnitedStates.is_presidential_year(2015))
        self.assertTrue(UnitedStates.is_presidential_year(2016))

    def test_election_day(self):
        # Election day is:
        # the Tuesday next after the first Monday in the month of November
        self.assertEqual(date(2013, 11, 5), self.cal.get_election_date(2013))
        self.assertEqual(date(2014, 11, 4), self.cal.get_election_date(2014))
        self.assertEqual(date(2015, 11, 3), self.cal.get_election_date(2015))
        self.assertEqual(date(2016, 11, 8), self.cal.get_election_date(2016))
        self.assertEqual(date(2017, 11, 7), self.cal.get_election_date(2017))
        self.assertEqual(date(2018, 11, 6), self.cal.get_election_date(2018))
        self.assertEqual(date(2019, 11, 5), self.cal.get_election_date(2019))
        self.assertEqual(date(2020, 11, 3), self.cal.get_election_date(2020))

    def test_election_day_label(self):
        _, label = self.cal.get_election_day(2017)
        self.assertEqual(label, "Election Day")

    def test_federal_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)   # New Year
        self.assertIn(date(2014, 5, 26), holidays)  # Memorial day
        self.assertIn(date(2014, 7, 4), holidays)  # Nation day
        self.assertIn(date(2014, 9, 1), holidays)  # Labour day
        self.assertIn(date(2014, 11, 11), holidays)  # Armistice
        self.assertIn(date(2014, 11, 27), holidays)  # Thanskgiving
        self.assertIn(date(2014, 12, 25), holidays)  # XMas

    def test_federal_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)   # New Year
        self.assertIn(date(2015, 5, 25), holidays)  # Memorial day
        self.assertIn(date(2015, 7, 4), holidays)   # Nation day
        self.assertIn(date(2015, 9, 7), holidays)  # Labour day
        self.assertIn(date(2015, 11, 11), holidays)  # Armistice
        self.assertIn(date(2015, 11, 26), holidays)  # Thanskgiving
        self.assertIn(date(2015, 12, 25), holidays)  # XMas

    def test_federal_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(date(2017, 12, 27), holidays)  # XMas

    def test_columbus_day(self):
        holidays = self.cal.holidays_set(2017)
        # Columbus Day is included here
        self.assertIn(date(2017, 10, 9), holidays)

    def test_columbus_day_label(self):
        _, label = self.cal.get_columbus_day(2017)
        self.assertEqual(label, "Columbus Day")

    def test_presidential_day(self):
        # Washington's birthday, or sometimes called otherwise, may not
        # be included.
        holidays = self.cal.holidays_set(2017)
        day, _ = self.cal.get_presidents_day(2017)
        # Washington's birthday is included here
        self.assertIn(day, holidays)

    def test_president_day_label(self):
        _, label = self.cal.get_presidents_day(2017)
        self.assertEqual(label, "Washington's Birthday")

    def test_get_inauguration_date(self):
        self.assertEqual(
            date(2017, 1, 20), self.cal.get_inauguration_date(2017))
        # Not an "inauguration day" year
        with self.assertRaises(ValueError):
            self.cal.get_inauguration_date(2016)
        with self.assertRaises(ValueError):
            self.cal.get_inauguration_date(2015)
        with self.assertRaises(ValueError):
            self.cal.get_inauguration_date(2014)
        # Shifted to MON, since the 20th was on SUN
        self.assertEqual(
            date(2013, 1, 21), self.cal.get_inauguration_date(2013))
        # 2009, back to normal
        self.assertEqual(
            date(2009, 1, 20), self.cal.get_inauguration_date(2009))

    def test_inauguration_day(self):
        # NOTE: 2013 test is not relevant, it's the same day as MLK day.
        # NOTE: 1985 test is not relevant, it's the same day as MLK day.
        # By default, it's not a public holiday
        self.assertNotIn(
            self.cal.get_inauguration_date(2017),
            self.cal.holidays_set(2017)
        )
        self.assertNotIn(
            self.cal.get_inauguration_date(2009),
            self.cal.holidays_set(2009)
        )
        self.assertNotIn(
            self.cal.get_inauguration_date(1957),
            self.cal.holidays_set(1957)
        )

    def test_election_day_inclusion(self):
        # By default, election day is not included
        for year in range(2013, 2020):
            holidays = self.cal.holidays_set(year)
            self.assertNotIn(self.cal.get_election_date(year), holidays)

    def test_thanksgiving_friday_label(self):
        _, label = self.cal.get_thanksgiving_friday(2017)
        self.assertEqual(label, "Thanksgiving Friday")

    def test_national_memorial_label(self):
        _, label = self.cal.get_national_memorial_day(2017)
        self.assertEqual(label, "Memorial Day")

    def test_veterans_label(self):
        _, label = self.cal.get_veterans_day(2017)
        self.assertEqual(label, "Veterans Day")

    def test_mardi_gras(self):
        year = 2017
        day, _ = self.cal.get_mardi_gras(year)
        holidays = self.cal.holidays_set(year)
        self.assertNotIn(day, holidays)


class NoColumbus(object):
    """
    Some States don't include Columbus Day:

    * Alaska
    * Arkansas
    * California
    * Delaware
    """
    def test_columbus_day(self):
        # This overrides UnitedStates.test_columbus_day
        holidays = self.cal.holidays_set(2017)
        # Columbus Day... Not included
        self.assertNotIn(date(2017, 10, 9), holidays)


class NoPresidentialDay(object):
    """
    Washington's birthday is not included in Delaware calendar.
    """
    def test_presidential_day(self):
        # This function *overwrites* UnitedStates.test_presidential_day
        holidays = self.cal.holidays_set(2017)
        day, _ = self.cal.get_presidents_day(2017)
        # Washington's birthday not included here
        self.assertNotIn(day, holidays)


class InaugurationDay(object):
    """
    When Inauguration Day is a public holiday
    """
    def test_inauguration_day(self):
        # This method overwrites UnitedStatesTest.test_inauguration_day
        self.assertIn(
            self.cal.get_inauguration_date(2017),
            self.cal.holidays_set(2017)
        )
        # NOTE: 2013 test is not relevant, it's the same as MLK Day
        self.assertIn(
            self.cal.get_inauguration_date(2009),
            self.cal.holidays_set(2009)
        )
        # NOTE: 1985 is not relevant, it's the same as MLK Day


class ElectionDayEvenYears(object):
    """
    Some state include the election day on even years
    """
    def test_election_day_inclusion(self):
        # This method overwrites UnitedStates.test_election_day_inclusion()
        # Election Day is a public holiday on even years.
        holidays = self.cal.holidays_set(2014)
        self.assertIn(self.cal.get_election_date(2014), holidays)
        # Odd year -- not included
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(self.cal.get_election_date(2015), holidays)
        # Even year
        holidays = self.cal.holidays_set(2016)
        self.assertIn(self.cal.get_election_date(2016), holidays)
        # Odd year -- not included
        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(self.cal.get_election_date(2017), holidays)


class ElectionDayPresidentialYears(object):
    """
    Some state include the election day on presidential years
    """
    def test_election_day_inclusion(self):
        # This method overwrites UnitedStates.test_election_day_inclusion()
        # Election Day is a public holiday presidential years.
        # not included
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(self.cal.get_election_date(2014), holidays)
        # not included
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(self.cal.get_election_date(2015), holidays)
        # 2016 election
        holidays = self.cal.holidays_set(2016)
        self.assertIn(self.cal.get_election_date(2016), holidays)
        # not included
        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(self.cal.get_election_date(2017), holidays)


class ElectionDayEveryYear(object):
    """
    Some State include election day on every year
    """
    def test_election_day_inclusion(self):
        # Election day is included *every year*
        for year in range(2013, 2020):
            holidays = self.cal.holidays_set(year)
            self.assertIn(self.cal.get_election_date(year), holidays)


class IncludeMardiGras(object):
    """
    Louisiana and some areas (Alabama Counties) include Mardi Gras
    """
    def test_mardi_gras(self):
        year = 2017
        day, _ = self.cal.get_mardi_gras(year)
        holidays = self.cal.holidays_set(year)
        self.assertIn(day, holidays)


class AlabamaTest(UnitedStatesTest):
    cal_class = Alabama

    def test_mlk_label(self):
        # Overwrite UnitedStatesTest.test_mlk_label
        # Martin Luther King day is renamed in Alabama
        _, label = self.cal.get_martin_luther_king_day(2017)
        self.assertEqual(label, "Robert E. Lee/Martin Luther King Birthday")

    def test_president_day_label(self):
        # Overwrite UnitedStatesTest.test_president_day_label
        # Presidents day is renamed in Alabama
        _, label = self.cal.get_presidents_day(2017)
        self.assertEqual(label, "George Washington/Thomas Jefferson Birthday")

    def test_columbus_day_label(self):
        # Overwrite UnitedStatesTest.test_columbus_day_label
        # Columbus day is renamed in Alabama
        _, label = self.cal.get_columbus_day(2017)
        self.assertEqual(
            label,
            "Columbus Day / Fraternal Day / American Indian Heritage Day")

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 28), holidays)  # Confederate Memorial Day
        self.assertIn(date(2014, 6, 2), holidays)  # Jefferson Davis' birthday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 27), holidays)  # Confederate Memorial Day
        self.assertIn(date(2015, 6, 1), holidays)  # Jefferson Davis' birthday


class AlabamaBaldwinCountyTest(IncludeMardiGras, AlabamaTest):
    cal_class = AlabamaBaldwinCounty


class AlabamaMobileCountyTest(IncludeMardiGras, AlabamaTest):
    cal_class = AlabamaMobileCounty


class AlabamaPerryCountyTest(AlabamaTest):
    cal_class = AlabamaPerryCounty

    def test_county_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 11, 13), holidays)  # Obama Day


class AlaskaTest(NoColumbus, UnitedStatesTest):
    cal_class = Alaska

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 31), holidays)  # Seward's Day
        self.assertIn(date(2014, 10, 18), holidays)  # Alaska Day
        # Alaska Day is on SAT, shift to FRI
        self.assertIn(date(2014, 10, 17), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 30), holidays)  # Seward's Day
        self.assertIn(date(2015, 10, 18), holidays)  # Alaska Day
        # Alaska day is on SUN: shifted to MON
        self.assertIn(date(2015, 10, 19), holidays)

    def test_state_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 3, 27), holidays)  # Seward's Day
        self.assertIn(date(2017, 10, 18), holidays)  # Alaska Day
        # Alaska day is on WED: no shift
        self.assertNotIn(date(2017, 10, 19), holidays)
        self.assertNotIn(date(2017, 10, 17), holidays)


class ArizonaTest(UnitedStatesTest):
    cal_class = Arizona

    def test_mlk_label(self):
        # Overwrite UnitedStatesTest.test_mlk_label
        # Martin Luther King day is renamed in Arizona
        _, label = self.cal.get_martin_luther_king_day(2017)
        self.assertEqual(label, "Dr. Martin Luther King Jr./Civil Rights Day")

    def test_president_day_label(self):
        # Overwrite UnitedStatesTest.test_president_day_label
        # Presidents day is renamed in Arizona
        _, label = self.cal.get_presidents_day(2017)
        self.assertEqual(label, "Lincoln/Washington Presidents' Day")


class ArkansasTest(NoColumbus, UnitedStatesTest):
    cal_class = Arkansas

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 24), holidays)  # XMas Eve

    def test_christmas_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2016, 12, 23), holidays)  # XMas Eve shifted

    def test_president_day_label(self):
        # Overwrite UnitedStatesTest.test_president_day_label
        # Presidents day is renamed in Arkansas
        _, label = self.cal.get_presidents_day(2017)
        self.assertEqual(
            label,
            "George Washington's Birthday and Daisy Gatson Bates Day"
        )


class CaliforniaTest(NoColumbus, UnitedStatesTest):
    cal_class = California

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 31), holidays)  # Cesar Chavez Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 31), holidays)  # Cesar Chavez Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class CaliforniaEducationTest(CaliforniaTest):
    cal_class = CaliforniaEducation

    def test_specific_lincoln_birthday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 2, 12), holidays)  # Lincoln's Birthday

        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 2, 12), holidays)  # Lincoln's Birthday

        # Lincoln's Birthday wasn't included in 2009
        holidays = self.cal.holidays_set(2009)
        self.assertNotIn(date(2009, 2, 12), holidays)

    def test_specific_native_american_day(self):
        # Native American Day occurs on the 4th MON of September
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 9, 24), holidays)  # Native American Day

        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 9, 23), holidays)  # Native American Day


# Like California, except that it has:
# * No Chavez Day,
# * Includes Columbus day, but relabels it.
# * Adds Lincoln's Birthday.
class CaliforniaBerkeleyTest(UnitedStatesTest):
    cal_class = CaliforniaBerkeley

    def test_state_year_2014(self):
        # Overwriting CaliforniaTest, there's no Chavez Day for Berkeley
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(date(2014, 3, 31), holidays)  # NO Cesar Chavez Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        # Overwriting CaliforniaTest, there's no Chavez Day for Berkeley
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 3, 31), holidays)  # NO Cesar Chavez Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_specific_lincoln_birthday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 2, 12), holidays)  # Lincoln's Birthday

        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 2, 12), holidays)  # Lincoln's Birthday

    def test_specific_malcomx_birthday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 5, 19), holidays)  # Malcom X Day

        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 5, 19), holidays)  # Malcom X Day

    def test_columbus_day_label(self):
        # Overwrite UnitedStatesTest.test_columbus_day_label
        _, label = self.cal.get_columbus_day(2019)
        self.assertEqual(label, "Indigenous People's Day")


# Like California, except:
# * No Chavez Day,
# * Added Columbus Day
class CaliforniaSanFranciscoTest(UnitedStatesTest):
    cal_class = CaliforniaSanFrancisco

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(date(2014, 3, 31), holidays)  # NO Cesar Chavez Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 3, 31), holidays)  # NO Cesar Chavez Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


# Like California, except:
# * No Chavez Day,
# * No Thanksgiving Friday
# * Added Harvey Milk Day
class CaliforniaWestHollywoodTest(NoColumbus, UnitedStatesTest):
    cal_class = CaliforniaWestHollywood

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(date(2014, 3, 31), holidays)  # NO Cesar Chavez Day
        self.assertNotIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 3, 31), holidays)  # NO Cesar Chavez Day
        self.assertNotIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_harvey_milk_day(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 5, 22), holidays)  # Harvey Milk Day

        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 5, 22), holidays)  # Harvey Milk Day


class ColoradoTest(UnitedStatesTest):
    cal_class = Colorado
    # Colorado has only federal state holidays.
    # NOTE: Cesar Chavez Day is an optional holiday


class ConnecticutTest(UnitedStatesTest):
    cal_class = Connecticut

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)  # Lincoln's Birthday
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)  # Lincoln's Birthday
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday


class DelawareTest(ElectionDayEvenYears, NoPresidentialDay, NoColumbus,
                   UnitedStatesTest):
    cal_class = Delaware

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class DistrictOfColumbiaTest(InaugurationDay, UnitedStatesTest):
    cal_class = DistrictOfColumbia

    def test_state_year_2017(self):
        # President elected in 2016, Inauguration Day is year+1
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 20), holidays)  # Inauguration Day
        self.assertIn(date(2017, 4, 16), holidays)  # Emancipation Day

    def test_state_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        # No Inauguration Day the other years
        self.assertNotIn(date(2016, 1, 20), holidays)
        self.assertIn(date(2016, 4, 16), holidays)  # Emancipation Day


class FloridaBasicTest(object):
    """
    Core Florida tests.

    The difference is that it includes the Thanksgiving Friday *and* its label
    is renamed.
    """
    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_thanksgiving_friday_label(self):
        # Overwrite UnitedStatesTest.test_thanksgiving_friday_label
        _, label = self.cal.get_thanksgiving_friday(2017)
        self.assertEqual(label, "Friday after Thanksgiving")


class FloridaTest(NoColumbus, NoPresidentialDay, FloridaBasicTest,
                  UnitedStatesTest):
    """
    Florida includes all federal holidays except
    Washington's Birthday & Columbus day
    """
    cal_class = Florida


class FloridaLegalTest(IncludeMardiGras, ElectionDayEveryYear,
                       FloridaBasicTest, UnitedStatesTest):
    """
    Florida Legal Holidays include:

    * All Florida State Holidays,
    * Mardi Gras,
    * Lincoln's Birthday,
    * Susan B. Anthony Day,
    * Washington's Birthday,
    * Good Friday,
    * Pascua Florida Day,
    * Confederate Memorial Day,
    * Jefferson Davies Birthday,
    * Flag Day
    * Columbus Day renamed as "Columbus and Farmers' Day"
    * Election Day
    """
    cal_class = FloridaLegal

    @skipIf(PY2, "Python 2 warnings unsupported")
    def test_init_warning(self):
        warnings.simplefilter("always")
        with warnings.catch_warnings(record=True) as w:
            # Cause all warnings to always be triggered.
            # Trigger a warning.
            self.cal_class()
            # Verify some things
            assert len(w) == 1
            assert issubclass(w[-1].category, UserWarning)
            assert "Florida's laws separate the definitions between paid versus legal holidays." in str(w[-1].message)  # noqa
        warnings.simplefilter("ignore")

    def test_specific_lincoln_birthday(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)  # Lincoln's Birthday

        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)  # Lincoln's Birthday

    def test_susan_b_anthony_day(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 2, 15), holidays)  # Susan B. Anthony Day

    def test_good_friday(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday

    def test_pascua_florida_day(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 2), holidays)  # Pascua Florida Day

    def test_confederate_holidays(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 26), holidays)  # Confederate Memorial Day
        self.assertIn(date(2014, 6, 3), holidays)  # Jefferson Davis' birthday

        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 26), holidays)  # Confederate Memorial Day
        self.assertIn(date(2015, 6, 3), holidays)  # Jefferson Davis' birthday

        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 4, 26), holidays)  # Confederate Memorial Day
        self.assertIn(date(2018, 6, 3), holidays)  # Jefferson Davis' birthday

    def test_flag_day(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 6, 14), holidays)  # Flag Day

        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 6, 14), holidays)  # Flag Day

    def test_columbus_day_label(self):
        _, label = self.cal.get_columbus_day(2017)
        self.assertEqual(label, "Columbus Day and Farmers' Day")


class FloridaCircuitCourtsTest(NoColumbus, FloridaBasicTest, UnitedStatesTest):
    cal_class = FloridaCircuitCourts

    def test_good_friday(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday

    def test_rosh_hashanah_2018(self):
        # src: https://www.firstjudicialcircuit.org/about-court/court-holidays
        rosh_hashanah = self.cal.get_rosh_hashanah(2018)
        self.assertEqual(rosh_hashanah, date(2018, 9, 10))
        holidays = self.cal.holidays_set(2018)
        self.assertIn(rosh_hashanah, holidays)

    def test_rosh_hashanah_2019(self):
        # src: https://www.firstjudicialcircuit.org/about-court/court-holidays
        rosh_hashanah = self.cal.get_rosh_hashanah(2019)
        self.assertEqual(rosh_hashanah, date(2019, 9, 30))
        holidays = self.cal.holidays_set(2019)
        self.assertIn(rosh_hashanah, holidays)

    def test_yom_kippur_2018(self):
        # src: https://www.firstjudicialcircuit.org/about-court/court-holidays
        yom_kippur = self.cal.get_yom_kippur(2018)
        self.assertEqual(yom_kippur, date(2018, 9, 19))
        holidays = self.cal.holidays_set(2018)
        self.assertIn(yom_kippur, holidays)

    def test_yom_kippur_2019(self):
        # src: https://www.firstjudicialcircuit.org/about-court/court-holidays
        yom_kippur = self.cal.get_yom_kippur(2019)
        self.assertEqual(yom_kippur, date(2019, 10, 9))
        holidays = self.cal.holidays_set(2019)
        self.assertIn(yom_kippur, holidays)


class FloridaMiamiDadeTests(FloridaBasicTest, UnitedStatesTest):
    cal_class = FloridaMiamiDade


class GeorgiaTest(NoPresidentialDay, UnitedStatesTest):
    cal_class = Georgia

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 28), holidays)  # Confederate Memorial
        # FIXME: this holiday rule is Confusing, probably false
        self.assertIn(date(2014, 12, 26), holidays)  # Washington bday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 27), holidays)  # Confederate Memorial
        # FIXME: this holiday rule is Confusing, probably false
        self.assertIn(date(2015, 12, 24), holidays)  # Washington bday

    @skip("Confusing Rule, it's impossible to decide")
    def test_washington_birthday(self):
        # Source: https://georgia.gov/popular-topic/observing-state-holidays
        day, _ = self.cal.get_washington_birthday_december(2017)
        self.assertEqual(day, date(2017, 12, 26))

        day, _ = self.cal.get_washington_birthday_december(2016)
        self.assertEqual(
            day,
            date(2016, 12, 27),
        )

        day, _ = self.cal.get_washington_birthday_december(2015)
        self.assertEqual(
            day,
            date(2015, 12, 24),
        )

        day, _ = self.cal.get_washington_birthday_december(2014)
        self.assertEqual(
            day,
            date(2014, 12, 26),
        )

        day, _ = self.cal.get_washington_birthday_december(2013)
        self.assertEqual(
            day,
            date(2013, 12, 24),
        )


class HawaiiTest(ElectionDayEvenYears, NoColumbus, UnitedStatesTest):
    cal_class = Hawaii

    def test_state_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 3, 26),
                      holidays)  # Prince Jonah Kuhio Kalanianaole
        self.assertIn(date(2017, 3, 27),
                      holidays)  # Prince Jonah Kuhio Kalanianaole (shifted)
        self.assertIn(date(2017, 4, 14), holidays)  # Good Friday
        self.assertIn(date(2017, 6, 11), holidays)  # Kamehameha
        self.assertIn(date(2017, 6, 12), holidays)  # Kamehameha (shifted)
        self.assertIn(date(2017, 8, 18), holidays)  # Statehood day

    def test_state_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 3, 26),
                      holidays)  # Prince Jonah Kuhio Kalanianaole

        self.assertIn(date(2018, 3, 30), holidays)  # Good Friday
        self.assertIn(date(2018, 6, 11), holidays)  # Kamehameha
        self.assertIn(date(2018, 8, 17), holidays)  # Statehood day

        # Prince Jonah Kuhio Kalanianaole is not shifted
        self.assertNotIn(date(2018, 3, 27), holidays)
        # Kamehameha is not shifted
        self.assertNotIn(date(2018, 6, 12), holidays)


class IdahoTest(UnitedStatesTest):
    cal_class = Idaho
    # NOTE: Idaho only has federal holidays.

    def test_mlk_label(self):
        # Overwrite UnitedStatesTest.test_mlk_label
        # Martin Luther King day is renamed in Idaho
        _, label = self.cal.get_martin_luther_king_day(2017)
        self.assertEqual(
            label, "Martin Luther King Jr. / Idaho Human Rights Day")


class IllinoisTest(ElectionDayEvenYears, UnitedStatesTest):
    cal_class = Illinois

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)  # Lincoln's Birthday
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)  # Lincoln's Birthday
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class ChicagoIllinoisTest(ElectionDayEvenYears, UnitedStatesTest):
    cal_class = ChicagoIllinois

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)  # Lincoln's Birthday
        # Thanksgiving Friday is NOT a holiday in Chicago.
        self.assertNotIn(date(2014, 11, 28), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)  # Lincoln's Birthday
        # Thanksgiving Friday is NOT a holiday in Chicago.
        self.assertNotIn(date(2015, 11, 27), holidays)

    def test_pulaski_day(self):
        # Pulaski day is on the first MON in March.
        # Source: https://en.wikipedia.org/wiki/Casimir_Pulaski_Day
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 3, 5), holidays)
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 3, 4), holidays)
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 3, 2), holidays)
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 3, 1), holidays)


class IndianaTest(ElectionDayEvenYears, NoPresidentialDay, UnitedStatesTest):
    cal_class = Indiana

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        # Thanksgiving Friday -- Renamed into Lincoln's Birthday
        self.assertIn(date(2014, 11, 28), holidays)
        # FIXME: this holiday rule is Confusing, probably false
        self.assertIn(date(2014, 12, 26), holidays)  # Washington bday

        # Primary Election Day, only happen on even years
        self.assertIn(date(2014, 5, 6), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday
        # Thanksgiving Friday -- Renamed into Lincoln's Birthday
        self.assertIn(date(2015, 11, 27), holidays)
        # FIXME: this holiday rule is Confusing, probably false
        self.assertIn(date(2015, 12, 24), holidays)  # Washington bday

        # Primary Election Day, only happen on even years
        self.assertNotIn(date(2015, 5, 5), holidays)

    def test_primary_election_day(self):
        # Source:
        # -> https://www.timeanddate.com/holidays/us/primary-election-indiana
        # Year 2010
        election_day, _ = self.cal.get_primary_election_day(2010)
        self.assertEqual(election_day, date(2010, 5, 4))
        # Year 2012
        election_day, _ = self.cal.get_primary_election_day(2012)
        self.assertEqual(election_day, date(2012, 5, 8))
        # Year 2014
        election_day, _ = self.cal.get_primary_election_day(2014)
        self.assertEqual(election_day, date(2014, 5, 6))
        # Year 2016
        election_day, _ = self.cal.get_primary_election_day(2016)
        self.assertEqual(election_day, date(2016, 5, 3))

    def test_election_day_label(self):
        # Overwrite UnitedStatesTest.test_election_day_label
        # Election Day is "General Election Day" in Indiana
        _, label = self.cal.get_election_day(2017)
        self.assertEqual(label, "General Election Day")

    def test_thanksgiving_friday_label(self):
        # Overwrite UnitedStatesTest.test_thanksgiving_friday_label
        # Lincoln's Birthday is set on Thanksgiving Friday
        _, label = self.cal.get_thanksgiving_friday(2017)
        self.assertEqual(label, "Lincoln's Birthday")

    @skip("Confusing Rule, it's impossible to decide")
    def test_washington_birthday(self):
        # Sources:
        # http://www.in.gov/spd/files/2018_Holidays.pdf
        # http://www.in.gov/spd/files/2017_Holidays.pdf
        # http://www.in.gov/spd/files/2016_Holidays.pdf

        # Year 2016, shifted to the 26th
        washington_bday = self.cal.get_washington_birthday_december(2016)
        self.assertEqual(date(2016, 12, 26), washington_bday)

        # Year 2017, shifted to the 26th
        washington_bday = self.cal.get_washington_birthday_december(2017)
        self.assertEqual(date(2017, 12, 26), washington_bday)

        # Year 2018, back to XMas Eve
        washington_bday = self.cal.get_washington_birthday_december(2018)
        self.assertEqual(date(2018, 12, 24), washington_bday)


class IowaTest(NoPresidentialDay, NoColumbus, UnitedStatesTest):
    cal_class = Iowa

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 3), holidays)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class KansasTest(NoPresidentialDay, NoColumbus, UnitedStatesTest):
    cal_class = Kansas


class KentuckyTest(NoPresidentialDay, NoColumbus, UnitedStatesTest):
    cal_class = Kentucky

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2014, 12, 31), holidays)  # NY Eve

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2015, 12, 31), holidays)  # NY Eve


class LouisianaTest(IncludeMardiGras, NoColumbus, ElectionDayEvenYears,
                    UnitedStatesTest):
    cal_class = Louisiana

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday


class MaineTest(UnitedStatesTest):
    cal_class = Maine

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 21), holidays)   # Patriot's day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 20), holidays)   # Patriot's day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class MarylandTest(ElectionDayPresidentialYears, UnitedStatesTest):
    cal_class = Maryland

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        # Thanksgiving Friday == Native American Heritage Day
        self.assertIn(date(2014, 11, 28), holidays)

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        # Thanksgiving Friday == Native American Heritage Day
        self.assertIn(date(2015, 11, 27), holidays)

    def test_thanksgiving_friday_label(self):
        # Overwrite UnitedStatesTest.test_thanksgiving_friday_label
        # Thanksgiving Friday label changed to "Native American Heritage Day"
        _, label = self.cal.get_thanksgiving_friday(2017)
        self.assertEqual(label, "Native American Heritage Day")


class MassachusettsTest(UnitedStatesTest):
    cal_class = Massachusetts

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 21), holidays)  # Patriot's day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 20), holidays)  # Patriot's day


class SuffolkCountyMassachusettsTest(MassachusettsTest):
    cal_class = SuffolkCountyMassachusetts

    def test_county_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 3, 17), holidays)  # Evacuation Day
        self.assertIn(date(2018, 6, 17), holidays)  # Bunker Hill Day

    def test_county_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 3, 17), holidays)  # Evacuation Day
        self.assertIn(date(2019, 6, 17), holidays)  # Bunker Hill Day


class MichiganTest(NoColumbus, ElectionDayEvenYears, UnitedStatesTest):
    cal_class = Michigan

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2014, 12, 31), holidays)  # New Years Eve

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2015, 12, 31), holidays)  # New Years Eve

    def test_state_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 11, 24), holidays)  # Thanksgiving Friday

        # XMas Eve
        self.assertIn(date(2017, 12, 24), holidays)
        # XMAs Eve is on SUN, shifted to Dec, 22nd
        self.assertIn(date(2017, 12, 22), holidays)

        # New Years Eve
        self.assertIn(date(2017, 12, 31), holidays)
        # New Years Eve is on SUN, shifted to Dec, 29nd
        self.assertIn(date(2017, 12, 29), holidays)


class MinnesotaTest(NoColumbus, UnitedStatesTest):
    cal_class = Minnesota

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class MississippiTest(NoColumbus, UnitedStatesTest):
    cal_class = Mississippi

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 28), holidays)  # Confederate Memorial Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 27), holidays)  # Confederate Memorial Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_mlk_label(self):
        # Overwrite UnitedStatesTest.test_mlk_label
        # Martin Luther King day is renamed in Mississippi
        _, label = self.cal.get_martin_luther_king_day(2017)
        self.assertEqual(
            label, "Martin Luther King's and Robert E. Lee's Birthdays")

    def test_national_memorial_label(self):
        # Overwrite UnitedStatesTest.test_national_memorial_label
        # National Memorial Day is renamed in Mississippi
        _, label = self.cal.get_national_memorial_day(2017)
        self.assertEqual(
            label, "National Memorial Day / Jefferson Davis Birthday")

    def test_veterans_label(self):
        # Overwrite UnitedStatesTest.test_veterans_label
        # Veterans Day is renamed in Mississippi
        _, label = self.cal.get_veterans_day(2017)
        self.assertEqual(label, "Armistice Day (Veterans Day)")


class MissouriTest(UnitedStatesTest):
    cal_class = Missouri

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)  # Lincoln's Birthday
        self.assertIn(date(2014, 5, 8), holidays)   # Truman Day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)  # Lincoln's Birthday
        self.assertIn(date(2015, 5, 8), holidays)   # Truman Day


class MontanaTest(ElectionDayEvenYears, UnitedStatesTest):
    cal_class = Montana
    # NOTE: Montana include only Federal Holidays + General Election Day


class NebraskaTest(UnitedStatesTest):
    cal_class = Nebraska

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 25), holidays)  # Arbor Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 24), holidays)  # Arbor Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class NevadaTest(NoColumbus, UnitedStatesTest):
    cal_class = Nevada

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)  # Nevada Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 10, 30), holidays)  # Nevada Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_thanksgiving_friday_label(self):
        # Overwrite UnitedStatesTest.test_thanksgiving_friday_label
        # Thanksgiving Friday Label is Family Day in Nevada
        _, label = self.cal.get_thanksgiving_friday(2017)
        self.assertEqual(label, "Family Day")


class NewHampshireTest(UnitedStatesTest):
    cal_class = NewHampshire

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_mlk_label(self):
        # Overwrite UnitedStatesTest.test_mlk_label
        # Martin Luther King day is renamed in New Hampshire
        _, label = self.cal.get_martin_luther_king_day(2017)
        self.assertEqual(label, "Martin Luther King, Jr. Civil Rights Day")


class NewJerseyTest(ElectionDayEveryYear, UnitedStatesTest):
    cal_class = NewJersey

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday


class NewMexicoTest(NoPresidentialDay, UnitedStatesTest):
    cal_class = NewMexico

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_thanksgiving_friday_label(self):
        # Overwrite UnitedStatesTest.test_thanksgiving_friday_label
        # New Mexico is celebrating Presidents' Day on Thanksgiving Friday
        _, label = self.cal.get_thanksgiving_friday(2017)
        self.assertEqual(label, "Presidents' Day")


class NewYorkTest(ElectionDayEveryYear, UnitedStatesTest):
    cal_class = NewYork

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 12), holidays)  # Lincoln's Birthday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 2, 12), holidays)  # Lincoln's Birthday


class NorthCarolinaTest(NoPresidentialDay, NoColumbus, UnitedStatesTest):
    cal_class = NorthCarolina

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        self.assertIn(date(2014, 11, 27), holidays)  # Thanksgiving Thursday
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2014, 12, 26), holidays)  # Boxing Day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday
        self.assertIn(date(2015, 11, 26), holidays)  # Thanksgiving Thursday
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)  # Xmas Eve
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing Day

    def test_federal_year_2017(self):
        # It is different from other federal days.
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 4, 14), holidays)  # Good Friday
        self.assertIn(date(2017, 11, 23), holidays)  # Thanksgiving Thursday
        self.assertIn(date(2017, 11, 24), holidays)  # Thanksgiving Friday
        self.assertIn(date(2017, 12, 24), holidays)  # Xmas Eve
        self.assertIn(date(2017, 12, 25), holidays)  # Xmas Day
        self.assertIn(date(2017, 12, 26), holidays)  # Day after Xmas
        self.assertIn(date(2017, 12, 27), holidays)  # Xmas Shift

    def test_state_year_2016_xmas(self):
        # XMAS falls on SUN
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 12, 23), holidays)  # Day 1 - FRI
        self.assertIn(date(2016, 12, 26), holidays)  # Day 2 - MON
        self.assertIn(date(2016, 12, 27), holidays)  # Day 3 - TUE
        # 22nd and 28th are not included
        self.assertNotIn(date(2016, 12, 22), holidays)  # THU
        self.assertNotIn(date(2016, 12, 28), holidays)  # WED

    def test_state_year_2017_xmas(self):
        # XMAS falls on MON
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 12, 25), holidays)  # Day 1 - MON
        self.assertIn(date(2017, 12, 26), holidays)  # Day 2 - TUE
        self.assertIn(date(2017, 12, 27), holidays)  # Day 3 - WED
        # 22nd and 28th are not included
        self.assertNotIn(date(2017, 12, 22), holidays)  # FRI
        self.assertNotIn(date(2017, 12, 23), holidays)  # SAT
        self.assertNotIn(date(2017, 12, 28), holidays)  # THU

    def test_state_year_2018_xmas(self):
        # XMAS falls on TUE
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 12, 24), holidays)  # Day 1 - MON
        self.assertIn(date(2018, 12, 25), holidays)  # Day 2 - TUE
        self.assertIn(date(2018, 12, 26), holidays)  # Day 3 - WED
        # No shift:
        self.assertNotIn(date(2018, 12, 23), holidays)
        self.assertNotIn(date(2018, 12, 27), holidays)

    def test_state_year_2019_xmas(self):
        # XMAS falls on WED
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 12, 24), holidays)  # Day 1 - TUE
        self.assertIn(date(2019, 12, 25), holidays)  # Day 2 - WED
        self.assertIn(date(2019, 12, 26), holidays)  # Day 3 - THU
        # No shift:
        self.assertNotIn(date(2019, 12, 23), holidays)
        self.assertNotIn(date(2019, 12, 27), holidays)

    def test_state_year_2020_xmas(self):
        # XMAS falls on FRI
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 12, 24), holidays)  # Day 1 - THU
        self.assertIn(date(2020, 12, 25), holidays)  # Day 2 - FRI
        self.assertIn(date(2020, 12, 28), holidays)  # Day 3 - MON
        # 23rd and 29th are not included
        self.assertNotIn(date(2020, 12, 23), holidays)
        self.assertNotIn(date(2020, 12, 29), holidays)

    def test_state_year_2021_xmas(self):
        # XMAS falls on SAT
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 12, 23), holidays)  # Day 1 - THU
        self.assertIn(date(2021, 12, 24), holidays)  # Day 2 - FRI
        self.assertIn(date(2021, 12, 27), holidays)  # Day 3 - MON
        # 23rd and 29th are not included
        self.assertNotIn(date(2021, 12, 22), holidays)
        self.assertNotIn(date(2021, 12, 28), holidays)


class NorthDakotaTest(NoColumbus, UnitedStatesTest):
    cal_class = NorthDakota

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday


class OhioTest(UnitedStatesTest):
    cal_class = Ohio
    # Ohio includes only Federal holidays.
    # The wikipedia page say it also includes Election Day, but no official
    # document confirms this.


class OklahomaTest(NoColumbus, UnitedStatesTest):
    cal_class = Oklahoma

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 26), holidays)  # Boxing day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing day


class OregonTest(NoColumbus, UnitedStatesTest):
    cal_class = Oregon
    # NOTE: Oregon has only the federal holidays, except Columbus Day


class PennsylvaniaTest(ElectionDayEveryYear, UnitedStatesTest):
    cal_class = Pennsylvania

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday


class RhodeIslandTest(NoPresidentialDay, ElectionDayEvenYears,
                      UnitedStatesTest):
    cal_class = RhodeIsland

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 8, 11), holidays)  # Victory Day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 8, 10), holidays)  # Victory Day


class SouthCarolinaTest(NoColumbus, UnitedStatesTest):
    cal_class = SouthCarolina

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        # Confederate Memorial Day
        self.assertIn(date(2014, 5, 10), holidays)
        # Observed here, it falls on SAT
        self.assertIn(date(2014, 5, 9), holidays)

        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2014, 12, 26), holidays)  # Boxing day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 5, 10), holidays)  # Confederate Memorial Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)  # Xmas Eve
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing day

    @skip("No clear rules for implementing the XMas Eve shift")
    def test_state_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 5, 10), holidays)  # Confederate Memorial Day
        self.assertIn(date(2017, 11, 23), holidays)  # Thanksgiving Friday
        # Xmas Eve falls on SUN
        self.assertIn(date(2017, 12, 24), holidays)
        # Christmas Eve observed here
        self.assertIn(date(2017, 12, 22), holidays)
        self.assertIn(date(2017, 12, 26), holidays)  # Boxing day


class SouthDakotaTest(UnitedStatesTest):
    cal_class = SouthDakota
    # NOTE: South Dakota has all federal holidays, except Columbus Day,
    # but it's renamed as "Native Americans Day"

    def test_columbus_day_label(self):
        # Overwrite UnitedStatesTest.test_columbus_day_label
        _, label = self.cal.get_columbus_day(2017)
        self.assertEqual(label, "Native Americans Day")


class TennesseeTest(NoColumbus, UnitedStatesTest):
    cal_class = Tennessee

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good Friday
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 3), holidays)  # Good Friday
        self.assertIn(date(2015, 12, 24), holidays)  # XMas Eve


class TexasBaseTest(NoColumbus, UnitedStatesTest):
    cal_class = TexasBase
    # NOTE: "Stock" Texas doesn't include Columbus Day,
    # state holidays are handled differently

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        # Check that state holidays are not included here
        self.assertNotIn(date(2014, 1, 19), holidays)  # Confederate Heroes Day
        self.assertNotIn(date(2014, 3, 2), holidays)  # Texas Independence Day
        self.assertNotIn(date(2014, 4, 21), holidays)  # San Jacinto Day
        self.assertNotIn(date(2014, 6, 19), holidays)  # Emancipation Day
        self.assertNotIn(date(2014, 8, 27), holidays)  # Lyndon B. Johnson Day
        self.assertNotIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertNotIn(date(2014, 12, 24), holidays)  # XMas Eve
        self.assertNotIn(date(2014, 12, 26), holidays)  # Boxing day


class TexasTest(TexasBaseTest):
    cal_class = Texas

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 19), holidays)  # Confederate Heroes Day
        self.assertIn(date(2014, 3, 2), holidays)  # Texas Independence Day
        self.assertIn(date(2014, 4, 21), holidays)  # San Jacinto Day
        self.assertIn(date(2014, 6, 19), holidays)  # Emancipation Day
        self.assertIn(date(2014, 8, 27), holidays)  # Lyndon B. Johnson Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2014, 12, 26), holidays)  # Boxing day


class UtahTest(UnitedStatesTest):
    cal_class = Utah

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 7, 24), holidays)  # Pioneer Day

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 7, 24), holidays)  # Pioneer Day


class VermontTest(NoColumbus, UnitedStatesTest):
    cal_class = Vermont

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 4), holidays)  # Town Meeting Day
        self.assertIn(date(2014, 8, 16), holidays)  # Bennington Battle Day
        self.assertIn(date(2014, 8, 15), holidays)  # Shifted to FRI

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 3, 3), holidays)  # Town Meeting Day
        self.assertIn(date(2015, 8, 16), holidays)  # Bennington Battle Day
        self.assertIn(date(2015, 8, 17), holidays)  # Shifted to MON


class VirginiaTest(UnitedStatesTest):
    cal_class = Virginia

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 17), holidays)   # Lee-Jackson Day
        self.assertIn(date(2014, 11, 26), holidays)  # Thanksgiving Wednesday
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday
        self.assertIn(date(2014, 12, 24), holidays)  # XMas Eve

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 16), holidays)  # Lee-Jackson Day
        self.assertIn(date(2015, 11, 25), holidays)  # Thanksgiving Wednesday
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday
        self.assertIn(date(2015, 12, 24), holidays)  # XMas Eve

    def test_exclude_thanksgiving_wednesday(self):
        # Sub class
        class VirginiaExclude(Virginia):
            include_thanksgiving_wednesday = False
        cal = VirginiaExclude()
        holidays = cal.holidays_set(2015)
        # Not Thanksgiving Wednesday
        self.assertNotIn(date(2015, 11, 25), holidays)

    def test_president_day_label(self):
        # Overwrite UnitedStatesTest.test_president_day_label
        _, label = self.cal.get_presidents_day(2017)
        self.assertEqual(label, "George Washington Day")

    def test_inauguration_day(self):
        # Overwriting this test: in 2017, this day is a public holiday for
        # Virginia State: Lee-Jackson Day
        # NOTE: 2013 test is not relevant, it's the same day as MLK day.
        # NOTE: 1985 test is not relevant, it's the same day as MLK day.
        # By default, it's not a public holiday
        self.assertNotIn(
            self.cal.get_inauguration_date(2009),
            self.cal.holidays_set(2009)
        )
        self.assertNotIn(
            self.cal.get_inauguration_date(1957),
            self.cal.holidays_set(1957)
        )


class WashingtonTest(NoColumbus, UnitedStatesTest):
    cal_class = Washington
    # NOTE: Washington State includes all federal holidays, except Columbus Day


class WestVirginiaTest(ElectionDayEvenYears, UnitedStatesTest):
    cal_class = WestVirginia

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 20), holidays)  # West Virginia Day
        self.assertIn(date(2014, 11, 28), holidays)  # Thanksgiving Friday

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 20), holidays)  # West Virginia Day
        self.assertIn(date(2015, 11, 27), holidays)  # Thanksgiving Friday

    def test_state_half_holidays_base(self):
        # Using the "stock" calendar
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 12, 24), holidays)  # XMas Eve
        self.assertNotIn(date(2015, 12, 31), holidays)  # NYE

    def test_state_half_holidays_included(self):
        class WestVirginiaInclude(WestVirginia):
            west_virginia_include_christmas_eve = True
            west_virginia_include_nye = True
        cal = WestVirginiaInclude()
        holidays = cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2015, 12, 31), holidays)  # NYE
        # Test that these days are not shifted
        # In 2016, XMas Eve and NYE are on SAT
        holidays = cal.holidays_set(2016)
        self.assertIn(date(2016, 12, 24), holidays)  # XMas Eve
        self.assertIn(date(2016, 12, 31), holidays)  # NYE
        self.assertNotIn(date(2016, 12, 23), holidays)  # NO SHIFT for XMas Eve
        self.assertNotIn(date(2016, 12, 30), holidays)  # NO SHIFT for NYE

    def test_election_day_label(self):
        # Overwrite UnitedStatesTest.test_election_day_label
        _, label = self.cal.get_election_day(2017)
        self.assertEqual(label, "Election Day / Susan B. Anthony Day")


class WisconsinTest(NoPresidentialDay, NoColumbus, UnitedStatesTest):
    cal_class = Wisconsin

    def test_state_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 12, 24), holidays)  # Xmas Eve
        self.assertIn(date(2014, 12, 31), holidays)  # New Years Eve

    def test_state_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 24), holidays)  # Xmas Eve
        self.assertIn(date(2015, 12, 31), holidays)  # New Years Eve


class WyomingTest(UnitedStatesTest):
    cal_class = Wyoming
    # NOTE: Wyoming only has all federal holidays

    def test_mlk_label(self):
        # Overwrite UnitedStatesTest.test_mlk_label
        _, label = self.cal.get_martin_luther_king_day(2017)
        self.assertEqual(
            label,
            "Martin Luther King, Jr. / Wyoming Equality Day"
        )


class AmericanSamoaTest(UnitedStatesTest):
    cal_class = AmericanSamoa

    def test_family_day(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 12, 26), holidays)  # Family Day

    def test_flag_day(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 17), holidays)  # Flag Day

    def test_family_day_label(self):
        holidays = self.cal.holidays(2019)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[date(2019, 12, 26)], "Family Day")


class Guam(UnitedStatesTest):
    cal_class = Guam

    def test_state_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        # Guam History and Chamorro Heritage Day
        self.assertIn(date(2019, 3, 7), holidays)
        self.assertIn(date(2019, 7, 21), holidays)  # Liberation Day
        self.assertIn(date(2019, 11, 2), holidays)  # All Souls Day
        self.assertIn(date(2019, 12, 8), holidays)  # Lady of Camarin Day

    def test_state_year_2018(self):
        holidays = self.cal.holidays_set(2020)
        # Guam History and Chamorro Heritage Day
        self.assertIn(date(2020, 3, 7), holidays)
        self.assertIn(date(2020, 7, 21), holidays)  # Liberation Day
        self.assertIn(date(2020, 11, 2), holidays)  # All Souls Day
        self.assertIn(date(2020, 12, 8), holidays)  # Lady of Camarin Day

    def test_lady_of_camarin_label(self):
        holidays = self.cal.holidays(2019)
        holidays_dict = dict(holidays)
        self.assertEqual(
            holidays_dict[date(2019, 12, 8)],
            "Lady of Camarin Day"
        )


class NormalShiftTestCase(UnitedStatesTest):
    # Using a fake calendar here
    class NormalShiftUnitedStates(UnitedStates):
        "Normal Shift Fake United State calendar"
        include_christmas_eve = True

    cal_class = NormalShiftUnitedStates

    def test_shift_2015(self):
        # Test a normal shift on 4th of July.
        # 2015: Happens on a Saturday, observed on FRI
        holidays = self.cal.holidays(2015)
        holiday_dict = dict(holidays)
        fourth_july = date(2015, 7, 4)
        observed = date(2015, 7, 3)
        self.assertIn(fourth_july, holiday_dict)
        self.assertEqual(holiday_dict[fourth_july], "Independence Day")
        self.assertIn(observed, holiday_dict)
        self.assertEqual(holiday_dict[observed], "Independence Day (Observed)")

    def test_shift_2010(self):
        # Test a normal shift on 4th of July.
        # 2010: Happens on a SUN, observed on MON
        holidays = self.cal.holidays(2010)
        holiday_dict = dict(holidays)
        fourth_july = date(2010, 7, 4)
        observed = date(2010, 7, 5)
        self.assertIn(fourth_july, holiday_dict)
        self.assertEqual(holiday_dict[fourth_july], "Independence Day")
        self.assertIn(observed, holiday_dict)
        self.assertEqual(holiday_dict[observed], "Independence Day (Observed)")

    def test_new_years_shift(self):
        # If January, 1st *of the year after* happens on SAT, add New Years Eve
        holidays = self.cal.holidays(2010)
        holiday_dict = dict(holidays)
        new_years_eve = date(2010, 12, 31)
        self.assertIn(new_years_eve, holiday_dict)
        self.assertEqual(
            holiday_dict[new_years_eve],
            "New Years Day (Observed)"
        )
        # The year after, it's not shifted
        holidays = self.cal.holidays_set(2011)
        new_years_eve = date(2011, 12, 31)
        self.assertNotIn(new_years_eve, holidays)

    def test_christmas_extra_shift_2010(self):
        # XMAs Eve is included. *and* XMas falls on SAT.
        # So you have the following holidays:
        # * 24th & 25th (XMas Eve and XMas day)
        # * 27th (XMas Shift)
        # * 23rd (XMas Eve shifted on THU)
        holidays = self.cal.holidays(2010)
        holiday_dict = dict(holidays)
        dec_23rd = date(2010, 12, 23)
        dec_24th = date(2010, 12, 24)
        dec_25th = date(2010, 12, 25)
        for day in (dec_23rd, dec_24th, dec_25th):
            self.assertIn(day, holiday_dict)
        self.assertEqual(holiday_dict[dec_23rd], "Christmas Eve (Observed)")
        self.assertEqual(holiday_dict[dec_24th], "Christmas Eve")
        self.assertEqual(holiday_dict[dec_25th], "Christmas Day")

    def test_christmas_extra_shift_2006(self):
        # XMAs Eve is included. *and* XMas falls on MON.
        # So you have the following holidays:
        # * 24th & 25th (XMas Eve and XMas day)
        # * 26th (XMas Shift)
        holidays = self.cal.holidays(2006)
        holiday_dict = dict(holidays)
        dec_24th = date(2006, 12, 24)
        dec_25th = date(2006, 12, 25)
        dec_26th = date(2006, 12, 26)
        for day in (dec_24th, dec_25th, dec_26th):
            self.assertIn(day, holiday_dict)
        self.assertEqual(holiday_dict[dec_24th], "Christmas Eve")
        self.assertEqual(holiday_dict[dec_25th], "Christmas Day")
        self.assertEqual(holiday_dict[dec_26th], "Christmas Day (Observed)")


class NormalShiftTestCaseExceptions(UnitedStatesTest):
    # Using a fake calendar here
    class NormalShiftUnitedStatesExceptions(UnitedStates):
        "Normal Shift Fake United State calendar"
        shift_exceptions = (
            (7, 4),  # Month/Day == Fourth of July.
        )

    cal_class = NormalShiftUnitedStatesExceptions

    def test_shift_2015(self):
        # Test a normal shift on 4th of July.
        # 2015: Happens on a Saturday, not shifted
        holidays = self.cal.holidays(2015)
        holiday_dict = dict(holidays)
        fourth_july = date(2015, 7, 4)
        observed = date(2015, 7, 3)
        self.assertIn(fourth_july, holiday_dict)
        self.assertEqual(holiday_dict[fourth_july], "Independence Day")
        self.assertNotIn(observed, holiday_dict)

    def test_shift_2010(self):
        # Test a normal shift on 4th of July.
        # 2010: Happens on a SUN, not shifted
        holidays = self.cal.holidays(2010)
        holiday_dict = dict(holidays)
        fourth_july = date(2010, 7, 4)
        observed = date(2010, 7, 5)
        self.assertIn(fourth_july, holiday_dict)
        self.assertEqual(holiday_dict[fourth_july], "Independence Day")
        self.assertNotIn(observed, holiday_dict)
