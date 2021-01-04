from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-PA')
class Pennsylvania(UnitedStates):
    """Pennsylvania"""
    include_good_friday = True
    include_thanksgiving_friday = True
    include_election_day_every_year = True
