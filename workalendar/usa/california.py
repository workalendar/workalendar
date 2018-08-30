# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..core import MON
from ..registry import iso_register


@iso_register('US-CA')
class California(UnitedStates):
    """California"""
    include_thanksgiving_friday = True
    include_cesar_chavez_day = True
    include_columbus_day = False


class CaliforniaEducation(California):
    """California Education

    This administration holds its own calendar. In order to respect the goal
    of workalendar (to compute (non)working days), we've decided to only retain
    days when the schools are closed.
    """

    def get_variable_days(self, year):
        # usual variable days
        days = super(CaliforniaEducation, self).get_variable_days(year)

        if year != 2009:
            days.append(self.get_lincoln_birthday(year))

        days.append((
            self.get_nth_weekday_in_month(year, 9, MON, 4),
            'Native American Day'
        ))

        return days


class CaliforniaBerkeley(California):
    """
    Berkeley, California
    """
    FIXED_HOLIDAYS = California.FIXED_HOLIDAYS + (
        (5, 19, 'Malcolm X Day'),
    )
    include_cesar_chavez_day = False
    include_lincoln_birthday = True
    include_columbus_day = True
    columbus_day_label = "Indigenous People's Day"


class CaliforniaSanFrancisco(California):
    """
    San Francisco, California
    """
    include_cesar_chavez_day = False
    include_columbus_day = True


class CaliforniaWestHollywood(California):
    """
    West Hollywood, California
    """
    FIXED_HOLIDAYS = California.FIXED_HOLIDAYS + (
        (5, 22, 'Harvey Milk Day'),
    )
    include_cesar_chavez_day = False
    include_thanksgiving_friday = False
