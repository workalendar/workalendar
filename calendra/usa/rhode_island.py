from ..core import MON
from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-RI')
class RhodeIsland(UnitedStates):
    """Rhode Island"""
    include_federal_presidents_day = False
    include_election_day_even = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(
            (self.get_nth_weekday_in_month(year, 8, MON, 2), "Victory Day")
        )
        return days
