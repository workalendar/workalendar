from datetime import date, timedelta

from ..core import WesternCalendar, ChristianMixin
from ..core import MON, TUE, SAT, SUN
from ..registry_tools import iso_register


@iso_register('AU')
class Australia(WesternCalendar, ChristianMixin):
    "Australia"
    include_good_friday = True
    include_easter_monday = True
    include_queens_birthday = False
    include_labour_day_october = False
    include_boxing_day = True
    # Shall we shift Anzac Day?
    shift_anzac_day = True

    ANZAC_SHIFT_DAYS = (SAT, SUN)

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 26, "Australia Day"),
    )

    def get_canberra_day(self, year):
        return (
            Australia.get_nth_weekday_in_month(year, 3, MON, 2),
            "Canberra Day"
        )

    def get_queens_birthday(self, year):
        return (
            Australia.get_nth_weekday_in_month(year, 6, MON, 2),
            "Queen's Birthday"
        )

    def get_labour_day_october(self, year):
        return (
            Australia.get_nth_weekday_in_month(year, 10, MON),
            'Labour Day'
        )

    def get_anzac_day(self, year):
        anzac_day = date(year, 4, 25)
        if not self.shift_anzac_day:
            return (anzac_day, "Anzac Day")
        if anzac_day.weekday() in self.ANZAC_SHIFT_DAYS:
            anzac_day = self.find_following_working_day(anzac_day)
        return (anzac_day, "Anzac Day")

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)
        january_first = date(year, 1, 1)
        if january_first.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(january_first),
                "New Year's Day shift")
            )

        australia_day = date(year, 1, 26)
        if australia_day.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(australia_day),
                "Australia Day shift")
            )

        # was fixed, but might be shifted
        days.append(self.get_anzac_day(year))

        if self.include_queens_birthday:
            days.append(self.get_queens_birthday(year))
        if self.include_labour_day_october:
            days.append(self.get_labour_day_october(year))

        christmas = date(year, 12, 25)
        boxing_day = date(year, 12, 26)
        if christmas.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(christmas)
            days.append((shift, "Christmas Shift"))
            days.append((shift + timedelta(days=1), "Boxing Day Shift"))
        elif boxing_day.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(boxing_day)
            days.append((shift, "Boxing Day Shift"))

        return days


@iso_register('AU-ACT')
class AustralianCapitalTerritory(Australia):
    "Australian Capital Territory"
    include_easter_saturday = True
    include_queens_birthday = True
    include_labour_day_october = True
    include_boxing_day = True

    _family_community_label = "Family & Community Day"

    def get_family_community_day(self, year):
        """
        Return Family & Community Day.

        see: https://en.wikipedia.org/wiki/Family_Day#Australia
        """
        # Since this day is picked unsing the school year calendar, there's no
        # mathematical way yet to compute it.

        # This public holiday was declared in 2007. [..]
        # Per Holidays (Reconciliation Day) Amendment Bill 2017, 2017 is the
        # last year that ACT will celebrate family and community day. It is
        # being replaced by Reconciliaton day.
        if year < 2007 or year > 2018:
            # This would be interpreted as "this holiday must not be added"
            return None

        # Family & Community Day was celebrated on the first Tuesday of
        # November in 2007, 2008 and 2009
        if year in (2007, 2008, 2009):
            day = AustralianCapitalTerritory.get_nth_weekday_in_month(
                year, 11, TUE)
        # Family & Community Day was celebrated on the last Monday of
        # November in 2010, 2013, 2014, 2015, 2016, 2017
        elif year in (2010, 2013, 2014, 2015, 2016, 2017):
            day = AustralianCapitalTerritory.get_last_weekday_in_month(
                year, 9, MON)
        # Family & Community Day was celebrated on the second Monday of
        # October in 2011 and 2012
        elif year in (2011, 2012):
            day = AustralianCapitalTerritory.get_nth_weekday_in_month(
                year, 10, MON, 2)
        else:
            # If for some reason the year is not correctly provided
            # (not and int, or whatever)
            return None

        return (day, self._family_community_label)

    def get_reconciliation_day(self, year):
        """
        Return Reconciliaton Day.

        As of 2018, it replaces Family & Community Day.
        """
        if year < 2018:
            return None

        reconciliation_day = date(year, 5, 27)
        if reconciliation_day.weekday() == MON:
            return (reconciliation_day, "Reconciliation Day")
        else:
            shift = AustralianCapitalTerritory.get_first_weekday_after(
                reconciliation_day, MON)
            return shift, "Reconciliation Day Shift"

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_canberra_day(year))

        family_community_day = self.get_family_community_day(year)
        if family_community_day is not None:
            days.append(family_community_day)

        reconciliation_day = self.get_reconciliation_day(year)
        if reconciliation_day is not None:
            days.append(reconciliation_day)

        return days


