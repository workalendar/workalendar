from .. import gettext as _
from datetime import timedelta

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('PA')
class Panama(WesternCalendar, ChristianMixin):
    "Panama"
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 9, _("Martyrs' Day")),
        (5, 1, _("Labour Day")),
        (11, 3, _("Independence Day")),
        (11, 5, _("Colon Day")),
        (11, 10, _("Shout in Villa de los Santos")),
        (11, 28, _("Independence from Spain")),
        (12, 8, _("Mothers' Day")),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(
            (self.get_ash_wednesday(year) - timedelta(days=1), _("Carnival"))
        )
        return days
