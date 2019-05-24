# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from workalendar.core import MON
from ..registry_tools import iso_register


@iso_register('US-AK')
class Alaska(UnitedStates):
    """Alaska"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (10, 18, 'Alaska Day'),
    )
    include_columbus_day = False

    def get_variable_days(self, year):
        days = super(Alaska, self).get_variable_days(year)
        days.append(
            (Alaska.get_last_weekday_in_month(year, 3, MON), "Seward's Day")
        )
        return days
