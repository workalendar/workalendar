# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Minnesota(UnitedStates):
    """Minnesota"""
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Minnesota, self).get_variable_days(year)
        days = self.float(days, year)
        return days

    def get_fixed_holidays(self, year):
        days = super(Minnesota, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
