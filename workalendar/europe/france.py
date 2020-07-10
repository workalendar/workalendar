from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('FR')
class France(WesternCalendar):
    'France'

    # Christian holidays
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_all_saints = True
    include_assumption = True

    # Civil holidays
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 8, "Victory in Europe Day"),
        (7, 14, "Bastille Day"),
        (11, 11, "Armistice Day"),
    )


class FranceAlsaceMoselle(France):
    "France Alsace/Moselle"
    include_good_friday = True
    include_boxing_day = True
