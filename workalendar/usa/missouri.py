from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-MO')
class Missouri(UnitedStates):
    """Missouri"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 8, "Truman Day"),
    )
    include_lincoln_birthday = True
