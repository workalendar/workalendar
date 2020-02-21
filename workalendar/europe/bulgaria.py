from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('BG')
class Bulgaria(WesternCalendar, ChristianMixin):
    'Bulgaria'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 3, _("Liberation Day")),  # Ден на Освобождението на Б
        (5, 1, _("International Workers' Day")),  # Ден на труда и на междунар
        (5, 6, _("Saint George's Day")),  # Гергьовден, ден на храброс
        # Ден на българската просвет
        (5, 24, _("Saints Cyril & Methodius Day")),
        (9, 6, _("Unification Day")),  # Ден на Съединението
        (9, 22, _("Independence Day")),  # Ден на независимостта на Б
        # wikipedia says Non-attendance day for schools, otherwise a working da
        # (11, 1, _("National Awakening Day")),  # Ден на народните будители

    )

    include_easter_sunday = True
    include_easter_monday = True
    include_christmas_eve = True  # Бъдни вечер
    include_christmas = True  # Рождество Христово
    include_boxing_day = True

    # wikipedia says The Bulgarians have two days of Christmas,
    # both called Christmas Day
    boxing_day_label = "Christmas"
