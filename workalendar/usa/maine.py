# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, PatriotsDayMixin


class Maine(UnitedStates, PatriotsDayMixin):
    """Maine"""
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Maine, self).get_variable_days(year)
        days.extend([
            self.get_patriots_day(year),
        ])
        return days
