from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('PL')
class Poland(WesternCalendar, ChristianMixin):
    'Poland'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 6, _('Trzech Kroli')),
        (5, 1, _('Labour Day')),
        (5, 3, _('Constitution Day')),
        (11, 11, _('Independence Day')),
    )
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = _("Pentecost Sunday")
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_boxing_day = True
