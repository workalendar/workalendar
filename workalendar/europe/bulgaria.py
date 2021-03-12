from copy import copy
from datetime import timedelta, date

from ..core import OrthodoxCalendar, SAT, SUN
from ..registry_tools import iso_register


@iso_register('BG')
class Bulgaria(OrthodoxCalendar):
    'Bulgaria'

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (3, 3, "Liberation Day"),  # Ден на Освобождението на Б
        (5, 6, "Saint George's Day"),  # Гергьовден, ден на храброс
        (5, 24, "Saints Cyril & Methodius Day"),  # Ден на българската просвет
        (9, 6, "Unification Day"),  # Ден на Съединението
        (9, 22, "Independence Day"),  # Ден на независимостта на Б
    )

    # Civil holidays
    include_labour_day = True
    # Ден на труда и на междунар
    labour_day_label = "International Workers' Day"

    # Christian holidays
    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_christmas_eve = True  # Бъдни вечер
    include_christmas = True  # Рождество Христово
    include_boxing_day = True
    # despite being an Orthodox calendar, don't observe Orthodox XMas
    include_orthodox_christmas = False

    # wikipedia says The Bulgarians have two days of Christmas,
    # both called Christmas Day
    boxing_day_label = "Christmas"

    def get_shifted_holidays(self, days):
        for holiday, label in days:
            if holiday.weekday() == SUN:
                yield (
                    holiday + timedelta(days=1),
                    f'{label} shift'
                )
            elif holiday.weekday() == SAT:
                yield (
                    holiday + timedelta(days=2),
                    f'{label} shift'
                )

    def get_fixed_holidays(self, year):
        """
        Return fixed holidays, with shifts computed accordingly.
        """
        # 2021 exception.
        # Because May 1st is both International Workers' day and Easter
        self.include_labour_day = (year != 2021)

        # Unshifted days are here:
        days = super().get_fixed_holidays(year)
        days_to_inspect = copy(days)
        for day_shifted in self.get_shifted_holidays(days_to_inspect):
            days.append(day_shifted)

        # 2021 exception.
        # Because May 1st is both International Workers' day and Easter
        if year == 2021:
            days.append((date(2021, 5, 4), self.labour_day_label))
        return days

    def shift_christmas_boxing_days(self, year):
        """
        Return Christmas shifts.

        They usually follow the same rule as used in the UK, but the fact that
        there's a second Christmas holiday requires an override.
        """
        days = super().shift_christmas_boxing_days(year=year)
        # In this case we'll need an extra day for the Second day of XMas
        if date(year, 12, 25).weekday() == SUN:
            days.append(
                (date(year, 12, 28), "Christmas (in lieu)")
            )
        return days

    def get_variable_days(self, year):
        """
        Return variable holidays, with Christmas shifts computed accordingly.
        """
        days = super().get_variable_days(year)
        # Boxing day & XMas shift
        shifts = self.shift_christmas_boxing_days(year=year)
        days.extend(shifts)
        return days
