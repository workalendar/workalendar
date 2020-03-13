from gettext import gettext as _
from datetime import timedelta

from ..core import WesternCalendar, OrthodoxMixin
from ..registry_tools import iso_register


@iso_register('BY')
class Belarus(WesternCalendar, OrthodoxMixin):
    'Belarus'
    "as of http://president.gov.by/en/holidays_en/"

    include_christmas = False

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, _("Day After New Year")),
        (1, 7, _("Christmas (Orthodox)")),
        (3, 8, _("International Women's Day")),
        (5, 1, _("Labour Day")),
        (5, 9, _("Victory Day")),
        (7, 3, _("Republic Day")),
        (11, 7, _("October Revolution Day")),
        (12, 25, _("Christmas (Catholic)")),
    )
    # Radonitsa
    # https://en.wikipedia.org/wiki/Radonitsa

    def get_radonitsa(self, year):
        # Second Monday after easter sunday
        return self.get_easter_sunday(year) + timedelta(days=15)

    def get_day_after_radonitsa(self, year):
        # one day after the Radonsista Monday
        return self.get_radonitsa(year) + timedelta(days=1)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_radonitsa(year), _("Radonista")))
        days.append(
            (self.get_day_after_radonitsa(year), _("Radonista Holiday"))
        )
        return days
