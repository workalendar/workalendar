# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import timedelta, date

from ..core import WesternCalendar
from ..core import SUN, MON, FRI
from ..core import ChristianMixin
from ..exceptions import CalendarError
from ..registry import iso_register


@iso_register('ZA')
class SouthAfrica(WesternCalendar, ChristianMixin):
    "South Africa"
    include_good_friday = True
    include_christmas = True

    def holidays(self, year=None):
        if year < 1910:
            raise CalendarError("It's not possible to compute holidays prior"
                                " to 1910 for South Africa.")
        return super(SouthAfrica, self).holidays(year)

    def get_easter_monday_or_family_day(self, year):
        if year < 1980:
            label = "Easter Monday"
        else:
            label = "Family Day"
        return (self.get_easter_monday(year), label)

    def get_fixed_holidays(self, year):
        days = super(SouthAfrica, self).get_fixed_holidays(year)
        if year >= 1990:
            days.append((date(year, 3, 21), 'Human Rights Day'))

        # Van Riebeeck's day & Founder's day
        if year >= 1952 and year <= 1973:
            days.append((date(year, 4, 6), "Van Riebeeck's Day"))
        if year >= 1980 and year <= 1994:
            days.append((date(year, 4, 6), "Founder's Day"))

        if year >= 1994:
            days.append((date(year, 4, 27), "Freedom Day"))

        # Workers day established in 1995 to May 1st
        if year >= 1995:
            days.append((date(year, 5, 1), "Workers' Day"))

        if year <= 1951:
            days.append((date(year, 5, 24), "Victoria Day / Empire Day"))

        # May 31st: Union Day & Republic Day
        if year <= 1960:
            days.append((date(year, 5, 31), "Union Day"))
        elif year <= 1993:
            days.append((date(year, 5, 31), "Republic Day"))

        if year >= 1995:
            days.append((date(year, 6, 16), "Youth Day"))

        if year > 1960 and year <= 1973:
            days.append((date(year, 7, 10), "Family Day"))

        if year >= 1995:
            days.append((date(year, 8, 9), "National Women's Day"))
            days.append((date(year, 9, 24), "Heritage Day"))

        if year >= 1952 and year <= 1993:
            days.append((date(year, 10, 10), "Kruger Day"))

        if year <= 1951:
            december_16th_label = "Dingaan's Day"
        elif 1952 <= year <= 1979:
            december_16th_label = "Day of the Covenant"
        elif 1980 <= year <= 1994:
            december_16th_label = "Day of the Vow"
        else:
            december_16th_label = "Day of Reconciliation"
        days.append((date(year, 12, 16), december_16th_label))

        # Boxing day renamed
        boxing_day_label = "Boxing Day"
        if year >= 1980:
            boxing_day_label = "Day of Goodwill"
        days.append((date(year, 12, 26), boxing_day_label))

        return days

    def get_variable_days(self, year):
        days = super(SouthAfrica, self).get_variable_days(year)

        days.append(self.get_easter_monday_or_family_day(year))

        # Workers day was first friday of may 1987-1989
        if 1987 <= year <= 1989:
            days.append(
                (self.get_nth_weekday_in_month(year, 5, FRI), "Workers' Day")
            )

        if year <= 1993:
            days.append((self.get_ascension_thursday(year), "Ascension Day"))

        # Queen's Birthday on the 2nd Monday of july 1952-1960
        if 1952 <= year <= 1960:
            days.append((
                self.get_nth_weekday_in_month(year, 7, MON, 2),
                "Queen's Birthday"
            ))

        # King's Birthday on the first Monday of August 1910-1951
        if 1910 <= year <= 1951:
            days.append((
                self.get_nth_weekday_in_month(year, 8, MON),
                "King's Birthday"
            ))

        if year >= 1952 and year <= 1979:
            days.append((self.get_nth_weekday_in_month(year, 9, MON),
                         "Settlers' Day"))
        return days

    def get_calendar_holidays(self, year):
        days = super(SouthAfrica, self).get_calendar_holidays(year)
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
