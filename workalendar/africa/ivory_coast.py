from ..core import IslamoWesternCalendar, SAT, SUN
from ..registry_tools import iso_register


@iso_register('CI')
class IvoryCoast(IslamoWesternCalendar):
    "Ivory Coast"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
    # Islamic holidays
    include_day_after_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Feast of the Sacrifice"

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (8, 7, "Independence Day"),
        (11, 15, "National Peace Day"),
    )

    # Ivory Coast has adopted the "western" workweek.
    WEEKEND_DAYS = (SAT, SUN)
