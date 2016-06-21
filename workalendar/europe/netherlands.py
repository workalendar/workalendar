# -*- coding: utf-8 -*-
from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin


class Netherlands(WesternCalendar, ChristianMixin):
    "Netherlands"
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 5, "Liberation Day"),
        (12, 31, "New Year's Eve"),
    )

    def get_kingsday(self, year):
        """27 April unless this is a Sunday in which case it is the 26th """
        if (date(year, 4, 27).weekday() != 6):
            return date(year, 4, 27)
        return date(year, 4, 26)

    def get_variable_days(self, year):
        days = super(Netherlands, self).get_variable_days(year)
        days += [
            (
                self.get_kingsday(year),
                "King's Day")
        ]
        return days
