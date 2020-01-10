from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-ME')
class Maine(UnitedStates):
    """Maine"""
    include_thanksgiving_friday = True
    include_patriots_day = True
