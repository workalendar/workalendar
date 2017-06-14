# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, FloatToNearestWeekdayMixin
from workalendar.core import MON


class Alaska(UnitedStates, FloatToNearestWeekdayMixin):
    """Alaska"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (10, 18, 'Alaska Day'),
    )

    def get_variable_days(self, year):
        days = super(Alaska, self).get_variable_days(year)
        days = self.float(days)
        days.append(
            (Alaska.get_last_weekday_in_month(year, 3, MON), "Seward's Day")
        )
        return days

    def get_fixed_holidays(self, year):
        days = super(Alaska, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
