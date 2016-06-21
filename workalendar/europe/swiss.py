# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Switzerland(WesternCalendar, ChristianMixin):
    "Switzerland"

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_christmas = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Berchtold's Day"),
        (5, 1, "Labour Day"),
        (8, 1, "National Holiday"),
    )
