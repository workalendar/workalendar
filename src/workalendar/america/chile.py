from datetime import date

from ..core import WesternCalendar, MON, TUE, WED, FRI
from ..registry_tools import iso_register


@iso_register('CL')
class Chile(WesternCalendar):
    "Chile"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 21, "Navy Day"),
        (6, 29, "Saint Peter and Saint Paul"),
        (7, 16, "Our Lady of Mount Carmel"),
        (9, 18, "National holiday"),
        (9, 19, "Army holiday"),
        (10, 12, "Columbus Day"),
        (12, 31, "Banking Holiday"),
    )
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_good_friday = True
    include_easter_saturday = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        september_17 = date(year, 9, 17)
        if september_17.weekday() == MON:
            days.append((september_17, '"Bridge" holiday'))
        september_20 = date(year, 9, 20)
        if september_20.weekday() == FRI:
            days.append((september_20, '"Bridge" holiday'))

        reformation_day = date(year, 10, 31)
        if reformation_day.weekday() == WED:
            reformation_day = date(year, 11, 2)
        elif reformation_day.weekday() == TUE:
            reformation_day = date(year, 10, 27)

        days.append((reformation_day, "Reformation Day"))

        return days
