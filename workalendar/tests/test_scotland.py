from datetime import date
from unittest import TestCase
import warnings

from . import GenericCalendarTest
from ..europe import (
    Scotland, Aberdeen, Angus, Arbroath, Ayr, CarnoustieMonifieth, Clydebank,
    DumfriesGalloway, Dundee, EastDunbartonshire, Edinburgh, Elgin, Falkirk,
    Fife, Galashiels, Glasgow, Hawick, Inverclyde, Inverness, Kilmarnock,
    Lanark, Linlithgow, Lochaber, NorthLanarkshire, Paisley, Perth,
    ScottishBorders, SouthLanarkshire, Stirling, WestDunbartonshire,
)


class GoodFridayTestMixin:
    def test_good_friday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 3, 30), holidays)


class EasterMondayTestMixin:
    def test_easter_monday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 4, 2), holidays)


class SpringHolidayFirstMondayAprilTestMixin:
    def test_spring_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 4, 2), holidays)


class SpringHolidaySecondMondayAprilTestMixin:
    def test_spring_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 4, 9), holidays)


class SpringHolidayLastMondayMayTestMixin:
    def test_spring_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 5, 28), holidays)


class FairHolidayLastMondayJuneTestMixin:
    def test_fair_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 6, 25), holidays)


class FairHolidayFirstMondayJulyTestMixin:
    def test_fair_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 7, 2), holidays)


class FairHolidaySecondMondayJulyTestMixin:
    def test_fair_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 7, 9), holidays)


class FairHolidayThirdMondayJulyTestMixin:
    def test_fair_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 7, 16), holidays)


class FairHolidayLastMondayJulyTestMixin:
    def test_fair_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 7, 30), holidays)


class FairHolidayFourthFridayJulyTestMixin:
    def test_fair_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 7, 27), holidays)


class FairHolidayFirstMondayAugustTestMixin:
    def test_fair_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 8, 6), holidays)


class LateSummerTestMixin:
    def test_late_summer(self):
        # First monday of september
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 9, 3), holidays)


class BattleStirlingBridgeTestMixin:
    def test_stirling(self):
        # Second monday of september
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 9, 10), holidays)


class AutumnHolidayLastMondaySeptemberTestMixin:
    def test_autumn_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 9, 24), holidays)


class AutumnHolidayFirstMondayOctoberTestMixin:
    def test_autumn_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 10, 1), holidays)


class AutumnHolidaySecondMondayOctoberTestMixin:
    def test_autumn_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 10, 8), holidays)


class AutumnHolidayThirdMondayOctoberTestMixin:
    def test_autumn_holiday(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 10, 15), holidays)


class SaintAndrewTestMixin:
    def test_saint_andrew(self):
        # St. Andrew's day happens on November 30th
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 11, 30), holidays)


class VictoriaDayLastMondayMayTestMixin:
    def test_victoria_day(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 5, 28), holidays)


class SpringHolidayTuesdayAfterFirstMondayMayTestMixin:
    def test_spring_holiday_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 5, 8), holidays)

    def test_spring_holiday_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 5, 2), holidays)


class VictoriaDayFirstMondayJuneTestMixin:
    def test_victoria_day(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 6, 4), holidays)


class VictoriaDayFourthMondayMayTestMixin:
    def test_victoria_day(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 5, 28), holidays)


class AyrGoldCupTestMixin:
    """
    Ayr Gold cup - two holidays for Ayr and Kilmarnock
    """
    def test_ayr_gold_cup(self):
        # Specific holidays in Ayr:
        # * 3rd Friday in September
        # * + the following Monday
        holidays = self.cal.holidays_set(2018)
        gold_cup_friday = date(2018, 9, 21)
        gold_cup_monday = date(2018, 9, 24)
        self.assertIn(gold_cup_friday, holidays)
        self.assertIn(gold_cup_monday, holidays)
        # Testing labels
        holidays = self.cal.holidays(2018)
        holidays_dict = dict(holidays)
        self.assertEqual(holidays_dict[gold_cup_friday], "Ayr Gold Cup Friday")
        self.assertEqual(holidays_dict[gold_cup_monday], "Ayr Gold Cup Monday")


# -----------------------------------------------------------------------------
class SpringHolidayTestCase(TestCase):

    def test_not_implemented_error(self):
        class FakeCalendar(Scotland):
            include_spring_holiday = True

        cal = FakeCalendar()
        with self.assertRaises(NotImplementedError):
            cal.holidays_set(2018)

    def test_correct_implementation(self):
        class FakeCalendar(Scotland):
            include_spring_holiday = True

            def get_spring_holiday(self, year):
                return (date(year, 1, 1), "Spring Holiday")

        cal = FakeCalendar()
        self.assertTrue(cal.holidays_set(2018))


