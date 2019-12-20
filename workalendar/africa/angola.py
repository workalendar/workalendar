from datetime import timedelta
from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('AO')
class Angola(WesternCalendar, ChristianMixin):
    """Angola"""

    include_good_friday = True
    include_easter_sunday = True
    include_christmas = True
    include_all_souls = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 4, "Dia do Inicio da Luta Armada"),
        (3, 8, "Dia Internacional da Mulher"),
        (4, 4, "Dia da Paz"),
        (5, 1, "Dia Internacional do Trabalhador"),
        (9, 17, "Dia do Fundador da Nação e do Herói Nacional"),
        (11, 11, "Dia da Independência Nacional"),
    )

    def get_variable_entrudo(self, year):
        easter_sunday = self.get_easter_sunday(year)
        return easter_sunday - timedelta(days=47)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_variable_entrudo(year), "Dia de Carnaval"))
        return days
