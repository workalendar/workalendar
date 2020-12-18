from datetime import date

from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('HR')
class Croatia(WesternCalendar):
    'Croatia'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (6, 22, "Anti-Fascist Struggle Day"),
        (8, 5, "Victory & Homeland Thanksgiving & Day of Croatian defenders"),
    )

    # Civil holidays
    include_labour_day = True
    labour_day_label = "International Workers' Day"

    # Christian holidays
    include_epiphany = True
    include_easter_sunday = True
    include_easter_monday = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)

        if year >= 2020:
            days.extend([
                # Statehood date has changed in 2020
                (date(year, 5, 30), "Statehood Day"),
                # Remembrance Day has been added in 2020
                (date(year, 11, 18), "Remembrance Day"),
            ])
        else:
            days.extend([
                (date(year, 6, 25), "Statehood Day"),
                # Independance day was a holiday until 2020
                (date(year, 10, 8), "Independence Day"),
            ])

        return days
