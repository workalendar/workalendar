# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from gettext import gettext as _
from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-NH')
class NewHampshire(UnitedStates):
    """New Hampshire"""
    include_thanksgiving_friday = True
    martin_luther_king_label = _("Martin Luther King, Jr. Civil Rights Day")
