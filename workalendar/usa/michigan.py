# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from .core import UnitedStates


class Michigan(UnitedStates):
    """Michigan"""
    include_christmas_eve = True
    include_thanksgiving_friday = True

    # FIXME: fixed with float here
    def get_fixed_holidays(self, year):
        days = super(Michigan, self).get_fixed_holidays(year)
        days.append((date(year, 12, 31), "New Years Eve"))
        return days
