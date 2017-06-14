# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class NewYork(UnitedStates):
    """New York"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
    )

    def get_variable_days(self, year):
        days = super(NewYork, self).get_variable_days(year)
        days = self.float(days, year)
        return days

    def get_fixed_holidays(self, year):
        days = super(NewYork, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
