from .. import gettext as _

from ..core import WesternCalendar, OrthodoxMixin
from ..registry_tools import iso_register


@iso_register('GR')
class Greece(OrthodoxMixin, WesternCalendar):
    'Greece'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 25, _("Independence Day")),
        (5, 1, _("Labour Day")),
        (10, 28, _("Ohi Day")),
    )
    include_epiphany = True
    include_clean_monday = True
    include_annunciation = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = _("Pentecost")
    include_whit_monday = True
    include_assumption = True
    include_boxing_day = True
    boxing_day_label = _("Glorifying Mother of God")
