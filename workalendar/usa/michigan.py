# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from ..core import SUN
from ..registry_tools import iso_register

from .core import UnitedStates


@iso_register('US-MI')
class Michigan(UnitedStates):
    """Michigan"""
    include_christmas_eve = True
    include_thanksgiving_friday = True
    include_election_day_even = True
    include_columbus_day = False

    def get_fixed_holidays(self, year):
        days = super(Michigan, self).get_fixed_holidays(year)

        # New Year's Eve to be added
        new_years_eve = date(year, 12, 31)
        days.append(
            (new_years_eve, "New Years Eve")
        )

        # Christmas Eve & New Year's Eve shift when it falls on SUN
        xmas_eve = date(year, 12, 24)
        if xmas_eve.weekday() == SUN:
            days.append(
                (date(year, 12, 22), "Christmas Eve shift")
            )
            days.append(
                (date(year, 12, 29), "New Years Eve Shift")
            )

        return days
