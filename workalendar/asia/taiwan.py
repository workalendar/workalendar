# -*- coding: utf-8 -*-
from datetime import timedelta

from workalendar.core import LunarCalendar, WesternCalendar
from workalendar.core import EphemMixin


class Taiwan(EphemMixin, LunarCalendar, WesternCalendar):
    "Taiwan (Republic of China)"
    FIXED_HOLIDAYS = (
        LunarCalendar.FIXED_HOLIDAYS +
        WesternCalendar.FIXED_HOLIDAYS +
        (
            (2, 28, "228 Peace Memorial Day"),
            (4, 4, "Combination of Women's Day and Children's Day"),
            (10, 10, "National Day/Double Tenth Day"),
        )
    )

    def get_variable_days(self, year):
        days = super(Taiwan, self).get_variable_days(year)
        lunar_first_day = LunarCalendar.lunar(year, 1, 1)
        # Qingming begins when the sun reaches the celestial
        # longitude of 15° (usually around April 4th or 5th)
        qingming = EphemMixin.solar_term(self, year, 15, 'Asia/Taipei')

        days.extend([
            # a day before
            (lunar_first_day - timedelta(days=1), "Chinese New Year's Eve"),
            (lunar_first_day, "Chinese New Year"),
            # a day after
            (LunarCalendar.lunar(year, 1, 2), "Chinese New Year"),
            (LunarCalendar.lunar(year, 1, 3), "Chinese New Year"),
            (qingming, "Qingming Festival"),
            (LunarCalendar.lunar(year, 5, 5), "Dragon Boat Festival"),
            (LunarCalendar.lunar(year, 8, 15), "Mid-Autumn Festival"),
        ])
        return days
