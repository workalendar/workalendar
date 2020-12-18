from ..core import OrthodoxCalendar
from ..registry_tools import iso_register


@iso_register('GR')
class Greece(OrthodoxCalendar):
    'Greece'

    # Civil holidays
    include_labour_day = True
    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (3, 25, "Independence Day"),
        (10, 28, "Ohi Day"),
    )

    # Christian holidays
    include_epiphany = True
    include_clean_monday = True
    include_annunciation = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost"
    include_whit_monday = True
    include_assumption = True
    include_boxing_day = True
    boxing_day_label = "Glorifying Mother of God"
    # No Orthodox Christmas
    include_orthodox_christmas = False
