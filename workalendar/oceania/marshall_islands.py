# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ..core import WesternCalendar, ChristianMixin
from ..core import FRI
from ..registry import iso_register


@iso_register('MH')
class MarshallIslands(WesternCalendar, ChristianMixin):
    "Marshall Islands"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 3, "Remembrance Day"),
        (5, 1, "Constitution Day"),
        (11, 17, "Presidents' Day"),
        (12, 31, "New Year's Eve"),
    )
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(MarshallIslands, self).get_variable_days(year)
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 7, FRI),
            "Fishermen's Holiday"
        ))
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 9, FRI),
            "Labour Day"
        ))
        days.append((
            MarshallIslands.get_last_weekday_in_month(year, 9, FRI),
            "Manit Day"
        ))
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 12, FRI),
            "Gospel Day"
        ))
        return days
