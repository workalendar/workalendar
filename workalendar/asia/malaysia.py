from datetime import date

from ..core import (
    IslamicMixin, ChineseNewYearCalendar,
    SAT, SUN
)
from ..registry_tools import iso_register


@iso_register('MY')
class Malaysia(IslamicMixin, ChineseNewYearCalendar):
    "Malaysia"
    # Civil holidays
    include_labour_day = True
    labour_day_label = "Workers' Day"

    # Islamic holidays
    include_nuzul_al_quran = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 2
    eid_al_fitr_label = "Hari Raya Puasa"
    include_day_of_sacrifice = True
    day_of_sacrifice_label = "Hari Raya Haji"
    include_islamic_new_year = True
    include_prophet_birthday = True

    # Most of th Malaysian territory uses these Week-end days
    WEEKEND_DAYS = (SAT, SUN)
    # TODO: Add calendar exceptions

    FIXED_HOLIDAYS = ChineseNewYearCalendar.FIXED_HOLIDAYS + (
        (2, 1, "Federal Territory Day"),
        (8, 31, "National Day"),
        (9, 16, "Malaysia Day"),
        (12, 25, "Christmas Day"),
    )

    # Ref: https://publicholidays.com.my/deepavali/
    MSIA_DEEPAVALI = {
        2010: date(2010, 11, 5),
        2011: date(2011, 10, 26),
        2012: date(2012, 11, 13),
        2013: date(2013, 11, 2),
        2014: date(2014, 10, 22),
        2015: date(2015, 11, 10),
        2016: date(2016, 10, 29),
        2017: date(2017, 10, 18),
        2018: date(2018, 11, 6),
        2019: date(2019, 10, 27),
        2020: date(2020, 11, 14),
        2021: date(2021, 11, 4),
        2022: date(2022, 10, 24),
        2023: date(2023, 11, 13),  # in lieu of 12th Nov
        2024: date(2024, 10, 31),
    }

    # Ref: https://publicholidays.com.my/thaipusam/
    MSIA_THAIPUSAM = {
        2010: date(2010, 1, 30),
        2011: date(2011, 1, 20),
        2012: date(2012, 2, 7),
        2013: date(2013, 1, 28),
        2014: date(2014, 1, 17),
        2015: date(2015, 2, 3),
        2016: date(2016, 1, 25),
        2017: date(2017, 2, 9),
        2018: date(2018, 1, 31),
        2019: date(2019, 1, 21),
        2020: date(2020, 2, 8),
        2021: date(2021, 1, 28),
        2022: date(2022, 1, 18),
        2023: date(2023, 2, 4),
        2024: date(2024, 1, 25),
    }
    chinese_new_year_label = "First Day of Lunar New Year"
    include_chinese_second_day = True
    chinese_second_day_label = "Second Day of Lunar New Year"
    shift_sunday_holidays = True

    def get_variable_days(self, year):
        """
        Malaysia variable days
        """
        days = super().get_variable_days(year)

        # Vesak Day
        days.append(
            (ChineseNewYearCalendar.lunar(year, 4, 15), "Vesak Day"),
        )

        # Add in Deepavali and Thaipusam (hardcoded dates, so no need to shift)
        msia_deepavali = self.MSIA_DEEPAVALI.get(year)
        if not msia_deepavali:
            mdmsg = f'Missing date for Malaysia Deepavali for year: {year}'
            raise KeyError(mdmsg)
        days.append((msia_deepavali, 'Deepavali'))

        msia_thaipusam = self.MSIA_THAIPUSAM.get(year)
        if not msia_thaipusam:
            mtmsg = f'Missing date for Malaysia Thaipusam for year: {year}'
            raise KeyError(mtmsg)
        days.append((msia_thaipusam, 'Thaipusam'))
        return days
