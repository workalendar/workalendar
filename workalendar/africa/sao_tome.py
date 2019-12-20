from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('ST')
class SaoTomeAndPrincipe(WesternCalendar, ChristianMixin):
    "São Tomé and Príncipe"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 3, "Martyr's Day"),
        (5, 1, "Labour Day"),
        (7, 12, "Independence Day"),
        (9, 6, "Armed Forces Day"),
        (9, 30, "Agricultural Reform Day"),
        (12, 21, "São Tomé Day"),
    )
    include_all_saints = True
