from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('MC')
class Monaco(WesternCalendar):
    'Monaco'

    # Christian holidays
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_all_saints = True
    include_assumption = True
    include_corpus_christi = True
    include_immaculate_conception = True

    # Civil holidays
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 27, "Saint Dévote's Day"),
        (11, 19, "H.S.H. the Sovereign Prince's Day"),
    )
