# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-TN')
class Tennessee(UnitedStates):
    """Tennessee"""
    include_columbus_day = False

    include_good_friday = True
    include_christmas_eve = True
