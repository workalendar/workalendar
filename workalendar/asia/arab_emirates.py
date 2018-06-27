# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date

from workalendar.core import WesternCalendar
from workalendar.core import MON, TUE, WED, FRI


class ArabEmirates(WesternCalendar):
    "Arab Emirates"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 14, "Israa & Miaraj Night"),
        (6, 14, "Eid Al Fitr Holiday"),
        (6, 15, "Eid Al Fitr Holiday"),
        (6, 16, "Eid Al Fitr Holiday"),
        (6, 17, "Eid Al Fitr Holiday"),
        (8, 20, "Arafat (Haj) Day"),
        (8, 21, "Eid Al Adha"),
        (8, 22, "Eid Al Adha"),
        (8, 23, "Eid Al Adha"),
        (9, 11, "Islamic New Year"),
        (11, 19, "Prophet Mohammed's Birthday"),
        (11, 30, "Martyrs' Day"),
        (12, 2, "UAE National Day"),
        (12, 3, "UAE National Day"),
    )
    include_good_friday = False
    include_easter_saturday = False
    include_assumption = False
    include_all_saints = False
    include_immaculate_conception = False

    def get_variable_days(self, year):
        days = super(ArabEmirates, self).get_variable_days(year)
        return days
