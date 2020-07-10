from ..core import IslamicCalendar
from ..registry_tools import iso_register


@iso_register('DZ')
class Algeria(IslamicCalendar):
    "Algeria"
    # Civil holidays
    include_labour_day = True
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_islamic_new_year = True

    FIXED_HOLIDAYS = IslamicCalendar.FIXED_HOLIDAYS + (
            (7, 5, "Independence Day"),
            (11, 1, "Anniversary of the revolution"),
        )

    ISLAMIC_HOLIDAYS = IslamicCalendar.ISLAMIC_HOLIDAYS + (
        (1, 10, "Ashura"),
    )
