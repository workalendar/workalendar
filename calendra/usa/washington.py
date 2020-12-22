from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-WA')
class Washington(UnitedStates):
    """Washington"""
    include_columbus_day = False
