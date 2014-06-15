# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import SUN, MON, TUE, WED, THU, FRI, SAT


class UnitedStates(WesternCalendar, ChristianMixin):
    "United States of America"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 4, 'Independence Day'),
        (11, 11, 'Veterans Day'),
    )

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_variable_days(self, year):
        # usual variable days
        days = super(UnitedStates, self).get_variable_days(year)
        days += [
            (UnitedStates.get_nth_weekday_in_month(year, 1, MON, 3),
                'Martin Luther King, Jr. Day'),

            (UnitedStates.get_nth_weekday_in_month(year, 2, MON, 3),
                "Washington's Birthday"),

            (UnitedStates.get_last_weekday_in_month(year, 5, MON),
                "Memorial Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 9, MON),
                "Labor Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 10, MON, 2),
                "Colombus Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 11, THU, 4),
                "Thanksgiving Day"),
        ]
        # Inauguration day
        if UnitedStates.is_presidential_year(year - 1):
            inauguration_day = date(year, 1, 20)
            if inauguration_day.weekday() == SUN:
                inauguration_day = date(year, 1, 21)
            days.append((inauguration_day, "Inauguration Day"))
        return days


