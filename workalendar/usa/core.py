# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date, timedelta

from ..core import WesternCalendar, ChristianMixin
from ..core import SUN, MON, TUE, WED, THU, FRI, SAT
from ..registry import iso_register


@iso_register('US')
class UnitedStates(WesternCalendar, ChristianMixin):
    "United States of America"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 4, 'Independence Day'),
    )
    # Veterans day label
    include_veterans_day = True
    veterans_day_label = 'Veterans Day'

    # MLK
    martin_luther_king_label = 'Birthday of Martin Luther King, Jr.'

    include_thanksgiving_friday = False
    thanksgiving_friday_label = "Thanksgiving Friday"
    # Some states don't include Washington's Birthday, or move it to December.
    include_federal_presidents_day = True
    presidents_day_label = "Washington's Birthday"

    include_lincoln_birthday = False

    # Columbus day is included by default
    include_columbus_day = True
    columbus_day_label = "Columbus Day"
    # Confederation day
    include_confederation_day = False

    # Include Cesar Chavez day(s)
    include_cesar_chavez_day = False
    # Patriot's day
    include_patriots_day = False

    # Boxing day label is not "boxing day" in the US
    boxing_day_label = "Day After Christmas"

    # Election Day
    # To include every year?
    include_election_day_every_year = False
    # To include on even years?
    include_election_day_even = False
    # NOTE: if it's included on every year, it'll also be included
    # on even years. Setting these two flags to ON will give priority to the
    # yearly flag.
    election_day_label = "Election Day"
    # Inauguration Day
    include_inauguration_day = False

    # National Memorial Day
    national_memorial_day_label = "Memorial Day"

    # Some regional variants
    include_mardi_gras = False

    # Shift day mechanism
    # These days won't be shifted to next MON or previous FRI
    shift_exceptions = (
        # Exemple:
        # (11, 11),  # Veterans day won't be shifted
    )

    def shift(self, holidays, year):
        new_holidays = []
        holiday_lookup = [x[0] for x in holidays]
        exceptions = [
            date(year, month, day) for month, day in self.shift_exceptions
        ]

        # For each holiday available:
        # * if it falls on SUN, add the observed on MON
        # * if it falls on SAT, add the observed on FRI
        for day, label in holidays:
            # ... except if it's been explicitely excepted.
            if day in exceptions:
                continue
            if day.weekday() == SAT:
                new_holidays.append((day - timedelta(days=1),
                                     label + " (Observed)"))
            elif day.weekday() == SUN:
                new_holidays.append((day + timedelta(days=1),
                                     label + " (Observed)"))

        # If year+1 January the 1st is on SAT, add the FRI before to observed
        if date(year + 1, 1, 1).weekday() == SAT:
            new_holidays.append((date(year, 12, 31,),
                                 "New Years Day (Observed)"))

        # Special rules for XMas and XMas Eve
        christmas = date(year, 12, 25)
        christmas_eve = date(year, 12, 24)
        # Is XMas eve in your calendar?
        if christmas_eve in holiday_lookup:
            # You are observing the THU before, as an extra XMas Eve
            if christmas.weekday() == SAT:
                # Remove the "fake" XMAS Day shift, the one done before.
                new_holidays.remove(
                    (christmas_eve, "Christmas Day (Observed)")
                )
                new_holidays.append((date(year, 12, 23),
                                     "Christmas Eve (Observed)"))
            # You are observing the 26th (TUE)
            elif christmas.weekday() == MON:
                # Remove the "fake" XMAS Eve shift, done before
                new_holidays.remove(
                    (christmas, "Christmas Eve (Observed)")
                )
                new_holidays.append((date(year, 12, 26),
                                     "Christmas Day (Observed)"))
        return holidays + new_holidays

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_election_date(self, year):
        """
        Return the Election Day *Date*

        Definition: on an election year, "the Tuesday next after the first
        Monday in the month of November".
        """
        first_monday_november = self.get_nth_weekday_in_month(year, 11, MON)
        return self.get_nth_weekday_in_month(
            year, 11, TUE, start=first_monday_november
        )

    def get_election_day(self, year):
        """
        Return the Election Day
        """
        return (self.get_election_date(year), self.election_day_label)

    def get_thanksgiving_friday(self, year):
        "Thanksgiving friday is on the 4th Friday in November"
        return (
            self.get_nth_weekday_in_month(year, 11, FRI, 4),
            self.thanksgiving_friday_label
        )

    def get_confederate_day(self, year):
        """
        Confederation memorial day is on the 4th MON of April.
        """
        day = self.get_nth_weekday_in_month(year, 4, MON, 4)
        return (day, "Confederate Memorial Day")

    def get_martin_luther_king_date(self, year):
        """
        Martin Luther King is on 3rd MON of January, starting of 1985.

        """
        if year < 1985:
            raise ValueError(
                "Martin Luther King Day became a holiday in 1985"
            )
        return UnitedStates.get_nth_weekday_in_month(year, 1, MON, 3)

    def get_martin_luther_king_day(self, year):
        """
        Return holiday record for Martin Luther King Jr. Day.
        """
        day = self.get_martin_luther_king_date(year)
        return (day, self.martin_luther_king_label)

    def get_presidents_day(self, year):
        """
        Presidents Day is on the 3rd MON of February

        May be called Washington's or Lincoln's birthday
        """
        day = UnitedStates.get_nth_weekday_in_month(year, 2, MON, 3)
        return (day, self.presidents_day_label)

    def get_cesar_chavez_days(self, year):
        """
        Cesar Chavez day is on 31st of March, float to 1st April if Monday.

        Will return a list of days.
        """
        days = [(date(year, 3, 31), "Cesar Chavez Day")]
        if date(year, 3, 31).weekday() == SUN:
            days.append((date(year, 4, 1), "Cesar Chavez Day (Observed)"))
        return days

    def get_patriots_day(self, year):
        """3rd Monday of April"""
        return (self.get_nth_weekday_in_month(year, 4, MON, 3), "Patriots Day")

    def get_washington_birthday_december(self, year):
        """
        Floating observance, to give long weekend at christmas.
        It's only observed in Georgia and Indiana.
        """
        christmas_day = date(year, 12, 25).weekday()
        if christmas_day == MON:
            day = date(year, 12, 26)  # TUE
        elif christmas_day == TUE:
            day = date(year, 12, 24)  # MON
        elif christmas_day == WED:
            day = date(year, 12, 24)  # TUE
        elif christmas_day == THU:
            day = date(year, 12, 26)  # FRI
        elif christmas_day == FRI:
            day = date(year, 12, 24)  # THU
        elif christmas_day == SAT:
            day = date(year, 12, 23)  # THU
        else:  # christmas_day == SUN:
            day = date(year, 12, 23)  # FRI
        return (day, self.label_washington_birthday_december)

    def get_columbus_day(self, year):
        """
        Columbus day is on the 2nd MON of October.

        Only half of the states recognize it.
        """
        day = UnitedStates.get_nth_weekday_in_month(year, 10, MON, 2)
        return (day, self.columbus_day_label)

    def get_lincoln_birthday(self, year):
        """
        February the 2nd is Lincoln's birthday in the following States:

        * Connecticut,
        * Illinois,
        * Missouri,
        * New York
        """
        return (date(year, 2, 12), "Lincoln's Birthday")

    def get_inauguration_date(self, year):
        """
        If the year is an Inauguration Year, will return the Inauguration Day
        date.

        If this day falls on SUN, it's replaced by the next MON.
        If the year is not a Inauguration Year, it raises a ValueError.
        """
        if ((year - 1) % 4) != 0:
            raise ValueError(
                "The year {} is not an Inauguration Year".format(year))
        inauguration_day = date(year, 1, 20)
        if inauguration_day.weekday() == SUN:
            inauguration_day = date(year, 1, 21)
        return inauguration_day

    def get_national_memorial_day(self, year):
        """
        Return National Memorial Day
        """
        return (
            UnitedStates.get_last_weekday_in_month(year, 5, MON),
            self.national_memorial_day_label
        )

    def get_mardi_gras(self, year):
        """
        Mardi Gras is the Tuesday happening 47 days before Easter
        """
        sunday = self.get_easter_sunday(year)
        return (sunday - timedelta(days=47), "Mardi Gras")

    def get_variable_days(self, year):
        # usual variable days
        days = super(UnitedStates, self).get_variable_days(year)

        # Martin Luther King's Day started only in 1985
        if year >= 1985:
            days.append(self.get_martin_luther_king_day(year))

        days.extend([
            self.get_national_memorial_day(year),
            (UnitedStates.get_nth_weekday_in_month(year, 9, MON),
                "Labor Day"),
            (UnitedStates.get_nth_weekday_in_month(year, 11, THU, 4),
                "Thanksgiving Day"),
        ])

        if self.include_mardi_gras:
            days.append(self.get_mardi_gras(year))

        if self.include_federal_presidents_day:
            days.append(self.get_presidents_day(year))

        if self.include_lincoln_birthday:
            days.append(self.get_lincoln_birthday(year))

        if self.include_cesar_chavez_day:
            days.extend(self.get_cesar_chavez_days(year))

        if self.include_patriots_day:
            days.append(self.get_patriots_day(year))

        if self.include_columbus_day:
            days.append(self.get_columbus_day(year))

        if self.include_confederation_day:
            days.append(self.get_confederate_day(year))

        if self.include_inauguration_day:
            # Is it a "Inauguration year"?
            if UnitedStates.is_presidential_year(year - 1):
                days.append(
                    (self.get_inauguration_date(year), "Inauguration Day")
                )

        if self.include_election_day_every_year:
            days.append(self.get_election_day(year))
        elif self.include_election_day_even:
            if (year % 2) == 0:
                days.append(self.get_election_day(year))

        if self.include_thanksgiving_friday:
            days.append(
                self.get_thanksgiving_friday(year)
            )

        return days

    def get_veterans_day(self, year):
        """
        Return Veterans Day (November 11th).

        Placed here because some States are renaming it.
        """
        return (date(year, 11, 11), self.veterans_day_label)

    def get_fixed_holidays(self, year):
        days = super(UnitedStates, self).get_fixed_holidays(year)
        if self.include_veterans_day:
            days.append(self.get_veterans_day(year))
        return days

    def get_calendar_holidays(self, year):
        """
        Will return holidays and their shifted days
        """
        days = super(UnitedStates, self).get_calendar_holidays(year)
        days = self.shift(days, year)
        return days
