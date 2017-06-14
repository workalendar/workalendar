# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import (
    UnitedStates, FloatToNearestWeekdayMixin, DayAfterChristmasNoFloatMixin
)


class SouthCarolina(UnitedStates, FloatToNearestWeekdayMixin,
                    DayAfterChristmasNoFloatMixin):
    """South Carolina"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 10, "Confederate Memorial Day"),
    )
    include_good_friday = True
    include_christmas_eve = True
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(SouthCarolina, self).get_variable_days(year)
        days = self.float(days)
        days.extend([
            self.get_day_after_christmas(year)
        ])
        return days

    def get_fixed_holidays(self, year):
        days = super(SouthCarolina, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
