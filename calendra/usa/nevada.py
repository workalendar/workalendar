from ..core import FRI
from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-NV')
class Nevada(UnitedStates):
    """Nevada"""
    include_thanksgiving_friday = True
    thanksgiving_friday_label = "Family Day"
    include_columbus_day = False

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(
            (self.get_last_weekday_in_month(year, 10, FRI), "Nevada Day")
        )
        return days
