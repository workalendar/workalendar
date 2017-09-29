# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('ES')
class Spain(WesternCalendar, ChristianMixin):
    name = 'Spain'

    include_epiphany = True
    include_immaculate_conception = True
    include_good_friday = True
    include_assumption = True
    include_all_saints = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Día del trabajador"),
        (10, 12, "Fiesta nacional de España"),
        (12, 6, "Día de la Constitución Española")
    )


class Catalonia(Spain):
    "Catalonia"

    include_easter_monday = True
    include_boxing_day = True
    boxing_day_label = "Sant Esteve"

    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (6, 24, "Sant Joan"),
        (9, 11, "Diada nacional de Catalunya"),
    )
