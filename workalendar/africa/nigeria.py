from datetime import date

from ..core import IslamoWesternCalendar, SAT, SUN
from ..registry_tools import iso_register


@iso_register("NG")
class Nigeria(IslamoWesternCalendar):
    "Nigeria"

    # Civil holidays
    include_labour_day = True
    labour_day_label = "Workers' Day"

    # Christian holidays
    include_good_friday = True
    include_easter_monday = True
    include_boxing_day = True

    # Islamic holidays
    include_eid_al_fitr = True
    include_day_of_sacrifice = True

    shift_sunday_holidays = True
    shift_new_years_day = True

    # Explicitly assign these WE days, Nigeria has adopted the western workweek
    WEEKEND_DAYS = (SAT, SUN)

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (10, 1, "Independence Day"),
    )

    def get_fixed_holidays(self, year):
        """Get fixed holidays.

        Args:
            year (int): Year

        Returns:
            tuple: Tuple of date and label
        """
        days = super().get_fixed_holidays(year)

        democracy_day_label = "Democracy Day"

        if 2000 <= year < 2018:
            days.append((date(year, 5, 29), democracy_day_label))

        if year >= 2018:
            days.append((date(year, 6, 12), democracy_day_label))

        return days
