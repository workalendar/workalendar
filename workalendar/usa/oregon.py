# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-OR')
class Oregon(UnitedStates):
    """Oregon"""
    include_columbus_day = False
