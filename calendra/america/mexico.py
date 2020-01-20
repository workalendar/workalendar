from datetime import date

from dateutil import relativedelta as rd

from ..core import WesternCalendar, ChristianMixin
from ..core import Holiday
from ..registry import iso_register


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
