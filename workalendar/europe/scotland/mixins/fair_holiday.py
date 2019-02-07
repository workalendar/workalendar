"""
Fair Holiday mixins
"""
from workalendar.core import MON, FRI


class FairHoliday(object):
    include_fair_holiday = True
    fair_holiday_label = "Fair Holiday"


class FairHolidayLastMondayJune(FairHoliday):

    def get_fair_holiday(self, year):
        return (
            self.get_last_weekday_in_month(year, 6, MON),
            self.fair_holiday_label
        )


class FairHolidayFirstMondayJuly(FairHoliday):

    def get_fair_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 7, MON),
            self.fair_holiday_label
        )


class FairHolidaySecondMondayJuly(FairHoliday):

    def get_fair_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 7, MON, 2),
            self.fair_holiday_label
        )


class FairHolidayThirdMondayJuly(FairHoliday):

    def get_fair_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 7, MON, 3),
            self.fair_holiday_label
        )


class FairHolidayLastMondayJuly(FairHoliday):

    def get_fair_holiday(self, year):
        return (
            self.get_last_weekday_in_month(year, 7, MON),
            self.fair_holiday_label
        )


class FairHolidayFourthFridayJuly(FairHoliday):

    def get_fair_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 7, FRI, 4),
            self.fair_holiday_label
        )


class FairHolidayFirstMondayAugust(FairHoliday):

    def get_fair_holiday(self, year):
        return (
            self.get_nth_weekday_in_month(year, 8, MON),
            self.fair_holiday_label
        )
