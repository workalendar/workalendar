from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('BG')
class Bulgaria(WesternCalendar):
    'Bulgaria'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 3, "Liberation Day"),  # Ден на Освобождението на Б
        (5, 6, "Saint George's Day"),  # Гергьовден, ден на храброс
        (5, 24, "Saints Cyril & Methodius Day"),  # Ден на българската просвет
        (9, 6, "Unification Day"),  # Ден на Съединението
        (9, 22, "Independence Day"),  # Ден на независимостта на Б
        # wikipedia says Non-attendance day for schools, otherwise a working da
        # (11, 1, "National Awakening Day"),  # Ден на народните будители
    )

    # Civil holidays
    include_labour_day = True
    # Ден на труда и на междунар
    labour_day_label = "International Workers' Day"

    # Christian holidays
    include_easter_sunday = True
    include_easter_monday = True
    include_christmas_eve = True  # Бъдни вечер
    include_christmas = True  # Рождество Христово
    include_boxing_day = True

    # wikipedia says The Bulgarians have two days of Christmas,
    # both called Christmas Day
    boxing_day_label = "Christmas"
