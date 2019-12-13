from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register("US-CT")
class Connecticut(UnitedStates):
    """Connecticut"""

    include_good_friday = True
    include_lincoln_birthday = True
