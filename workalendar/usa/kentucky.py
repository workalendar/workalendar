# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Kentucky(UnitedStates):
    """Kentucky"""
    include_good_friday = True
    include_thanksgiving_friday = True
    include_christmas_eve = True
    include_columbus_day = False
    include_federal_presidents_day = False
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (12, 31, "New Year's Eve"),
    )
