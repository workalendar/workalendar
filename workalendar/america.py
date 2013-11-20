from workalendar.core import WesternCalendar
from workalendar.core import SUN, MON, THU
from datetime import date, timedelta


class UnitedStatesCalendar(WesternCalendar):
    "USA calendar"
    FIXED_DAYS = WesternCalendar.FIXED_DAYS + (
        (7, 4),
        (11, 11),
    )

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_variable_days(self, year):
        # usual variable days
        days = set([
            WesternCalendar.get_nth_weekday_in_month(year, 1, MON, 3),
            WesternCalendar.get_nth_weekday_in_month(year, 2, MON, 3),
            WesternCalendar.get_last_weekday_in_month(year, 5, MON),
            WesternCalendar.get_nth_weekday_in_month(year, 9, MON),
            WesternCalendar.get_nth_weekday_in_month(year, 10, MON, 2),
            WesternCalendar.get_nth_weekday_in_month(year, 11, THU, 4),
        ])
        # Inauguration day
        if UnitedStatesCalendar.is_presidential_year(year - 1):
            inauguration_day = date(year, 1, 20)
            if inauguration_day.weekday() == SUN:
                inauguration_day = date(year, 1, 21)
            days.add(inauguration_day)
        return days


class GoodFridayCalendar(UnitedStatesCalendar):
    "Good friday is a holiday in several areas"
    def get_variable_days(self, year):
        return super(GoodFridayCalendar, self).get_variable_days(year).union(
            set([self.get_easter_sunday(year) - timedelta(days=2)])
        )

# Good friday states
ConnecticutCalendar = GoodFridayCalendar
DelawareCalendar = GoodFridayCalendar
FloridaCalendar = GoodFridayCalendar
HawaiiCalendar = GoodFridayCalendar
IndianaCalendar = GoodFridayCalendar
KentuckyCalendar = GoodFridayCalendar
LouisianaCalendar = GoodFridayCalendar
NewJerseyCalendar = GoodFridayCalendar
NorthCarolinaCalendar = GoodFridayCalendar
NorthDakotaCalendar = GoodFridayCalendar
TennesseeCalendar = GoodFridayCalendar
TexasCalendar = GoodFridayCalendar
# Good friday areas
GuamCalendar = GoodFridayCalendar
VirginIslandCalendar = GoodFridayCalendar
PuertoRicoCalendar = GoodFridayCalendar
