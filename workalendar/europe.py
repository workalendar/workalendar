from workalendar.core import WesternCalendar
from datetime import timedelta


class CzechRepublicCalendar(WesternCalendar):
    "Czech Republic calendar class"

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
        return [
            (self.get_easter_monday(year), "Easter Monday"),
        ]


class FranceCalendar(WesternCalendar):
    "France calendar class"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (5, 8, "Victory in Europe Day"),
        (7, 14, "Bastille Day"),
        (8, 15, "Assumption of Mary to Heaven"),
        (11, 1, "All Saints' Day"),
        (11, 11, "Armistice Day"),
    )

    def get_ascension_thursday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=39)

    def get_pentecote_monday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=50)

    def get_variable_days(self, year):
        return [
            (self.get_easter_monday(year), "Easter Monday"),
            (self.get_ascension_thursday(year), "Ascension Day"),
            (self.get_pentecote_monday(year), "Whit Monday"),
        ]
