from datetime import timedelta, date

from ..core import WesternCalendar, MON
from ..registry_tools import iso_register


@iso_register('CO')
class Colombia(WesternCalendar):
    "Colombia"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 20, "Independence Day"),
        (8, 7, "Boyacá Battle"),
    )
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_palm_sunday = True
    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_corpus_christi = True
    include_immaculate_conception = True

    def get_epiphany(self, year):
        """
        Epiphany is shifted in Colombia
        """
        base_day = date(year, 1, 6)
        return self.get_first_weekday_after(base_day, MON)

    def get_saint_joseph(self, year):
        base_day = date(year, 3, 19)
        return self.get_first_weekday_after(base_day, MON)

    def get_ascension(self, year):
        # By default, Ascension falls on THU.
        # But in Colombia, they celebrate it the next MON.
        base_day = self.get_ascension_thursday(year)
        return self.get_first_weekday_after(base_day, MON)

    def get_corpus_christi(self, year):
        # By default, Corpus Christi falls 60 days after Easter.
        # But in Colombia, they celebrate it the next MON.
        base_day = super().get_corpus_christi(year)
        return self.get_first_weekday_after(base_day, MON)

    def get_sacred_heart(self, year):
        # By default, Sacred Heart falls 68 days after Easter.
        # But in Colombia, they celebrate it the next MON.
        base_day = self.get_easter_sunday(year) + timedelta(days=68)
        return self.get_first_weekday_after(base_day, MON)

    def get_saint_peter_and_saint_paul(self, year):
        base_day = date(year, 6, 29)
        return self.get_first_weekday_after(base_day, MON)

    def get_assumption(self, year):
        # By default, Assumption is a fixed date (August 15th)
        # But in Colombia, they celebrate it the next MON.
        base_day = date(year, 8, 15)
        return self.get_first_weekday_after(base_day, MON)

    def get_day_of_the_races(self, year):
        """
        Return Day of the Races and Hispanity

        a.k.a. "Día de la Raza"
        Fixed to the next MON after October 12th (Columbus Day)
        """
        base_day = date(year, 10, 12)
        return self.get_first_weekday_after(base_day, MON)

    def get_all_saints(self, year):
        # By default, All Saints is a fixed date (November 1st)
        # But in Colombia, they celebrate it the next MON.
        base_day = date(year, 11, 1)
        return self.get_first_weekday_after(base_day, MON)

    def get_cartagena_independence(self, year):
        """
        Cartagena independance day

        Fixed to the next MON after November 11th.
        """
        base_day = date(year, 11, 11)
        return self.get_first_weekday_after(base_day, MON)

    def get_variable_days(self, year):
        """
        Return variable holidays for Colombia

        The following days are set to "the next MON after the 'true' date".

        * Epiphany,
        * Saint Joseph,
        * Ascension,
        * Corpus Christi,
        * Sacred Heart,
        * Saint Peter & Saint Paul
        * Assumption
        * Columbus Day / Race Day
        * All Saints
        * Cartagena Independance
        """
        days = super().get_variable_days(year)
        days.extend([
            (self.get_epiphany(year), "Epiphany"),
            (self.get_saint_joseph(year), "Saint Joseph"),
            (self.get_ascension(year), "Ascension"),
            (self.get_sacred_heart(year), "Sacred Heart"),
            (self.get_saint_peter_and_saint_paul(year),
                "Saint Peter and Saint Paul"),
            (self.get_assumption(year), "Assumption of Mary to Heaven"),
            (self.get_day_of_the_races(year),
                "Day of the Races and Hispanity"),
            (self.get_all_saints(year), "All Saints"),
            (self.get_cartagena_independence(year),
                "Cartagena's Independence"),
        ])

        return days
