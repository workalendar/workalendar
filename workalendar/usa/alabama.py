# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..core import MON
from ..registry import iso_register


@iso_register('US-AL')
class Alabama(UnitedStates):
    "Alabama"
    include_confederation_day = True
    martin_luther_king_label = "Robert E. Lee/Martin Luther King Birthday"
    presidents_day_label = "George Washington/Thomas Jefferson Birthday"
    columbus_day_label = ("Columbus Day / Fraternal Day /"
                          " American Indian Heritage Day")

    def get_jefferson_davis_birthday(self, year):
        """
        The first MON of June is Jefferson Davis Birthday
        """
        return (
            self.get_nth_weekday_in_month(year, 6, MON, 1),
            "Jefferson Davis Birthday"
        )

    def get_variable_days(self, year):
        days = super(Alabama, self).get_variable_days(year)
        days.append(self.get_jefferson_davis_birthday(year))
        return days


class AlabamaBaldwinCounty(Alabama):
    "Baldwin County, Alabama"
    include_mardi_gras = True


class AlabamaMobileCounty(Alabama):
    "Mobile County, Alabama"
    include_mardi_gras = True


class AlabamaPerryCounty(Alabama):
    "Mobile Perry, Alabama"

    def get_obama_day(self, year):
        """
        Obama Day happens on the 2nd MON of November.
        """
        return (
            self.get_nth_weekday_in_month(year, 11, MON, 2),
            "Obama Day"
        )

    def get_variable_days(self, year):
        days = super(AlabamaPerryCounty, self).get_variable_days(year)
        days.append(self.get_obama_day(year))
        return days
