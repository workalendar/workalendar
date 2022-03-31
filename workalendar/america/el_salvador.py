from datetime import timedelta

from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('SV')
class ElSalvador(WesternCalendar):
    "El Salvador"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_holy_thursday = True
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_all_saints = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 10, "Mothers' Day"),
        (6, 17, "Fathers' Day"),
        (8, 6, "Celebrations of San Salvador"),
        (9, 15, "Independence Day"),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        return days
