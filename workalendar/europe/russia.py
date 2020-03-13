from .. import gettext as _

from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('RU')
class Russia(WesternCalendar):
    'Russia'

    shift_new_years_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, _("Day After New Year")),
        (1, 7, _("Christmas")),
        (2, 23, _("Defendence of the Fatherland")),
        (3, 8, _("International Women's Day")),
        (5, 1, _("Labour Day")),
        (5, 9, _("Victory Day")),
        (6, 12, _("National Day")),
        (11, 4, _("Day of Unity")),
    )
