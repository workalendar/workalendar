# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import MON
from .core import UnitedStates


class RhodeIsland(UnitedStates):
    """Rhode Island"""
    include_federal_presidents_day = False
    include_election_day_even = True

    def get_variable_days(self, year):
        days = super(RhodeIsland, self).get_variable_days(year)
        days.append(
            (self.get_nth_weekday_in_month(year, 8, MON, 2), "Victory Day")
        )
        return days
