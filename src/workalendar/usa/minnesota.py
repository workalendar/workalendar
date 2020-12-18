from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-MN')
class Minnesota(UnitedStates):
    """Minnesota"""
    include_thanksgiving_friday = True
    include_columbus_day = False
