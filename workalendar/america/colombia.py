from datetime import timedelta, date
from gettext import gettext as _

from ..core import WesternCalendar, ChristianMixin, MON
from ..registry_tools import iso_register


@iso_register('CO')
class Colombia(WesternCalendar, ChristianMixin):
    "Colombia"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, _("Labour Day")),
        (7, 20, _("Independence Day")),
        (8, 7, _("Boyacá Battle")),
    )
    include_palm_sunday = True
    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_corpus_christi = True
    include_immaculate_conception = True

    def get_epiphany(self, year):
        base_day = date(year, 1, 6)
        return Colombia.get_first_weekday_after(base_day, MON)

    def get_saint_joseph(self, year):
        base_day = date(year, 3, 19)
        return Colombia.get_first_weekday_after(base_day, MON)

    def get_ascension(self, year):
        return self.get_easter_sunday(year) + timedelta(days=43)

    def get_corpus_christi(self, year):
        return self.get_easter_sunday(year) + timedelta(days=64)

    def get_sacred_heart(self, year):
        return self.get_easter_sunday(year) + timedelta(days=71)

    def get_saint_peter_and_saint_paul(self, year):
        base_day = date(year, 6, 29)
        return Colombia.get_first_weekday_after(base_day, MON)

    def get_assumption(self, year):
        base_day = date(year, 8, 15)
        return Colombia.get_first_weekday_after(base_day, MON)

    def get_race_day(self, year):
        base_day = date(year, 10, 12)
        return Colombia.get_first_weekday_after(base_day, MON)

    def get_all_saints(self, year):
        base_day = date(year, 11, 1)
        return Colombia.get_first_weekday_after(base_day, MON)

    def get_cartagena_independence(self, year):
        base_day = date(year, 11, 11)
        return Colombia.get_first_weekday_after(base_day, MON)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_epiphany(year), _("Epiphany")),
            (self.get_saint_joseph(year), _("Saint Joseph")),
            (self.get_ascension(year), _("Ascension")),
            (self.get_sacred_heart(year), _("Sacred Heart")),
            (self.get_saint_peter_and_saint_paul(year),
                _("Saint Peter and Saint Paul")),
            (self.get_assumption(year), _("Assumption of Mary to Heaven")),
            (self.get_race_day(year), _("Race Day")),
            (self.get_all_saints(year), _("All Saints")),
            (self.get_cartagena_independence(year),
                _("Cartagena's Independence")),
        ])

        return days
