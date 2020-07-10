from datetime import timedelta
from ..core import OrthodoxCalendar
from ..registry_tools import iso_register


@iso_register('BY')
class Belarus(OrthodoxCalendar):
    'Belarus'
    "as of http://president.gov.by/en/holidays_en/"

    include_christmas = False

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (1, 7, "Christmas (Orthodox)"),
        (3, 8, "International Women's Day"),
        (5, 1, "Labour Day"),
        (5, 9, "Victory Day"),
        (7, 3, "Republic Day"),
        (11, 7, "October Revolution Day"),
        (12, 25, "Christmas (Catholic)"),
    )
    # Radonitsa
    # https://en.wikipedia.org/wiki/Radonitsa

    def get_radonitsa(self, year):
        # 9 Days after the Orthodox easter sunday
        return self.get_easter_sunday(year) + timedelta(days=9)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_radonitsa(year), "Radonitsa"))
        return days
