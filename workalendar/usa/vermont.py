# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import TUE
from .core import UnitedStates, FloatToNearestWeekdayMixin


class Vermont(UnitedStates, FloatToNearestWeekdayMixin):
    """Vermont"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (8, 16, "Bennington Battle Day"),
    )

    def get_variable_days(self, year):
        days = super(Vermont, self).get_variable_days(year)
        days = self.float(days)
        days.append(
            (self.get_nth_weekday_in_month(year, 3, TUE, 1),
             "Town Meeting Day")
        )
        return days

    def get_fixed_holidays(self, year):
        days = super(Vermont, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
