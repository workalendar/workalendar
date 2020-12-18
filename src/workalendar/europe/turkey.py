from datetime import timedelta
from ..core import IslamicCalendar, SAT, SUN
from ..registry_tools import iso_register


@iso_register('TR')
class Turkey(IslamicCalendar):
    'Turkey'
    shift_new_years_day = True
    # Even though they're using an islamic calendar, the work week is MON->FRI
    WEEKEND_DAYS = (SAT, SUN)

    # Islamic Holidays
    include_eid_al_fitr = True
    length_eid_al_fitr = 3
    include_eid_al_adha = True
    length_eid_al_adha = 4

    # Civil holidays
    include_labour_day = True
    labour_day_label = "Labor and Solidarity Day"
    FIXED_HOLIDAYS = IslamicCalendar.FIXED_HOLIDAYS + (
        (4, 23, "National Sovereignty and Children's Day"),
        (5, 19, "Commemoration of Atatürk, Youth and Sports Day"),
        (7, 15, "Democracy and National Unity Day"),
        (8, 30, "Victory Day"),
        (10, 29, "Republic Day"),
    )

    def get_delta_islamic_holidays(self, year):
        """
        Turkey Islamic holidays are shifted by one day every year.
        """
        return timedelta(days=-1)
