# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..core import TUE
from ..registry import iso_register
from .core import UnitedStates


@iso_register('US-VT')
class Vermont(UnitedStates):
    """Vermont"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (8, 16, "Bennington Battle Day"),
    )
    include_columbus_day = False

    def get_variable_days(self, year):
        days = super(Vermont, self).get_variable_days(year)
        days.append(
            (self.get_nth_weekday_in_month(year, 3, TUE, 1),
             "Town Meeting Day")
        )
        return days
