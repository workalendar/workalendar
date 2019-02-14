from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-AS')
class AmericanSamoa(UnitedStates):
    "American Samoa"
    include_boxing_day = True
    boxing_day_label = "Family Day"

    def get_flag_day(self, year):
        """
        Flag day is on April 17th
        """
        return (
            date(year, 4, 17),
            "Flag Day"
        )

    def get_variable_days(self, year):
        days = super(AmericanSamoa, self).get_variable_days(year)
        days.extend([
            self.get_flag_day(year),
        ])
        return days
