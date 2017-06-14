# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Utah(UnitedStates):
    """Utah"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (7, 24, "Pioneer Day"),
    )
