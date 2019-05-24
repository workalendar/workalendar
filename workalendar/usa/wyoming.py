# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-WY')
class Wyoming(UnitedStates):
    """Wyoming"""
    martin_luther_king_label = "Martin Luther King, Jr. / Wyoming Equality Day"
