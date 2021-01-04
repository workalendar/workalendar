from datetime import timedelta
from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('CY')
class Cyprus(WesternCalendar):
    'Cyprus'

    # Civil holidays
    include_labour_day = True

    # Christian holidays
    include_epiphany = True
    include_clean_monday = True
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_monday = True
    whit_monday_label = 'Pentecost Monday'
    include_christmas_eve = True
    include_christmas_day = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 25, "Greek Independence Day"),
        (4, 1, "Cyprus National Day"),
        (7, 15, "Dormition of the Theotokos"),
        (10, 1, "Cyprus Independence Day"),
        (10, 28, "Greek National Day"),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_easter_monday(year) +
                     timedelta(days=1), "Easter Tuesday"))
        return days
