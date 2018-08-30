# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('PL')
class Poland(WesternCalendar, ChristianMixin):
    'Poland'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 6, 'Trzech Kroli'),
        (5, 1, 'Labour Day'),
        (5, 3, 'Constitution Day'),
        (11, 11, 'Independence Day'),
    )
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost Sunday"
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_boxing_day = True
