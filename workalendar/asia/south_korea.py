# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from gettext import gettext as _
from ..core import ChineseNewYearCalendar, WesternCalendar
from ..registry_tools import iso_register


@iso_register('KR')
class SouthKorea(WesternCalendar, ChineseNewYearCalendar):
    "South Korea"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 1, _("Independence Day")),
        (5, 5, _("Children's Day")),
        (6, 6, _("Memorial Day")),
        (8, 15, _("Liberation Day")),
        (10, 3, _("National Foundation Day")),
        (10, 9, _("Hangul Day")),
        (12, 25, _("Christmas Day")),
    )
    chinese_new_year_label = _("Korean New Year's Day")
    include_chinese_new_year_eve = True
    chinese_new_year_eve_label = _("Korean New Year's Day")
    include_chinese_second_day = True
    chinese_second_day_label = _("Korean New Year's Day")

    def get_variable_days(self, year):
        days = super(SouthKorea, self).get_variable_days(year)
        days.extend([
            (ChineseNewYearCalendar.lunar(year, 4, 8), _("Buddha's Birthday")),
            # Midautumn Festival (3 days)
            (ChineseNewYearCalendar.lunar(year, 8, 14),
             _("Midautumn Festival")),
            (ChineseNewYearCalendar.lunar(year, 8, 15),
             _("Midautumn Festival")),
            (ChineseNewYearCalendar.lunar(year, 8, 16),
             _("Midautumn Festival")),
        ])
        return days
