from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('ST')
class SaoTomeAndPrincipe(WesternCalendar, ChristianMixin):
    "São Tomé and Príncipe"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 3, _("Martyr's Day")),
        (5, 1, _("Labour Day")),
        (7, 12, _("Independence Day")),
        (9, 6, _("Armed Forces Day")),
        (9, 30, _("Agricultural Reform Day")),
        (12, 21, _("São Tomé Day")),
    )
    include_all_saints = True
