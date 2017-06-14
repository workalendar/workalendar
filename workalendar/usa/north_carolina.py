# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import (
    UnitedStates, DayAfterChristmasNoFloatMixin
)


class NorthCarolina(UnitedStates, DayAfterChristmasNoFloatMixin):
    """North Carolina"""
    include_good_friday = True
    include_christmas_eve = True
    include_thanksgiving_friday = True

    # FIXME: should if shift or not?
    def get_variable_days(self, year):
        days = super(NorthCarolina, self).get_variable_days(year)
        days.extend([
            self.get_day_after_christmas(year)
        ])
        return days
