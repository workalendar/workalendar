# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import FRI
from .core import (
    UnitedStates,
    WashingtonsBirthdayInDecemberMixin
)


class Georgia(UnitedStates, WashingtonsBirthdayInDecemberMixin):
    """Georgia"""
    include_confederation_day = True

    def get_variable_days(self, year):
        days = super(Georgia, self).get_variable_days(year)
        days = self.float(days, year)
        days.extend([
            (Georgia.get_nth_weekday_in_month(year, 11, FRI, 4),
             "Robert E. Lee's Birthday (Observed)"),
        ])
        return days

    def get_fixed_holidays(self, year):
        days = super(Georgia, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
