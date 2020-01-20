from .core import UnitedStates
from ..registry import iso_register


@iso_register('US-CT')
class Connecticut(UnitedStates):
    """Connecticut"""
    include_good_friday = True
    include_lincoln_birthday = True
