# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('AT')
class Austria(WesternCalendar, ChristianMixin):
    name = 'Austria'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "National Holiday"),  # Staatsfeiertag
        (10, 26, "National Holiday"),  # Nationalfeiertag
    )

    include_epiphany = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"  # Stefanitag
