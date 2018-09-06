"""
Scotland calendar mixins.

There are so many of them that it became necessary to move them to a different
module.
"""
from workalendar.core import MON, FRI
from datetime import timedelta

from .spring_holiday import (
    SpringHolidayFirstMondayApril,
    SpringHolidaySecondMondayApril,
    SpringHolidayTuesdayAfterFirstMondayMay,
    SpringHolidayLastMondayMay,
    SpringHolidayFirstMondayJune,
)

from .fair_holiday import (
    FairHolidayLastMondayJune,
    FairHolidayFirstMondayJuly,
    FairHolidaySecondMondayJuly,
    FairHolidayThirdMondayJuly,
    FairHolidayLastMondayJuly,
    FairHolidayFourthFridayJuly,
    FairHolidayFirstMondayAugust,
)

from .victoria_day import (
    VictoriaDayFourthMondayMay,
    VictoriaDayLastMondayMay,
    VictoriaDayFirstMondayJune,
)

from .autumn_holiday import (
    AutumnHolidayLastMondaySeptember,
    AutumnHolidayFirstMondayOctober,
    AutumnHolidaySecondMondayOctober,
    AutumnHolidayThirdMondayOctober,
)


class LateSummer(object):
    def get_variable_days(self, year):
        """
        Add Late Summer holiday (First Monday of September)
        """
        days = super(LateSummer, self).get_variable_days(year)
        days.append((
            self.get_nth_weekday_in_month(year, 9, MON),
            "Late Summer Holiday"
        ))
        return days


class BattleStirlingBridge(object):
    def get_variable_days(self, year):
        """
        Add Battle of Stirling Bridge holiday (Second Monday of September)
        """
        days = super(BattleStirlingBridge, self).get_variable_days(year)
        days.append((
            self.get_nth_weekday_in_month(year, 9, MON, 2),
            "Battle of Stirling Bridge Holiday"
        ))
        return days


class AyrGoldCup(object):
    def get_variable_days(self, year):
        days = super(AyrGoldCup, self).get_variable_days(year)
        # Ayr Gold Cup
        gold_cup_friday = self.get_nth_weekday_in_month(year, 9, FRI, 3)
        days.append(
            (gold_cup_friday, "Ayr Gold Cup Friday")
        )
        days.append(
            (gold_cup_friday + timedelta(days=3), "Ayr Gold Cup Monday")
        )
        return days


__all__ = [
    'AyrGoldCup',
    'SpringHolidayFirstMondayApril',
    'SpringHolidaySecondMondayApril',
    'SpringHolidayTuesdayAfterFirstMondayMay',
    'SpringHolidayLastMondayMay',
    'SpringHolidayFirstMondayJune',
    'VictoriaDayFourthMondayMay',
    'VictoriaDayLastMondayMay',
    'VictoriaDayTuesdayAfterFirstMondayMay',
    'VictoriaDayFirstMondayJune',
    'FairHolidayLastMondayJune',
    'FairHolidayFirstMondayJuly',
    'FairHolidaySecondMondayJuly',
    'FairHolidayThirdMondayJuly',
    'FairHolidayLastMondayJuly',
    'FairHolidayFourthFridayJuly',
    'FairHolidayFirstMondayAugust',
    'AutumnHolidayLastMondaySeptember',
    'AutumnHolidayFirstMondayOctober',
    'AutumnHolidaySecondMondayOctober',
    'AutumnHolidayThirdMondayOctober',
]
