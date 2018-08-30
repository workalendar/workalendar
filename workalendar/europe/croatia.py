# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('HR')
class Croatia(WesternCalendar, ChristianMixin):
    'Croatia'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "International Workers' Day"),
        (6, 22, "Anti-Fascist Struggle Day"),
        (6, 25, "Statehood Day"),
        (8, 5, "Victory & Homeland Thanksgiving & Day of Croatian defenders"),
        (10, 8, "Independence Day"),
    )

    include_epiphany = True
    include_easter_sunday = True
    include_easter_monday = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"
