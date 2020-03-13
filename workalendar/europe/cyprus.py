from .. import gettext as _
from datetime import timedelta

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('CY')
class Cyprus(WesternCalendar, ChristianMixin):
    'Cyprus'

    include_epiphany = True
    include_clean_monday = True
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_monday = True
    whit_monday_label = _('Pentecost Monday')
    include_christmas_eve = True
    include_christmas_day = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 25, _("Greek Independence Day")),
        (4, 1, _("Cyprus National Day")),
        (5, 1, _("Labour Day")),
        (7, 15, _("Dormition of the Theotokos")),
        (10, 1, _("Cyprus Independence Day")),
        (10, 28, _("Greek National Day")),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_easter_monday(year) +
                     timedelta(days=1), _("Easter Tuesday")))
        return days
