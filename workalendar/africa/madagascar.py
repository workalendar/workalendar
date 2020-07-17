from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('MG')
class Madagascar(WesternCalendar):
    "Madagascar"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 29, "Martyrs' Day"),
        (6, 26, "Independence Day"),
    )
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
