# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-MD')
class Maryland(UnitedStates):
    """Maryland"""
    thanksgiving_friday_label = "Native American Heritage Day"
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Maryland, self).get_variable_days(year)
        if Maryland.is_presidential_year(year):
            days.append(self.get_election_day(year))
        return days
