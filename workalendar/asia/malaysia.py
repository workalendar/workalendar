# -*- coding: utf-8 -*-
from copy import copy
from datetime import date, timedelta

from workalendar.core import LunarCalendar, WesternCalendar
from workalendar.core import SUN, IslamicMixin


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
