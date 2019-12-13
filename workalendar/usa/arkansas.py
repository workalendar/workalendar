from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-AR')
class Arkansas(UnitedStates):
    """Arkansas"""
    include_christmas_eve = True
    presidents_day_label = ("George Washington's Birthday"
                            " and Daisy Gatson Bates Day")
    include_columbus_day = False
