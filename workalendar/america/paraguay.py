from datetime import date

from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('PY')
class Paraguay(WesternCalendar):
    "Paraguay"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 14, "Independence Day"),
        (6, 12, "Chaco Armistice"),
        (9, 19, "Army holiday"),
    )
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_holy_thursday = True
    include_good_friday = True
    include_easter_saturday = True
    include_immaculate_conception = True
    immaculate_conception_label = "Virgin of Caacupé Day"

    def get_heroes_day(self, year):
        """
        Heroes Day is a fixed holidays.

        In 2017, it has been moved to February 27th ; otherwise, it happens on
        March 1st.

        ref: https://en.wikipedia.org/wiki/Public_holidays_in_Paraguay
        """
        label = "Heroes' Day"
        if year == 2017:
            day = date(year, 2, 27)
        else:
            day = date(year, 3, 1)
        return day, label

    def get_founding_of_asuncion(self, year):
        """
        Return the Founding of Asunción.

        In 2017, it has been moved to August 14th ; otherwise it happens on
        August 15th.
        """
        label = "Founding of Asunción"
        if year == 2017:
            day = date(year, 8, 14)
        else:
            day = date(year, 8, 15)
        return day, label

    def get_boqueron_battle_victory_day(self, year):
        """
        Return Boqueron Battle Victory Day.

        In 2017, it has been moved to October 2nd ; otherwise it happens on
        September 29th.
        """
        label = "Boqueron Battle Victory Day"
        if year == 2017:
            day = date(year, 10, 2)
        else:
            day = date(year, 9, 29)
        return day, label

    def get_fixed_holidays(self, year):
        """
        Return fixed holidays for Paraguay.
        """
        days = super().get_fixed_holidays(year)
        days.append(self.get_heroes_day(year))
        days.append(self.get_founding_of_asuncion(year))
        days.append(self.get_boqueron_battle_victory_day(year))
        return days
