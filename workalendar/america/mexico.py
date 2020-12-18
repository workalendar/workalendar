from datetime import date, timedelta

from ..core import WesternCalendar, SUN, MON, SAT
from ..registry_tools import iso_register


@iso_register('MX')
class Mexico(WesternCalendar):
    "Mexico"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (9, 16, "Independence Day"),
    )
    # Civil holidays
    include_labour_day = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(
            (Mexico.get_nth_weekday_in_month(year, 2, MON),
             "Constitution Day"))

        days.append(
            (Mexico.get_nth_weekday_in_month(year, 3, MON, 3),
             "Benito Juárez's birthday"))

        days.append(
            (Mexico.get_nth_weekday_in_month(year, 11, MON, 3),
             "Revolution Day"))

        return days

    def get_calendar_holidays(self, year):
        days = super().get_calendar_holidays(year)
        # If any statutory day is on Sunday, the monday is off
        # If it's on a Saturday, the Friday is off
        for day, label in days:
            if day.weekday() == SAT:
                days.append((day - timedelta(days=1), f"{label} substitute"))
            elif day.weekday() == SUN:
                days.append((day + timedelta(days=1), f"{label} substitute"))
        # Extra: if new year's day is a saturday, the friday before is off
        next_new_year = date(year + 1, 1, 1)
        if next_new_year.weekday():
            days.append((date(year, 12, 31), "New Year Day substitute"))
        return days
