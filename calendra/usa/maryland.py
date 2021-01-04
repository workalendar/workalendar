from .core import UnitedStates
from ..registry_tools import iso_register


@iso_register('US-MD')
class Maryland(UnitedStates):
    """Maryland"""
    thanksgiving_friday_label = "Native American Heritage Day"
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        if Maryland.is_presidential_year(year):
            days.append(self.get_election_day(year))
        return days
