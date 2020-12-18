from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-IA')
class Iowa(UnitedStates):
    """Iowa"""
    include_thanksgiving_friday = True
    include_columbus_day = False
    include_federal_presidents_day = False
