from datetime import date

from dateutil import relativedelta as rd

from ..core import WesternCalendar, ChristianMixin
from ..core import Holiday
from ..registry_tools import iso_register


def _by_name(holidays):
    return {day.name: day for day in holidays if hasattr(day, 'name')}


@iso_register("NZ")
class NewZealand(WesternCalendar, ChristianMixin):
    "New Zealand"
    include_good_friday = True
    include_easter_monday = True
    include_boxing_day = True
    shift_new_years_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        Holiday(date(2000, 2, 6), "Waitangi Day"),
        Holiday(date(2000, 4, 25), "ANZAC Day"),
    )

    def get_queens_birthday(self, year):
        return Holiday(
            date(year, 6, 1) + rd.relativedelta(weekday=rd.MO(1)),
            "Queen's Birthday",
            indication="First Monday in June",
        )

    def get_labour_day(self, year):
        return Holiday(
            date(year, 10, 1) + rd.relativedelta(weekday=rd.MO(4)),
            "Labour Day",
            indication="Fourth Monday in October",
        )

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)
        days.append(Holiday(
            date(year, 1, 2),
            "Day after New Year's Day",
            observe_after=_by_name(days)["New year"],
        ))
        days.append(self.get_queens_birthday(year))
        days.append(self.get_labour_day(year))
        return days
