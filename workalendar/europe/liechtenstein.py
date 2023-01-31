from datetime import date
from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register("LI")
class Liechtenstein(WesternCalendar):
    "Liechtenstein"

    # Public Holyday
    include_epiphany = True
    include_easter_sunday = True
    include_easter_monday = True
    include_labour_day = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_corpus_christi = True
    include_assumption = True  # National Day
    include_nativity_of_mary = True
    include_all_saints = True
    include_immaculate_conception = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"  # Stefanstag

    # bank holydays
    fat_tuesday_label = "Shrove Tuesday"

    def __init__(self, include_rest_days=True, include_bankholyday=False):
        # legally public rest days
        self.include_candlemas = include_rest_days
        self.include_st_josephs_day = include_rest_days

        # bank holydays
        self.include_berchtolds_day = include_bankholyday
        self.include_fat_tuesday = include_bankholyday
        self.include_good_friday = include_bankholyday
        self.include_christmas_eve = include_bankholyday
        self.include_new_years_eve = include_bankholyday

        super().__init__()

    def has_berchtolds_day(self, year):
        return self.include_berchtolds_day

    def get_variable_days(self, year):
        days = super().get_variable_days(year)

        if self.has_berchtolds_day(year):
            days.append((date(year, 1, 2), "Berchtold's Day"))

        if self.include_st_josephs_day:
            days.append((date(year, 3, 19), "St Joseph's Day"))

        if self.include_candlemas:
            days.append((date(year, 2, 2), "Candlemas"))

        if self.include_candlemas:
            days.append((date(year, 9, 8), "Nativity of Mary"))

        return days
