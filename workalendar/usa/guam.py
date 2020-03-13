from gettext import gettext as _

from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-GU')
class Guam(UnitedStates):
    """Guam"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (3, 7, _('Guam History and Chamorro Heritage Day')),
        (7, 21, _('Liberation Day')),
    )
    include_all_souls = True
    include_immaculate_conception = True
    immaculate_conception_label = _("Lady of Camarin Day")
