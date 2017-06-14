# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Arizona(UnitedStates):
    """Arizona"""
    def get_variable_days(self, year):
        days = super(Arizona, self).get_variable_days(year)
        days = self.float(days, year)
        return days

    def get_fixed_holidays(self, year):
        days = super(Arizona, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
