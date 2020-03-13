from datetime import date
from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin, FRI, SAT
from ..registry_tools import iso_register


@iso_register('FI')
class Finland(WesternCalendar, ChristianMixin):
    'Finland'

    include_epiphany = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    whit_sunday_label = _('Pentecost')
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = _("St. Stephen's Day")

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, _("Labour Day")),
        (12, 6, _("Independence Day")),
    )

    def get_midsummer_eve(self, year):
        date_eve = Finland.get_nth_weekday_in_month(
            year, 6, FRI, start=date(year, 6, 19))
        return date_eve

    def get_midsummer_day(self, year):
        date_eve = Finland.get_nth_weekday_in_month(
            year, 6, SAT, start=date(year, 6, 20))
        return date_eve

    def get_variable_all_saints(self, year):
        all_saints = date(year, 10, 31)
        if all_saints.weekday() != SAT:
            all_saints = Finland.get_nth_weekday_in_month(
                year, 11, SAT)
        return all_saints

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_midsummer_eve(year), _("Midsummer's Eve")))
        days.append((self.get_midsummer_day(year), _("Midsummer's Day")))
        days.append((self.get_variable_all_saints(year), _("All Saints")))
        return days
