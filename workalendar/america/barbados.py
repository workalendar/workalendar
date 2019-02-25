from __future__ import absolute_import, division, print_function
from datetime import date
from dateutil import easter

from ..core import WesternCalendar, ChristianMixin
from ..core import Calendar, SUN, MON
from ..registry import iso_register


@iso_register("BB")
class Barbados(ChristianMixin, WesternCalendar):
    "Barbados"

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_monday = True
    include_boxing_day = True
    shift_sunday_holidays = True
    EASTER_METHOD = easter.EASTER_WESTERN

    # All holiday are shifted if on a Sunday
    almost_fixed_holidays = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 21, "Errol Barrow Day"),
        (4, 28, "National Heroes Day"),
        (5, 1, "Labour Day"),
        (8, 1, "Emancipation Day"),
        (11, 30, "Independance Day"),
    )

    def get_kadooment_day(self, year):
        """First Monday of August.
        """
        return (Barbados.get_nth_weekday_in_month(year, 8, MON),
                "Kadooment Day")

    def get_almost_fixed_holidays(self, year):
        """
        Return the fixed days according to the almost_fixed_holidays
        class property. All holidays are shifted to Monday if on a Sunday
        """
        days = []
        for month, day, label in self.almost_fixed_holidays:
            days.append((date(year, month, day), label))
        return days

    def get_variable_days(self, year):
        ch_days = super(Barbados, self).get_variable_days(year)
        almost_fixed = self.get_almost_fixed_holidays(year)
        all_days = ch_days + almost_fixed
        all_days.append(self.get_kadooment_day(year))
        days = []
        for day in all_days:
            if day[0].weekday() == SUN:
                days.append(
                    (Calendar.get_first_weekday_after(day[0], MON), day[1])
                )
            else:
                days.append(day)
        return days
