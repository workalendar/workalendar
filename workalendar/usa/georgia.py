import warnings
from datetime import date
from ..core import MON, TUE, WED, THU, FRI, SAT
from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-GA')
class Georgia(UnitedStates):
    """Georgia"""
    include_confederation_day = True
    include_federal_presidents_day = False
    label_washington_birthday_december = "Washington's Birthday (Observed)"
    thanksgiving_friday_label = "State Holiday"

    def get_washington_birthday_december(self, year):
        """
        Washington birthday observance
        Similar to Christmas Eve, but with special rules.
        It's only observed in Georgia.
        """
        warnings.warn(
            "Washington birthday rules for Georgia State are possibly wrong. "
            "Use this calendar with care")
        christmas_day = date(year, 12, 25).weekday()

        # Special case: 2011 / Source:
        # Christmas day is SUN, but doesn't follow the same rule as year 2016.
        # https://web.archive.org/web/20110927122533/http://www.georgia.gov/00/channel_modifieddate/0,2096,4802_64437763,00.html  # noqa
        if year == 2011:
            day = date(year, 12, 26)
        elif christmas_day == MON:
            day = date(year, 12, 26)  # TUE
        elif christmas_day == TUE:
            day = date(year, 12, 24)  # MON
        elif christmas_day == WED:
            day = date(year, 12, 24)  # TUE
        elif christmas_day == THU:
            day = date(year, 12, 26)  # FRI
        elif christmas_day == FRI:
            day = date(year, 12, 24)  # THU
        elif christmas_day == SAT:
            day = date(year, 12, 23)  # THU
        else:  # christmas_day == SUN:
            day = date(year, 12, 27)  # FRI
        return (day, self.label_washington_birthday_december)

    def get_confederate_day(self, year):
        """
        Confederate memorial day is on the 4th MON of April.

        Exception: Year 2020, when it happened on April 10th.
        """
        if year >= 2016:
            label = "State Holiday"
        else:
            label = "Confederate Memorial Day"

        # At the moment, it's the only exception we know about.
        if year == 2020:
            return (date(year, 4, 10), label)

        day = self.get_nth_weekday_in_month(year, 4, MON, 4)
        return (day, label)

    def get_robert_lee_birthday(self, year):
        """
        Robert E. Lee's birthday.

        Happens on the day after Thanksgiving.
        """
        if year < 2016:
            label = "Robert E. Lee's Birthday (Observed)"
        else:
            label = "State Holiday"
        date, _ = self.get_thanksgiving_friday(year)
        return (date, label)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            self.get_robert_lee_birthday(year),
            self.get_washington_birthday_december(year),
        ])
        return days
