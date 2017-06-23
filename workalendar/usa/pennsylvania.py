# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class Pennsylvania(UnitedStates):
    """Pennsylvania"""
    include_good_friday = True
    include_thanksgiving_friday = True
    include_election_day_every_year = True
