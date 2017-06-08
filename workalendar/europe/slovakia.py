# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Slovakia(WesternCalendar, ChristianMixin):
    "Slovakia"
    include_epiphany = True
    include_easter_monday = True
    include_good_friday = True
    include_all_saints = True
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day (The Second Christmas Day)"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 1, "Day of the Establishment of the Slovak Republic"),
        (5, 1, "Labour Day"),
        (5, 8, "Liberation Day"),
        (7, 5, "Saints Cyril and Methodius Day"),
        (8, 29, "Slovak National Uprising anniversary"),
        (9, 1, "Day of the Constitution of the Slovak Republic"),
        (9, 15, "Day of Blessed Virgin Mary, patron saint of Slovakia"),
        (11, 17, "Struggle for Freedom and Democracy Day"),
    )
