# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class NewJersey(UnitedStates):
    """New Jersey"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(NewJersey, self).get_variable_days(year)
        days.append(self.get_election_day(year))
        return days
