# -*- coding: utf-8 -*-
from datetime import timedelta
from workalendar.core import WesternCalendar, ChristianMixin


class Portugal(WesternCalendar, ChristianMixin):
    "Portugal"
    include_good_friday = True
    include_easter_sunday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 25, "Dia da Liberdade"),
        (5, 1, "Dia do Trabalhador"),
        (6, 10, "Dia de Portugal"),
        (8, 15, "Assunção de Nossa Senhora"),
        (12, 8, "Imaculada Conceição"),
    )

    def get_variable_entrudo(self, year):
        easter_sunday = self.get_easter_sunday(year)
        return easter_sunday - timedelta(days=47)

    def get_variable_days(self, year):
        days = super(Portugal, self).get_variable_days(year)
        days.append((self.get_variable_entrudo(year), "Entrudo"))

        return days
