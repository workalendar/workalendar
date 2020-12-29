from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('AO')
class Angola(WesternCalendar):
    "Angola"
    # Civil holiday
    include_labour_day = True
    labour_day_label = "Dia Internacional do Trabalhador"
    # Christian holidays
    include_fat_tuesday = True
    fat_tuesday_label = "Dia de Carnaval"
    include_good_friday = True
    include_easter_sunday = True
    include_christmas = True
    include_all_souls = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 4, "Dia do Inicio da Luta Armada"),
        (3, 8, "Dia Internacional da Mulher"),
        (4, 4, "Dia da Paz"),
        (9, 17, "Dia do Fundador da Nação e do Herói Nacional"),
        (11, 11, "Dia da Independência Nacional"),
    )
