# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from gettext import gettext as _
from ..core import WesternCalendar, ChristianMixin
from ..core import FRI
from ..registry_tools import iso_register


@iso_register('MH')
class MarshallIslands(WesternCalendar, ChristianMixin):
    "Marshall Islands"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 3, _("Remembrance Day")),
        (5, 1, _("Constitution Day")),
        (11, 17, _("Presidents' Day")),
        (12, 31, _("New Year's Eve")),
    )
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(MarshallIslands, self).get_variable_days(year)
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 7, FRI),
            _("Fishermen's Holiday")
        ))
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 9, FRI),
            _("Labour Day")
        ))
        days.append((
            MarshallIslands.get_last_weekday_in_month(year, 9, FRI),
            _("Manit Day")
        ))
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 12, FRI),
            _("Gospel Day")
        ))
        return days
