# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('MT')
class Malta(WesternCalendar, ChristianMixin):
    'Malta'

    include_good_friday = True
    include_assumption = True
    include_immaculate_conception = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        # National Holidays
        (3, 31, "Freedom Day"),            # (Jum il-Ħelsien)
        (6, 7, "Sette Giugno"),
        (9, 8, "Victory Day"),             # (Jum il-Vitorja)
        (9, 21, "Independence Day"),       # (Jum l-Indipendenza)
        (12, 13, "Republic Day"),          # (Jum ir-Repubblika)
        # Public Holidays
        (1, 1, "New Year's Day"),          # (L-Ewwel tas-Sena)
        (2, 10, "Feast of Saint Paul's Shipwreck"),
        (3, 19, "Feast of Saint Joseph"),  # (San Ġużepp)
        (5, 1, "Worker's Day"),            # (Jum il-Ħaddiem)
        (6, 29, "Feast of Saint Peter & Saint Paul"),  # (L-Imnarja)
    )
