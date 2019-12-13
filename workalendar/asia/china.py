# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date
import warnings
from gettext import gettext as _

from ..core import ChineseNewYearCalendar, WesternCalendar
from ..registry_tools import iso_register
from ..exceptions import CalendarError

holidays = {
    2018:
        {
            _('Ching Ming Festival'): [(4, 5), (4, 6), (4, 7)],
            _('Labour Day Holiday'): [(4, 29), (4, 30), (5, 1)],
            _('Dragon Boat Festival'): [(6, 18)],
            _('Mid-Autumn Festival'): [(9, 24)],
            _('New year'): [(12, 30), (12, 31)]
        },
    2019:
        {
            _('Ching Ming Festival'): [(4, 5)],
            _('Labour Day Holiday'): [(5, 1), (5, 2), (5, 3)],
            _('Dragon Boat Festival'): [(6, 7)],
            _('Mid-Autumn Festival'): [(9, 13)]
        },
    2020:
        {
            _('Ching Ming Festival'): [(4, 4), (4, 5), (4, 6)],
            _('Labour Day Holiday'): [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)],
            _('Dragon Boat Festival'): [(6, 25), (6, 26), (6, 27)],
            _('National Day'): [(10, 8)]
        },
}

workdays = {
    2018:
        {
            _('Spring Festival Shift'): [(2, 11), (2, 24)],
            _('Ching Ming Festival Shift'): [(4, 8)],
            _('Labour Day Holiday Shift'): [(4, 28)],
            _('National Day Shift'): [(9, 29), (9, 30)],
            _('New year Shift'): [(12, 29)]
        },
    2019:
        {
            _('Spring Festival Shift'): [(2, 2), (2, 3)],
            _('Labour Day Holiday Shift'): [(4, 28), (5, 5)],
            _('National Day Shift'): [(9, 29), (10, 12)],
        },
    2020:
        {
            _('Spring Festival Shift'): [(1, 19), (2, 1)],
            _('Labour Day Holiday Shift'): [(4, 26), (5, 9)],
            _('Dragon Boat Festival Shift'): [(6, 28)],
            _('National Day Shift'): [(9, 27), (10, 10)]
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

    def __init__(self, *args, **kwargs):
        super(China, self).__init__(*args, **kwargs)
        self.extra_working_days = []
        for year, data in workdays.items():
            for holiday_name, day_list in data.items():
                for v in day_list:
                    self.extra_working_days.append(date(year, v[0], v[1]))

    def get_calendar_holidays(self, year):
        warnings.warn(
            "Support 2018, 2019, 2020 currently, need update every year."
        )
        if year not in holidays.keys():
            msg = "Need configure {} for China.".format(year)
            raise CalendarError(msg)
        return super(China, self).get_calendar_holidays(year)

    def get_variable_days(self, year):
        days = super(China, self).get_variable_days(year)
        # Spring Festival, eve, 1.1, and 1.2 - 1.6 in lunar day
        for i in range(2, 7):
            days.append((ChineseNewYearCalendar.lunar(year, 1, i),
                         _("Spring Festival")))
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
