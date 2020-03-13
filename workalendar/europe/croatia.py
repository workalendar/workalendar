from .. import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('HR')
class Croatia(WesternCalendar, ChristianMixin):
    'Croatia'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, _("International Workers' Day")),
        (6, 22, _("Anti-Fascist Struggle Day")),
        (6, 25, _("Statehood Day")),
        (8, 5,
         _("Victory & Homeland Thanksgiving & Day of Croatian defenders")),
        (10, 8, _("Independence Day")),
    )

    include_epiphany = True
    include_easter_sunday = True
    include_easter_monday = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = _("St. Stephen's Day")
