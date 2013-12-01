from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON
from datetime import date


class AustraliaCalendar(WesternCalendar, ChristianMixin):
    "Australia base calendar"
    include_good_friday = True
    include_easter_monday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 26, "Australia Day"),
        (4, 25, "Anzac Day"),
    )

    def get_canberra_day(self, year):
        return (
            AustraliaCalendar.get_nth_weekday_in_month(year, 3, MON, 2),
            "Canberra Day"
        )

    def get_variable_days(self, year):
        # usual variable days
        days = super(AustraliaCalendar, self).get_variable_days(year)
        days += [

        ]
        return days


class AustraliaCapitalTerritoryCalendar(AustraliaCalendar):
    include_easter_saturday = True

    def get_variable_days(self, year):
        days = super(AustraliaCapitalTerritoryCalendar, self) \
            .get_variable_days(year)
        days += [
            self.get_canberra_day(year),
        ]
        return days
