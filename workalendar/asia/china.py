# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from datetime import date

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
    "China, holidays based on https://publicholidays.cn/, need update every year. Support 2018, 2019 currently."

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
        if year not in holidays.keys():
            raise CalendarError("It's not possible to compute holidays in {} for China. Need config.".format(year))
        return super(China, self).get_calendar_holidays(year)

    def get_variable_days(self, year):
        days = super(China, self).get_variable_days(year)
        # Spring Festival, eve, 1.1, and 1.2 - 1.6 in lunar day
        for i in range(2, 7):
            days.append((ChineseNewYearCalendar.lunar(year, 1, i), "Spring Festival"))
        # other holidays
        for holiday_name, day_list in holidays[year].items():
            for v in day_list:
                days.append((date(year, v[0], v[1]), holiday_name))
        return days

    def is_working_day(self, day):
        return super(China, self).is_working_day(day, self.extra_working_days)

    def add_working_days(self, day, delta):
        return super(China, self).add_working_days(day, delta, self.extra_working_days)

    def sub_working_days(self, day, delta):
        return super(China, self).sub_working_days(day, delta, self.extra_working_days)


if __name__ == '__main__':
    from datetime import timedelta

    print(len(China().holidays(2019)))
    c = China()
    count = 0
    s = date(2019, 1, 1)
    for i in range(365):
        t = s + timedelta(days=i)
        if c.is_working_day(t):
            count += 1
    print(count)
