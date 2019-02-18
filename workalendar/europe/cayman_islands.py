# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date, timedelta

from ..core import WesternCalendar, ChristianMixin, MON, SAT
from ..registry import iso_register


QUEENS_BIRTHDAY_EXCEPTIONS = {
    2013: date(2013, 6, 17),
    2017: date(2017, 6, 19),
}


@iso_register('KY')
class CaymanIslands(WesternCalendar, ChristianMixin):
    "Cayman Islands"
    include_ash_wednesday = True
    include_good_friday = True
    include_easter_monday = True
    include_boxing_day = True
    shift_new_years_day = True

    def get_variable_days(self, year):
        days = super(CaymanIslands, self).get_variable_days(year)
        days += [
            (self.get_national_heroes_day(year), "National Heroes Day"),
            (self.get_discovery_day(year), "Discovery Day"),
            (self.get_queens_birthday(year), "Queen's Birthday"),
            (self.get_constitution_day(year), "Constitution Day"),
            (self.get_remembrance_day(year), "Remembrance Day"),
        ]

        shifts = self.shift_christmas_boxing_days(year=year)
        days.extend(shifts)

        if year == 2017:
            days += [(date(2017, 5, 24), "Election day")]

        return days

    def get_national_heroes_day(self, year):
        """Fourth Monday in January"""
        return CaymanIslands.get_nth_weekday_in_month(year, 1, MON, 4)

    def get_discovery_day(self, year):
        """Third Monday in May"""
        return CaymanIslands.get_nth_weekday_in_month(year, 5, MON, 3)

    def get_queens_birthday(self, year):
        """On monday after second saturday in June"""
        sat = CaymanIslands.get_nth_weekday_in_month(year, 6, SAT, 2)
        holiday = sat + timedelta(days=2)
        return QUEENS_BIRTHDAY_EXCEPTIONS.get(year, holiday)

    def get_constitution_day(self, year):
        return CaymanIslands.get_nth_weekday_in_month(year, 7, MON, 1)

    def get_remembrance_day(self, year):
        return CaymanIslands.get_nth_weekday_in_month(year, 11, MON, 2)
