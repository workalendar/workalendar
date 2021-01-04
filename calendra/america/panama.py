from datetime import timedelta

from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('PA')
class Panama(WesternCalendar):
    "Panama"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 9, "Martyrs' Day"),
        (11, 3, "Independence Day"),
        (11, 5, "Colon Day"),
        (11, 10, "Shout in Villa de los Santos"),
        (11, 28, "Independence from Spain"),
        (12, 8, "Mothers' Day"),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(
            (self.get_ash_wednesday(year) - timedelta(days=1), "Carnival")
        )
        return days
