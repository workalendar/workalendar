# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-DC')
class DistrictOfColumbia(UnitedStates):
    "District of Columbia"
    include_inauguration_day = True
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (4, 16, "Emancipation Day"),
    )
