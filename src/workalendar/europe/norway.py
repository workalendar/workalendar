from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('NO')
class Norway(WesternCalendar):
    'Norway'

    # Christian holidays
    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_whit_sunday = True
    include_boxing_day = True
    boxing_day_label = "St Stephen's Day"

    # Civil holidays
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 17, "Constitution Day"),
    )
