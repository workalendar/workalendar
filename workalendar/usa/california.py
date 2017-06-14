# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import MON
from .core import UnitedStates, CesarChavezDayMixin


class California(UnitedStates, CesarChavezDayMixin):
    """California"""
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(California, self).get_variable_days(year)
        days.extend([
            (self.get_nth_weekday_in_month(year, 10, MON, 2),
             "Indingenous People's Day")
        ])
        return days

    def get_fixed_holidays(self, year):
        days = super(California, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
