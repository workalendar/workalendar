# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from workalendar.core import WesternCalendar, IslamicMixin, ChristianMixin


class Benin(WesternCalendar, IslamicMixin, ChristianMixin):
    "Benin"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Tabaski"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 10, "Traditional Day"),
        (5, 1, "Labour Day"),
        (8, 1, "Independence Day"),
        (10, 26, "Armed Forces Day"),
        (11, 30, "National Day"),
    )
