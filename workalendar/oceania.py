from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON, TUE, FRI, SAT, SUN
from datetime import date, timedelta


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
        days = super(Australia, self).get_variable_days(year)
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


class AustralianCapitalTerritory(Australia):
    "Australian Capital Territory"
    include_easter_saturday = True
    include_queens_birthday = True
    include_labour_day_october = True
    include_boxing_day = True

    def get_family_community_day(self, year):
        # Since this day is picked unsing the school year calendar, there's no
        # mathematical way yet to provide it surely

        # Family & Community Day was celebrated on the first Tuesday of
        # November in 2007, 2008 and 2009

        # Per Holidays (Reconciliation Day) Amendment Bill 2017, 2017 is the
        # last year that ACT will celebrate family and community day. It is
        # being replaced by Reconciliaton day
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
            return None
        return (day, "Family & Community Day")

    def get_reconciliation_day(self, year):
        if year >= 2018:
            reconciliation_day = date(year, 5, 27)
            if reconciliation_day.weekday() == MON:
                return (reconciliation_day, "Reconciliation Day")
            else:
                shift = AustralianCapitalTerritory.get_first_weekday_after(
                    reconciliation_day, MON)
                return shift, "Reconciliation Day Shift"

    def get_variable_days(self, year):
        days = super(AustralianCapitalTerritory, self).get_variable_days(year)
        days.append(self.get_canberra_day(year))

        family_community_day = self.get_family_community_day(year)
        if family_community_day is not None:
            days.append(family_community_day)

        reconciliation_day = self.get_reconciliation_day(year)
        if reconciliation_day is not None:
            days.append(reconciliation_day)

        return days


class NewSouthWales(Australia):
    "New South Wales"
    include_queens_birthday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_labour_day_october = True
    include_boxing_day = True

    ANZAC_SHIFT_DAYS = (SUN,)


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
        days = super(NorthernTerritory, self).get_variable_days(year)
        days.extend([
            self.get_may_day(year),
            self.get_picnic_day(year),
        ])
        return days


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
        days = super(Queensland, self).get_variable_days(year)
        days.append(self.get_labour_day_may(year))
        return days


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
        days = super(SouthAustralia, self).get_variable_days(year)
        days.extend([
            self.get_adelaides_cup(year),
            self.get_proclamation_day(year),
        ])
        return days


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
        days = super(Tasmania, self).get_variable_days(year)
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
        days = super(Hobart, self).get_variable_days(year)
        days.append(self.get_hobart(year))
        return days


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
        days = super(Victoria, self).get_variable_days(year)
        days.append(self.get_labours_day_in_march(year))
        days.append(self.get_melbourne_cup(year))
        return days


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
        days = super(WesternAustralia, self).get_variable_days(year)
        days.append(self.get_labours_day_in_march(year))
        days.append(self.get_western_australia_day(year))
        return days


class MarshallIslands(WesternCalendar, ChristianMixin):
    "Marshall Islands"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 3, "Remembrance Day"),
        (5, 1, "Constitution Day"),
        (11, 17, "Presidents' Day"),
        (12, 31, "New Year's Eve"),
    )
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(MarshallIslands, self).get_variable_days(year)
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 7, FRI),
            "Fishermen's Holiday"
        ))
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 9, FRI),
            "Labour Day"
        ))
        days.append((
            MarshallIslands.get_last_weekday_in_month(year, 9, FRI),
            "Manit Day"
        ))
        days.append((
            MarshallIslands.get_nth_weekday_in_month(year, 12, FRI),
            "Gospel Day"
        ))
        return days
