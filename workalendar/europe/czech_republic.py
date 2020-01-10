from ..core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('CZ')
class CzechRepublic(WesternCalendar, ChristianMixin):
    'Czech Republic'

    include_easter_monday = True
    include_good_friday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 1, "Restoration Day of the Independent Czech State"),
        (5, 1, "Labour Day"),
        (5, 8, "Liberation Day"),
        (7, 5, "Saints Cyril and Methodius Day"),
        (7, 6, "Jan Hus Day"),
        (9, 28, "St. Wenceslas Day (Czech Statehood Day)"),
        (10, 28, "Independent Czechoslovak State Day"),
        (11, 17, "Struggle for Freedom and Democracy Day"),
        (12, 24, "Christmas Eve"),
        (12, 26, "St. Stephen's Day (The Second Christmas Day)"),
    )

    def get_variable_days(self, year):
        # As of 2016, Good Friday became a holiday
        self.include_good_friday = (year >= 2016)
        return super().get_variable_days(year)
