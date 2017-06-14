# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from .core import UnitedStates, CesarChavezDayMixin


class Texas(UnitedStates, CesarChavezDayMixin):
    """Texas"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Texas, self).get_variable_days(year)
        days = self.float(days, year)
        return days

    # FIXME: fixed days that DON'T float.
    def get_fixed_holidays(self, year):
        days = super(Texas, self).get_fixed_holidays(year)
        days = self.float(days, year)
        days.extend([
            (date(year, 1, 19), "Confederate Heroes Day"),
            (date(year, 3, 2), "Texas Independence Day"),
            (date(year, 4, 21), "San Jacinto Day"),
            (date(year, 6, 19), "Emancipation Day"),
            (date(year, 8, 27), "Lyndon B. Jonhson Day")
        ])
        return days
