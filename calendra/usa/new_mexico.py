# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class NewMexico(UnitedStates):
    """New Mexico"""
    include_thanksgiving_friday = True
    thanksgiving_friday_label = "Presidents' Day"
    include_federal_presidents_day = False
