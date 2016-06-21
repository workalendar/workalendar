# -*- coding: utf-8 -*-
from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import FRI, SAT


class Finland(WesternCalendar, ChristianMixin):
    "Finland"
    include_epiphany = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    whit_sunday_label = 'Pentecost'
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (12, 6, "Independence Day"),
    )

    def get_midsummer_eve(self, year):
        date_eve = Finland.get_nth_weekday_in_month(
            year, 6, FRI, start=date(year, 6, 19))
        return date_eve

    def get_midsummer_day(self, year):
        date_eve = Finland.get_nth_weekday_in_month(
            year, 6, SAT, start=date(year, 6, 20))
        return date_eve

    def get_variable_all_saints(self, year):
        all_saints = date(year, 10, 31)
        if all_saints.weekday() != SAT:
            all_saints = Finland.get_nth_weekday_in_month(
                year, 11, SAT)
        return all_saints

    def get_variable_days(self, year):
        days = super(Finland, self).get_variable_days(year)
        days.append((self.get_midsummer_eve(year), "Midsummer's Eve"))
        days.append((self.get_midsummer_day(year), "Midsummer's Day"))
        days.append((self.get_variable_all_saints(year), "All Saints"))
        return days
