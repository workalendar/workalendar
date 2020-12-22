from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-NJ')
class NewJersey(UnitedStates):
    """New Jersey"""
    include_good_friday = True
    include_election_day_every_year = True
