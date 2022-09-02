from datetime import date

from ..core import ChineseNewYearCalendar, cleaned_date
from ..astronomy import solar_term
from ..registry_tools import iso_register


@iso_register('TW')
class Taiwan(ChineseNewYearCalendar):
    "Taiwan (Republic of China)"
    FIXED_HOLIDAYS = ChineseNewYearCalendar.FIXED_HOLIDAYS + (
        (2, 28, "228 Peace Memorial Day"),
        (4, 4, "Combination of Women's Day and Children's Day"),
        (10, 10, "National Day/Double Tenth Day"),
    )
    include_chinese_new_year_eve = True
    include_chinese_second_day = True

    def is_working_day(self, day, *args, **kwargs):
        day = cleaned_date(day)
        if day in (date(2021, 2, 20), date(2021, 9, 11)):
            return True
        return super().is_working_day(day, *args, **kwargs)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Qingming begins when the sun reaches the celestial
        # longitude of 15° (usually around April 4th or 5th)
        qingming = solar_term(year, 15, 'Asia/Taipei')

        days.extend([
            (
                ChineseNewYearCalendar.lunar(year, 1, 3),
                "Chinese New Year (3rd day)"
            ),
            (qingming, "Qingming Festival"),
            (ChineseNewYearCalendar.lunar(year, 5, 5), "Dragon Boat Festival"),
            (ChineseNewYearCalendar.lunar(year, 8, 15), "Mid-Autumn Festival"),
        ])
        return days
