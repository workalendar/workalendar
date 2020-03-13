from datetime import date
from gettext import gettext as _

from ..core import WesternCalendar, OrthodoxMixin
from ..registry_tools import iso_register


@iso_register('RO')
class Romania(OrthodoxMixin, WesternCalendar):
    'Romania'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, _("Day After New Years")),
        (1, 24, _("Union Day")),
        (5, 1, _("Labour Day")),
        (8, 15, _("Dormition of the Theotokos")),
        (11, 30, _("St. Andrew's Day")),
        (12, 1, _("National Day/Great Union")),
    )

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = _('Pentecost')
    include_whit_monday = True

    include_christmas = True
    include_boxing_day = True
    boxing_day_label = _('Christmas Day')

    def get_childrens_day(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if year >= 2017:
            actual_date = date(year, 6, 1)
            days = [(actual_date, _("Children's Day"))]

        return days

    def get_liberation_day(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if year >= 1949 and year <= 1990:
            actual_date = date(year, 8, 23)
            days = [(actual_date, _("Liberation from Fascist Occupation Day"))]

        return days

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend(self.get_childrens_day(year))
        days.extend(self.get_liberation_day(year))
        return days
