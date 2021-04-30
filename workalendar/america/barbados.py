from copy import copy
from datetime import date, timedelta

from ..core import MON, SUN, WesternCalendar
from ..registry_tools import iso_register


@iso_register("BB")
class Barbados(WesternCalendar):
    "Barbados"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_monday = True
    non_computable_holiday_dict = {
        2016: [(date(2016, 12, 27), "Public Holiday")],
        2021: [
            (date(2021, 1, 4), "Public Holiday"),
            (date(2021, 1, 5), "Public Holiday"),
            ],
    }

    # All holiday are shifted if on a Sunday
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 21, "Errol Barrow Day"),
        (4, 28, "National Heroes Day"),
        (11, 30, "Independance Day"),
        (12, 26, "Boxing Day"),  # Not the same as UK Boxing Day
    )

    def get_kadooment_day(self, year):
        """
        First Monday of August.
        """
        return (Barbados.get_nth_weekday_in_month(year, 8, MON),
                "Kadooment Day")

    def get_emancipation_day(self, year):
        emancipation_day = date(year, 8, 1)
        if emancipation_day.weekday() == SUN:
            emancipation_day += timedelta(days=1)
        kadooment_day = self.get_kadooment_day(year)
        if emancipation_day == kadooment_day[0]:
            emancipation_day += timedelta(days=1)
        return (emancipation_day, "Emancipation Day")

    def get_variable_days(self, year):
        """
        Return variable holidays of the Barbados calendar.
        """
        days = super().get_variable_days(year)
        days.append(self.get_kadooment_day(year))
        days.append(self.get_emancipation_day(year))
        non_computable = self.non_computable_holiday(year)
        if non_computable:
            days.extend(non_computable)
        return days

    def non_computable_holiday(self, year):
        non_computable = self.non_computable_holiday_dict.get(year, None)
        return non_computable

    def get_fixed_holidays(self, year):
        """
        Return fixed holidays of the Barbados calendar.

        A shift day is appended if a fixed holiday happens on SUN.
        """
        days = super().get_fixed_holidays(year)
        days_to_shift = copy(days)
        for day, label in days_to_shift:
            if day.weekday() == SUN:
                days.append((day + timedelta(days=1), f"{label} (shifted)"))
        return days
