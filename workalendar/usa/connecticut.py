# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-CT')
class Connecticut(UnitedStates):
    """Connecticut"""
    include_good_friday = True
    include_lincoln_birthday = True
