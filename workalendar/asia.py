# -*- coding: utf-8 -*-
from datetime import date, timedelta

from workalendar.core import LunarCalendar, WesternCalendar, Calendar
from workalendar.core import (
    MON, FRI, SAT, SUN, ChristianMixin, IslamicMixin, EphemMixin
)


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


class Singapore(WesternCalendar, ChristianMixin, IslamicMixin):
    "Singapore"
    include_good_friday = True
    shift_sunday_holidays = True
    include_eid_al_fitr = True
    eid_al_fitr_label = "Hari Raya Puasa"
    include_day_of_sacrifice = True
    day_of_sacrifice_label = "Hari Raya Haji"

    # All holidays in Singapore will roll on a Sunday
    FIXED_HOLIDAYS = ()

    # Diwali/Deepavali is sometimes celebrated on a different day to India
    # so this can't be put into a HinduMixin
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
        2013: date(2013, 11, 2),
        2014: date(2014, 10, 22),
        2015: date(2015, 11, 10),
        2016: date(2016, 10, 29),
        2017: date(2017, 10, 18),
        2018: date(2018, 11, 6)  # This might change
    }

    def get_variable_days(self, year):
        # Call super on all parents
        days = []
        pre_shifted_days = super(Singapore, self).get_variable_days(year)
        pre_shifted_days += [
            (LunarCalendar.lunar(year, 1, 1), "Chinese New Year"),
            (LunarCalendar.lunar(year, 1, 2), "Chinese New Year"),
            (LunarCalendar.lunar(year, 4, 15), "Vesak Day")
        ]
        pre_shifted_days += [(date(year, 1, 1), "New Year"),
                             (date(year, 5, 1), "Labour Day"),
                             (date(year, 8, 9), "National Day")]
        # Singapore rolls all Sunday holidays.
        # I feel this should be baked deeper in the class hierarchy
        for holiday, label in pre_shifted_days:
            if holiday.weekday() == SUN:
                day = (
                    self.find_following_working_day(holiday),
                    label + ' shift'
                )
            else:
                day = (holiday, label)
            days.append(day)

        # Add in Deepavali (hardcoded dates, so no need to shift)
        deepavali = self.DEEPAVALI.get(year)
        if not deepavali:
            msg = 'Missing date for Singapore Deepavali for year: %s' % year
            raise KeyError(msg)
        days.append((deepavali, 'Deepavali'))
        return days


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
