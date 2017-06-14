# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from .core import UnitedStates


class Wisconsin(UnitedStates):
    """Wisconsin"""
    include_christmas_eve = True
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Wisconsin, self).get_variable_days(year)
        days = self.float(days, year)
        return days

    # FIXME: fixed holidays that don't float
    def get_fixed_holidays(self, year):
        days = super(Wisconsin, self).get_fixed_holidays(year)
        days.append((date(year, 12, 31), "New Years Eve"))
        days = self.float(days, year)
        return days
