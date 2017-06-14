# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from workalendar.core import SUN
from .core import UnitedStates


class WestVirginia(UnitedStates):
    """West Virginia"""
    include_christmas_eve = True
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(WestVirginia, self).get_variable_days(year)
        days.extend([
            (date(year, 6, 20), "West Virgina Day")
        ])
        if date(year, 6, 20).weekday() == SUN:
            days.append((date(year, 6, 21), "West Virgina Day (Observed)"))
        return days

    # FIXME: fixed holidays that don't float.
    def get_fixed_holidays(self, year):
        days = super(WestVirginia, self).get_fixed_holidays(year)
        days.append((date(year, 12, 31), "New Years Eve"))
        return days
