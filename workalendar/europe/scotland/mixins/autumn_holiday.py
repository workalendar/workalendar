"""
Autumn Holiday mixins
"""
from workalendar.core import MON


class AutumHoliday(object):
    include_autumn_holiday = True
    autumn_holiday_label = "Autumn Holiday"


class AutumnHolidayLastMondaySeptember(AutumHoliday):
    def get_autumn_holiday(self, year):
        return (
            self.get_last_weekday_in_month(year, 9, MON),
            self.autumn_holiday_label
        )


class AutumnHolidayFirstMondayOctober(AutumHoliday):
    def get_autumn_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 10, MON),
            self.autumn_holiday_label
        )


class AutumnHolidaySecondMondayOctober(AutumHoliday):
    def get_autumn_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 10, MON, 2),
            self.autumn_holiday_label
        )


class AutumnHolidayThirdMondayOctober(AutumHoliday):
    def get_autumn_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 10, MON, 3),
            self.autumn_holiday_label
        )
