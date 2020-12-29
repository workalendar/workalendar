from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('PL')
class Poland(WesternCalendar):
    'Poland'

    # Civil holidays
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 6, 'Trzech Kroli'),
        (5, 3, 'Constitution Day'),
        (11, 11, 'Independence Day'),
    )

    # Christian holidays
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost Sunday"
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_boxing_day = True
