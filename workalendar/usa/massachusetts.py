# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-MA')
class Massachusetts(UnitedStates):
    """Massachusetts"""
    include_patriots_day = True


class SuffolkCountyMassachusetts(Massachusetts):
    """Suffolk County, Massachusetts"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (3, 17, 'Evacuation Day'),
        (6, 17, 'Bunker Hill Day'),
    )
