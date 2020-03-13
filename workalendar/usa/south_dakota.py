from .. import gettext as _

from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-SD')
class SouthDakota(UnitedStates):
    """South Dakota"""
    columbus_day_label = _("Native Americans Day")

# NOTE: South Dakota has all federal holidays, except Columbus Day,
# but it's renamed as "Native Americans Day"
