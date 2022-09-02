from datetime import date, timedelta

from dateutil import relativedelta as rd

from ..core import WesternCalendar
from ..core import SUN, MON, TUE, THU
from ..core import Holiday
from ..registry_tools import iso_register


@iso_register('US')
class UnitedStates(WesternCalendar):
    "United States of America"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        Holiday(
            date(2000, 7, 4),
            'Independence Day',
            indication='July 4',
        ),
    )

    @property
    def observance_shift(self):
        return Holiday.nearest_weekday

    # Veterans day label
    include_veterans_day = False
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
    # Jefferson Davis Birthday.
    include_jefferson_davis_birthday = False

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
    include_fat_tuesday = False
    fat_tuesday_label = "Mardi Gras"

    # Shift day mechanism
    # These days won't be shifted to next MON or previous FRI
    shift_exceptions = (
        # Example:
        # (11, 11),  # Veterans day won't be shifted
    )

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
        return self.get_election_date(year), self.election_day_label

    def get_thanksgiving_friday(self, year):
        """
        Thanksgiving friday is on the day following Thanksgiving Day
        """
        thanksgiving = UnitedStates.get_nth_weekday_in_month(year, 11, THU, 4)
        thanksgiving_friday = thanksgiving + timedelta(days=1)
        return thanksgiving_friday, self.thanksgiving_friday_label

    def get_confederate_day(self, year):
        """
        Confederate memorial day is on the 4th MON of April.
        """
        day = self.get_nth_weekday_in_month(year, 4, MON, 4)
        return day, "Confederate Memorial Day"

    def get_jefferson_davis_birthday(self, year):
        """
        The first MON of June is Jefferson Davis Birthday
        """
        return (
            self.get_nth_weekday_in_month(year, 6, MON, 1),
            "Jefferson Davis Birthday"
        )

    def get_martin_luther_king_date(self, year):
        if year < 1985:
            raise ValueError(
                "Martin Luther King Day became a holiday in 1985"
            )
        return date(year, 1, 1) + rd.relativedelta(weekday=rd.MO(3))

    def get_martin_luther_king_day(self, year):
        """
        Return holiday record for Martin Luther King Jr. Day.
        """
        return Holiday(
            self.get_martin_luther_king_date(year),
            self.martin_luther_king_label,
            indication="3rd Monday in January",
        )

    def get_presidents_day(self, year):
        """
        Presidents Day is on the 3rd MON of February

        May be called Washington's or Lincoln's birthday
        """
        return Holiday(
            date(year, 2, 1) + rd.relativedelta(weekday=rd.MO(3)),
            self.presidents_day_label,
            indication="3rd Monday in February",
        )

    def get_cesar_chavez_days(self, year):
        """
        Cesar Chavez day is on 31st of March

        Will return a list of days, because in some states (California),
        it can float to MON if it happens on SUN.
        """
        days = [(date(year, 3, 31), "Cesar Chavez Day")]
        return days

    def get_patriots_day(self, year):
        """3rd Monday of April"""
        return self.get_nth_weekday_in_month(year, 4, MON, 3), "Patriots Day"

    def get_columbus_day(self, year):
        """
        Columbus day is on the 2nd MON of October.

        Only half of the states recognize it.
        """
        return Holiday(
            date(year, 10, 1) + rd.relativedelta(weekday=rd.MO(2)),
            self.columbus_day_label,
            indication="2nd Monday in October",
        )

    def get_lincoln_birthday(self, year):
        """
        February the 2nd is Lincoln's birthday in the following States:

        * Connecticut,
        * Illinois,
        * Missouri,
        * New York
        """
        return date(year, 2, 12), "Lincoln's Birthday"

    def get_inauguration_date(self, year):
        """
        If the year is an Inauguration Year, will return the Inauguration Day
        date.

        If this day falls on SUN, it's replaced by the next MON.
        If the year is not a Inauguration Year, it raises a ValueError.
        """
        if ((year - 1) % 4) != 0:
            raise ValueError(
                f"The year {year} is not an Inauguration Year")
        inauguration_day = date(year, 1, 20)
        if inauguration_day.weekday() == SUN:
            inauguration_day = date(year, 1, 21)
        return inauguration_day

    def get_national_memorial_day(self, year):
        return Holiday(
            date(year, 5, 31) + rd.relativedelta(weekday=rd.MO(-1)),
            self.national_memorial_day_label,
            indication="Last Monday in May",
        )

    def get_variable_days(self, year):  # noqa: C901
        # usual variable days
        days = super().get_variable_days(year)

        days += [
            self.get_veterans_day(year),
            self.get_national_memorial_day(year),
            Holiday(
                date(year, 9, 1) + rd.relativedelta(weekday=rd.MO(1)),
                "Labor Day",
                indication="1st Monday in September",
            ),

            Holiday(
                date(year, 11, 1) + rd.relativedelta(weekday=rd.TH(4)),
                "Thanksgiving Day",
                indication="4th Thursday in November",
            ),
        ]

        # Martin Luther King's Day started only in 1985
        if year >= 1985:
            days.append(self.get_martin_luther_king_day(year))

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

        if self.include_jefferson_davis_birthday:
            days.append(self.get_jefferson_davis_birthday(year))

        ind = "January 20 (or 21st if Sunday) following an election year"
        if self.include_inauguration_day:
            # Is it a "Inauguration year"?
            if UnitedStates.is_presidential_year(year - 1):
                days.append(
                    Holiday(
                        self.get_inauguration_date(year),
                        "Inauguration Day",
                        indication=ind,
                    ),
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
        return Holiday(
            date(year, 11, 11),
            self.veterans_day_label,
            indication='Nov 11',
        )

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)
        if self.include_veterans_day:
            days.append(self.get_veterans_day(year))
        return days
