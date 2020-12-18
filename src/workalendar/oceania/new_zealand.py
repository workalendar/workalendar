from datetime import date, timedelta

from ..core import WesternCalendar, MON, SAT, SUN
from ..registry_tools import iso_register


@iso_register("NZ")
class NewZealand(WesternCalendar):
    "New Zealand"
    include_good_friday = True
    include_easter_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day after New Year's Day"),
        (2, 6, "Waitangi Day"),
        (4, 25, "ANZAC Day")
    )

    def get_queens_birthday(self, year):
        return (
            NewZealand.get_nth_weekday_in_month(year, 6, MON, 1),
            "Queen's Birthday"
        )

    def get_labour_day(self, year):
        return (
            NewZealand.get_nth_weekday_in_month(year, 10, MON, 4),
            "Labour Day"
        )

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)
        days.append(self.get_queens_birthday(year))
        days.append(self.get_labour_day(year))

        waitangi_day = date(year, 2, 6)
        if waitangi_day.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(waitangi_day),
                "Waitangi Day Shift")
            )

        anzac_day = date(year, 4, 25)
        if anzac_day.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(anzac_day),
                "ANZAC Day Shift")
            )

        christmas = date(year, 12, 25)
        boxing_day = date(year, 12, 26)
        if christmas.weekday() == SAT:
            shift = self.find_following_working_day(christmas)
            days.append((shift, "Christmas Shift"))
        elif christmas.weekday() == SUN:
            shift = self.find_following_working_day(christmas)
            days.append((shift + timedelta(days=1), "Christmas Shift"))

        if boxing_day.weekday() == SAT:
            shift = self.find_following_working_day(boxing_day)
            days.append((shift, "Boxing Day Shift"))
        elif boxing_day.weekday() == SUN:
            shift = self.find_following_working_day(boxing_day)
            days.append((shift + timedelta(days=1), "Boxing Day Shift"))

        new_year = date(year, 1, 1)
        day_after_new_year = date(year, 1, 2)
        if new_year.weekday() == SAT:
            shift = self.find_following_working_day(new_year)
            days.append((shift, "New Year Shift"))
        elif new_year.weekday() == SUN:
            shift = self.find_following_working_day(new_year)
            days.append((shift + timedelta(days=1), "New Year Shift"))

        if day_after_new_year.weekday() == SAT:
            shift = self.find_following_working_day(day_after_new_year)
            days.append((shift, "Day after New Year's Day Shift"))
        elif day_after_new_year.weekday() == SUN:
            shift = self.find_following_working_day(day_after_new_year)
            days.append((shift + timedelta(days=1),
                         "Day after New Year's Day Shift"))

        return days
