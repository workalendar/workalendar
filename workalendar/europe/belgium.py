from .. import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('BE')
class Belgium(WesternCalendar, ChristianMixin):
    'Belgium'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, _("Labour Day")),
        (7, 21, _("National Day")),
        (11, 11, _("Armistice of 1918")),
    )

    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
