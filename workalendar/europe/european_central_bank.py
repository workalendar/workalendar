from .. import gettext as _

from ..core import WesternCalendar, ChristianMixin


class EuropeanCentralBank(WesternCalendar, ChristianMixin):
    "European Central Bank"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, _("Labour Day")),
        (12, 26, _("St. Stephen's Day")),
    )

    include_good_friday = True
    include_easter_monday = True
