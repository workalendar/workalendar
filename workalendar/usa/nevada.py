# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import FRI
from .core import UnitedStates, FloatToNearestWeekdayMixin


class Nevada(UnitedStates, FloatToNearestWeekdayMixin):
    """Nevada"""
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Nevada, self).get_variable_days(year)
        days = self.float(days)
        days.extend([
            (self.get_last_weekday_in_month(year, 10, FRI), "Nevada Day")
        ])
        return days

    def get_fixed_holidays(self, year):
        days = super(Nevada, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
