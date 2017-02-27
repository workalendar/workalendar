# -*- coding: utf-8 -*-
from datetime import timedelta, date

from workalendar.core import SUN
from workalendar.core import WesternCalendar
from workalendar.core import ChristianMixin


class SouthAfrica(WesternCalendar, ChristianMixin):
    "South Africa"
    include_good_friday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 21, 'Human Rights Day'),
        (4, 27, "Freedom Day"),
        (5, 1, "Workers Day"),
        (6, 16, "Youth Day"),
        (8, 9, "National Women Day"),
        (9, 24, "Heritage Day"),
        (12, 16, "Day of reconcilation"),
        (12, 26, "Day of good will"),
    )

    def get_family_day(self, year):
        return (self.get_good_friday(year), "Family Day")

    def get_variable_days(self, year):
        days = super(SouthAfrica, self).get_variable_days(year)
        days.append(self.get_family_day(year))
        # compute shifting days
        for month, day, label in self.FIXED_HOLIDAYS:
            holiday = date(year, month, day)
            if holiday.weekday() == SUN:
                days.append((
                    holiday + timedelta(days=1),
                    "%s substitute" % label
                ))
        return days
