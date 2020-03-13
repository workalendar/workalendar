from datetime import timedelta
from .. import gettext as _

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
        (2, 4, _("Dia do Inicio da Luta Armada")),
        (3, 8, _("Dia Internacional da Mulher")),
        (4, 4, _("Dia da Paz")),
        (5, 1, _("Dia Internacional do Trabalhador")),
        (9, 17, _("Dia do Fundador da Nação e do Herói Nacional")),
        (11, 11, _("Dia da Independência Nacional")),
    )

    def get_variable_entrudo(self, year):
        easter_sunday = self.get_easter_sunday(year)
        return easter_sunday - timedelta(days=47)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_variable_entrudo(year), _("Dia de Carnaval")))
        return days
