# -*- coding: utf-8 -*-
from datetime import date, timedelta

from workalendar.core import LunarCalendar, WesternCalendar, Calendar
from workalendar.core import MON, FRI, SAT, IslamicMixin, EphemMixin


class SouthKorea(LunarCalendar):
    "South Korea"
    FIXED_HOLIDAYS = LunarCalendar.FIXED_HOLIDAYS + (
        (3, 1, "Independence Day"),
        (5, 5, "Children's Day"),
        (6, 6, "Memorial Day"),
        (8, 15, "Liberation Day"),
        (10, 3, "National Foundation Day"),
        (10, 9, "Hangul Day"),
        (12, 25, "Christmas Day"),
    )

    def get_variable_days(self, year):
        lunar_first_day = LunarCalendar.lunar(year, 1, 1)
        days = [
            # new year (3 days)
            (lunar_first_day, "Korean New Year's Day"),
            # a day before
            (lunar_first_day - timedelta(days=1), "Korean New Year's Day"),
            # a day after
            (LunarCalendar.lunar(year, 1, 2), "Korean New Year's Day"),
            (LunarCalendar.lunar(year, 4, 8), "Buddha's Birthday"),
            # Midautumn Festival (3 days)
            (LunarCalendar.lunar(year, 8, 14), "Midautumn Festival"),
            (LunarCalendar.lunar(year, 8, 15), "Midautumn Festival"),
            (LunarCalendar.lunar(year, 8, 16), "Midautumn Festival"),
        ]
        return days


class Japan(WesternCalendar, EphemMixin):
    "Japan"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 11, "Foundation Day"),
        (4, 29, "Showa Day"),
        (5, 3, "Constitution Memorial Day"),
        (5, 4, "Greenery Day"),
        (5, 5, "Children's Day"),
        (11, 3, "Culture Day"),
        (11, 23, "Labour Thanksgiving Day"),
        (12, 23, "The Emperor's Birthday"),
    )

    def get_fixed_holidays(self, year):
        """
        Fixed holidays for Japan.

        As of 2016, the "Mountain Day is being added"
        """
        days = super(Japan, self).get_fixed_holidays(year)
        if year >= 2016:
            days.append((date(year, 8, 11), "Mountain Day"))
        return days

    def get_variable_days(self, year):
        # usual variable days

        equinoxes = self.calculate_equinoxes(year, 'Asia/Tokyo')

        days = super(Japan, self).get_variable_days(year)
        days += [
            (Japan.get_nth_weekday_in_month(year, 1, MON, 2),
                'Coming of Age Day'),

            (Japan.get_nth_weekday_in_month(year, 7, MON, 3),
                "Marine Day"),

            (equinoxes[0], "Vernal Equinox Day"),

            (Japan.get_nth_weekday_in_month(year, 9, MON, 3),
                "Respect-for-the-Aged Day"),

            (equinoxes[1], "Autumnal Equinox Day"),

            (Japan.get_nth_weekday_in_month(year, 10, MON, 2),
                "Health and Sports Day"),
        ]

        return days


class Qatar(IslamicMixin, Calendar):
    "Qatar"
    WEEKEND_DAYS = (FRI, SAT)

    FIXED_HOLIDAYS = (
        (12, 18, "National Day"),
    )
    include_start_ramadan = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 4
    include_eid_al_adha = True
    length_eid_al_adha = 4


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
        lunar_first_day = LunarCalendar.lunar(year, 1, 1)

        # Qingming begins when the sun reaches the celestial
        # longitude of 15° (usually around April 4th or 5th)
        qingming = EphemMixin.solar_term(self, year, 15, 'Asia/Taipei')

        days = super(Taiwan, self).get_variable_days(year)
        days += [
            # a day before
            (lunar_first_day - timedelta(days=1), "Chinese New Year's Eve"),
            (lunar_first_day, "Chinese New Year"),
            # a day after
            (LunarCalendar.lunar(year, 1, 2), "Chinese New Year"),
            (LunarCalendar.lunar(year, 1, 3), "Chinese New Year"),
            (qingming, "Qingming Festival"),
            (LunarCalendar.lunar(year, 5, 5), "Dragon Boat Festival"),
            (LunarCalendar.lunar(year, 8, 15), "Mid-Autumn Festival"),
        ]
        return days
