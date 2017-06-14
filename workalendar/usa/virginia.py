# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import WED, FRI
from .core import UnitedStates


class Virginia(UnitedStates):
    """Virginia"""
    include_christmas_eve = True
    include_thanksgiving_friday = True
    include_boxing_day = True
    shift_exceptions = (
        (12, 26),
    )

    def get_variable_days(self, year):
        days = super(Virginia, self).get_variable_days(year)
        days.extend([
            (self.get_nth_weekday_in_month(year, 1, FRI, 3),
             "Lee-Jackson Day"),
            (self.get_nth_weekday_in_month(year, 11, WED, 4),
             "Additional Thanksgiving Holiday")
        ])
        return days
