# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Connecticut(UnitedStates):
    """Connecticut"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
    )

    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Connecticut, self).get_variable_days(year)
        days = self.float(days, year)
        return days

    def get_fixed_holidays(self, year):
        days = super(Connecticut, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
