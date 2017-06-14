# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import FRI
from .core import UnitedStates


class Georgia(UnitedStates):
    """Georgia"""
    include_confederation_day = True
    include_washington_birthday_december = True

    def get_variable_days(self, year):
        days = super(Georgia, self).get_variable_days(year)
        days.extend([
            (Georgia.get_nth_weekday_in_month(year, 11, FRI, 4),
             "Robert E. Lee's Birthday (Observed)"),
        ])
        return days
