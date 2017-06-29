# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import timedelta, date
from workalendar.core import WesternCalendar
from workalendar.core import SUN, MON
from workalendar.core import ChristianMixin


class SouthAfrica(WesternCalendar, ChristianMixin):
    "South Africa"
    include_good_friday = True
    include_easter_monday = True
    include_christmas = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Workers Day"),
        (12, 16, "Day of reconcilation"),
    )

    def get_family_day(self, year):
        return (self.get_good_friday(year), "Family Day")

    def get_fixed_holidays(self, year):
        days = super(SouthAfrica, self).get_fixed_holidays(year)
        if year < 1952:
            days.append((date(year, 5, 24), "Empire Day"))
        if year >= 1952 and year <= 1974:
            days.append((date(year, 4, 6), "Van Riebeeck's Day"))
        if year >= 1952 and year <= 1979:
            days.append((self.get_nth_weekday_in_month(year, 9, MON, 1),
                         "Settlers' Day"))
        if year >= 1952 and year <= 1993:
            days.append((date(year, 10, 10), "Kruger Day"))
        if year <= 1960:
            days.append((date(year, 5, 31), "Union Day"))
        if year > 1960 and year <= 1993:
            days.append((date(year, 5, 31), "Republic Day"))
        if year > 1960 and year <= 1974:
            days.append((date(year, 7, 10), "Family Day"))
        if year >= 1980 and year <= 1994:
            days.append((date(year, 4, 6), "Founder's Day"))
        if year >= 1990:
            days.append((date(year, 3, 21), 'Human Rights Day'))
        if year <= 1993:
            days.append((self.get_ascension_thursday(year), "Ascension Day"))
        if year >= 1994:
            days.append((date(year, 4, 27), "Freedom Day"))
            days.append((date(year, 12, 26), "Day of good will"))
        if year >= 1995:
            days.append((date(year, 6, 16), "Youth Day"))
            days.append((date(year, 8, 9), "National Women Day"))
            days.append((date(year, 9, 24), "Heritage Day"))

        return days

    def get_variable_days(self, year):
        days = super(SouthAfrica, self).get_variable_days(year)
        days.append(self.get_family_day(year))
        days += self.get_fixed_holidays(year)
        # compute shifting days
        for holiday, label in days:
            if holiday.weekday() == SUN:
                days.append((
                    holiday + timedelta(days=1),
                    "%s substitute" % label
                ))

        # Other one-offs. Don't shift these
        if year == 1999:
            days.append((date(year, 6, 2), "National Elections"))
            days.append((date(year, 12, 31), "Y2K"))
        if year == 2000:
            # 2 January 2000 public holidays to accommodate the Y2K changeover,
            # 3 January 2000 because the previous holiday was a Sunday
            days.append((date(year, 1, 2), "Y2K"))
            days.append((date(year, 1, 3), "Y2K"))
        if year == 2001:
            days.append((date(year, 1, 2), "Y2K"))
        if year == 2004:
            days.append((date(year, 4, 14), "National Elections"))
        if year == 2006:
            days.append((date(year, 3, 1), "Local Elections"))
        if year == 2008:
            # 2 May 2008 was declared a public holiday when Human Rights Day
            # and Good Friday coincided on 21 March 2008
            days.append((date(year, 5, 2), "Special Human Rights"))
        if year == 2009:
            days.append((date(year, 4, 22), "National Elections"))
        if year == 2011:
            days.append((date(year, 5, 18), "Local Elections"))
            days.append((date(year, 12, 27), "Special Day of Goodwill"))
        if year == 2014:
            days.append((date(year, 5, 7), "National Elections"))
        if year == 2016:
            days.append((date(year, 8, 3), "Local Elections"))

        return days
