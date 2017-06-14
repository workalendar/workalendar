# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class NorthCarolina(UnitedStates):
    """North Carolina"""
    include_good_friday = True
    include_christmas_eve = True
    include_thanksgiving_friday = True
    include_boxing_day = True
    shift_exceptions = (
        (12, 26),
    )