class VictoriaDayTestCase(TestCase):

    def test_not_implemented_error(self):
        class FakeCalendar(Scotland):
            include_victoria_day = True

        cal = FakeCalendar()
        with self.assertRaises(NotImplementedError):
            cal.holidays_set(2018)

    def test_correct_implementation(self):
        class FakeCalendar(Scotland):
            include_victoria_day = True

            def get_victoria_day(self, year):
                return (date(year, 1, 1), "Victoria Day")

        cal = FakeCalendar()
        self.assertTrue(cal.holidays_set(2018))


class FairHolidayTestCase(TestCase):

    def test_not_implemented_error(self):
        class FakeCalendar(Scotland):
            include_fair_holiday = True

        cal = FakeCalendar()
        with self.assertRaises(NotImplementedError):
            cal.holidays_set(2018)

    def test_correct_implementation(self):
        class FakeCalendar(Scotland):
            include_fair_holiday = True

            def get_fair_holiday(self, year):
                return (date(year, 1, 1), "Fair Holiday")

        cal = FakeCalendar()
        self.assertTrue(cal.holidays_set(2018))


class AutumnHolidayTestCase(TestCase):

    def test_not_implemented_error(self):
        class FakeCalendar(Scotland):
            include_autumn_holiday = True

        cal = FakeCalendar()
        with self.assertRaises(NotImplementedError):
            cal.holidays_set(2018)

    def test_correct_implementation(self):
        class FakeCalendar(Scotland):
            include_autumn_holiday = True

            def get_autumn_holiday(self, year):
                return (date(year, 1, 1), "Autumn Holiday")

        cal = FakeCalendar()
        self.assertTrue(cal.holidays_set(2018))


class ScotlandTest(GenericCalendarTest):
    """
    Generic Scotland test calendar.

    Scotland calendar includes the generic holidays + GoodFriday
    Some towns or cities don't necessarily observe it.
    """
    cal_class = Scotland

    def test_init_warning(self):
        warnings.simplefilter("always")
        with warnings.catch_warnings(record=True) as w:
            # Cause all warnings to always be triggered.
            # Trigger a warning.
            self.cal_class()
            # Verify some things
            assert len(w) == 1
            assert issubclass(w[-1].category, UserWarning)
            assert "experimental" in str(w[-1].message)
            # Back to normal filtering
        warnings.simplefilter("ignore")

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)  # New year's day
        self.assertIn(date(2018, 1, 2), holidays)  # New year holiday
        self.assertIn(date(2018, 5, 7), holidays)  # May day
        self.assertIn(date(2018, 12, 25), holidays)  # XMas
        self.assertIn(date(2018, 12, 26), holidays)  # Boxing day

    def test_good_friday(self):
        # By default, Good Friday is not a holiday
        holidays = self.cal.holidays_set(2018)
        self.assertNotIn(date(2018, 3, 30), holidays)


class ScotlandAberdeenTest(
        GoodFridayTestMixin,
        FairHolidaySecondMondayJulyTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        ScotlandTest):
    cal_class = Aberdeen


class ScotlandAngusTest(
        SpringHolidaySecondMondayAprilTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        SaintAndrewTestMixin,
        ScotlandTest):
    cal_class = Angus


class ScotlandArbroathTest(
        FairHolidayThirdMondayJulyTestMixin, ScotlandTest):
    cal_class = Arbroath


class ScotlandAyrTest(
        GoodFridayTestMixin,
        EasterMondayTestMixin,
        SpringHolidayLastMondayMayTestMixin,
        AyrGoldCupTestMixin,
        ScotlandTest):
    cal_class = Ayr


class ScotlandCarnoustieMonifiethTest(
        SpringHolidayFirstMondayAprilTestMixin,
        AutumnHolidayFirstMondayOctoberTestMixin,
        ScotlandTest):
    cal_class = CarnoustieMonifieth


class ScotlandClydebankTest(
        SpringHolidayTuesdayAfterFirstMondayMayTestMixin,
        ScotlandTest):
    cal_class = Clydebank


class ScotlandDumfriesGallowayTest(GoodFridayTestMixin, ScotlandTest):
    cal_class = DumfriesGalloway


class ScotlandDundeeTest(
        SpringHolidayFirstMondayAprilTestMixin,
        VictoriaDayLastMondayMayTestMixin,
        FairHolidayLastMondayJulyTestMixin,
        AutumnHolidayFirstMondayOctoberTestMixin,
        ScotlandTest):
    cal_class = Dundee


