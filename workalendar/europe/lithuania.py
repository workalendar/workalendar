from .. import gettext as _

from ..core import WesternCalendar, ChristianMixin, SUN
from ..registry_tools import iso_register


@iso_register('LT')
class Lithuania(WesternCalendar, ChristianMixin):
    'Lithuania'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 16, _("Restoration of the State Day")),
        (3, 11, _("Restoration of Independence Day")),
        (5, 1, _("Labour Day")),
        (6, 24, _("St. John's Day")),
        (7, 6, _("Anniversary of the Coronation of King Mindaugas")),
        (8, 15, _("Assumption Day")),
        (11, 1, _("All Saints' Day")),
    )

    include_easter_sunday = True
    include_easter_monday = True
    include_christmas_eve = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = _("Second day of Christmas")

    def get_mothers_day(self, year):
        return (
            Lithuania.get_nth_weekday_in_month(year, 5, SUN, 1),
            _("Mother's day")
        )

    def get_fathers_day(self, year):
        return (
            Lithuania.get_nth_weekday_in_month(year, 6, SUN, 1),
            _("Father's day")
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_mothers_day(year))
        days.append(self.get_fathers_day(year))
        return days
