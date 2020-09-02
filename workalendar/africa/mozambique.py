from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('MZ')
class Mozambique(WesternCalendar):
    "Mozambique"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 3, "Mozambican Heroes' Day"),
        (4, 7, "Mozambican Women's Day"),
        (6, 25, "Independence Day"),
        (9, 7, "Victory Day"),
        (9, 25, "Armed Forces Day"),
        (10, 4, "Peace And Reconciliation Day"),
    )

    # Civil holidays
    include_labour_day = True

    # Christian holidays
    include_good_friday = True
    include_christmas = True
