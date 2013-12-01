from workalendar.core import WesternCalendar, ChristianMixin
from datetime import date


class AustraliaCalendar(WesternCalendar, ChristianMixin):
    "Australia base calendar"
    include_good_friday = True
    include_easter_monday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 26, "Australia Day"),
        (4, 25, "Anzac Day"),
    )

    def get_variable_days(self, year):
        # usual variable days
        days = super(AustraliaCalendar, self).get_variable_days(year)
        days += [

        ]
        return days

