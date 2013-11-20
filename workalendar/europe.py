from workalendar.core import WesternCalendar
from datetime import date, timedelta


class FranceCalendar(WesternCalendar):
    "France calendar class"

    def get_ascension_thursday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=39)

    def get_pentecote_monday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=50)

    def get_calendar_holidays(self, year):
        days = super(FranceCalendar, self).get_calendar_holidays(year)
        days.add(date(year, 5, 1))    # Labour day
        days.add(date(year, 5, 8))    # 1939-45 victory
        days.add(date(year, 7, 14))   # National day
        days.add(date(year, 8, 15))   # Assomption
        days.add(date(year, 11, 1))   # Toussaint
        days.add(date(year, 11, 11))  # Armistice
        days.add(date(year, 12, 25))  # Christmas
        days.add(self.get_easter_monday(year))
        days.add(self.get_ascension_thursday(year))
        days.add(self.get_pentecote_monday(year))
        return days
