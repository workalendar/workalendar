# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date
from gettext import gettext as _

from ..core import MON
from ..core import WesternCalendar
from ..astronomy import calculate_equinoxes
from ..registry_tools import iso_register


@iso_register('JP')
class Japan(WesternCalendar):
    "Japan"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 11, _("Foundation Day")),
        (4, 29, _("Showa Day")),
        (5, 3, _("Constitution Memorial Day")),
        (5, 4, _("Greenery Day")),
        (5, 5, _("Children's Day")),
        (11, 3, _("Culture Day")),
        (11, 23, _("Labour Thanksgiving Day")),
    )

    def get_fixed_holidays(self, year):
        """
        Fixed holidays for Japan.
        """
        days = super(Japan, self).get_fixed_holidays(year)
        if year >= 2016:
            days.append((date(year, 8, 11), "Mountain Day"))
        # Change in Emperor
        if year < 2019:
            days.append((date(year, 12, 23), "The Emperor's Birthday"))
        if year > 2019:
            days.append((date(year, 2, 23), "The Emperor's Birthday"))
        # Lots of adjustments for new emperor
        if year == 2019:
            days.extend([
                (date(year, 4, 30), _("Coronation Day")),
                (date(year, 5, 1), _("Coronation Day")),
                (date(year, 5, 2), _("Coronation Day")),
                (date(year, 5, 6), _("Children's Day Observed")),
                (date(year, 8, 12), _("Mountain Day Observed")),
                (date(year, 10, 22), _("Enthronement Ceremony Day")),
                (date(year, 11, 4), _("Culture Day Observed")),
            ])
        if year == 2020:
            days.extend([
                (date(year, 2, 24), _("The Emperor's Birthday Observed")),
                (date(year, 5, 6), _("Constitution Memorial Day Observed")),
                (date(year, 8, 10), _("Mountain Day")),
            ])
            # Mountain Day is 8/10 this year for some reason
            # The next year that will be different is 2024
            days.remove((date(year, 8, 11), _("Mountain Day")))
        return days

    def get_variable_days(self, year):
        # usual variable days
        days = super(Japan, self).get_variable_days(year)
        equinoxes = calculate_equinoxes(year, 'Asia/Tokyo')
        coming_of_age_day = Japan.get_nth_weekday_in_month(year, 1, MON, 2)
        marine_day = Japan.get_nth_weekday_in_month(year, 7, MON, 3)
        respect_for_the_aged = Japan.get_nth_weekday_in_month(year, 9, MON, 3)
        health_and_sport = Japan.get_nth_weekday_in_month(year, 10, MON, 2)
        days.extend([
            (coming_of_age_day, _('Coming of Age Day')),
            (marine_day, _("Marine Day")),
            (equinoxes[0], _("Vernal Equinox Day")),
            (respect_for_the_aged, _("Respect-for-the-Aged Day")),
            (equinoxes[1], _("Autumnal Equinox Day")),
            (health_and_sport, _("Health and Sports Day")),
        ])

        # Marine Day is on a Thursday in 2020 for some year
        # https://www.timeanddate.com/holidays/japan/sea-day
        # Health and Sports Day will continue on the 2nd monday
        # of October, except in 2020 when it will happen in July
        # https://www.timeanddate.com/holidays/japan/sports-day
        if year == 2020:
            days.remove((marine_day, _("Marine Day")))
            days.append((date(2020, 7, 23), _("Marine Day")))
            days.remove((health_and_sport, _("Health and Sports Day")))
            days.append((date(2020, 7, 24), _("Health and Sports Day")))
        return days


class JapanBank(Japan):
    """The Bank of Japan is closed additional days other than
    national holidays.
    https://www.boj.or.jp/en/about/outline/holi.htm/
    """

    FIXED_HOLIDAYS = Japan.FIXED_HOLIDAYS + (
        (1, 2, _("New Year Bank Holiday")),
        (1, 3, _("New Year Bank Holiday")),
        (12, 31, _("New Year Bank Holiday")),
    )
