from datetime import date, timedelta
from ..core import WesternCalendar, ChristianMixin, SUN
from ..registry_tools import iso_register


@iso_register('NL')
class Netherlands(WesternCalendar, ChristianMixin):
    'Netherlands'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 5, "Liberation Day"),
    )

    def get_king_queen_day(self, year):
        """27 April unless this is a Sunday in which case it is the 26th

        Before 2013 it was called Queensday, falling on
        30 April, unless this is a Sunday in which case it is the 29th.
        """
        if year > 2013:
            king_day = date(year, 4, 27)
            if king_day.weekday() != SUN:
                return (king_day, "King's day")
            return (king_day - timedelta(days=1), "King's day")
        else:
            queen_day = date(year, 4, 30)
            if queen_day.weekday() != SUN:
                return (queen_day, "Queen's day")
            return (queen_day - timedelta(days=1), "Queen's day")

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_king_queen_day(year))
        return days
