# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Ohio(UnitedStates):
    """Ohio"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (12, 1, "Rosa Parks Day"),
    )
