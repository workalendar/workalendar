# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Norway(WesternCalendar, ChristianMixin):
    "Norway"
    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_whit_sunday = True
    include_boxing_day = True
    boxing_day_label = "St Stephen's Day"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (5, 17, "Constitution Day"),
    )
