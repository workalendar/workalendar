# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date
import warnings

from ..core import ChineseNewYearCalendar, WesternCalendar
from ..registry import iso_register
from ..exceptions import CalendarError

holidays = {
    2018:
        {
            'Ching Ming Festival': [(4, 5), (4, 6), (4, 7)],
            'Labour Day Holiday': [(4, 29), (4, 30), (5, 1)],
            'Dragon Boat Festival': [(6, 18)],
            'Mid-Autumn Festival': [(9, 24)],
            'New year': [(12, 30), (12, 31)]
        },
    2019:
        {
            'Ching Ming Festival': [(4, 5)],
            'Labour Day Holiday': [(5, 1)],
            'Dragon Boat Festival': [(6, 7)],
            'Mid-Autumn Festival': [(9, 13)]
        },
}

workdays = {
    2018:
        {
            'Spring Festival Shift': [(2, 11), (2, 24)],
            'Ching Ming Festival Shift': [(4, 8)],
            'Labour Day Holiday Shift': [(4, 28)],
            'National Day Shift': [(9, 29), (9, 30)],
            'New year Shift': [(12, 29)]
        },
    2019:
        {
            'Spring Festival Shift': [(2, 2), (2, 3)],
            'National Day Shift': [(9, 29), (10, 12)],
        },
}


@iso_register('CN')
class China(ChineseNewYearCalendar, WesternCalendar):
    "China"
    # WARNING: Support 2018, 2019 currently, need update every year.
    # National Days, 10.1 - 10.7
    national_days = [(10, i, "National Day") for i in range(1, 8)]
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + tuple(national_days)

    include_chinese_new_year_eve = True

    extra_working_days = []
    for year, data in workdays.items():
        for holiday_name, day_list in data.items():
            for v in day_list:
                extra_working_days.append(date(year, v[0], v[1]))

    def get_calendar_holidays(self, year):
        warnings.warn("Support 2018, 2019 currently, need update every year.")
        if year not in holidays.keys():
            msg = "Need configure {} for China.".format(year)
            raise CalendarError(msg)
        return super(China, self).get_calendar_holidays(year)

    def get_variable_days(self, year):
        days = super(China, self).get_variable_days(year)
        # Spring Festival, eve, 1.1, and 1.2 - 1.6 in lunar day
        for i in range(2, 7):
            days.append((ChineseNewYearCalendar.lunar(year, 1, i),
                         "Spring Festival"))
        # other holidays
        for holiday_name, day_list in holidays[year].items():
            for v in day_list:
                days.append((date(year, v[0], v[1]), holiday_name))
        return days

    def is_working_day(self, day,
                       extra_working_days=None, extra_holidays=None):
        extra_working_days = extra_working_days or self.extra_working_days
        return super(China, self).is_working_day(day, extra_working_days,
                                                 extra_holidays)

    def add_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        extra_working_days = extra_working_days or self.extra_working_days
        return super(China, self).add_working_days(day, delta,
                                                   extra_working_days,
                                                   extra_holidays,
                                                   keep_datetime)

    def sub_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        extra_working_days = extra_working_days or self.extra_working_days
        return super(China, self).sub_working_days(day, delta,
                                                   extra_working_days,
                                                   extra_holidays,
                                                   keep_datetime)
