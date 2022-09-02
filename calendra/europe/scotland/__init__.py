"""
Scotland specific module.

The main source of information is:
https://en.wikipedia.org/wiki/Public_and_bank_holidays_in_Scotland

Note on "inheritance":

* Carnoustie and Monifieth area is a subdivision of Angus
* Lanark is part of South Lanarkshire

FIXME:

* Galashiels is part of the Scottish Borders
* Hawick is part of the Scottish Borders
* Kilmarnock is probably part of AyrShire (?)
* Lanark is part of South Lanarkshire
* Linlithgow... part of N/A
* Lochaber... part of N/A
* ...

"""
# Since Scotland territories have a lot of different variations, it has become
# necessary to split this module and associated tests
from datetime import date, timedelta
import warnings
from ...core import WesternCalendar, MON, THU, FRI
from .mixins import (
    SpringHolidayFirstMondayApril,
    SpringHolidaySecondMondayApril,
    SpringHolidayTuesdayAfterFirstMondayMay,
    SpringHolidayLastMondayMay,
    SpringHolidayFirstMondayJune,
    VictoriaDayFourthMondayMay,
    VictoriaDayLastMondayMay,
    VictoriaDayFirstMondayJune,
    FairHolidayLastMondayJune,
    FairHolidayFirstMondayJuly,
    FairHolidaySecondMondayJuly,
    FairHolidayThirdMondayJuly,
    FairHolidayLastMondayJuly,
    FairHolidayFourthFridayJuly,
    FairHolidayFirstMondayAugust,
    LateSummer,
    BattleStirlingBridge,
    AutumnHolidayLastMondaySeptember,
    AutumnHolidayFirstMondayOctober,
    AutumnHolidaySecondMondayOctober,
    AutumnHolidayThirdMondayOctober,
    AyrGoldCup,
)


class Scotland(WesternCalendar):
    "Scotland"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "New Year Holiday"),
        (12, 26, "Boxing Day"),
    )
    include_spring_holiday = False
    spring_holiday_label = "Spring Holiday"
    include_fair_holiday = False
    include_autumn_holiday = False
    include_saint_andrew = False
    include_victoria_day = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            """
Please bear in mind that every Scotland (sub)calendar is highly experimental.

It appeared throughout out searches that Scottish calendars have many
exceptions and somes sources of information contradicts with each other.

As a consequence, we advise our user to treat this Scotland submodule with
as much care as possible.
"""
        )

    def get_may_day(self, year):
        """
        May Day is the first Monday in May
        """
        return (
            Scotland.get_nth_weekday_in_month(year, 5, MON),
            "May Day"
        )

    def get_spring_holiday(self, year):
        """
        Return spring holiday date and label.

        You need to implement it as soon as the flag `include_spring_holiday`
        is True.
        """
        raise NotImplementedError(
            "Tried to add spring holiday while "
            "`get_spring_holiday` is not implemented.")

    def get_fair_holiday(self, year):
        """
        Return fair holiday date and label.

        You need to implement it as soon as the flag `include_fair_holiday`
        is True.
        """
        raise NotImplementedError(
            "Tried to add fair holiday while "
            "`get_fair_holiday` is not implemented.")

    def get_autumn_holiday(self, year):
        """
        Return autumn holiday date and label.

        You need to implement it as soon as the flag `include_autumn_holiday`
        is True.
        """
        raise NotImplementedError(
            "Tried to add autumn holiday while "
            "`get_autumn_holiday` is not implemented.")

    def get_victoria_day(self, year):
        """
        Return Victoria day date and label.

        You need to implement it as soon as the flag `include_victoria_day`
        is True.
        """
        raise NotImplementedError(
            "Tried to add autumn holiday while "
            "`include_victoria_day` is not implemented.")

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_may_day(year))
        if self.include_spring_holiday:
            # This method is included in the spring_holiday mixins
            days.append(self.get_spring_holiday(year))
        if self.include_fair_holiday:
            # This method is included in the fair_holiday mixins
            days.append(self.get_fair_holiday(year))
        if self.include_autumn_holiday:
            # This method is included in the autumn_holiday mixins
            days.append(self.get_autumn_holiday(year))
        if self.include_victoria_day:
            # This method is included in the victoria_day mixins
            days.append(self.get_victoria_day(year))
        return days

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)
        if self.include_saint_andrew:
            days.append((date(year, 11, 30), "Saint Andrew's Day"))
        return days


