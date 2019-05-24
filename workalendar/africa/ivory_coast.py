# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from ..core import WesternCalendar, IslamicMixin, ChristianMixin
from ..registry_tools import iso_register


@iso_register('CI')
class IvoryCoast(WesternCalendar, ChristianMixin, IslamicMixin):
    "Ivory Coast"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
    include_day_after_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Feast of the Sacrifice"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (8, 7, "Independence Day"),
        (11, 15, "National Peace Day"),
    )
