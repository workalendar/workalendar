# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-CO')
class Colorado(UnitedStates):
    """Colorado"""
    # Colorado has only federal state holidays.
    # NOTE: Cesar Chavez Day is an optional holiday
