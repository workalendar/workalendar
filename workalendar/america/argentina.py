# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta, date
from workalendar.core import WesternCalendar, ChristianMixin
from ..core import MON, TUE, WED, THU, FRI, SAT, SUN
from ..registry_tools import iso_register

@iso_register('AR')
class Argentina(WesternCalendar, ChristianMixin):
    'Argentina'

    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 24, "Día de la Memoria"),                                       # -- ok
        (4, 2 , "Día de las Malvinas"),                                     # -- ok
        (5, 1 , "Día del Trabajador"),                                      # -- ok
        (5, 25, "Día de la Revolución de Mayo"),                            # -- ok
        (6, 20, "Día Paso a la Inmortalidad del General Manuel Belgrano"),  # -- ok
        (7, 9 , "Día de la Independencia"),                                 # -- ok
        (12, 8, "Día de la Inmaculada Concepción de María"),                # -- ok
    )

    def get_variable_days(self, year):

        days = super(Argentina, self).get_variable_days(year)
        days.append(
            (self.get_easter_sunday(year) - timedelta(days=48),
             "Carnival Lunes"))

        days.append(
            (self.get_easter_sunday(year) - timedelta(days=47),
            "Carnival"))

        days.append(
            (self.get_general_guemes_day(year)))

        days.append(
            (self.get_general_martin_day(year)))

        days.append(
            (self.get_soberania_day(year)))

        days.append(
            (self.get_diversidad_day(year)))

        return days

    def get_general_guemes_day(self, year):
        general_guemes_day = date(year, 6, 17)

        if general_guemes_day.weekday() == THU:
            general_guemes_day = Argentina.get_first_weekday_after(date(year, 6, 17), MON)
        elif general_guemes_day.weekday() == WED:
            general_guemes_day = general_guemes_day - timedelta(days=2) # monday of the same week
        else:
            general_guemes_day

        return (general_guemes_day,
            "Día Paso a la Inmortalidad del General Martín Miguel de Güemes")

    def get_general_martin_day(self, year):
        general_martin_day = Argentina.get_nth_weekday_in_month(year, 8, MON, 3)

        return (general_martin_day,
            "Día Paso a la Inmortalidad del Gral. José de San Martín")

    def get_soberania_day(self, year):
        first_friday_november = Argentina.get_nth_weekday_in_month(year, 11, FRI, 1)

        soberania_day = Argentina.get_nth_weekday_in_month(year, 11, MON, n = 3, start=first_friday_november)

        return (soberania_day,
            "Día de la Soberanía Nacional")

    def get_diversidad_day(self, year):
        diversidad_day = date(year, 10, 12)

        if diversidad_day.weekday() == WED or diversidad_day.weekday() == THU or diversidad_day.weekday() == FRI or diversidad_day.weekday() == SAT:
            diversidad_day = Argentina.get_first_weekday_after(date(year, 10, 12), MON)
        elif diversidad_day.weekday() == TUE:
            diversidad_day = diversidad_day - timedelta(days=1)
        else:
            diversidad_day

        return (diversidad_day,
            "Día del Respeto a la Diversidad Cultural")
