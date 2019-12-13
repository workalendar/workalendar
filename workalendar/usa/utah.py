# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from gettext import gettext as _
from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-UT')
class Utah(UnitedStates):
    """Utah"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (7, 24, _("Pioneer Day")),
    )
