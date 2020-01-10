from ..core import Calendar
from ..core import FRI, SAT, IslamicMixin
from ..registry_tools import iso_register


@iso_register('QA')
class Qatar(IslamicMixin, Calendar):
    "Qatar"
    WEEKEND_DAYS = (FRI, SAT)

    FIXED_HOLIDAYS = (
        (12, 18, "National Day"),
    )
    include_start_ramadan = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 4
    include_eid_al_adha = True
    length_eid_al_adha = 4
