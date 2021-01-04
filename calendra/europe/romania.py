from datetime import date
from ..core import OrthodoxCalendar
from ..registry_tools import iso_register


@iso_register('RO')
class Romania(OrthodoxCalendar):
    'Romania'

    # Civil holidays
    include_labour_day = True
    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (1, 24, "Union Day"),
        (8, 15, "Dormition of the Theotokos"),
        (11, 30, "St. Andrew's Day"),
        (12, 1, "National Day/Great Union"),
    )

    # Christian holidays
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = 'Pentecost'
    include_whit_monday = True

    include_christmas = True
    include_boxing_day = True
    boxing_day_label = 'Christmas Day'
    # No Orthodox Christmas
    include_orthodox_christmas = False

    def get_childrens_day(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if year >= 2017:
            actual_date = date(year, 6, 1)
            days = [(actual_date, "Children's Day")]

        return days

    def get_liberation_day(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if 1949 <= year <= 1990:
            actual_date = date(year, 8, 23)
            days = [(actual_date, "Liberation from Fascist Occupation Day")]

        return days

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend(self.get_childrens_day(year))
        days.extend(self.get_liberation_day(year))
        return days
