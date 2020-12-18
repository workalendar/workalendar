from ..core import IslamicCalendar
from ..registry_tools import iso_register


@iso_register('QA')
class Qatar(IslamicCalendar):
    "Qatar"

    include_new_years_day = False

    FIXED_HOLIDAYS = (
        (12, 18, "National Day"),
    )
    include_start_ramadan = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 4
    include_eid_al_adha = True
    length_eid_al_adha = 4
