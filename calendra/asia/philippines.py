from ..core import (
    WesternMixin, IslamicMixin, ChineseNewYearCalendar,
    SAT, SUN
)
from ..registry_tools import iso_register


@iso_register('PH')
class Philippines(WesternMixin, IslamicMixin, ChineseNewYearCalendar):
    "Philippines"
    # Civil holidays
    include_labour_day = True
    include_new_years_eve = True

    # Christian holiday
    include_holy_thursday = True
    holy_thursday_label = "Maundy Thursday"
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    easter_saturday_label = "Black Saturday"
    include_all_saints = True
    include_all_souls = True
    include_immaculate_conception = True
    include_christmas_eve = True

    # Islamic holidays
    include_eid_al_fitr = True
    eid_al_fitr_label = "Eid'l Fitr"
    include_eid_al_adha = True
    day_of_sacrifice_label = "Eid'l Adha"

    WEEKEND_DAYS = (SAT, SUN)

    FIXED_HOLIDAYS = ChineseNewYearCalendar.FIXED_HOLIDAYS + (
        (2, 25, "EDSA Revolution Anniversary"),
        (4, 9, "Araw ng Kagitingan"),
        (6, 12, "Independence Day"),
        (8, 21, "Ninoy Aquino Day"),
        (8, 30, "National Heroes' Day"),
        (11, 30, "Bonifacio Day"),
        (12, 30, "Rizal Day"),
    )
