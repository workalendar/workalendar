from ..core import WesternCalendar, ChristianMixin, SUN
from ..registry_tools import iso_register


@iso_register('LT')
class Lithuania(WesternCalendar, ChristianMixin):
    'Lithuania'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 16, "Restoration of the State Day"),
        (3, 11, "Restoration of Independence Day"),
        (5, 1, "Labour Day"),
        (6, 24, "St. John's Day"),
        (7, 6, "Anniversary of the Coronation of King Mindaugas"),
    )

    include_easter_sunday = True
    include_easter_monday = True
    include_assumption = True
    include_all_saints = True
    include_christmas_eve = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = "Second day of Christmas"

    def get_mothers_day(self, year):
        return (
            Lithuania.get_nth_weekday_in_month(year, 5, SUN, 1),
            "Mother's day"
        )

    def get_fathers_day(self, year):
        return (
            Lithuania.get_nth_weekday_in_month(year, 6, SUN, 1),
            "Father's day"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_mothers_day(year))
        days.append(self.get_fathers_day(year))
        return days
