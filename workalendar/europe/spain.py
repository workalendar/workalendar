# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Spain(WesternCalendar, ChristianMixin):
    "Spain"
    include_epiphany = True
    include_immaculate_conception = True
    include_good_friday = True
    include_assumption = True
    include_all_saints = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, u"Día del trabajador"),
        (10, 12, u"Fiesta nacional de España"),
        (12, 6, u"Día de la Constitución Española")
    )


class Catalonia(Spain):
    "Catalonia"

    include_easter_monday = True
    include_boxing_day = True
    boxing_day_label = "Sant Esteve"

    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (6, 24, u"Sant Joan"),
        (9, 11, u"Diada nacional de Catalunya"),
    )
