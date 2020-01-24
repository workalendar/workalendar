from datetime import date

from ..core import WesternCalendar, ChristianMixin, Calendar
from ..core import SUN, MON, SAT
from ..registry_tools import iso_register


@iso_register('CA')
class Canada(WesternCalendar, ChristianMixin):
    "Canada"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 1, "Canada Day"),
    )
    shift_new_years_day = True

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)
        days.append(
            (Canada.get_nth_weekday_in_month(year, 9, MON, 1), "Labor Day")
        )
        # Canada day
        canadaday = date(year, 7, 1)
        if canadaday.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(canadaday)
            days.append((shift, "Canada Day Shift"))
        christmas = date(year, 12, 25)
        if christmas.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(christmas)
            days.append((shift, "Christmas Shift"))
        return days


class LateFamilyDayMixin(Calendar):
    "3rd Monday of February"

    def get_family_day(self, year, label="Family Day"):
        return (self.get_nth_weekday_in_month(year, 2, MON, 3), label)


class VictoriaDayMixin(Calendar):
    "Monday preceding the 25th of May"

    def get_victoria_day(self, year):
        for day in range(18, 25):
            if date(year, 5, day).weekday() == MON:
                return (date(year, 5, day), "Victoria Day")


class AugustCivicHolidayMixin(Calendar):
    "1st Monday of August; different names depending on location"

    def get_civic_holiday(self, year, label="Civic Holiday"):
        return (self.get_nth_weekday_in_month(year, 8, MON), label)


class ThanksgivingMixin(Calendar):
    "2nd Monday of October"

    def get_thanksgiving(self, year):
        thanksgiving = self.get_nth_weekday_in_month(year, 10, MON, 2)
        return (thanksgiving, "Thanksgiving")


class BoxingDayMixin(Calendar):
    "26th of December; shift to next working day"

    def get_boxing_day(self, year):
        boxingday = date(year, 12, 26)
        if boxingday.weekday() == MON:
            days = [(boxingday, "Boxing Day"), (date(year, 12, 27),
                    "Boxing Day (Shift)")]
        elif boxingday.weekday() == SAT or boxingday.weekday() == SUN:
            days = [(boxingday, "Boxing Day"), (date(year, 12, 28),
                    "Boxing Day (Shift)")]
        else:
            days = [(boxingday, "Boxing Day")]
        return days


class StJeanBaptisteMixin(Calendar):
    "24th of June; shift to next working day"

    def get_st_jean(self, year):
        stjean = date(year, 6, 24)
        if stjean.weekday() in self.get_weekend_days():
            days = [(stjean, "St Jean Baptiste"),
                    (self.find_following_working_day(stjean),
                     "St Jean Baptiste (Shift)")]
        else:
            days = [(stjean, "St Jean Baptiste")]
        return days


class RemembranceDayShiftMixin(Calendar):
    "11th of November; shift to next day"
    def get_remembrance_day(self, year):
        remembranceday = date(year, 11, 11)
        if remembranceday.weekday() in self.get_weekend_days():
            days = [(remembranceday, "Remembrance Day"),
                    (self.find_following_working_day(remembranceday),
                    "Remembrance Day (Shift)")]
        else:
            days = [(remembranceday, "Remembrance Day")]
        return days


@iso_register('CA-ON')
class Ontario(Canada, BoxingDayMixin, ThanksgivingMixin, VictoriaDayMixin,
              LateFamilyDayMixin, AugustCivicHolidayMixin):
    "Ontario"
    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_family_day(year)),
            (self.get_victoria_day(year)),
            (self.get_civic_holiday(year, "Civic Holiday (Not for all)")),
            (self.get_thanksgiving(year)),
        ])
        days.extend(self.get_boxing_day(year))

        return days


@iso_register('CA-QC')
class Quebec(Canada, VictoriaDayMixin, StJeanBaptisteMixin, ThanksgivingMixin):
    "Quebec"
    include_easter_monday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_victoria_day(year)),
            (self.get_thanksgiving(year)),
        ])
        days.extend(self.get_st_jean(year))
        return days


