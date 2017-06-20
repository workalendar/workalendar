# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import timedelta
from .core import UnitedStates


class Louisiana(UnitedStates):
    """Louisiana"""
    include_good_friday = True
    include_election_day_even = True
    include_columbus_day = False

    def get_mardi_gras(self, year):
        sunday = self.get_easter_sunday(year)
        return (sunday - timedelta(days=47), "Mardi Gras")

    def get_variable_days(self, year):
        days = super(Louisiana, self).get_variable_days(year)
        days.append(self.get_mardi_gras(year))
        return days
