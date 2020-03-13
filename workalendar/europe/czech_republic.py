from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('CZ')
class CzechRepublic(WesternCalendar, ChristianMixin):
    'Czech Republic'

    include_easter_monday = True
    include_good_friday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 1, _("Restoration Day of the Independent Czech State")),
        (5, 1, _("Labour Day")),
        (5, 8, _("Liberation Day")),
        (7, 5, _("Saints Cyril and Methodius Day")),
        (7, 6, _("Jan Hus Day")),
        (9, 28, _("St. Wenceslas Day (Czech Statehood Day)")),
        (10, 28, _("Independent Czechoslovak State Day")),
        (11, 17, _("Struggle for Freedom and Democracy Day")),
        (12, 24, _("Christmas Eve")),
        (12, 26, _("St. Stephen's Day (The Second Christmas Day)")),
    )

    def get_variable_days(self, year):
        # As of 2016, Good Friday became a holiday
        self.include_good_friday = (year >= 2016)
        return super().get_variable_days(year)
