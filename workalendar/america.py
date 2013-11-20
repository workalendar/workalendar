from workalendar.core import WesternCalendar
from workalendar.core import SUN, MON, THU
from datetime import date


class UnitedStatesCalendar(WesternCalendar):
    "USA calendar"

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_calendar_holidays(self, year):
        days = super(UnitedStatesCalendar, self).get_calendar_holidays(year)
        days.add(date(year, 7, 4))
        days.add(date(year, 11, 11))
        # variable days
        days.add(WesternCalendar.get_nth_weekday_in_month(year, 1, MON, 3))
        days.add(WesternCalendar.get_nth_weekday_in_month(year, 2, MON, 3))
        days.add(WesternCalendar.get_last_weekday_in_month(year, 5, MON))
        days.add(WesternCalendar.get_nth_weekday_in_month(year, 9, MON))
        days.add(WesternCalendar.get_nth_weekday_in_month(year, 10, MON, 2))
        days.add(WesternCalendar.get_nth_weekday_in_month(year, 11, THU, 4))
        # Inauguration day
        if UnitedStatesCalendar.is_presidential_year(year - 1):
            inauguration_day = date(year, 1, 20)
            if inauguration_day.weekday() == SUN:
                inauguration_day = date(year, 1, 21)
            days.add(inauguration_day)
        return days
