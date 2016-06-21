# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Luxembourg(WesternCalendar, ChristianMixin):
    "Luxembourg"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_all_saints = True
    include_assumption = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 23, "Luxembourg National Holiday"),
    )
