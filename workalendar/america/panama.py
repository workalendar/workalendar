# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import timedelta

from workalendar.core import WesternCalendar, ChristianMixin


class Panama(WesternCalendar, ChristianMixin):
    "Panama"
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 9, "Martyrs' Day"),
        (5, 1, "Labour Day"),
        (11, 3, "Independence Day"),
        (11, 5, "Colon Day"),
        (11, 10, "Shout in Villa de los Santos"),
        (12, 2, "Independence from Spain"),
        (12, 8, "Mothers' Day"),
    )

    def get_variable_days(self, year):
        days = super(Panama, self).get_variable_days(year)
        days.append(
            (self.get_ash_wednesday(year) - timedelta(days=1), "Carnival")
        )
        return days
