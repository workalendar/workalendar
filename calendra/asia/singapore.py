from datetime import date

from ..core import (
    WesternMixin, IslamicMixin, ChineseNewYearCalendar,
    SAT, SUN
)
from ..registry_tools import iso_register


@iso_register('SG')
class Singapore(WesternMixin, IslamicMixin, ChineseNewYearCalendar):
    "Singapore"
    # Civil holidays
    include_labour_day = True

    # Christian holiday
    include_good_friday = True

    # Islamic holidays
    include_eid_al_fitr = True
    eid_al_fitr_label = "Hari Raya Puasa"
    include_day_of_sacrifice = True
    day_of_sacrifice_label = "Hari Raya Haji"

    FIXED_HOLIDAYS = ChineseNewYearCalendar.FIXED_HOLIDAYS + (
        (8, 9, "National Day"),
    )

    # Explicitly assign these WE days, Singapore calendar is too much of a mix
    WEEKEND_DAYS = (SAT, SUN)

    # Diwali/Deepavali is sometimes celebrated on a different day to India
    # so this can't be put into a HinduMixin
    # Ref:
    # https://holidays.kayaposoft.com/public_holidays.php?year=2022&country=sgp
    DEEPAVALI = {
        2000: date(2000, 10, 26),
        2001: date(2001, 11, 14),
        2002: date(2002, 11, 3),
        2003: date(2003, 10, 23),
        2004: date(2004, 11, 11),
        2005: date(2005, 11, 1),
        2006: date(2006, 10, 21),
        2007: date(2007, 11, 8),
        2008: date(2008, 10, 27),
        2009: date(2009, 10, 17),
        2010: date(2010, 11, 5),
        2011: date(2011, 10, 26),
        2012: date(2012, 11, 13),
        2013: date(2013, 11, 3),
        2014: date(2014, 10, 22),
        2015: date(2015, 11, 10),
        2016: date(2016, 10, 29),
        2017: date(2017, 10, 18),
        2018: date(2018, 11, 6),
        2019: date(2019, 10, 27),
        2020: date(2020, 11, 14),
        2021: date(2021, 11, 4),
        2022: date(2022, 10, 24),
        2023: date(2023, 11, 13),
        2024: date(2024, 10, 31),
        2025: date(2025, 10, 20),
        2026: date(2026, 11, 9),
        2027: date(2027, 10, 28),
        2028: date(2028, 11, 15),
        2029: date(2029, 11, 5),
        2030: date(2030, 10, 25),
    }
    chinese_new_year_label = "Chinese Lunar New Year's Day"
    include_chinese_second_day = True
    chinese_second_day_label = "Second day of Chinese Lunar New Year"
    shift_sunday_holidays = True

    def get_variable_days(self, year):
        """
        Singapore variable days
        """
        if year not in self.DEEPAVALI:
            msg = f'Missing date for Singapore Deepavali for year: {year}'
            raise KeyError(msg)

        days = super().get_variable_days(year)

        # Vesak Day
        days.append(
            (ChineseNewYearCalendar.lunar(year, 4, 15), "Vesak Day"),
        )

        # Add in Deepavali (hardcoded dates, so no need to shift)
        days.append((self.DEEPAVALI.get(year), 'Deepavali'))
        return days
