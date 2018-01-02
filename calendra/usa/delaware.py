# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Delaware(UnitedStates):
    """Delaware"""
    include_good_friday = True
    include_thanksgiving_friday = True
    include_federal_presidents_day = False
    include_columbus_day = False
    include_election_day_even = True
