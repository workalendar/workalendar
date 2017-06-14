# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, FloatToNearestWeekdayMixin, PatriotsDayMixin


class Massachusetts(UnitedStates, FloatToNearestWeekdayMixin,
                    PatriotsDayMixin):
    """Massachusetts"""
    def get_variable_days(self, year):
        days = super(Massachusetts, self).get_variable_days(year)
        days = self.float(days)
        days.append(self.get_patriots_day(year))
        return days

    def get_fixed_holidays(self, year):
        days = super(Massachusetts, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
