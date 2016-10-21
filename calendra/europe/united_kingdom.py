# -*- coding: utf-8 -*-
from datetime import date

from dateutil import relativedelta as rd

from ..core import WesternCalendar, ChristianMixin
from ..core import Holiday


class UnitedKingdom(WesternCalendar, ChristianMixin):
    "United Kingdom"
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_boxing_day = True
    shift_new_years_day = True

    def get_variable_days(self, year):
        days = super(UnitedKingdom, self).get_variable_days(year)
        days += [
            Holiday(
                date(year, 5, 1) + rd.relativedelta(weekday=rd.MO(1)),
                "Early May Bank Holiday",
                indication="1st Monday in May",
            ),
            Holiday(
                date(year, 5, 30) + rd.relativedelta(weekday=rd.MO(-1)),
                "Spring Bank Holiday",
                indication="Last Monday in May",
            ),
            Holiday(
                date(year, 8, 31) + rd.relativedelta(weekday=rd.MO(-1)),
                "Late Summer Bank Holiday",
                indication="Last Monday in August",
            ),
        ]
        return days


class UnitedKingdomNorthernIreland(UnitedKingdom):
    "Northern Ireland (UK)"
    def get_variable_days(self, year):
        days = super(UnitedKingdomNorthernIreland, self) \
            .get_variable_days(year)
        # St Patrick's day
        st_patrick = date(year, 3, 17)
        days.append((st_patrick, "Saint Patrick's Day"))
        if st_patrick.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(st_patrick),
                "Saint Patrick substitute"))

        # Battle of boyne
        battle_of_boyne = date(year, 7, 12)
        days.append((battle_of_boyne, "Battle of the Boyne"))
        if battle_of_boyne.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(battle_of_boyne),
                "Battle of the Boyne substitute"))
        return days
