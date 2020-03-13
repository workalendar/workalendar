from .. import gettext as _

from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-ID')
class Idaho(UnitedStates):
    """Idaho"""
    martin_luther_king_label = (
        _("Martin Luther King Jr. / Idaho Human Rights Day")
    )
