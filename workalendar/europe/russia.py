# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from workalendar.core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('RU')
class Russia(WesternCalendar):
    'Russia'

    shift_new_years_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (1, 7, "Christmas"),
        (2, 23, "Defendence of the Fatherland"),
        (3, 8, "International Women's Day"),
        (5, 1, "Labour Day"),
        (5, 9, "Victory Day"),
        (6, 12, "National Day"),
        (11, 4, "Day of Unity"),
    )
