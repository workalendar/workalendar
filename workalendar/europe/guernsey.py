from datetime import date

from ..core import MON, WesternCalendar
from ..registry_tools import iso_register


@iso_register('GG')
class Guernsey(WesternCalendar):
    'Guernsey'

    include_easter_monday = True
    include_boxing_day = True
    shift_new_years_day = True
    include_good_friday = True

    def get_spring_bank_holiday(self, year):
        spring_bank_holiday = Guernsey \
            .get_last_weekday_in_month(year, 5, MON)
        return (
            spring_bank_holiday,
            "Spring Bank Holiday"
        )

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
            Guernsey.get_nth_weekday_in_month(year, 5, MON),
            "Early May Bank Holiday"
        )

    def get_summer_bank_holiday(self, year):
        return (
            Guernsey.get_last_weekday_in_month(year, 8, MON),
            "Summer Bank Holiday"
        )

    def get_liberation_day(self, year):
        return (date(year, 5, 9), "Liberation Day")

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_early_may_bank_holiday(year))
        days.append(self.get_spring_bank_holiday(year))
        days.append(self.get_summer_bank_holiday(year))
        days.append(self.get_liberation_day(year))
        # Boxing day & XMas shift
        shifts = self.shift_christmas_boxing_days(year=year)
        days.extend(shifts)
        return days
