# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from workalendar.core import MON


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
