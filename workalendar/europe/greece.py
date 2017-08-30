# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from workalendar.core import WesternCalendar, OrthodoxMixin
from workalendar.registry import iso_register


@iso_register('GR')
class Greece(OrthodoxMixin, WesternCalendar):
    name = 'Greece'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 25, "Independence Day"),
        (5, 1, "Labour Day"),
        (10, 28, "Ohi Day"),
    )
    include_epiphany = True
    include_clean_monday = True
    include_annunciation = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost"
    include_whit_monday = True
    include_assumption = True
    include_boxing_day = True
    boxing_day_label = "Glorifying Mother of God"
