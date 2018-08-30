# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..registry import iso_register
from .core import UnitedStates


@iso_register('US-NH')
class NewHampshire(UnitedStates):
    """New Hampshire"""
    include_thanksgiving_friday = True
    martin_luther_king_label = "Martin Luther King, Jr. Civil Rights Day"
