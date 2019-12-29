# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from gettext import gettext as _
from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-MO')
class Missouri(UnitedStates):
    """Missouri"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 8, _("Truman Day")),
    )
    include_lincoln_birthday = True
