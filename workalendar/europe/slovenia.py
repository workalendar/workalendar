from datetime import date
from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('SI')
class Slovenia(WesternCalendar, ChristianMixin):
    'Slovenia'

    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    include_assumption = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 8, _("Preseren Day, the Slovenian Cultural Holiday")),
        (4, 27, _("Day of Uprising Against Occupation")),
        (5, 1, _("Labour Day")),
        (5, 2, _("Labour Day")),
        (6, 25, _("Statehood Day")),
        (10, 31, _("Reformation Day")),
        (11, 1, _("Day of Remembrance of the Dead")),
        (12, 26, _("Independence and Unity Day")),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)

        # From 1955 until May 2012, when the National Assembly of Slovenia
        # passed the Public Finance Balance Act, 2 January was a work-free day.
        # It has been re-introduced in 2017.
        # Source - Wikipedia
        # https://en.wikipedia.org/wiki/Public_holidays_in_Slovenia
        if 1955 <= year <= 2012 or year >= 2017:
            days.append((date(year, 1, 2), _("January 2nd")))

        return days