class Aberdeen(
        FairHolidaySecondMondayJuly,
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "Aberdeen"
    include_good_friday = True


class Angus(
        SpringHolidaySecondMondayApril,
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "Angus"
    include_saint_andrew = True


class Arbroath(FairHolidayThirdMondayJuly, Scotland):
    "Arbroath"


class Ayr(SpringHolidayLastMondayMay, AyrGoldCup, Scotland):
    "Ayr"
    include_good_friday = True
    include_easter_monday = True


class CarnoustieMonifieth(
        SpringHolidayFirstMondayApril,
        AutumnHolidayFirstMondayOctober,
        Scotland):
    "Carnoustie & Monifieth"


class Clydebank(
        SpringHolidayTuesdayAfterFirstMondayMay,
        Scotland):
    "Clydebank"


class DumfriesGalloway(Scotland):
    "Dumfries & Galloway"
    include_good_friday = True


class Dundee(
        SpringHolidayFirstMondayApril,
        VictoriaDayLastMondayMay,
        FairHolidayLastMondayJuly,
        AutumnHolidayFirstMondayOctober,
        Scotland):
    "Dundee"


class EastDunbartonshire(
        SpringHolidayLastMondayMay,
        FairHolidayThirdMondayJuly,
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "East Dunbartonshire"
    include_good_friday = True
    include_easter_monday = True


class Edinburgh(Scotland):
    "Edinburgh"
    include_good_friday = True
    include_easter_monday = True
    include_spring_holiday = True
    include_victoria_day = True
    include_autumn_holiday = True

    def get_spring_holiday(self, year):
        """
        Return Spring Holiday for Edinburgh.

        Set to the 3rd Monday of April, unless it falls on Easter Monday, then
        it's shifted to previous week.
        """
        easter = self.get_easter_monday(year)
        spring_holiday = self.get_nth_weekday_in_month(year, 4, MON, 3)
        if easter == spring_holiday:
            spring_holiday = self.get_nth_weekday_in_month(
                year, 4, MON, 2)

        return spring_holiday, self.spring_holiday_label

    def get_victoria_day(self, year):
        """
        Return Victoria Day for Edinburgh.

        Set to the Monday strictly before May 24th. It means that if May 24th
        is a Monday, it's shifted to the week before.
        """
        may_24th = date(year, 5, 24)
        # Since "MON(day) == 0", it's either the difference between MON and the
        # current weekday (starting at 0), or 7 days before the May 24th
        shift = may_24th.weekday() or 7
        victoria_day = may_24th - timedelta(days=shift)
        return victoria_day, "Victoria Day"

    def get_autumn_holiday(self, year):
        """
        Return Autumn Holiday for Edinburgh.

        Set to the third Monday in September. Since it's the only region to
        follow this rule, we won't have a Mixin associated to it.
        """
        return (
            self.get_nth_weekday_in_month(year, 9, MON, 3),
            "Autumn Holiday"
        )


class Elgin(
        SpringHolidaySecondMondayApril,
        FairHolidayLastMondayJune,
        LateSummer,
        AutumnHolidayThirdMondayOctober,
        Scotland):
    "Elgin"


class Falkirk(FairHolidayFirstMondayJuly, BattleStirlingBridge, Scotland):
    "Falkirk"
    include_good_friday = True
    include_easter_monday = True


class Fife(
        VictoriaDayFirstMondayJune,
        FairHolidayThirdMondayJuly,
        AutumnHolidayThirdMondayOctober,
        Scotland):
    "Fife"
    include_saint_andrew = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Special computation rule, Fife has TWO spring holidays
        # 1. First Monday in April
        days.append((
            self.get_nth_weekday_in_month(year, 4, MON),
            "Spring Holiday"
        ))
        # 2. First Monday in June
        days.append((
            self.get_nth_weekday_in_month(year, 6, MON),
            "Spring Holiday"
        ))
        return days


class Galashiels(SpringHolidayFirstMondayJune, Scotland):
    "Galashiels"

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Adding Braw Lads Gathering, 1st Friday in July
        days.append((
            self.get_nth_weekday_in_month(year, 7, FRI),
            "Braw Lads Gathering"
        ))
        return days


class Glasgow(
        SpringHolidayLastMondayMay,
        FairHolidayThirdMondayJuly,
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "Glasgow"
    include_easter_monday = True


class Hawick(Scotland):
    "Hawick"

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Common Riding happens on the FRI after the first MON in June
        first_monday = self.get_nth_weekday_in_month(year, 6, MON)
        friday = first_monday + timedelta(days=4)
        # And on the saturday. Adding this one, even if SAT is already a
        # non-working day.
        saturday = first_monday + timedelta(days=5)
        days.append((friday, "Common Riding Day 1"))
        days.append((saturday, "Common Riding Day 2"))
        return days


class Inverclyde(LateSummer, Scotland):
    "Inverclyde"
    include_good_friday = True
    include_easter_monday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Special computation rule, Inverclyde has TWO spring holidays
        # 1. First Monday in April
        days.append((
            self.get_last_weekday_in_month(year, 4, MON),
            "Spring Holiday"
        ))
        # 2. First Monday in June
        days.append((
            self.get_nth_weekday_in_month(year, 6, MON),
            "Spring Holiday"
        ))
        return days


class Inverness(
        SpringHolidayFirstMondayApril,
        FairHolidayFirstMondayJuly,
        AutumnHolidayFirstMondayOctober,
        Scotland):
    "Inverness"

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((
            self.get_nth_weekday_in_month(year, 2, MON),
            "Winter Holiday (February)"
        ))
        days.append((
            self.get_nth_weekday_in_month(year, 3, MON),
            "Winter Holiday (March)"
        ))
        days.append((
            self.get_nth_weekday_in_month(year, 11, MON),
            "Samhain Holiday"
        ))
        return days


class Kilmarnock(AyrGoldCup, Scotland):
    "Kilmarnock"
    include_good_friday = True
    include_easter_monday = True


class Lanark(Scotland):
    "Lanark"

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Lanimer is 2nd THU in June
        days.append((
            self.get_nth_weekday_in_month(year, 6, THU, 2),
            "Lanimer Day"
        ))
        return days


class Linlithgow(Scotland):
    "Linlithgow"
    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Linlithgow Marches is on TUE after the 2nd THU in June
        second_thursday = self.get_nth_weekday_in_month(year, 6, THU, 2)
        marches_day = second_thursday + timedelta(days=5)
        days.append((
            marches_day,
            "Linlithgow Marches"
        ))
        return days


class Lochaber(Scotland):
    "Lochaber"
    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Winter holiday is on the last MON of march
        days.append((
            self.get_last_weekday_in_month(year, 3, MON),
            "Winter holiday"
        ))
        return days


class NorthLanarkshire(
        SpringHolidayLastMondayMay,
        FairHolidayThirdMondayJuly,
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "North Lanarkshire"
    include_easter_monday = True


class Paisley(
        VictoriaDayLastMondayMay,
        FairHolidayFirstMondayAugust,
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "Paisley"
    include_good_friday = True
    include_easter_monday = True


class Perth(
        SpringHolidayFirstMondayApril,
        VictoriaDayFourthMondayMay,
        BattleStirlingBridge,
        AutumnHolidayFirstMondayOctober,
        Scotland):
    "Perth"


class ScottishBorders(
        SpringHolidayFirstMondayApril,
        FairHolidayFourthFridayJuly,
        AutumnHolidaySecondMondayOctober,
        Scotland):
    "Scottish Borders"
    include_saint_andrew = True


class SouthLanarkshire(
        SpringHolidayLastMondayMay,
        FairHolidayThirdMondayJuly,
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "South Lanarkshire"
    include_good_friday = True
    include_easter_monday = True


class Stirling(
        SpringHolidayTuesdayAfterFirstMondayMay,
        BattleStirlingBridge,
        Scotland):
    "Stirling"
    include_good_friday = True
    include_easter_monday = True


class WestDunbartonshire(
        AutumnHolidayLastMondaySeptember,
        Scotland):
    "West Dunbartonshire"
    include_good_friday = True
    include_easter_monday = True
