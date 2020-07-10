from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('BE')
class Belgium(WesternCalendar):
    'Belgium'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 21, "National Day"),
        (11, 11, "Armistice of 1918"),
    )
    # Civil holidays
    include_labour_day = True

    # Christian holidays
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
