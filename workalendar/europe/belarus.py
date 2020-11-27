from datetime import timedelta
from ..core import OrthodoxCalendar
from ..registry_tools import iso_register


@iso_register('BY')
class Belarus(OrthodoxCalendar):
    'Belarus'
    "as of http://president.gov.by/en/holidays_en/"
    # Civil holidays
    include_labour_day = True

    # Christian holidays
    include_christmas = True
    christmas_day_label = "Christmas Day (Catholic)"
    orthodox_christmas_day_label = "Christmas (Orthodox)"

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (3, 8, "International Women's Day"),
        (5, 9, "Victory Day"),
        (7, 3, "Republic Day"),
        (11, 7, "October Revolution Day"),
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
