from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-LA')
class Louisiana(UnitedStates):
    """Louisiana"""
    include_good_friday = True
    include_election_day_even = True
    include_columbus_day = False
    include_fat_tuesday = True
