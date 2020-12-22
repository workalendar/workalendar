from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-NY')
class NewYork(UnitedStates):
    """New York"""
    include_lincoln_birthday = True
    include_election_day_every_year = True
