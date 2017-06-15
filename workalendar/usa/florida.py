# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Florida(UnitedStates):
    """Florida"""
    include_thanksgiving_friday = True
    thanksgiving_friday_label = "Friday after Thanksgiving"
    include_columbus_day = False
    include_federal_presidents_day = False
