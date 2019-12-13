# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from gettext import gettext as _
from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-NM')
class NewMexico(UnitedStates):
    """New Mexico"""
    include_thanksgiving_friday = True
    thanksgiving_friday_label = _("Presidents' Day")
    include_federal_presidents_day = False
