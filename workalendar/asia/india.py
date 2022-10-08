from ..core import (
    WesternCalendar,
    IslamicCalendar,
    HinduCalender
)
from ..registry_tools import iso_register


@iso_register('IN')
class India(HinduCalender, WesternCalendar, IslamicCalendar):
    """India"""
    include_new_years_day = True
    include_good_friday = True
    include_eid_al_fitr = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 26, "Republic Day"),
        (4, 14, "Mahavir Jayanti/Ambedkar Jayanti"),
        (8, 15, "Independence Day"),
        (10, 2, "Gandhi Jayanti"),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        return days
