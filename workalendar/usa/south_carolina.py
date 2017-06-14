# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import (
    UnitedStates, DayAfterChristmasNoFloatMixin
)


class SouthCarolina(UnitedStates, DayAfterChristmasNoFloatMixin):
    """South Carolina"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 10, "Confederate Memorial Day"),
    )
    include_good_friday = True
    include_christmas_eve = True
    include_thanksgiving_friday = True

    # FIXME: should it shift or not?
    def get_variable_days(self, year):
        days = super(SouthCarolina, self).get_variable_days(year)
        days.extend([
            self.get_day_after_christmas(year)
        ])
        return days
