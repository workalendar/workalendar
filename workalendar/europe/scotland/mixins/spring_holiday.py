"""
Spring Holiday mixins
"""
from datetime import timedelta

from workalendar.core import MON


class SpringHoliday(object):
    include_spring_holiday = True


class SpringHolidayFirstMondayApril(SpringHoliday):
    def get_spring_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 4, MON),
            self.spring_holiday_label
        )


class SpringHolidaySecondMondayApril(SpringHoliday):
    def get_spring_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 4, MON, 2),
            self.spring_holiday_label
        )


class SpringHolidayTuesdayAfterFirstMondayMay(SpringHoliday):

    def get_spring_holiday(self, year):
        first_monday = self.get_nth_weekday_in_month(year, 5, MON)
        return (
            first_monday + timedelta(days=1),
            self.spring_holiday_label
        )


class SpringHolidayLastMondayMay(SpringHoliday):
    def get_spring_holiday(self, year):
        return (
            self.get_last_weekday_in_month(year, 5, MON),
            self.spring_holiday_label
        )


class SpringHolidayFirstMondayJune(SpringHoliday):
    def get_spring_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 6, MON),
            self.spring_holiday_label
        )
