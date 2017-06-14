# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, CesarChavezDayMixin


class Colorado(UnitedStates, CesarChavezDayMixin):
    """Colorado"""

    def get_variable_days(self, year):
        days = super(Colorado, self).get_variable_days(year)
        return days

    def get_fixed_holidays(self, year):
        days = super(Colorado, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
