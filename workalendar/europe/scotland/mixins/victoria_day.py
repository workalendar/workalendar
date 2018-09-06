"""
Victoria Day mixins
"""
from workalendar.core import MON


class VictoriaDayMixin(object):
    include_victoria_day = True
    victoria_day_label = "Victoria Day"


class VictoriaDayFourthMondayMay(VictoriaDayMixin):

    def get_victoria_day(self, year):
        return (
            self.get_nth_weekday_in_month(year, 5, MON, 4),
            self.victoria_day_label
        )


class VictoriaDayLastMondayMay(VictoriaDayMixin):

    def get_victoria_day(self, year):
        return (
            self.get_last_weekday_in_month(year, 5, MON),
            self.victoria_day_label
        )


class VictoriaDayFirstMondayJune(VictoriaDayMixin):

    def get_victoria_day(self, year):
        return (
            self.get_nth_weekday_in_month(year, 6, MON),
            self.victoria_day_label
        )
