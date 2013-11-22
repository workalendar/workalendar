from datetime import timedelta
from workalendar.core import LunarCalendar


class SouthKoreaCalendar(LunarCalendar):
    "South Korean calendar"
    FIXED_DAYS = LunarCalendar.FIXED_DAYS + (
        (3, 1, "Independance Day"),
        (5, 5, "Children's Day"),
        (6, 6, "Memorial Day"),
        (8, 15, "Liberation Day"),
        (10, 3, "National Foundation Day"),
        (10, 9, "Hangul Day"),
        (12, 25, "Christmas Day"),
    )

    def get_variable_days(self, year):
        lunar_first_day = LunarCalendar.lunar(year, 1, 1)
        days = [
            # new year (3 days)
            (lunar_first_day, "Korean New Year's Day"),
            # a day before
            (lunar_first_day - timedelta(days=1), "Korean New Year's Day"),
            # a day after
            (LunarCalendar.lunar(year, 1, 2), "Korean New Year's Day"),
            (LunarCalendar.lunar(year, 4, 8), "Buddha's Birthday"),
            # Midautumn Festival (3 days)
            (LunarCalendar.lunar(year, 8, 14), "Midautumn Festival"),
            (LunarCalendar.lunar(year, 8, 15), "Midautumn Festival"),
            (LunarCalendar.lunar(year, 8, 16), "Midautumn Festival"),
        ]
        return days
