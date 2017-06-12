# -*- coding: utf-8 -*-
from workalendar.core import ChineseNewYearCalendar, WesternCalendar
from workalendar.core import EphemMixin


class Taiwan(EphemMixin, ChineseNewYearCalendar, WesternCalendar):
    "Taiwan (Republic of China)"
    FIXED_HOLIDAYS = (
        WesternCalendar.FIXED_HOLIDAYS +
        (
            (2, 28, "228 Peace Memorial Day"),
            (4, 4, "Combination of Women's Day and Children's Day"),
            (10, 10, "National Day/Double Tenth Day"),
        )
    )
    include_chinese_new_year_eve = True
    include_chinese_second_day = True

    def get_variable_days(self, year):
        days = super(Taiwan, self).get_variable_days(year)
        # Qingming begins when the sun reaches the celestial
        # longitude of 15° (usually around April 4th or 5th)
        qingming = EphemMixin.solar_term(self, year, 15, 'Asia/Taipei')

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
