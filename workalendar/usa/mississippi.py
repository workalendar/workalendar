# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Mississippi(UnitedStates):
    """Mississippi"""
    include_thanksgiving_friday = True
    include_confederation_day = True
    include_columbus_day = False

    martin_luther_king_label = ("Martin Luther King's"
                                " and Robert E. Lee's Birthdays")
    veterans_day_label = "Armistice Day (Veterans Day)"
    national_memorial_day_label = ("National Memorial Day / "
                                   "Jefferson Davis Birthday")
