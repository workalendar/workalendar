# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date, timedelta
from .core import WesternCalendar, ChristianMixin
from .core import SUN, MON, TUE, WED, FRI, SAT


class Brazil(WesternCalendar, ChristianMixin):
    "Brazil"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 21, "Tiradentes' Day"),
        (5, 1, "Labour Day"),
        (9, 7, "Independence Day"),
        (10, 12, "Our Lady of Aparecida"),
        (11, 2, "All Souls' Day"),
        (11, 15, "Republic Day"),
    )


class BrazilSaoPauloState(Brazil):
    "Brazil São Paulo State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 9, "Constitutional Revolution of 1932"),
    )


class BrazilSaoPauloCity(BrazilSaoPauloState):
    "Brazil São Paulo City"
    FIXED_HOLIDAYS = BrazilSaoPauloState.FIXED_HOLIDAYS + (
        (1, 25, "Anniversary of the city of São Paulo"),
        (11, 20, "Dia da Consciência Negra")
    )
    include_easter_sunday = True
    include_corpus_christi = True

    def get_carnaval(self, year):
        return self.get_easter_sunday(year) - timedelta(days=47)

    def get_variable_days(self, year):
        days = super(BrazilSaoPauloCity, self).get_variable_days(year)
        days.append((self.get_carnaval(year), "Carnaval"))
        days.append((self.get_good_friday(year), "Sexta-feira da Paixão"))
        return days


class Chile(WesternCalendar, ChristianMixin):
    "Chile"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (5, 21, "Navy Day"),
        (6, 29, "Saint Peter and Saint Paul"),
        (7, 16, "Our Lady of Mount Carmel"),
        (9, 18, "National holiday"),
        (9, 19, "Army holiday"),
        (10, 12, "Columbus Day"),
        (12, 31, "Banking Holiday"),
    )
    include_good_friday = True
    include_easter_saturday = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True

    def get_variable_days(self, year):
        days = super(Chile, self).get_variable_days(year)
        september_17 = date(year, 9, 17)
        if september_17.weekday() == MON:
            days.append((september_17, '"Bridge" holiday'))
        september_20 = date(year, 9, 20)
        if september_20.weekday() == FRI:
            days.append((september_20, '"Bridge" holiday'))

        reformation_day = date(year, 10, 31)
        if reformation_day.weekday() == WED:
            reformation_day = date(year, 11, 2)
        elif reformation_day.weekday() == TUE:
            reformation_day = date(year, 10, 27)

        days.append((reformation_day, "Reformation Day"))

        return days


class Mexico(WesternCalendar, ChristianMixin):
    "Mexico"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (9, 16, "Independence Day"),
    )

    def get_variable_days(self, year):
        days = super(Mexico, self).get_variable_days(year)
        days.append(
            (Mexico.get_nth_weekday_in_month(year, 2, MON),
             "Constitution Day"))

        days.append(
            (Mexico.get_nth_weekday_in_month(year, 3, MON, 3),
             "Benito Juárez's birthday"))

        days.append(
            (Mexico.get_nth_weekday_in_month(year, 11, MON, 3),
             "Revolution Day"))

        return days

    def get_calendar_holidays(self, year):
        days = super(Mexico, self).get_calendar_holidays(year)
        # If any statutory day is on Sunday, the monday is off
        # If it's on a Saturday, the Friday is off
        for day, label in days:
            if day.weekday() == SAT:
                days.append((day - timedelta(days=1), "%s substitute" % label))
            elif day.weekday() == SUN:
                days.append((day + timedelta(days=1), "%s substitute" % label))
        # Extra: if new year's day is a saturday, the friday before is off
        next_new_year = date(year + 1, 1, 1)
        if next_new_year.weekday():
            days.append((date(year, 12, 31), "New Year Day substitute"))
        return days


class Panama(WesternCalendar, ChristianMixin):
    "Panama"
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 9, "Martyrs' Day"),
        (5, 1, "Labour Day"),
        (11, 3, "Independence Day"),
        (11, 5, "Colon Day"),
        (11, 10, "Shout in Villa de los Santos"),
        (12, 2, "Independence from Spain"),
        (12, 8, "Mothers' Day"),
    )

    def get_variable_days(self, year):
        days = super(Panama, self).get_variable_days(year)
        days.append(
            (self.get_ash_wednesday(year) - timedelta(days=1), "Carnival")
        )
        return days
