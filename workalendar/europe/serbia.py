from ..core import OrthodoxCalendar
from ..registry_tools import iso_register


@iso_register('RS')
class Serbia(OrthodoxCalendar):
    'Serbia'

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (1, 7, "Christmas"),
        (2, 15, "Statehood Day"),
        (2, 16, "Statehood Day"),
        (5, 1, "Labour Day"),
        (5, 2, "Labour Day Holiday"),
        (11, 11, "Armistice Day"),
    )

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_christmas = False
