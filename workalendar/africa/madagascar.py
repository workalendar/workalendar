# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('MG')
class Madagascar(WesternCalendar, ChristianMixin):
    "Madagascar"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 29, "Martyrs' Day"),
        (5, 1, "Labour Day"),
        (6, 26, "Independence Day"),
    )
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
