# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Mississippi(UnitedStates):
    """Mississippi"""
    include_thanksgiving_friday = True
    include_confederation_day = True

    def get_variable_days(self, year):
        days = super(Mississippi, self).get_variable_days(year)
        days = self.float(days, year)
        return days

    def get_fixed_holidays(self, year):
        days = super(Mississippi, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
