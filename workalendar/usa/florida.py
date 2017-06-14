# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import FRI
from .core import UnitedStates, FloatToNearestWeekdayMixin


class Florida(UnitedStates, FloatToNearestWeekdayMixin):
    """Florida"""
    def get_variable_days(self, year):
        days = super(Florida, self).get_variable_days(year)
        days = self.float(days)
        days.append(
            (Florida.get_nth_weekday_in_month(year, 11, FRI, 4),
             "Friday after Thanksgiving")
        )
        return days

    def get_fixed_holidays(self, year):
        days = super(Florida, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
