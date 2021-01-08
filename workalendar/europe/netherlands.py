from datetime import date, timedelta
from ..core import WesternCalendar, SUN
from ..registry_tools import iso_register


@iso_register('NL')
class Netherlands(WesternCalendar):
    'Netherlands'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 5, "Liberation Day"),
    )

    def __init__(self, include_carnival=False):
        self.include_carnival = include_carnival
        super().__init__()

    def get_king_queen_day(self, year):
        """27 April unless this is a Sunday in which case it is the 26th

        Before 2013 it was called Queensday, falling on
        30 April, unless this is a Sunday in which case it is the 29th.
        """
        if year > 2013:
            king_day = date(year, 4, 27)
            if king_day.weekday() != SUN:
                return king_day, "King's day"
            return king_day - timedelta(days=1), "King's day"
        else:
            queen_day = date(year, 4, 30)
            if queen_day.weekday() != SUN:
                return queen_day, "Queen's day"
            return queen_day - timedelta(days=1), "Queen's day"

    def get_carnival_days(self, year):
        """Carnival starts 7 weeks before Easter Sunday and lasts 3 days."""
        n_days = 3
        start = self.get_easter_sunday(year) - timedelta(weeks=7)

        return [
            (
                start + timedelta(days=i), "Carnival"
            ) for i in range(n_days)
        ]

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_king_queen_day(year))
        if self.include_carnival:
            days.extend(self.get_carnival_days(year))
        return days


FALL_HOLIDAYS_EARLY_REGIONS = {
    2025: ["south"],
    2024: ["south"],
    2023: ["middle", "south"],
    2022: ["north"],
    2021: ["north", "middle"],
    2020: ["north"],
    2019: ["south"],
    2018: ["south"],
    2017: ["middle", "south"],
    2016: ["north", "middle"],
}

SPRING_HOLIDAYS_EARLY_REGIONS = {
    2025: ["north"],
    2024: ["south"],
    2023: ["south"],
    2022: ["north"],
    2021: ["south"],
    2020: ["north"],
    2019: ["north"],
    2018: ["south"],
    2017: ["north"],
    2016: ["middle", "south"],
}

SUMMER_HOLIDAYS_EARLY_REGIONS = {
    2025: ["south"],
    2024: ["south"],
    2023: ["middle"],
    2022: ["middle"],
    2021: ["north"],
    2020: ["north"],
    2019: ["south"],
    2018: ["south"],
    2017: ["middle"],
    2016: ["middle"],
}

SUMMER_HOLIDAYS_LATE_REGIONS = {
    2025: ["middle"],
    2024: ["north"],
    2023: ["north"],
    2022: ["south"],
    2021: ["south"],
    2020: ["middle"],
    2019: ["middle"],
    2018: ["north"],
    2017: ["north"],
    2016: ["south"],
}


