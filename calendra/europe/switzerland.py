from datetime import date, timedelta
from ..core import WesternCalendar, ChristianMixin, SUN
from ..registry import iso_register


@iso_register('CH')
class Switzerland(WesternCalendar, ChristianMixin):
    'Switzerland'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_christmas = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Berchtold's Day"),
        (5, 1, "Labour Day"),
        (8, 1, "National Holiday"),
    )


@iso_register('CH-VD')
class Vaud(Switzerland):
    'Vaud'

    include_boxing_day = False
    include_federal_thanksgiving_monday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Berchtold's Day"),
        (8, 1, "National Holiday"),
    )

    def get_federal_thanksgiving_monday(self, year):
        "Monday following the 3rd sunday of September"
        september_1st = date(year, 9, 1)
        return (
            september_1st +
            (6 - september_1st.weekday()) * timedelta(days=1) +  # 1st sunday
            timedelta(days=15)  # Monday following 3rd sunday
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        if self.include_federal_thanksgiving_monday:
            days.append((self.get_federal_thanksgiving_monday(year),
                         "Federal Thanksgiving Monday"))
        return days


@iso_register('CH-GE')
class Geneva(Switzerland):
    'Geneva'

    include_boxing_day = False

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (8, 1, "National Holiday"),
        (12, 31, "Creation of Geneva Republic"),
    )

    def get_genevan_fast(self, year):
        "Thursday following the first Sunday of September"
        first_sunday = self.get_nth_weekday_in_month(year, 9, SUN)
        # The following thursday is 4 days after
        return (
            first_sunday + timedelta(days=4),
            "Genevan Fast"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_genevan_fast(year))
        return days
