# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates


class NewYork(UnitedStates):
    """New York"""
    include_lincoln_birthday = True
    include_election_day_every_year = True
