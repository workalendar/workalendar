# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class EuropeanCentralBank(WesternCalendar, ChristianMixin):
    "European Central Bank"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (12, 26, "St. Stephen's Day"),
    )

    include_good_friday = True
    include_easter_monday = True
