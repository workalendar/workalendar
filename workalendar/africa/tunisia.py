from datetime import date

from ..core import IslamicCalendar, SAT, SUN
from ..registry_tools import iso_register


@iso_register('TN')
class Tunisia(IslamicCalendar):
    "Tunisia"
    # Civil holidays
    include_labour_day = True
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 2
    include_day_of_sacrifice = True
    length_eid_al_adha = 4
    include_islamic_new_year = True

    FIXED_HOLIDAYS = IslamicCalendar.FIXED_HOLIDAYS + (
            (3, 20, "Independence Day"),
            (7, 25, "Republic Day"),
            (4, 9, "Martyrs' Day"),
            (8, 13, "Women's Day"),
            (10, 15, "Evacuation Day")
        )

    # Tunisia has adopted the "western" workweek.
    WEEKEND_DAYS = (SAT, SUN)

    def get_fixed_holidays(self, year):
        """Get fixed holidays.

        Args:
            year (int): Year

        Returns:
            tuple: Tuple of date and label
        """
        days = super().get_fixed_holidays(year)

        revolution_day_label = "Revolution Day"

        if 2011 < year <= 2020:
            days.append((date(year, 1, 14), revolution_day_label))

        if year >= 2021:
            days.append((date(year, 12, 17), revolution_day_label))

        return days
