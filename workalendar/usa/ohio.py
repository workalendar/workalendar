# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..registry import iso_register
from .core import UnitedStates


@iso_register('US-OH')
class Ohio(UnitedStates):
    """Ohio"""

# NOTE: Ohio includes only Federal holidays.
# The wikipedia page say it also includes Election Day, but no official
# document confirms this.
