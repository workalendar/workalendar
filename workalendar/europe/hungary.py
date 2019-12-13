from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('HU')
class Hungary(WesternCalendar, ChristianMixin):
    'Hungary'

    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost Sunday"
    include_whit_monday = True
    whit_monday_label = "Pentecost Monday"
    include_boxing_day = True
    boxing_day_label = "Second Day of Christmas"
    include_all_saints = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 15, "National Day"),
        (5, 1, "Labour Day"),
        (8, 20, "St Stephen's Day"),
        (10, 23, "National Day"),
    )

    def get_variable_days(self, year):
        # As of 2017, Good Friday became a holiday
        self.include_good_friday = (year >= 2017)
        days = super().get_variable_days(year)
        return days
