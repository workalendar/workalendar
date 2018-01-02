# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class California(UnitedStates):
    """California"""
    include_thanksgiving_friday = True
    include_cesar_chavez_day = True
    include_columbus_day = False
