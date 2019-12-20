from datetime import date
from ..core import WesternCalendar, OrthodoxMixin
from ..registry_tools import iso_register


@iso_register('UA')
class Ukraine(OrthodoxMixin, WesternCalendar):
    'Ukraine'

    shift_sunday_holidays = True
    shift_new_years_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 8, "International Women’s Day"),
        (5, 1, "Workers Solidarity Day"),
        (5, 9, "Victory Day"),
    )

    include_christmas = False
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_monday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)

        # Orthodox Christmas holiday is moved when it falls over the week
        orthodox_christmas = date(year, 1, 7)
        if orthodox_christmas.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(orthodox_christmas),
                "Orthodox Christmas (postponed)"))
        else:
            days.append((orthodox_christmas, "Orthodox Christmas"))

        # Constitution Day was celebrated for the first time in 1996
        if year >= 1996:
            constitution_day = date(year, 6, 28)
            if constitution_day.weekday() in self.get_weekend_days():
                days.append((
                    self.find_following_working_day(constitution_day),
                    "Constitution Day (postponed)"))
            else:
                days.append((constitution_day, "Constitution Day"))

        # Independence Day was first celebrated in 1991 on the 16th of June
        # After the official independence has been moved to the 24th of August
        if year == 1991:
            days.append((date(year, 6, 16), "Independence Day"))
        if year >= 1992:
            independence_day = date(year, 8, 24)

            if independence_day.weekday() in self.get_weekend_days():
                days.append((
                    self.find_following_working_day(independence_day),
                    "Independence Day (postponed)"))
            else:
                days.append((independence_day, "Independence Day"))

        # Defender of Ukraine from 2015
        # https://en.wikipedia.org/wiki/Defender_of_Ukraine_Day
        if year >= 2015:
            days.append((date(year, 10, 14), "Day of Defender of Ukraine"))

        # Catholic Christmas has become an holiday only starting from 2017
        if year >= 2017:
            days.append((date(year, 12, 25), "Christmas Day"))

        # Workers Solidarity Day was celebrated also on the 2nd till 2017
        if year <= 2017:
            days.append((date(year, 5, 2), "Workers Solidarity Day"))

        return days
