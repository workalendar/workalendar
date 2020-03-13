from gettext import gettext as _

from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-MA')
class Massachusetts(UnitedStates):
    """Massachusetts"""
    include_patriots_day = True


class SuffolkCountyMassachusetts(Massachusetts):
    """Suffolk County, Massachusetts"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (3, 17, _('Evacuation Day')),
        (6, 17, _('Bunker Hill Day')),
    )
