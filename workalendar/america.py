from workalendar.core import WesternCalendar
from workalendar.core import SUN, MON, THU
from datetime import date


class UnitedStatesCalendar(WesternCalendar):
    "USA calendar"
    FIXED_DAYS = WesternCalendar.FIXED_DAYS + (
        (7, 4, 'Independance Day'),
        (11, 11, 'Veterans Day'),
    )

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_variable_days(self, year):
        # usual variable days
        days = [
            (WesternCalendar.get_nth_weekday_in_month(year, 1, MON, 3),
                'Martin Luther King, Jr. Day'),

            (WesternCalendar.get_nth_weekday_in_month(year, 2, MON, 3),
                "Washington's Birthday"),

            (WesternCalendar.get_last_weekday_in_month(year, 5, MON),
                "Memorial Day"),

            (WesternCalendar.get_nth_weekday_in_month(year, 9, MON),
                "Labor Day"),

            (WesternCalendar.get_nth_weekday_in_month(year, 10, MON, 2),
                "Colombus Day"),

            (WesternCalendar.get_nth_weekday_in_month(year, 11, THU, 4),
                "Thanksgiving Day"),
        ]
        # Inauguration day
        if UnitedStatesCalendar.is_presidential_year(year - 1):
            inauguration_day = date(year, 1, 20)
            if inauguration_day.weekday() == SUN:
                inauguration_day = date(year, 1, 21)
            days.append((inauguration_day, "Inauguration Day"))
        return days
