# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-ID')
class Idaho(UnitedStates):
    """Idaho"""
    martin_luther_king_label = (
        "Martin Luther King Jr. / Idaho Human Rights Day"
    )
