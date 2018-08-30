# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import warnings

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-MT')
class Montana(UnitedStates):
    """Montana"""
    include_election_day_even = True

    def get_variable_days(self, year):
        warnings.warn(
            "Montana states is supposed to observe General Election Day on "
            "even years, but for some reason some sources are including it "
            "in 2019. Please use with care."
        )
        return super(Montana, self).get_variable_days(year)
