# -*- coding: utf-8 -*-
from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin


class Latvia(WesternCalendar, ChristianMixin):
    "Latvia"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 23, "Midsummer Day"),
        (6, 24, "St. John's Day"),
        (11, 18, "Proclamation Day"),
        (12, 31, "New Years Eve"),
    )

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_christmas_eve = True
    include_christmas = True
    include_boxing_day = True

    def get_independence_days(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if year > 2004:
            actual_date = date(year, 5, 4)
            days = [(actual_date, "Restoration of Independence Day")]
            if actual_date.weekday() in self.get_weekend_days():
                days += [(self.find_following_working_day(actual_date),
                          "Restoration of Independence Observed")]
        return days

    def get_republic_days(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if year > 1918:
            actual_date = date(year, 11, 18)
            days = [(actual_date, "Proclamation of Republic Day")]
            if actual_date.weekday() in self.get_weekend_days():
                days += [(self.find_following_working_day(actual_date),
                          "Proclamation of Republic Observed")]
        return days

    def get_variable_days(self, year):
        days = super(Latvia, self).get_variable_days(year)
        days.extend(self.get_independence_days(year))
        days.extend(self.get_republic_days(year))
        return days
