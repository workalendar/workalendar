from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-LA')
class Louisiana(UnitedStates):
    """Louisiana"""
    include_good_friday = True
    include_election_day_even = True
    include_columbus_day = False
    include_mardi_gras = True
