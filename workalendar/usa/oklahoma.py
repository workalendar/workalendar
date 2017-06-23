# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Oklahoma(UnitedStates):
    """Oklahoma"""
    include_thanksgiving_friday = True
    include_boxing_day = True
    include_columbus_day = False
