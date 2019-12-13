# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from gettext import gettext as _
from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-WY')
class Wyoming(UnitedStates):
    """Wyoming"""
    martin_luther_king_label = _("Martin Luther King, Jr. / Wyoming Equality Day")
