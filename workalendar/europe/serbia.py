from .. import gettext as _

from ..core import WesternCalendar, OrthodoxMixin
from ..registry_tools import iso_register


@iso_register('RS')
class Serbia(OrthodoxMixin, WesternCalendar):
    'Serbia'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, _("Day After New Year")),
        (1, 7, _("Christmas")),
        (2, 15, _("Statehood Day")),
        (2, 16, _("Statehood Day")),
        (5, 1, _("Labour Day")),
        (5, 2, _("Labour Day Holiday")),
        (11, 11, _("Armistice Day")),
    )

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_christmas = False
