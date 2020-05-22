from datetime import date, timedelta

from ..core import (
    ChineseNewYearCalendar, WesternCalendar, ChristianMixin,
    SUN, SAT
)
from ..astronomy import solar_term
from ..registry_tools import iso_register


@iso_register('HK')
class HongKong(WesternCalendar, ChineseNewYearCalendar, ChristianMixin):
    "Hong Kong"
    include_good_friday = True
    include_easter_saturday = True
    include_easter_monday = True
    include_boxing_day = True

    WEEKEND_DAYS = (SUN,)

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

        days = super().get_variable_days(year)
        chingming = solar_term(year, 15, 'Asia/Hong_Kong')
        solar_term_chingming = chingming
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

        # All holidays that fall on SUN are shifted in
        # ``ChineseNewYearCalendar.get_calendar_holidays()``
        # Special case for Boxing Day.
        # If Christmas day is on SUN, the December 27th is also a holiday
        if date(year, 12, 25).weekday() == SUN:
            days.append(
                (date(year, 12, 27), "The second weekday after Christmas")
            )

        # Special case when Ching Ming and Easter overlap
        # Ching Ming is shifted to easter monday (but it's handled elsewhere)
        # Easter Monday is also shifted
        easter_sunday = self.get_easter_sunday(year)
        if easter_sunday == solar_term_chingming:
            days.append((
                easter_sunday + timedelta(days=2),
                "The day following Easter Monday"
            ))
        return days


class HongKongBank(HongKong):
    "Hong Kong Bank"
    WEEKEND_DAYS = (SAT, SUN)
