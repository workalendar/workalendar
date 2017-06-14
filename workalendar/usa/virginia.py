# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import WED, FRI
from .core import (
    UnitedStates, FloatToNearestWeekdayMixin, DayAfterChristmasNoFloatMixin
)


class Virginia(UnitedStates, FloatToNearestWeekdayMixin,
               DayAfterChristmasNoFloatMixin):
    """Virginia"""
    include_christmas_eve = True
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Virginia, self).get_variable_days(year)
        days = self.float(days)
        days.extend([
            (self.get_nth_weekday_in_month(year, 1, FRI, 3),
             "Lee-Jackson Day"),
            (self.get_nth_weekday_in_month(year, 11, WED, 4),
             "Additional Thanksgiving Holiday")
        ])
        return days

    def get_fixed_holidays(self, year):
        days = super(Virginia, self).get_fixed_holidays(year)
        days = self.float(days, year)
        days += [self.get_day_after_christmas(year)]
        return days
