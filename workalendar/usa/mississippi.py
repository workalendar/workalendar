from .. import gettext as _

from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-MS')
class Mississippi(UnitedStates):
    """Mississippi"""
    include_thanksgiving_friday = True
    include_confederation_day = True
    include_columbus_day = False

    martin_luther_king_label = _("Martin Luther King's"
                                 " and Robert E. Lee's Birthdays")
    veterans_day_label = _("Armistice Day (Veterans Day)")
    national_memorial_day_label = _("National Memorial Day / "
                                    "Jefferson Davis Birthday")