class ScotlandEastDunbartonshireTest(
        GoodFridayTestMixin, EasterMondayTestMixin,
        SpringHolidayLastMondayMayTestMixin,
        FairHolidayThirdMondayJulyTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        ScotlandTest):
    cal_class = EastDunbartonshire


class ScotlandEdinburghTest(
        GoodFridayTestMixin, EasterMondayTestMixin,
        ScotlandTest):
    cal_class = Edinburgh

    def test_edinburgh_spring_holiday(self):
        # Stated as the 3rd Monday in April...
        holidays = self.cal.holidays_set(2018)
        spring_holiday = date(2018, 4, 16)
        self.assertIn(spring_holiday, holidays)
        # ... except if it falls on Easter Monday
        # Then it's shifted to the previous week.
        # That was the case in 2017
        holidays = self.cal.holidays(2017)
        holidays_dict = dict(holidays)
        easter_monday = date(2017, 4, 17)
        spring_holiday = date(2017, 4, 10)
        self.assertIn(easter_monday, holidays_dict)
        self.assertIn(spring_holiday, holidays_dict)
        self.assertEqual(holidays_dict[easter_monday], "Easter Monday")
        self.assertEqual(holidays_dict[spring_holiday], "Spring Holiday")

    def test_edinburgh_victoria_day(self):
        # The Monday strictly before May 24th
        holidays = self.cal.holidays_set(2018)
        victoria_day = date(2018, 5, 21)
        self.assertIn(victoria_day, holidays)
        # In 2010, May 24th was a monday, so Victoria Day is on 17th.
        holidays = self.cal.holidays_set(2010)
        victoria_day = date(2010, 5, 17)
        self.assertIn(victoria_day, holidays)

    def test_edinbirgh_autumn_holiday(self):
        # Third Monday in September
        holidays = self.cal.holidays_set(2018)
        autumn_holiday = date(2018, 9, 17)
        self.assertIn(autumn_holiday, holidays)


class ScotlandElginTest(
        SpringHolidaySecondMondayAprilTestMixin,
        FairHolidayLastMondayJuneTestMixin,
        LateSummerTestMixin,
        AutumnHolidayThirdMondayOctoberTestMixin,
        ScotlandTest):
    cal_class = Elgin


class ScotlandFalkirkTest(
        GoodFridayTestMixin,
        EasterMondayTestMixin,
        FairHolidayFirstMondayJulyTestMixin,
        BattleStirlingBridgeTestMixin,
        ScotlandTest):
    cal_class = Falkirk


class ScotlandFifeTest(
        VictoriaDayFirstMondayJuneTestMixin,
        FairHolidayThirdMondayJulyTestMixin,
        AutumnHolidayThirdMondayOctoberTestMixin,
        SaintAndrewTestMixin,
        ScotlandTest):
    cal_class = Fife

    def test_spring_holiday(self):
        # Special computation rule, Fife has TWO spring holidays
        holidays = self.cal.holidays_set(2018)
        # First MON in April
        self.assertIn(date(2018, 4, 2), holidays)
        # First MON in June
        self.assertIn(date(2018, 6, 4), holidays)


class ScotlandGalashiels(VictoriaDayFirstMondayJuneTestMixin, ScotlandTest):
    cal_class = Galashiels

    def test_braw_lads_gathering(self):
        # First friday in July
        holidays = self.cal.holidays_set(2018)
        braw_lads_gathering = date(2018, 7, 6)
        self.assertIn(braw_lads_gathering, holidays)


class ScotlandGlasgowTest(
        EasterMondayTestMixin,
        SpringHolidayLastMondayMayTestMixin,
        FairHolidayThirdMondayJulyTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        ScotlandTest):
    cal_class = Glasgow


class ScotlandHawickTest(ScotlandTest):
    cal_class = Hawick

    def test_common_riding(self):
        # Friday after first monday in june & saturday
        holidays = self.cal.holidays_set(2018)
        common_riding_day1 = date(2018, 6, 8)
        common_riding_day2 = date(2018, 6, 9)
        self.assertIn(common_riding_day1, holidays)
        self.assertIn(common_riding_day2, holidays)


# https://www.inverclyde.gov.uk/council-and-government/council-public-holidays
# These documents say that Spring Holidays happened:
# * on April 11th 2016 (second monday of April)
# * on April 24th 2017 (last monday April)
# * on April 16th 2018 (3rd monday April)
# * on April 29th 2019 (last monday April)
# ...
# I think I'm becoming crazy
class ScotlandInverclydeTest(
        GoodFridayTestMixin, EasterMondayTestMixin,
        LateSummerTestMixin,
        ScotlandTest):
    cal_class = Inverclyde

    def test_spring_holiday(self):
        # Special computation rule, Fife has TWO spring holidays
        holidays = self.cal.holidays_set(2018)
        # Last MON in April
        self.assertIn(date(2018, 4, 30), holidays)
        # First MON in June
        self.assertIn(date(2018, 6, 4), holidays)


