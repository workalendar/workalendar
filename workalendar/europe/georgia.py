from ..core import OrthodoxCalendar
from ..registry_tools import iso_register


@iso_register('GE')
class Georgia(OrthodoxCalendar):
    'Country of Georgia'

    "Sources: "
    "https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)"
    "https://www.officeholidays.com/countries/georgia/2021"

    include_christmas = False
    include_christmas_eve = False

    include_new_years_day = True
    include_orthodox_christmas = True
    include_epiphany = False
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_easter_monday = True

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (1, 19, "Orthodox Epiphany"),
        (3, 3, "Mother's Day"),
        (3, 8, "International Women's Day"),
        (4, 9, "Day Of National Unity"),
        (5, 9, "Day Of Victory Over Fascism"),
        (5, 12, "Saint Andrew The First-Called Day"),
        (5, 26, "Independence Day"),
        (8, 28, "Saint Mary's Day"),
        (10, 14, "Day Of Svetitskovloba"),
        (11, 23, "Saint George's Day"),
    )
