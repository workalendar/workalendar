# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import timedelta, date

from workalendar.core import WesternCalendar, ChristianMixin


class Colombia(WesternCalendar, ChristianMixin):
    "Colombia"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (7, 20, "Independence Day"),
        (8, 7, "Boyacá Battle"),
    )
    include_palm_sunday = True
    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_corpus_christi = True
    include_immaculate_conception = True

    def get_epiphany(self, year):
        base_day = date(year, 1, 6)
        return Colombia.get_first_weekday_after(base_day, 0)

    def get_saint_joseph(self, year):
        base_day = date(year, 3, 19)
        return Colombia.get_first_weekday_after(base_day, 0)

    def get_ascension(self, year):
        return self.get_easter_sunday(year) + timedelta(days=43)

    def get_corpus_christi(self, year):
        return self.get_easter_sunday(year) + timedelta(days=64)

    def get_sacred_heart(self, year):
        return self.get_easter_sunday(year) + timedelta(days=71)

    def get_saint_peter_and_saint_paul(self, year):
        base_day = date(year, 6, 29)
        return Colombia.get_first_weekday_after(base_day, 0)

    def get_assumption(self, year):
        base_day = date(year, 8, 15)
        return Colombia.get_first_weekday_after(base_day, 0)

    def get_race_day(self, year):
        base_day = date(year, 10, 12)
        return Colombia.get_first_weekday_after(base_day, 0)

    def get_all_saints(self, year):
        base_day = date(year, 11, 1)
        return Colombia.get_first_weekday_after(base_day, 0)

    def get_cartagena_independence(self, year):
        base_day = date(year, 11, 11)
        return Colombia.get_first_weekday_after(base_day, 0)

    def get_variable_days(self, year):
        days = super(Colombia, self).get_variable_days(year)
        days.extend([
            (self.get_epiphany(year), "Epiphany"),
            (self.get_saint_joseph(year), "Saint Joseph"),
            (self.get_ascension(year), "Ascension"),
            (self.get_sacred_heart(year), "Sacred Heart"),
            (self.get_saint_peter_and_saint_paul(year),
                "Saint Peter and Saint Paul"),
            (self.get_assumption(year), "Assumption of Mary to Heaven"),
            (self.get_race_day(year), "Race Day"),
            (self.get_all_saints(year), "All Saints"),
            (self.get_cartagena_independence(year),
                "Cartagena's Independence"),
        ])

        return days
