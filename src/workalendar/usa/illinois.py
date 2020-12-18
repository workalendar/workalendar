from .core import UnitedStates
from ..registry_tools import iso_register
from ..core import MON


@iso_register('US-IL')
class Illinois(UnitedStates):
    """Illinois"""
    include_thanksgiving_friday = True
    include_lincoln_birthday = True
    include_election_day_even = True


class ChicagoIllinois(Illinois):
    "Chicago, Illinois"
    include_thanksgiving_friday = False

    def get_pulaski_day(self, year):
        """
        Return Casimir Pulaski Day.

        Defined on the first MON of March.
        ref: https://en.wikipedia.org/wiki/Casimir_Pulaski_Day
        """
        day = self.get_nth_weekday_in_month(year, 3, MON)
        return (
            day,
            "Casimir Pulaski Day"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_pulaski_day(year))
        return days
