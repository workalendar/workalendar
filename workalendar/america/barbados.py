from datetime import timedelta
from copy import copy

from ..core import WesternCalendar, ChristianMixin
from ..core import SUN, MON
from ..registry_tools import iso_register


@iso_register("BB")
class Barbados(WesternCalendar, ChristianMixin):
    "Barbados"

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_monday = True
    include_boxing_day = True

    # All holiday are shifted if on a Sunday
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 21, "Errol Barrow Day"),
        (4, 28, "National Heroes Day"),
        (5, 1, "Labour Day"),
        (8, 1, "Emancipation Day"),
        (11, 30, "Independance Day"),
    )

    def get_kadooment_day(self, year):
        """
        First Monday of August.
        """
        return (Barbados.get_nth_weekday_in_month(year, 8, MON),
                "Kadooment Day")

    def get_variable_days(self, year):
        """
        Return variable holidays of the Barbados calendar.
        """
        days = super().get_variable_days(year)
        days.append(self.get_kadooment_day(year))
        return days

    def get_fixed_holidays(self, year):
        """
        Return fixed holidays of the Barbados calendar.

        A shift day is appended if a fixed holiday happens on SUN.
        """
        days = super().get_fixed_holidays(year)
        days_to_shift = copy(days)
        for day, label in days_to_shift:
            if day.weekday() == SUN:
                days.append(
                    (day + timedelta(days=1), "%s %s" % (label, "(shifted)"))
                )
        return days
