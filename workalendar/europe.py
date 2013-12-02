from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin, THU, MON


class CzechRepublicCalendar(WesternCalendar, ChristianMixin):
    "Czech Republic calendar class"
    include_easter_monday = True

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


class FranceCalendar(WesternCalendar, ChristianMixin):
    "France calendar class"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (5, 8, "Victory in Europe Day"),
        (7, 14, "Bastille Day"),
        (8, 15, "Assumption of Mary to Heaven"),
        (11, 1, "All Saints' Day"),
        (11, 11, "Armistice Day"),
    )


class IcelandCalendar(WesternCalendar, ChristianMixin):
    "Iceland calendar class"
    include_holy_thursday = True
    include_good_friday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_christmas_eve = True
    include_st_stephen = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 17, "Icelandic National Day"),
        (12, 31, "New Year's Eve"),
    )

    def get_first_day_of_summer(self, year):
        """It's the first thursday *after* April, 18th.
        If April the 18th is a thursday, then it jumps to the 24th.
        """
        return WesternCalendar.get_nth_weekday_in_month(
            year, 4, THU,
            start=date(year, 4, 19))

    def get_variable_days(self, year):
        days = super(IcelandCalendar, self).get_variable_days(year)
        days += [
            (
                self.get_first_day_of_summer(year),
                "First day of summer"),
            (
                WesternCalendar.get_nth_weekday_in_month(year, 8, MON),
                "Commerce Day"),
        ]
        return days


class UnitedKingdomCalendar(WesternCalendar, ChristianMixin):
    "United Kingdom calendar"
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True

    def get_early_may_bank_holiday(self, year):
        return (
            UnitedKingdomCalendar.get_nth_weekday_in_month(year, 5, MON),
            "Early May Bank Holiday"
        )

    def get_spring_bank_holiday(self, year):
        return (
            UnitedKingdomCalendar.get_last_weekday_in_month(year, 5, MON),
            "Spring Bank Holiday"
        )

    def get_late_summer_bank_holiday(self, year):
        return (
            UnitedKingdomCalendar.get_last_weekday_in_month(year, 8, MON),
            "Late Summer Bank Holiday"
        )

    def get_variable_days(self, year):
        days = super(UnitedKingdomCalendar, self).get_variable_days(year)
        days.append(self.get_early_may_bank_holiday(year))
        days.append(self.get_spring_bank_holiday(year))
        days.append(self.get_late_summer_bank_holiday(year))
        return days
