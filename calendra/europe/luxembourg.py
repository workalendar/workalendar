from datetime import date
from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('LU')
class Luxembourg(WesternCalendar, ChristianMixin):
    'Luxembourg'

    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_all_saints = True
    include_assumption = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 23, "Luxembourg National Holiday"),
    )

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)
        if year > 2018:
            days.append((date(year, 5, 9), "Europe Day"))

        return days
