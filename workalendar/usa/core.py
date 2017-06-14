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

    # MLK
    martin_luther_king_label = 'Martin Luther King, Jr. Day'

    include_thanksgiving_friday = False
    thanksgiving_friday_label = "Thanksgiving Friday"
    # Some states don't include Washington's Birthday, or move it to December.
    include_federal_presidents_day = True
    presidents_day_label = "Washington's Birthday"

    # Columbus day is included by default
    include_columbus_day = True
    columbus_day_label = "Columbus Day"
    # Confederation day
    include_confederation_day = False
    # Shift day mechanism
    # These days won't be shifted to next MON or previous FRI
    shift_exceptions = (
        # Exemple:
        # (11, 11),  # Veterans day won't be shifted
    )

    def shift(self, holidays, year):
        new_holidays = []
        holiday_lookup = [x[0] for x in holidays]
        exceptions = [
            date(year, month, day) for month, day in self.shift_exceptions
        ]

        # For each holiday available:
        # * if it falls on SUN, add the observed on MON
        # * if it falls on SAT, add the observed on FRI
        for day, label in holidays:
            # ... except if it's been explicitely excepted.
            if day in exceptions:
                continue
            if day.weekday() == SAT:
                new_holidays.append((day - timedelta(days=1),
                                     label + " (Observed)"))
            elif day.weekday() == SUN:
                new_holidays.append((day + timedelta(days=1),
                                     label + " (Observed)"))

        # If year+1 January the 1st is on SAT, add the FRI before to observed
        if date(year + 1, 1, 1).weekday() == SAT:
            new_holidays.append((date(year, 12, 31,),
                                 "New Years Day (Observed)"))

        # Special rules for XMas and XMas Eve
        christmas = date(year, 12, 25)
        christmas_eve = date(year, 12, 24)
        # Is XMas eve in your calendar?
        if christmas_eve in holiday_lookup:
            # You are observing the THU before, as an extra XMas Eve
            if christmas.weekday() == SAT:
                new_holidays.append((date(year, 12, 23),
                                     "Christmas Eve (Observed)"))
            # You are observing the 26th (TUE) and 27th (WED)
            elif christmas.weekday() == MON:
                new_holidays.append((date(year, 12, 26),
                                     "Christmas Eve (Observed)"))
                new_holidays.append((date(year, 12, 27),
                                     "Christmas Day (Observed)"))
        return holidays + new_holidays

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
        return (day, "Confederate Memorial Day")

    def get_martin_luther_king_day(self, year):
        """
        Martin Luther King days is on the 3rd MON of January
        """
        day = UnitedStates.get_nth_weekday_in_month(year, 1, MON, 3)
        return (day, self.martin_luther_king_label)

    def get_presidents_day(self, year):
        """
        Presidents Day is on the 3rd MON of February

        May be called Washington's or Lincoln's birthday
        """
        day = UnitedStates.get_nth_weekday_in_month(year, 2, MON, 3)
        return (day, self.presidents_day_label)

    def get_columbus_day(self, year):
        """
        Columbus day is on the 2nd MON of October.

        Only half of the states recognize it.
        """
        day = UnitedStates.get_nth_weekday_in_month(year, 10, MON, 2)
        return (day, self.columbus_day_label)

    def get_variable_days(self, year):
        # usual variable days
        days = super(UnitedStates, self).get_variable_days(year)
        days.extend([
            self.get_martin_luther_king_day(year),

            (UnitedStates.get_last_weekday_in_month(year, 5, MON),
                "Memorial Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 9, MON),
                "Labor Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 11, THU, 4),
                "Thanksgiving Day"),
        ])

        if self.include_federal_presidents_day:
            days.append(self.get_presidents_day(year))

        if self.include_columbus_day:
            days.append(self.get_columbus_day(year))

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

    def get_calendar_holidays(self, year):
        """
        Will return holidays and their shifted days
        """
        days = super(UnitedStates, self).get_calendar_holidays(year)
        days = self.shift(days, year)
        return days


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
