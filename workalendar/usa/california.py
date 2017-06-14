# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import MON
from .core import UnitedStates


class California(UnitedStates):
    """California"""
    include_thanksgiving_friday = True
    include_cesar_chavez_day = True

    def get_variable_days(self, year):
        days = super(California, self).get_variable_days(year)
        days.extend([
            (self.get_nth_weekday_in_month(year, 10, MON, 2),
             "Indingenous People's Day")
        ])
        return days
