from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-NM')
class NewMexico(UnitedStates):
    """New Mexico"""
    include_thanksgiving_friday = True
    thanksgiving_friday_label = "Presidents' Day"
    include_federal_presidents_day = False
