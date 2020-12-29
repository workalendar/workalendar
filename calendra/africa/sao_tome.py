from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('ST')
class SaoTomeAndPrincipe(WesternCalendar):
    "São Tomé and Príncipe"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 3, "Martyr's Day"),
        (7, 12, "Independence Day"),
        (9, 6, "Armed Forces Day"),
        (9, 30, "Agricultural Reform Day"),
        (12, 21, "São Tomé Day"),
    )
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_all_saints = True