class ScotlandInvernessTest(
        SpringHolidayFirstMondayAprilTestMixin,
        FairHolidayFirstMondayJulyTestMixin,
        AutumnHolidayFirstMondayOctoberTestMixin,
        ScotlandTest):
    cal_class = Inverness

    def test_winter_february(self):
        # First MON of February
        holidays = self.cal.holidays_set(2018)
        winter_february = date(2018, 2, 5)
        self.assertIn(winter_february, holidays)

    def test_winter_march(self):
        # First MON of March
        holidays = self.cal.holidays_set(2018)
        winter_march = date(2018, 3, 5)
        self.assertIn(winter_march, holidays)

    def test_samhain_holiday(self):
        # First MON of November
        holidays = self.cal.holidays_set(2018)
        samhain_holiday = date(2018, 11, 5)
        self.assertIn(samhain_holiday, holidays)


class ScotlandKilmarnockTest(
        GoodFridayTestMixin, EasterMondayTestMixin,
        AyrGoldCupTestMixin,
        ScotlandTest):
    cal_class = Kilmarnock


class ScotlandLanarkTest(ScotlandTest):
    cal_class = Lanark

    def test_lanimer_day(self):
        # Second THU in June
        holidays = self.cal.holidays_set(2018)
        lanimer_day = date(2018, 6, 14)
        self.assertIn(lanimer_day, holidays)


class ScotlandLinlithgowTest(ScotlandTest):
    cal_class = Linlithgow

    def test_linlithgow_marches(self):
        # Linlithgow marches is on TUE after the 2nd THU in June
        holidays = self.cal.holidays_set(2018)
        linlithgow_marches = date(2018, 6, 19)
        self.assertIn(linlithgow_marches, holidays)


class ScotlandLochaberTest(ScotlandTest):
    cal_class = Lochaber

    def test_winter_holiday(self):
        # Winter holiday is on last MON in March.
        holidays = self.cal.holidays_set(2018)
        winter_holiday = date(2018, 3, 26)
        self.assertIn(winter_holiday, holidays)
        # Not the 4th, the *last*
        holidays = self.cal.holidays_set(2015)
        winter_holiday = date(2015, 3, 30)
        self.assertIn(winter_holiday, holidays)


class ScotlandNorthLanarkshireTest(
        EasterMondayTestMixin,
        SpringHolidayLastMondayMayTestMixin,
        FairHolidayThirdMondayJulyTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        ScotlandTest):
    cal_class = NorthLanarkshire


class ScotlandPaisleyTest(
        GoodFridayTestMixin, EasterMondayTestMixin,
        VictoriaDayLastMondayMayTestMixin,
        FairHolidayFirstMondayAugustTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        ScotlandTest):
    cal_class = Paisley


class ScotlandPerthTest(
        SpringHolidayFirstMondayAprilTestMixin,
        VictoriaDayFourthMondayMayTestMixin,
        BattleStirlingBridgeTestMixin,
        AutumnHolidayFirstMondayOctoberTestMixin,
        ScotlandTest):
    cal_class = Perth


class ScotlandScottishBordersTest(
        SpringHolidayFirstMondayAprilTestMixin,
        FairHolidayFourthFridayJulyTestMixin,
        AutumnHolidaySecondMondayOctoberTestMixin,
        SaintAndrewTestMixin,
        ScotlandTest):
    cal_class = ScottishBorders


class ScotlandSouthLanarkshireTest(
        GoodFridayTestMixin,
        EasterMondayTestMixin,
        SpringHolidayLastMondayMayTestMixin,
        FairHolidayThirdMondayJulyTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        ScotlandTest):
    cal_class = SouthLanarkshire


class ScotlandStirlingTest(
        GoodFridayTestMixin,
        EasterMondayTestMixin,
        SpringHolidayTuesdayAfterFirstMondayMayTestMixin,
        BattleStirlingBridgeTestMixin,
        ScotlandTest):
    cal_class = Stirling


class ScotlandWestDunbartonshireTest(
        GoodFridayTestMixin,
        EasterMondayTestMixin,
        AutumnHolidayLastMondaySeptemberTestMixin,
        ScotlandTest):
    cal_class = WestDunbartonshire
