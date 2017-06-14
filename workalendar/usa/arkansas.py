# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, FloatToNearestWeekdayMixin


class Arkansas(UnitedStates, FloatToNearestWeekdayMixin):
    """Arkansas"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(Arkansas, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Arkansas, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
