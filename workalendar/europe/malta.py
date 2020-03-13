from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('MT')
class Malta(WesternCalendar, ChristianMixin):
    'Malta'

    include_good_friday = True
    include_assumption = True
    include_immaculate_conception = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        # National Holidays
        (3, 31, _("Freedom Day")),            # (Jum il-Ħelsien)
        (6, 7, _("Sette Giugno")),
        (9, 8, _("Victory Day")),             # (Jum il-Vitorja)
        (9, 21, _("Independence Day")),       # (Jum l-Indipendenza)
        (12, 13, _("Republic Day")),          # (Jum ir-Repubblika)
        # Public Holidays
        (1, 1, _("New Year's Day")),          # (L-Ewwel tas-Sena)
        (2, 10, _("Feast of Saint Paul's Shipwreck")),
        (3, 19, _("Feast of Saint Joseph")),  # (San Ġużepp)
        (5, 1, _("Worker's Day")),            # (Jum il-Ħaddiem)
        (6, 29, _("Feast of Saint Peter & Saint Paul")),  # (L-Imnarja)
    )
