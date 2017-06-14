# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Missouri(UnitedStates):
    """Missouri"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 8, "Truman Day"),
    )
    include_lincoln_birthday = True