@iso_register('CA-BC')
class BritishColumbia(Canada, VictoriaDayMixin, AugustCivicHolidayMixin,
                      ThanksgivingMixin):
    "British Columbia"

    include_good_friday = True

    FIXED_HOLIDAYS = Canada.FIXED_HOLIDAYS + (
        (11, 11, "Remembrance Day"),
    )

    def get_family_day(self, year):
        """
        Return Family Day for British Columbia.

        From 2013 to 2018, Family Day was on 2nd MON of February
        As of 2019, Family Day happens on 3rd MON of February
        """
        label = "Family Day"
        if year >= 2019:
            return (self.get_nth_weekday_in_month(year, 2, MON, 3), label)
        return (self.get_nth_weekday_in_month(year, 2, MON, 2), label)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        if year >= 2013:
            days.append(self.get_family_day(year))

        days.extend([
            (self.get_victoria_day(year)),
            (self.get_civic_holiday(year, "British Columbia Day")),
            (self.get_thanksgiving(year)),
        ])
        return days


@iso_register('CA-AB')
class Alberta(Canada, LateFamilyDayMixin, VictoriaDayMixin, ThanksgivingMixin):
    "Alberta"
    include_good_friday = True

    FIXED_HOLIDAYS = Canada.FIXED_HOLIDAYS + (
        (11, 11, "Remembrance Day"),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_family_day(year)),
            (self.get_victoria_day(year)),
            (self.get_thanksgiving(year)),
        ])
        return days


@iso_register('CA-SK')
class Saskatchewan(Canada, LateFamilyDayMixin, VictoriaDayMixin,
                   RemembranceDayShiftMixin, AugustCivicHolidayMixin,
                   ThanksgivingMixin):
    "Saskatchewan"
    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_family_day(year)),
            (self.get_victoria_day(year)),
            (self.get_civic_holiday(year)),
            (self.get_thanksgiving(year)),
        ])
        days.extend(self.get_remembrance_day(year))
        return days


@iso_register('CA-MB')
class Manitoba(Canada, LateFamilyDayMixin, VictoriaDayMixin,
               AugustCivicHolidayMixin, ThanksgivingMixin):
    "Manitoba"
    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_family_day(year, "Louis Riel Day")),
            (self.get_victoria_day(year)),
            (self.get_civic_holiday(year)),
            (self.get_thanksgiving(year)),
        ])
        return days


@iso_register('CA-NB')
class NewBrunswick(Canada, AugustCivicHolidayMixin):
    "New Brunswick"

    FIXED_HOLIDAYS = Canada.FIXED_HOLIDAYS + (
        (11, 11, "Remembrance Day"),
    )

    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_civic_holiday(year))
        return days


@iso_register('CA-NS')
class NovaScotia(Canada, RemembranceDayShiftMixin, LateFamilyDayMixin):
    "Nova Scotia"

    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend(self.get_remembrance_day(year))
        if year >= 2015:
            days.append(self.get_family_day(year, "Viola Desmond Day"))
        return days


@iso_register('CA-PE')
class PrinceEdwardIsland(Canada, LateFamilyDayMixin, RemembranceDayShiftMixin):
    "Prince Edward Island"

    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append((self.get_family_day(year, "Islander Day")))
        days.extend(self.get_remembrance_day(year))
        return days


@iso_register('CA-NL')
class Newfoundland(Canada):
    "Newfoundland and Labrador"
    include_good_friday = True


@iso_register('CA-YT')
class Yukon(Canada, VictoriaDayMixin, ThanksgivingMixin):
    "Yukon"

    FIXED_HOLIDAYS = Canada.FIXED_HOLIDAYS + (
        (11, 11, "Remembrance Day"),
    )

    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_nth_weekday_in_month(year, 8, MON, 3), "Discovery Day"),
            (self.get_victoria_day(year)),
            (self.get_thanksgiving(year)),
        ])
        return days


@iso_register('CA-NT')
class NorthwestTerritories(Canada, RemembranceDayShiftMixin, VictoriaDayMixin,
                           ThanksgivingMixin):
    "Northwest Territories"

    FIXED_HOLIDAYS = Canada.FIXED_HOLIDAYS + (
        (6, 21, "National Aboriginal Day"),
    )

    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_victoria_day(year)),
            (self.get_thanksgiving(year)),
        ])
        days.extend(self.get_remembrance_day(year))
        return days


@iso_register('CA-NU')
class Nunavut(Canada, VictoriaDayMixin, ThanksgivingMixin,
              RemembranceDayShiftMixin):
    "Nunavut"
    include_good_friday = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (self.get_victoria_day(year)),
            (self.get_thanksgiving(year)),
        ])

        days.extend(self.get_remembrance_day(year))

        nuvanutday = date(year, 7, 9)
        days.append((nuvanutday, "Nuvanut Day"))
        if nuvanutday.weekday() == SUN:
            days.append((date(year, 7, 10), "Nuvanut Day (Shift)"))
        return days
