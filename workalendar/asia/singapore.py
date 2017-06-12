# -*- coding: utf-8 -*-
from copy import copy
from datetime import date, timedelta

from workalendar.core import LunarCalendar, WesternCalendar
from workalendar.core import (
    SUN, ChristianMixin, IslamicMixin
)


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
