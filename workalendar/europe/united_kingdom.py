# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON
from workalendar.registry import iso_register


@iso_register('GB')
class UnitedKingdom(WesternCalendar, ChristianMixin):
    'United Kingdom'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_boxing_day = True
    shift_new_years_day = True

    def get_early_may_bank_holiday(self, year):
        return (
            UnitedKingdom.get_nth_weekday_in_month(year, 5, MON),
            "Early May Bank Holiday"
        )

    def get_spring_bank_holiday(self, year):
        return (
            UnitedKingdom.get_last_weekday_in_month(year, 5, MON),
            "Spring Bank Holiday"
        )

    def get_late_summer_bank_holiday(self, year):
        return (
            UnitedKingdom.get_last_weekday_in_month(year, 8, MON),
            "Late Summer Bank Holiday"
        )

    def get_variable_days(self, year):
        days = super(UnitedKingdom, self).get_variable_days(year)
        days.append(self.get_early_may_bank_holiday(year))
        days.append(self.get_spring_bank_holiday(year))
        days.append(self.get_late_summer_bank_holiday(year))
        # Boxing day & XMas shift
        shifts = self.shift_christmas_boxing_days(year=year)
        days.extend(shifts)
        return days


@iso_register('GB-NIR')
class UnitedKingdomNorthernIreland(UnitedKingdom):
    'Northern Ireland'

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
