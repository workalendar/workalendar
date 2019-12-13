from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register("US-ME")
class Maine(UnitedStates):
    """Maine"""

    include_thanksgiving_friday = True
    include_patriots_day = True
