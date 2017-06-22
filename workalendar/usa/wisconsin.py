# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Wisconsin(UnitedStates):
    """Wisconsin"""
    include_columbus_day = False
    include_federal_presidents_day = False
    include_christmas_eve = True
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (12, 31, "New Years Eve"),
    )
