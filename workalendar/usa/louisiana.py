# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import timedelta
from .core import UnitedStates, FloatToNearestWeekdayMixin


class Louisiana(UnitedStates, FloatToNearestWeekdayMixin):
    """Louisiana"""
    include_good_friday = True

    def get_mardi_gras(self, year):
        sunday = self.get_easter_sunday(year)
        return (sunday - timedelta(days=47), "Mardi Gras")

    def get_variable_days(self, year):
        days = super(Louisiana, self).get_variable_days(year)
        days = self.float(days)
        days.append(self.get_mardi_gras(year))
        return days

    def get_fixed_holidays(self, year):
        days = super(Louisiana, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
