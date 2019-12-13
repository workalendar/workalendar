from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register("US-ID")
class Idaho(UnitedStates):
    """Idaho"""

    martin_luther_king_label = "Martin Luther King Jr. / Idaho Human Rights Day"
