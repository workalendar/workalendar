# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import warnings
from datetime import date
from workalendar.core import MON, TUE, WED, THU, FRI, SAT
from .core import UnitedStates


class Indiana(UnitedStates):
    """Indiana"""
    include_good_friday = True
    include_thanksgiving_friday = True
    thanksgiving_friday_label = "Lincoln's Birthday"
    include_federal_presidents_day = False
    label_washington_birthday_december = "Washington's Birthday (Observed)"
    include_election_day_even = True
    election_day_label = "General Election Day"

    def get_washington_birthday_december(self, year):
        """
        Washington birthday observance
        Similar to Christmas Eve, but with special rules.
        It's only observed in Georgia.
        """
        warnings.warn(
            "Washington birthday rules for Indiana State are confusing. "
            "Use this calendar with care")
        christmas_day = date(year, 12, 25).weekday()
        if christmas_day == MON:
            day = date(year, 12, 26)  # TUE
        elif christmas_day == TUE:
            day = date(year, 12, 24)  # MON
        elif christmas_day == WED:
            day = date(year, 12, 26)  # TUE
        elif christmas_day == THU:
            day = date(year, 12, 26)  # FRI
        elif christmas_day == FRI:
            day = date(year, 12, 24)  # THU
        elif christmas_day == SAT:
            day = date(year, 12, 23)  # THU
        else:  # christmas_day == SUN:
            day = date(year, 12, 23)  # FRI
        return (day, self.label_washington_birthday_december)

    def get_primary_election_day(self, year):
        """
        Return the Primary Election Day

        FIXME: Wikipedia says it's a floating MON, but other sources say it's
        "the first Tuesday after the first Monday of May and every two years
        thereafter".
        """
        first_monday_may = self.get_nth_weekday_in_month(year, 5, MON)
        tuesday_after = self.get_nth_weekday_in_month(
            year, 5, TUE, start=first_monday_may)
        return (
            tuesday_after,
            "Primary Election Day"
        )

    def get_variable_days(self, year):
        days = super(Indiana, self).get_variable_days(year)
        days.extend([
            self.get_washington_birthday_december(year),
        ])
        if (year % 2) == 0:
            days.append(self.get_primary_election_day(year))
        return days
