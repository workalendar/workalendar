# -*- coding: utf-8 -*-
from workalendar.core import Calendar
from workalendar.core import FRI, SAT, IslamicMixin


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
