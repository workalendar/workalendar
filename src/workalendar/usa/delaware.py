from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-DE')
class Delaware(UnitedStates):
    """Delaware"""
    include_good_friday = True
    include_thanksgiving_friday = True
    include_federal_presidents_day = False
    include_columbus_day = False
    include_election_day_even = True
