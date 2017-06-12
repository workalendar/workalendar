# -*- coding: utf-8 -*-
from datetime import date

from workalendar.core import MON, EphemMixin
from workalendar.core import WesternCalendar


class Japan(WesternCalendar, EphemMixin):
    "Japan"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 11, "Foundation Day"),
        (4, 29, "Showa Day"),
        (5, 3, "Constitution Memorial Day"),
        (5, 4, "Greenery Day"),
        (5, 5, "Children's Day"),
        (11, 3, "Culture Day"),
        (11, 23, "Labour Thanksgiving Day"),
        (12, 23, "The Emperor's Birthday"),
    )

    def get_fixed_holidays(self, year):
        """
        Fixed holidays for Japan.

        As of 2016, the "Mountain Day is being added"
        """
        days = super(Japan, self).get_fixed_holidays(year)
        if year >= 2016:
            days.append((date(year, 8, 11), "Mountain Day"))
        return days

    def get_variable_days(self, year):
        # usual variable days
        days = super(Japan, self).get_variable_days(year)
        equinoxes = self.calculate_equinoxes(year, 'Asia/Tokyo')
        coming_of_age_day = Japan.get_nth_weekday_in_month(year, 1, MON, 2)
        marine_day = Japan.get_nth_weekday_in_month(year, 7, MON, 3)
        respect_for_the_aged = Japan.get_nth_weekday_in_month(year, 9, MON, 3)
        health_and_sport = Japan.get_nth_weekday_in_month(year, 10, MON, 2)
        days.extend([
            (coming_of_age_day, 'Coming of Age Day'),
            (marine_day, "Marine Day"),
            (equinoxes[0], "Vernal Equinox Day"),
            (respect_for_the_aged, "Respect-for-the-Aged Day"),
            (equinoxes[1], "Autumnal Equinox Day"),
            (health_and_sport, "Health and Sports Day"),
        ])
        return days
