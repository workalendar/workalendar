from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-MA')
class Massachusetts(UnitedStates):
    """Massachusetts"""
    include_patriots_day = True


class SuffolkCountyMassachusetts(Massachusetts):
    """Suffolk County, Massachusetts"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (3, 17, 'Evacuation Day'),
        (6, 17, 'Bunker Hill Day'),
    )
