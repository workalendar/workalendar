# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Slovenia(WesternCalendar, ChristianMixin):
    "Slovenia"
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    include_assumption = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 8, "Preseren Day, the Slovenian Cultural Holiday"),
        (4, 27, "Day of Uprising Against Occupation"),
        (5, 1, "Labour Day"),
        (5, 2, "Labour Day"),
        (6, 25, "Statehood Day"),
        (10, 31, "Reformation Day"),
        (11, 1, "Day of Remembrance of the Dead"),
        (12, 26, "Independence and Unity Day"),
    )
