# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Illinois(UnitedStates):
    """Illinois"""
    include_thanksgiving_friday = True
    include_lincoln_birthday = True
    include_election_day_even = True
