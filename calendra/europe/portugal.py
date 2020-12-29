from datetime import date
from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('PT')
class Portugal(WesternCalendar):
    'Portugal'

    # Christian holidays
    include_good_friday = True
    include_easter_sunday = True
    include_christmas = True
    include_immaculate_conception = True
    immaculate_conception_label = "Imaculada Conceição"

    # Civil holidays
    include_labour_day = True
    labour_day_label = "Dia do Trabalhador"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 25, "Dia da Liberdade"),
        (6, 10, "Dia de Portugal"),
        (8, 15, "Assunção de Nossa Senhora"),
    )

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)
        if year > 2015 or year < 2013:
            days.append((date(year, 10, 5), "Implantação da República"))
            days.append((date(year, 11, 1), "Todos os santos"))
            days.append((date(year, 12, 1), "Restauração da Independência"))
        return days

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        if year > 2015 or year < 2013:
            days.append((self.get_corpus_christi(year), "Corpus Christi"))
        return days
