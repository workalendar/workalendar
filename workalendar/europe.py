from workalendar.core import WesternCalendar
from datetime import timedelta


class FranceCalendar(WesternCalendar):
    "France calendar class"

    FIXED_DAYS = WesternCalendar.FIXED_DAYS + (
        (5, 1),
        (5, 8),
        (7, 14),
        (8, 15),
        (11, 1),
        (11, 11),
        (12, 25),
    )

    def get_ascension_thursday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=39)

    def get_pentecote_monday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=50)

    def get_variable_days(self, year):
        return set([
            self.get_easter_monday(year),
            self.get_ascension_thursday(year),
            self.get_pentecote_monday(year)]
        )
