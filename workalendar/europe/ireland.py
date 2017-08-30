# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON
from workalendar.registry import iso_register


@iso_register('IE')
class Ireland(WesternCalendar, ChristianMixin):
    name = 'Ireland'

    include_easter_monday = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"
    shift_new_years_day = True

    def get_june_holiday(self, year):
        return (
            Ireland.get_nth_weekday_in_month(year, 6, MON),
            "June Holiday"
        )

    def get_august_holiday(self, year):
        return (
            Ireland.get_nth_weekday_in_month(year, 8, MON),
            "August Holiday"
        )

    def get_variable_days(self, year):
        self.include_whit_monday = (year <= 1973)
        days = super(Ireland, self).get_variable_days(year)

        # St Patrick's day
        st_patrick = date(year, 3, 17)
        days.append((st_patrick, "Saint Patrick's Day"))
        if st_patrick.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(st_patrick),
                "Saint Patrick substitute"))

        # May Day
        if year >= 1994:
            days.append((
                Ireland.get_nth_weekday_in_month(year, 5, MON),
                "May Day"
            ))

        days.append(self.get_june_holiday(year))
        days.append(self.get_august_holiday(year))

        if year >= 1977:
            days.append((
                Ireland.get_last_weekday_in_month(year, 10, MON),
                "October Holiday"
            ))

        # Boxing day & Xmas shift
        christmas = date(year, 12, 25)
        st_stephens_day = date(year, 12, 26)
        if christmas.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(christmas)
            days.append((shift, "Christmas Shift"))
            days.append((shift + timedelta(days=1), "St. Stephen's Day Shift"))
        elif st_stephens_day.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(st_stephens_day)
            days.append((shift, "St. Stephen's Day Shift"))
        return days
