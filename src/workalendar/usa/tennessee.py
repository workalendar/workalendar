from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-TN')
class Tennessee(UnitedStates):
    """Tennessee"""
    include_columbus_day = False

    include_good_friday = True
    include_christmas_eve = True
