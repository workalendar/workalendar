# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date

from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON, TUE, WED, FRI


class Paraguay(WesternCalendar, ChristianMixin):
    "Paraguay"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 26, "Day of Heroes"),
        (5, 1, "Labour Day"),
        (5, 14, "Independence Day"),
        (5, 15, "Independence Day"),
        (6, 12, "Chaco Armistice"),
        (8, 15, "Founding of Asuncion"),
        (9, 29, "Boqueron Battle Victory Day"),
        (9, 19, "Army holiday"),
        (12, 8, "Virgin of Caacupé Day"),
        (12, 31, "New Year's Eve"),
    )
    include_holy_thursday = True
    include_good_friday = True
    include_easter_saturday = True
    include_assumption = False
    include_all_saints = False
    include_immaculate_conception = False

    def get_variable_days(self, year):
        days = super(Paraguay, self).get_variable_days(year)
        #days.append((reformation_day, "Reformation Day"))

        return days
