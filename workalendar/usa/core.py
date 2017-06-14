# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date, timedelta

from workalendar.core import WesternCalendar, ChristianMixin, Calendar
from workalendar.core import SUN, MON, TUE, WED, THU, FRI, SAT


class UnitedStates(WesternCalendar, ChristianMixin):
    "United States of America"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 4, 'Independence Day'),
        (11, 11, 'Veterans Day'),
    )
    include_thanksgiving_friday = False
    thanksgiving_friday_label = "Thanksgiving Friday"
    # Some states don't include Washington's Birthday, or move it to December.
    include_federal_washington_bday = True
    # Columbus day is included by default
    include_columbus_day = True
    # Confederation day
    include_confederation_day = False

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_thanksgiving_friday(self, year):
        "Thanksgiving friday is on the 4th Friday in November"
        return (
            self.get_nth_weekday_in_month(year, 11, FRI, 4),
            self.thanksgiving_friday_label
        )

    def get_confederate_day(self, year):
        """
        Confederation memorial day is on the 4th MON of April.
        """
        day = self.get_nth_weekday_in_month(year, 4, MON, 4)
        return (day, "Confederate Day")

    def get_variable_days(self, year):
        # usual variable days
        days = super(UnitedStates, self).get_variable_days(year)
        days.extend([
            (UnitedStates.get_nth_weekday_in_month(year, 1, MON, 3),
                'Martin Luther King, Jr. Day'),

            (UnitedStates.get_last_weekday_in_month(year, 5, MON),
                "Memorial Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 9, MON),
                "Labor Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 11, THU, 4),
                "Thanksgiving Day"),
        ])

        if self.include_federal_washington_bday:
            days.append(
                (UnitedStates.get_nth_weekday_in_month(year, 2, MON, 3),
                 "Washington's Birthday"),
            )

        if self.include_columbus_day:
            days.append(
                (UnitedStates.get_nth_weekday_in_month(year, 10, MON, 2),
                 "Columbus Day"),
            )

        if self.include_confederation_day:
            days.append(self.get_confederate_day(year))

        # Inauguration day
        if UnitedStates.is_presidential_year(year - 1):
            inauguration_day = date(year, 1, 20)
            if inauguration_day.weekday() == SUN:
                inauguration_day = date(year, 1, 21)
            days.append((inauguration_day, "Inauguration Day"))

        if self.include_thanksgiving_friday:
            days.append(
                self.get_thanksgiving_friday(year)
            )
        return days


class FloatToNearestWeekdayMixin(Calendar):
    "Float Saturady to Friday, Sunday to Monday"
    def float(self, holidays, year=0):
        new_holidays = []
        holiday_lookup = [x[0] for x in holidays]
        for holiday in holidays:
            if holiday[0].weekday() == SAT:
                new_holidays.append((holiday[0] - timedelta(days=1),
                                     holiday[1] + " (Observed)"))
            elif holiday[0].weekday() == SUN:
                new_holidays.append((holiday[0] + timedelta(days=1),
                                     holiday[1] + " (Observed)"))

        if year > 0 and date(year + 1, 1, 1).weekday() == SAT:
            new_holidays.append((date(year, 12, 31,),
                                 "New Years Day (Observed)"))

        year = holiday_lookup[0].year
        if (date(year, 12, 25) in holiday_lookup and
                date(year, 12, 24) in holiday_lookup and
                date(year, 12, 25).weekday() == SAT):
            new_holidays.append((date(year, 12, 23),
                                 "Christmas Eve (Observed)"))
        if (date(year, 12, 25) in holiday_lookup and
                date(year, 12, 24) in holiday_lookup and
                date(year, 12, 25).weekday() == MON):
            new_holidays.append((date(year, 12, 26),
                                 "Christmas Eve (Observed)"))
            new_holidays.append((date(year, 12, 27),
                                 "Christmas Day (Observed)"))
        return holidays + new_holidays


class WashingtonsBirthdayInDecemberMixin(Calendar):
    """Floating observance, to give long weekend at christmas.

    It's only observed in Georgia and Indiana.
    """
    label_washington_bday_observed = "Washington's Birthday (Observed)"

    def get_washington_birthday(self, year):
        christmas_day = date(year, 12, 25).weekday()
        if christmas_day == MON:
            day = date(year, 12, 26)  # TUE
        elif christmas_day == TUE:
            day = date(year, 12, 24)  # MON
        elif christmas_day == WED:
            day = date(year, 12, 24)  # TUE
        elif christmas_day == THU:
            day = date(year, 12, 26)  # FRI
        elif christmas_day == FRI:
            day = date(year, 12, 24)  # THU
        elif christmas_day == SAT:
            day = date(year, 12, 23)  # THU
        else:  # christmas_day == SUN:
            day = date(year, 12, 23)  # FRI
        return (day, self.label_washington_bday_observed)

    def get_variable_days(self, year):
        days = super(WashingtonsBirthdayInDecemberMixin, self) \
            .get_variable_days(year)
        days.append(self.get_washington_birthday(year))
        return days


class CesarChavezDayMixin(Calendar):
    """31st of March, float to 1st April if Monday"""
    def get_chavez_day(self, year):
        days = [(date(year, 3, 31), "Cesar Chavez Day")]
        if date(year, 3, 31).weekday() == SUN:
            days.append((date(year, 4, 1), "Cesar Chavez Day (Observed)"))
        return days

    def get_variable_days(self, year):
        days = super(CesarChavezDayMixin, self).get_variable_days(year)
        days.extend(self.get_chavez_day(year))
        return days


class DayAfterChristmasNoFloatMixin(Calendar):
    """26th of December - but doesn't ever float"""
    def get_day_after_christmas(self, year):
        days = (date(year, 12, 26), "Day After Christmas")
        return days


class PatriotsDayMixin(Calendar):
    """3rd Monday of April"""
    def get_patriots_day(self, year):
        days = (self.get_nth_weekday_in_month(year, 4, MON, 3),
                "Patriots Day")
        return days
