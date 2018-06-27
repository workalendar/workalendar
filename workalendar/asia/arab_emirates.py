# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date

from workalendar.core import WesternCalendar, IslamicMixin
from workalendar.core import MON, TUE, WED, FRI


class ArabEmirates(WesternCalendar, IslamicMixin):
    "Arab Emirates"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 14, "Israa & Miaraj Night"),
        (8, 20, "Arafat (Haj) Day"),
        (9, 11, "Islamic New Year"),
        (11, 19, "Prophet Mohammed's Birthday"),
        (11, 30, "Martyrs' Day"),
        (12, 2, "UAE National Day"),
        (12, 3, "UAE National Day"),
    )
    # Islamic holidays
    include_eid_al_fitr = True
    length_eid_al_fitr = 4
    include_eid_al_adha = True
    length_eid_al_adha = 4
    include_islamic_new_year = True

    def get_variable_days(self, year):
        days = super(ArabEmirates, self).get_variable_days(year)
        return days
