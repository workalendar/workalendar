# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, FloatToNearestWeekdayMixin


class Missouri(UnitedStates, FloatToNearestWeekdayMixin):
    """Missouri"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
        (5, 8, "Truman Day"),
    )

    def get_variable_days(self, year):
        days = super(Missouri, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Missouri, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
