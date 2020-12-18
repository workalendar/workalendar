from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('AT')
class Austria(WesternCalendar):
    'Austria'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (10, 26, "National Holiday"),  # Nationalfeiertag
    )
    # Civil holidays
    include_labour_day = True
    labour_day_label = "State Holiday"  # Staatsfeiertag
    # Christian holidays
    include_epiphany = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"  # Stefanitag
