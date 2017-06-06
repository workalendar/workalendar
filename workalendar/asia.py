# -*- coding: utf-8 -*-
from copy import copy
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


class Malaysia(LunarCalendar, WesternCalendar, IslamicMixin):
    "Malaysia"
    include_nuzul_al_quran = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 2
    eid_al_fitr_label = "Hari Raya Puasa"
    include_day_of_sacrifice = True
    day_of_sacrifice_label = "Hari Raya Haji"
    include_islamic_new_year = True
    include_prophet_birthday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 1, "Federal Territory Day"),
        (5, 1, "Workers' Day"),
        (8, 31, "National Day"),
        (9, 16, "Malaysia Day"),
        (12, 25, "Christmas Day"),
    )

    MSIA_DEEPAVALI = {
        2010: date(2010, 11, 5),
        2011: date(2011, 10, 26),
        2012: date(2012, 11, 13),
        2013: date(2013, 11, 2),
        2014: date(2014, 10, 22),
        2015: date(2015, 11, 10),
        2016: date(2016, 10, 29),
        2017: date(2017, 10, 18),
        2018: date(2018, 11, 7),   # This might change
        2019: date(2019, 10, 27),  # This might change
        2020: date(2020, 11, 14),  # This might change
    }

    MSIA_THAIPUSAM = {
        2010: date(2010, 1, 30),
        2011: date(2011, 1, 20),
        2012: date(2012, 2, 7),
        2013: date(2013, 1, 28),
        2014: date(2014, 1, 17),
        2015: date(2015, 2, 3),
        2016: date(2016, 1, 25),
        2017: date(2017, 2, 9),
        2018: date(2018, 1, 31),   # This might change
    }

    # Following code is largely borrowed from Singapore class.
    # (Like Singapore, Malaysia rolls all PHs falling on Sundays.)
    def get_chinese_new_year(self, year):
        """
        Compute Chinese New Year days. To return a list of holidays
        * If the CNY1 falls on MON-FRI, there's not shift.
        * If the CNY1 falls on SAT, the CNY2 is shifted to the Monday after.
        * If the CNY1 falls on SUN, the CNY1 is shifted to the Monday after,
          and CNY2 is shifted to the Tuesday after.
        """
        new_year_day_1 = LunarCalendar.lunar(year, 1, 1)
        new_year_day_2 = LunarCalendar.lunar(year, 1, 2)
        days = [
            (new_year_day_1, "First Day of Lunar New Year"),
            (new_year_day_2, "Second Day of Lunar New Year"),
        ]
        if new_year_day_1.weekday() == SUN:
            days.append(
                (new_year_day_2 + timedelta(days=1),
                 "Second day of Chinese Lunar New Year shift"),
            )
        return days

    def get_shifted_holidays(self, dates):
        for holiday, label in dates:
            if holiday.weekday() == SUN:
                yield (
                    holiday + timedelta(days=1),
                    label + ' shift'
                )

    def get_variable_days(self, year):
        """
        Malaysia variable days
        """
        days = super(Malaysia, self).get_variable_days(year)

        # The `get_shifted_holidays` method will take care of the shifts.
        for day in self.get_chinese_new_year(year):
            days.append(day)

        # Vesak Day
        days.append(
            (LunarCalendar.lunar(year, 4, 15), "Vesak Day"),
        )

        # Add in Deepavali and Thaipusam (hardcoded dates, so no need to shift)
        msia_deepavali = self.MSIA_DEEPAVALI.get(year)
        if not msia_deepavali:
            mdmsg = 'Missing date for Malaysia Deepavali for year: %s' % year
            raise KeyError(mdmsg)
        days.append((msia_deepavali, 'Deepavali'))

        msia_thaipusam = self.MSIA_THAIPUSAM.get(year)
        if not msia_thaipusam:
            mtmsg = 'Missing date for Malaysia Thaipusam for year: %s' % year
            raise KeyError(mtmsg)
        days.append((msia_thaipusam, 'Thaipusam'))
        return days

    def get_calendar_holidays(self, year):
        """
        In Malaysia, any holiday that fall on SUN is shifted to the next
        available working day.
        """
        # Unshifted days are here:
        days = super(Malaysia, self).get_calendar_holidays(year)
        days_to_inspect = copy(days)
        for day_shifted in self.get_shifted_holidays(days_to_inspect):
            days.append(day_shifted)
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
    include_eid_al_fitr = True
    eid_al_fitr_label = "Hari Raya Puasa"
    include_day_of_sacrifice = True
    day_of_sacrifice_label = "Hari Raya Haji"

    # All holidays in Singapore will roll on a Sunday
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (8, 9, "National Day"),
    )

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
        2013: date(2013, 11, 3),
        2014: date(2014, 10, 22),
        2015: date(2015, 11, 10),
        2016: date(2016, 10, 29),
        2017: date(2017, 10, 18),
        2018: date(2018, 11, 6)  # This might change
    }

    def get_chinese_new_year(self, year):
        """
        Compute Chinese New Year days. To return a list of holidays

        * If the CNY1 falls on MON-FRI, there's not shift.
        * If the CNY1 falls on SAT, the CNY2 is shifted to the Monday after.
        * If the CNY1 falls on SUN, the CNY1 is shifted to the Monday after,
          and CNY2 is shifted to the Tuesday after.
        """
        new_year_day_1 = LunarCalendar.lunar(year, 1, 1)
        new_year_day_2 = LunarCalendar.lunar(year, 1, 2)
        days = [
            (new_year_day_1, "Chinese Lunar New Year's Day"),
            (new_year_day_2, "Second day of Chinese Lunar New Year"),
        ]
        if new_year_day_1.weekday() == SUN:
            days.append(
                (new_year_day_2 + timedelta(days=1),
                 "Second day of Chinese Lunar New Year shift"),
            )
        return days

    def get_shifted_holidays(self, dates):
        # Singapore rolls all Sunday holidays.
        # I feel this should be baked deeper in the class hierarchy
        for holiday, label in dates:
            if holiday.weekday() == SUN:
                yield (
                    holiday + timedelta(days=1),
                    label + ' shift'
                )

    def get_variable_days(self, year):
        """
        Singapore variable days
        """
        days = super(Singapore, self).get_variable_days(year)

        # The `get_shifted_holidays` method will take care of the shifts.
        for day in self.get_chinese_new_year(year):
            days.append(day)

        # Vesak Day
        days.append(
            (LunarCalendar.lunar(year, 4, 15), "Vesak Day"),
        )

        # Add in Deepavali (hardcoded dates, so no need to shift)
        deepavali = self.DEEPAVALI.get(year)
        if not deepavali:
            msg = 'Missing date for Singapore Deepavali for year: %s' % year
            raise KeyError(msg)
        days.append((deepavali, 'Deepavali'))
        return days

    def get_calendar_holidays(self, year):
        """
        In Singapore, any holiday that fall on SUN is shifted to the next
        available working day.
        """
        # Unshifted days are here:
        days = super(Singapore, self).get_calendar_holidays(year)
        days_to_inspect = copy(days)
        for day_shifted in self.get_shifted_holidays(days_to_inspect):
            days.append(day_shifted)
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
