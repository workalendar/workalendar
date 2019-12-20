from datetime import date
from ..core import WesternCalendar, ChristianMixin, MON
from ..registry_tools import iso_register


@iso_register('GB')
class UnitedKingdom(WesternCalendar, ChristianMixin):
    'United Kingdom'

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_boxing_day = True
    shift_new_years_day = True
    non_computable_holiday_dict = {
        1973: [(date(1973, 11, 14), "Royal wedding"), ],
        1977: [(date(1977, 6, 7), "Queen’s Silver Jubilee"), ],
        1981: [(date(1981, 7, 29), "Royal wedding"), ],
        1999: [(date(1999, 12, 31), "New Year's Eve"), ],
        2002: [(date(2002, 6, 3), "Queen’s Golden Jubilee"), ],
        2011: [(date(2011, 4, 29), "Royal Wedding"), ],
        2012: [(date(2012, 6, 5), "Queen’s Diamond Jubilee"), ],
    }

    def get_early_may_bank_holiday(self, year):
        """
        Return Early May bank holiday
        """
        # Special case in 2020, for the 75th anniversary of the end of WWII.
        if year == 2020:
            return (
                date(year, 5, 8),
                "Early May bank holiday (VE day)"
            )

        return (
            UnitedKingdom.get_nth_weekday_in_month(year, 5, MON),
            "Early May Bank Holiday"
        )

    def get_spring_bank_holiday(self, year):
        if year == 2012:
            spring_bank_holiday = date(2012, 6, 4)
        elif year == 1977:
            spring_bank_holiday = date(1977, 6, 6)
        elif year == 2002:
            spring_bank_holiday = date(2002, 6, 4)
        else:
            spring_bank_holiday = UnitedKingdom \
                .get_last_weekday_in_month(year, 5, MON)
        return (
            spring_bank_holiday,
            "Spring Bank Holiday"
        )

    def get_late_summer_bank_holiday(self, year):
        return (
            UnitedKingdom.get_last_weekday_in_month(year, 8, MON),
            "Late Summer Bank Holiday"
        )

    def non_computable_holiday(self, year):
        non_computable = self.non_computable_holiday_dict.get(year, None)
        return non_computable

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_early_may_bank_holiday(year))
        days.append(self.get_spring_bank_holiday(year))
        days.append(self.get_late_summer_bank_holiday(year))
        # Boxing day & XMas shift
        shifts = self.shift_christmas_boxing_days(year=year)
        days.extend(shifts)
        non_computable = self.non_computable_holiday(year)
        if non_computable:
            days.extend(non_computable)
        return days


@iso_register('GB-NIR')
class UnitedKingdomNorthernIreland(UnitedKingdom):
    'Northern Ireland'

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
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
