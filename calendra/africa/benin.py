from ..core import IslamoWesternCalendar, SAT, SUN
from ..registry_tools import iso_register


@iso_register('BJ')
class Benin(IslamoWesternCalendar):
    "Benin"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Tabaski"

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (1, 10, "Traditional Day"),
        (8, 1, "Independence Day"),
        (10, 26, "Armed Forces Day"),
        (11, 30, "National Day"),
    )

    # Explicitly assign these WE days, Benin has adopted the western workweek
    WEEKEND_DAYS = (SAT, SUN)
