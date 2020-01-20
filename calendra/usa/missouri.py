from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-MO')
class Missouri(UnitedStates):
    """Missouri"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 8, "Truman Day"),
    )
    include_lincoln_birthday = True
