# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('CH')
class Switzerland(WesternCalendar, ChristianMixin):
    name = 'Switzerland'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_christmas = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Berchtold's Day"),
        (5, 1, "Labour Day"),
        (8, 1, "National Holiday"),
    )


@iso_register('CH-VD')
class Vaud(Switzerland):
    name = 'Vaud'

    include_boxing_day = False
    include_federal_thanksgiving_monday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Berchtold's Day"),
        (8, 1, "National Holiday"),
    )

    def get_federal_thanksgiving_monday(self, year):
        "Monday following the 3rd sunday of September"
        september_1st = date(year, 9, 1)
        return (
            september_1st +
            (6 - september_1st.weekday()) * timedelta(days=1) +  # 1st sunday
            timedelta(days=15)  # Monday following 3rd sunday
        )

    def get_variable_days(self, year):
        days = super(Vaud, self).get_variable_days(year)
        if self.include_federal_thanksgiving_monday:
            days.append((self.get_federal_thanksgiving_monday(year),
                         "Federal Thanksgiving Monday"))
        return days
