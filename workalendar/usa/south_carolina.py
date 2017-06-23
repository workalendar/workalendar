# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class SouthCarolina(UnitedStates):
    """South Carolina"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 10, "Confederate Memorial Day"),
    )
    include_thanksgiving_friday = True
    include_christmas_eve = True
    include_boxing_day = True
    include_columbus_day = False
