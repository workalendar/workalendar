from datetime import date, timedelta

from dateutil import relativedelta as rd

from ..core import WesternCalendar, ChristianMixin
from ..core import SUN, SAT
from ..core import Holiday
from ..registry_tools import iso_register


@iso_register('MX')
class Mexico(WesternCalendar, ChristianMixin):
    "Mexico"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (9, 16, "Independence Day"),
    )

    shift_new_years_day = True

    @property
    def observance_shift(self):
        return Holiday.nearest_weekday

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(Holiday(
            date(year, 2, 1) + rd.relativedelta(weekday=rd.MO(1)),
            "Constitution Day",
        ))

        days.append(Holiday(
            date(year, 3, 1) + rd.relativedelta(weekday=rd.MO(3)),
            "Benito Juárez's birthday",
        ))

        days.append(Holiday(
            date(year, 11, 1) + rd.relativedelta(weekday=rd.MO(3)),
            "Revolution Day",
        ))

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