class NetherlandsWithSchoolHolidays(Netherlands):
    """Netherlands with school holidays (2016 to 2025).

    Data source and regulating body:
    https://www.rijksoverheid.nl/onderwerpen/schoolvakanties/overzicht-schoolvakanties-per-schooljaar
    """

    def __init__(
            self,
            region,
            carnival_instead_of_spring=False,
            **kwargs,
    ):
        """ Set up a calendar incl. school holidays for a specific region

        :param region: either "north", "middle" or "south"
        """
        if region not in ("north", "middle", "south"):
            raise ValueError("Set region to 'north', 'middle' or 'south'.")
        self.region = region
        self.carnival_instead_of_spring = carnival_instead_of_spring
        if carnival_instead_of_spring and "include_carnival" not in kwargs:
            kwargs["include_carnival"] = True
        super().__init__(**kwargs)

    def get_fall_holidays(self, year):
        n_days = 9
        week = 43

        # Exceptional years
        if year == 2024:
            week = 44

        # Holiday starts on the preceding Saturday
        try:
            start = date.fromisocalendar(year, week - 1, 6)
        except AttributeError:
            # Adapted from https://stackoverflow.com/a/59200842
            first = date(year, 1, 1)
            base = 1 if first.isocalendar()[1] == 1 else 8
            start = first + timedelta(
                days=base - first.isocalendar()[2] + 7 * (week - 1) - 2
            )

        # Some regions have their fall holiday 1 week earlier
        try:
            if self.region in FALL_HOLIDAYS_EARLY_REGIONS[year]:
                start = start - timedelta(weeks=1)
        except KeyError:
            raise NotImplementedError(f"Unknown fall holidays for {year}.")

        return [
            (start + timedelta(days=i), "Fall holiday") for i in range(n_days)
        ]

    def get_christmas_holidays(
            self, year, in_december=True, in_january=True
    ):
        """ Christmas holidays run partially in December and partially in January
        (spillover from previous year).
        """

        if in_december:

            # 27 December is always in a full week of holidays
            week = date(year, 12, 27).isocalendar()[1]

            # Holiday starts on the preceding Saturday
            try:
                start = date.fromisocalendar(year, week - 1, 6)
            except AttributeError:
                # Adapted from https://stackoverflow.com/a/59200842
                first = date(year, 1, 1)
                base = 1 if first.isocalendar()[1] == 1 else 8
                start = first + timedelta(
                    days=base - first.isocalendar()[2] + 7 * (week - 1) - 2
                )

            dates = [
                (
                    start + timedelta(days=i), "Christmas holiday"
                ) for i in range((date(year, 12, 31) - start).days + 1)
            ]

            if in_january:
                dates.extend(
                    self.get_christmas_holidays(year, in_december=False)
                )
            return dates

        n_days = 16
        # 27 December is always in a full week of holidays
        week = date(year - 1, 12, 27).isocalendar()[1]

        # Holiday ends 15 days after the preceding Saturday
        try:
            end = date.fromisocalendar(
                year - 1, week - 1, 6
            ) + timedelta(days=n_days - 1)
        except AttributeError:
            # Adapted from https://stackoverflow.com/a/59200842
            first = date(year - 1, 1, 1)
            base = 1 if first.isocalendar()[1] == 1 else 8
            end = first + timedelta(
                days=base - first.isocalendar()[2] + 7 * (week - 1)
                + n_days - 3
            )

        return [
            (
                date(year, 1, 1) + timedelta(days=i), "Christmas holiday"
            ) for i in range((end - date(year, 1, 1)).days + 1)
        ]

    def get_spring_holidays(self, year):
        n_days = 9
        week = 9

        # Exceptional years
        if year in [2024, 2021]:
            week = 8

        # Holiday starts on the preceding Saturday
        try:
            start = date.fromisocalendar(year, week - 1, 6)
        except AttributeError:
            # Adapted from https://stackoverflow.com/a/59200842
            first = date(year, 1, 1)
            base = 1 if first.isocalendar()[1] == 1 else 8
            start = first + timedelta(
                days=base - first.isocalendar()[2] + 7 * (week - 1) - 2
            )

        # Some regions have their spring holiday 1 week earlier
        try:
            if self.region in SPRING_HOLIDAYS_EARLY_REGIONS[year]:
                start = start - timedelta(weeks=1)
        except KeyError:
            raise NotImplementedError(f"Unknown spring holidays for {year}.")

        return [
            (
                start + timedelta(days=i), "Spring holiday"
            ) for i in range(n_days)
        ]

    def get_carnival_holidays(self, year):
        """Carnival holiday starts 7 weeks and 1 day before Easter Sunday
        and lasts 9 days.
        """
        n_days = 9
        start = self.get_easter_sunday(year) - timedelta(weeks=7, days=1)

        return [
            (
                start + timedelta(days=i), "Carnival holiday"
            ) for i in range(n_days)
        ]

    def get_may_holidays(self, year):
        n_days = 9
        week = 18

        # Exceptional years
        if year == 2017:
            week = 17

        # Holiday starts on the preceding Saturday
        try:
            start = date.fromisocalendar(year, week - 1, 6)
        except AttributeError:
            # Adapted from https://stackoverflow.com/a/59200842
            first = date(year, 1, 1)
            base = 1 if first.isocalendar()[1] == 1 else 8
            start = first + timedelta(
                days=base - first.isocalendar()[2] + 7 * (week - 1) - 2
            )

        return [
            (start + timedelta(days=i), "May holiday") for i in range(n_days)
        ]

    def get_summer_holidays(self, year):
        n_days = 44
        week = 29

        # Holiday starts on the preceding Saturday
        try:
            start = date.fromisocalendar(year, week - 1, 6)
        except AttributeError:
            # Adapted from https://stackoverflow.com/a/59200842
            first = date(year, 1, 1)
            base = 1 if first.isocalendar()[1] == 1 else 8
            start = first + timedelta(
                days=base - first.isocalendar()[2] + 7 * (week - 1) - 2
            )

        # Some regions have their summer holiday 1 week earlier
        try:
            if self.region in SUMMER_HOLIDAYS_EARLY_REGIONS[year]:
                start = start - timedelta(weeks=1)
        except KeyError:
            raise NotImplementedError(f"Unknown summer holidays for {year}.")

        # Some regions have their summer holiday 1 week later
        try:
            if self.region in SUMMER_HOLIDAYS_LATE_REGIONS[year]:
                start = start + timedelta(weeks=1)
        except KeyError:
            raise NotImplementedError(f"Unknown summer holidays for {year}.")

        return [
            (
                start + timedelta(days=i), "Summer holiday"
            ) for i in range(n_days)
        ]

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend(self.get_fall_holidays(year))
        days.extend(self.get_christmas_holidays(year))
        if self.carnival_instead_of_spring:
            days.extend(self.get_carnival_holidays(year))
        else:
            days.extend(self.get_spring_holidays(year))
        days.extend(self.get_may_holidays(year))
        days.extend(self.get_summer_holidays(year))
        return days
