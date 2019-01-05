# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..registry import iso_register
from .core import UnitedStates


@iso_register('US-NJ')
class NewJersey(UnitedStates):
    """New Jersey"""
    include_good_friday = True
    include_election_day_every_year = True
