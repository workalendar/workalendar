from gettext import gettext as _

from ..core import WesternCalendar, IslamicMixin, ChristianMixin
from ..registry_tools import iso_register


@iso_register('BJ')
class Benin(WesternCalendar, IslamicMixin, ChristianMixin):
    "Benin"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = _("Tabaski")

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 10, _("Traditional Day")),
        (5, 1, _("Labour Day")),
        (8, 1, _("Independence Day")),
        (10, 26, _("Armed Forces Day")),
        (11, 30, _("National Day")),
    )
