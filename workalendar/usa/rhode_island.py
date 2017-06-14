# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import MON
from .core import UnitedStates


class RhodeIsland(UnitedStates):
    """Rhode Island"""

    def get_variable_days(self, year):
        days = super(RhodeIsland, self).get_variable_days(year)
        days = self.float(days, year)
        days.append(
            (self.get_nth_weekday_in_month(year, 8, MON, 2), "Victory Day"))
        return days

    def get_fixed_holidays(self, year):
        days = super(RhodeIsland, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
