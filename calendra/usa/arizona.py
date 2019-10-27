# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-AZ')
class Arizona(UnitedStates):
    """Arizona"""
    martin_luther_king_label = "Dr. Martin Luther King Jr./Civil Rights Day"
    presidents_day_label = "Lincoln/Washington Presidents' Day"
