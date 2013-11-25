from datetime import timedelta
from workalendar.core import LunarCalendar


class SouthKoreaCalendar(LunarCalendar):
    "South Korean calendar"
    FIXED_HOLIDAYS = LunarCalendar.FIXED_HOLIDAYS + (
        (1, 2),    # Jan 2nd is holiday too
        (3, 1),    # independance day
        (5, 5),    # children's day
        (6, 6),    # Memorial day
        (8, 15),   # Liberation day
        (10, 3),   # National Foundation Day
        (10, 9),   # Hangul Day
        (12, 25),  # Christmas
    )

    def get_variable_days(self, year):
        lunar_first_day = LunarCalendar.lunar(year, 1, 1)
        days = set([
            # new year (3 days)
            lunar_first_day,
            lunar_first_day - timedelta(days=1),  # a day before
            LunarCalendar.lunar(year, 1, 2),      # a day after
            # Buddha's birthday
            LunarCalendar.lunar(year, 4, 8),
            # Midautumn Festival (3 days)
            LunarCalendar.lunar(year, 8, 14),
            LunarCalendar.lunar(year, 8, 15),
            LunarCalendar.lunar(year, 8, 16),
        ])
        return days
