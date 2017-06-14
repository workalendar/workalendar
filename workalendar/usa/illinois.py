# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Illinois(UnitedStates):
    """Illinois"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
    )
    include_thanksgiving_friday = True
