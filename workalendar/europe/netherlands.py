# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('NL')
class Netherlands(WesternCalendar, ChristianMixin):
    name = 'Netherlands'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 5, "Liberation Day"),
    )

    def get_king_queen_day(self, year):
        """27 April unless this is a Sunday in which case it is the 26th

        Before 2013 it was called Queensday, falling on
        30 April, unless this is a Sunday in which case it is the 29th.
        """
        if year > 2013:
            if date(year, 4, 27).weekday() != 6:
                return date(year, 4, 27), "King's day"
            else:
                return date(year, 4, 26), "King's day"
        else:
            if date(year, 4, 30).weekday() != 6:
                return date(year, 4, 30), "Queen's day"
            else:
                return date(year, 4, 29), "Queen's day"

    def get_variable_days(self, year):
        days = super(Netherlands, self).get_variable_days(year)
        days.append(self.get_king_queen_day(year))
        return days
