# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import FRI
from .core import UnitedStates


class Nebraska(UnitedStates):
    """Nebraska"""
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Nebraska, self).get_variable_days(year)
        days.append(
            (self.get_last_weekday_in_month(year, 4, FRI), "Arbor Day")
        )
        return days
