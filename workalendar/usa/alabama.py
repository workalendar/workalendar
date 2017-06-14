# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, FloatToNearestWeekdayMixin
from workalendar.core import MON


class Alabama(UnitedStates, FloatToNearestWeekdayMixin):
    "Alabama"
    include_confederation_day = True

    def get_variable_days(self, year):
        days = super(Alabama, self).get_variable_days(year)
        days = self.float(days)
        days.extend([
            (Alabama.get_nth_weekday_in_month(year, 6, MON, 1),
             "Jefferson Davis Birthday")
        ])
        return days

    def get_fixed_holidays(self, year):
        days = super(Alabama, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
