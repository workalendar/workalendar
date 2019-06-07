# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from workalendar.core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('IT')
class Italy(WesternCalendar, ChristianMixin):
    'Italy'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 25, "Liberation Day"),
        (5, 1, "International Workers' Day"),
        (6, 2, "Republic Day"),
    )
    include_immaculate_conception = True
    include_epiphany = True
    include_easter_monday = True
    include_assumption = True
    include_all_saints = True
    include_boxing_day = True
    boxing_day_label = "St Stephen's Day"
