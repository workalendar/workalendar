# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import (
    UnitedStates, DayAfterChristmasNoFloatMixin
)


class Kansas(UnitedStates, DayAfterChristmasNoFloatMixin):
    """Kansas"""
    include_christmas_eve = True
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Kansas, self).get_variable_days(year)
        days.extend([
            self.get_day_after_christmas(year)
        ])
        return days
