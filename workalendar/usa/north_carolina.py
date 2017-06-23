# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import warnings
from datetime import date
from workalendar.core import MON, TUE, WED, THU, FRI, SAT, SUN
from .core import UnitedStates


class NorthCarolina(UnitedStates):
    """North Carolina"""
    include_good_friday = True
    include_christmas_eve = True
    include_thanksgiving_friday = True
    include_boxing_day = True
    include_federal_presidents_day = False
    include_columbus_day = False

    def get_christmas_shifts(self, year):
        """
        Return Specific Christmas days extra shifts.
        There must be 3 holidays in a row: Christmas Eve, Christmas Day and
        Boxing Day. If one or the other falls on SUN/SAT, extra days must be
        added.
        """
        xmas = date(year, 12, 25)
        if xmas.weekday() in (TUE, WED, THU):
            # No shift, move along
            return []
        if xmas.weekday() == FRI:
            return [
                (date(year, 12, 28), "Boxing day shift"),
            ]
        elif xmas.weekday() == SAT:
            warnings.warn(
                "We didn't find any documentation about this configuration for"
                " the Christmas shift. Please use with care or help us build"
                " a better Workalendar"
            )
            return [
                (date(year, 12, 27), "Christmas Day shift"),
                (date(year, 12, 28), "Boxing Day shift"),
            ]
        elif xmas.weekday() == SUN:
            return [
                (date(year, 12, 23), "Christmas Eve shift"),
                (date(year, 12, 27), "Boxing Day shift"),
            ]
        elif xmas.weekday() == MON:
            return [
                (date(year, 12, 27), "Christmas Eve shift"),
            ]

    def get_variable_days(self, year):
        days = super(NorthCarolina, self).get_variable_days(year)
        days.extend(self.get_christmas_shifts(year))
        return days
