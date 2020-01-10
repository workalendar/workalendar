from datetime import date
from ..core import WesternCalendar, ChristianMixin, THU, MON
from ..registry_tools import iso_register


@iso_register('IS')
class Iceland(WesternCalendar, ChristianMixin):
    'Iceland'

    include_holy_thursday = True
    include_good_friday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = "St Stephen's Day"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 17, "Icelandic National Day"),
        (12, 31, "New Year's Eve"),
    )

    def get_first_day_of_summer(self, year):
        """It's the first thursday *after* April, 18th.
        If April the 18th is a thursday, then it jumps to the 24th.
        """
        return Iceland.get_nth_weekday_in_month(
            year, 4, THU,
            start=date(year, 4, 19))

    def get_commerce_day(self, year):
        return Iceland.get_nth_weekday_in_month(year, 8, MON)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_first_day_of_summer(year), "First day of summer"),
            (self.get_commerce_day(year), "Commerce Day"),
        ])
        return days
