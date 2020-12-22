from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-SC')
class SouthCarolina(UnitedStates):
    """South Carolina"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 10, "Confederate Memorial Day"),
    )
    include_thanksgiving_friday = True
    include_christmas_eve = True
    include_boxing_day = True
    include_columbus_day = False
