from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('SK')
class Slovakia(WesternCalendar, ChristianMixin):
    'Slovakia'

    include_epiphany = True
    include_easter_monday = True
    include_good_friday = True
    include_all_saints = True
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = _("St. Stephen's Day (The Second Christmas Day)")

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 1, _("Day of the Establishment of the Slovak Republic")),
        (5, 1, _("Labour Day")),
        (5, 8, _("Liberation Day")),
        (7, 5, _("Saints Cyril and Methodius Day")),
        (8, 29, _("Slovak National Uprising anniversary")),
        (9, 1, _("Day of the Constitution of the Slovak Republic")),
        (9, 15, _("Day of Blessed Virgin Mary, patron saint of Slovakia")),
        (11, 17, _("Struggle for Freedom and Democracy Day")),
    )
