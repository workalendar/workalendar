# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-IL')
class Illinois(UnitedStates):
    """Illinois"""
    include_thanksgiving_friday = True
    include_lincoln_birthday = True
    include_election_day_even = True