@iso_register('AU-NSW')
class NewSouthWales(Australia):
    "New South Wales"
    include_queens_birthday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_labour_day_october = True
    include_boxing_day = True

    ANZAC_SHIFT_DAYS = (SUN,)


@iso_register('AU-NT')
class NorthernTerritory(Australia):
    "Northern Territory"
    include_easter_saturday = True
    include_queens_birthday = True
    include_boxing_day = True

    ANZAC_SHIFT_DAYS = (SUN,)

    def get_may_day(self, year):
        return (
            NorthernTerritory.get_nth_weekday_in_month(year, 5, MON),
            "May Day"
        )

    def get_picnic_day(self, year):
        return (
            NorthernTerritory.get_nth_weekday_in_month(year, 8, MON),
            "Picnic Day"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            self.get_may_day(year),
            self.get_picnic_day(year),
        ])
        return days


@iso_register('AU-QLD')
class Queensland(Australia):
    "Queensland"
    include_easter_saturday = True
    include_queens_birthday = True
    include_boxing_day = True

    ANZAC_SHIFT_DAYS = (SUN,)

    def get_labour_day_may(self, year):
        return (
            Queensland.get_nth_weekday_in_month(year, 5, MON),
            "Labour Day"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_labour_day_may(year))
        return days


@iso_register('AU-SA')
class SouthAustralia(Australia):
    "South Australia"
    include_easter_saturday = True
    include_queens_birthday = True
    include_labour_day_october = True

    ANZAC_SHIFT_DAYS = (SUN,)

    def get_adelaides_cup(self, year):
        return (
            SouthAustralia.get_nth_weekday_in_month(year, 3, MON, 2),
            "Adelaide's cup"
        )

    def get_proclamation_day(self, year):
        return (date(year, 12, 26), "Proclamation Day")

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            self.get_adelaides_cup(year),
            self.get_proclamation_day(year),
        ])
        return days


@iso_register('AU-TAS')
class Tasmania(Australia):
    "Tasmania"
    include_queens_birthday = True
    include_boxing_day = True
    shift_anzac_day = False

    @property
    def has_recreation_day(self):
        return True

    def get_eight_hours_day(self, year):
        return (
            Tasmania.get_nth_weekday_in_month(year, 3, MON, 2),
            "Eight hours Day"
        )

    def get_recreation_day(self, year):
        return (
            Tasmania.get_nth_weekday_in_month(year, 11, MON),
            "Recreation Day"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_eight_hours_day(year))
        if self.has_recreation_day:
            days.append(self.get_recreation_day(year))
        return days


class Hobart(Tasmania):
    "Hobart"
    @property
    def has_recreation_day(self):
        return False

    def get_hobart(self, year):
        return (
            Hobart.get_nth_weekday_in_month(year, 2, MON, 2),
            "Royal Hobart Regatta"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_hobart(year))
        return days


@iso_register('AU-VIC')
class Victoria(Australia):
    "Victoria"
    include_easter_saturday = True
    include_queens_birthday = True
    include_boxing_day = True
    shift_anzac_day = False

    def get_labours_day_in_march(self, year):
        return (
            Victoria.get_nth_weekday_in_month(year, 3, MON, 2),
            "Labour Day"
        )

    def get_melbourne_cup(self, year):
        return (
            Victoria.get_nth_weekday_in_month(year, 11, TUE),
            "Melbourne Cup"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_labours_day_in_march(year))
        days.append(self.get_melbourne_cup(year))
        return days


@iso_register('AU-WA')
class WesternAustralia(Australia):
    "Western Australia"
    include_boxing_day = True

    def get_labours_day_in_march(self, year):
        return (
            WesternAustralia.get_nth_weekday_in_month(year, 3, MON),
            "Labour Day"
        )

    def get_western_australia_day(self, year):
        return (
            WesternAustralia.get_nth_weekday_in_month(year, 6, MON),
            "Western Australia Day"
        )

    def get_variable_days(self, year):
        # It is not possible to surely compute Queen's Birthday holiday in
        # The western Australia territory, since it's based on the Governor
        # Decision (it is typically the last Monday of September or the first
        # Monday of October)
        days = super().get_variable_days(year)
        days.append(self.get_labours_day_in_march(year))
        days.append(self.get_western_australia_day(year))
        return days
