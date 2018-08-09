# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('PT')
class Portugal(WesternCalendar, ChristianMixin):
    name = 'Portugal'

    include_good_friday = True
    include_easter_sunday = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 25, "Dia da Liberdade"),
        (5, 1, "Dia do Trabalhador"),
        (6, 10, "Dia de Portugal"),
        (8, 15, "Assunção de Nossa Senhora"),
        (12, 8, "Imaculada Conceição"),
    )

    def get_fixed_holidays(self, year):
        days = super(Portugal, self).get_fixed_holidays(year)
        if year > 2015 or year < 2013:

            days.append((date(year, 10, 5), "Implantação da República"))
            days.append((date(year, 11, 1), "Todos os santos"))
            days.append((date(year, 12, 1), "Restauração da Independência"))
        return days

    def get_variable_days(self, year):
        days = super(Portugal, self).get_variable_days(year)
        if year > 2015 or year < 2013:
            days.append((self.get_corpus_christi(year), "Corpus Christi"))
        return days
