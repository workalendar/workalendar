from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-WI')
class Wisconsin(UnitedStates):
    """Wisconsin"""
    include_columbus_day = False
    include_federal_presidents_day = False
    include_christmas_eve = True
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (12, 31, "New Years Eve"),
    )
