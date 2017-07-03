# -*- coding: utf-8 -*-

from datetime import timedelta

from workalendar.core import ChineseNewYearCalendar, WesternCalendar
from workalendar.core import ChristianMixin, EphemMixin


class HongKong(EphemMixin, WesternCalendar,
               ChineseNewYearCalendar, ChristianMixin):
    "Hong Kong"
    include_good_friday = True
    include_easter_saturday = True
    include_easter_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (7, 1, "SAR Establishment Day"),
        (10, 1, "National Day"),
    )

    chinese_new_year_label = "Chinese Lunar New Year's Day"
    include_chinese_second_day = True
    chinese_second_day_label = "Second day of Chinese Lunar New Year"
    include_chinese_third_day = True
    chinese_third_day_label = "Third day of Chinese Lunar New Year"
    shift_sunday_holidays = True  # Except CNY which rolls to Saturday
    shift_start_cny_sunday = False  # Prior to 2011 this was True

    def get_variable_days(self, year):
        """
        Hong Kong variable days
        """

        # Prior to the "General Holidays and Employment Legislation
        # (Substitution of Holidays)(Amendment) Ordinance 2011", the first day
        # of CNY rolled to a Sat if it was on a Sun.  After the Amendment, it
        # rolls to the following Wed
        if year < 2011:
            self.shift_start_cny_sunday = True

        days = super(HongKong, self).get_variable_days(year)
        chingming = EphemMixin.solar_term(self, year, 15, 'Asia/Hong_Kong')
        dupe_holiday = [chingming for day in days if chingming == day[0]]
        if dupe_holiday:
            # Roll Chingming forward a day as it clashes with another holiday
            chingming = chingming + timedelta(days=1)
        mid_autumn_label = "Day After Mid-Autumn Festival"
        days.extend([
            (ChineseNewYearCalendar.lunar(year, 4, 8), "Buddha's Birthday"),
            (chingming, "Ching Ming Festival"),
            (ChineseNewYearCalendar.lunar(year, 5, 5), "Tuen Ng Festival"),
            (ChineseNewYearCalendar.lunar(year, 8, 16), mid_autumn_label),
            (ChineseNewYearCalendar.lunar(year, 9, 9), "Chung Yeung Festival"),
        ])

        # Boxing day & XMas shift
        shifts = self.shift_christmas_boxing_days(year=year)
        days.extend(shifts)

        return days
