# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta
from workalendar.core import WesternCalendar, ChristianMixin
from ..registry_tools import iso_register


@iso_register('DK')
class Denmark(WesternCalendar, ChristianMixin):
    'Denmark'

    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost Sunday"
    include_whit_monday = True
    whit_monday_label = "Pentecost Monday"
    include_boxing_day = True
    boxing_day_label = "Second Day of Christmas"

    def get_store_bededag(self, year):  # 'great prayer day'
        easter_sunday = self.get_easter_sunday(year)
        return easter_sunday + timedelta(days=26)

    def get_variable_days(self, year):
        days = super(Denmark, self).get_variable_days(year)
        days.append((self.get_store_bededag(year), "Store Bededag"))
        return days
