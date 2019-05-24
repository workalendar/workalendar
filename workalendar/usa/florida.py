# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import date, timedelta
import warnings
from pyluach.dates import GregorianDate

from .core import UnitedStates
from ..registry import iso_register


class HebrewHolidays(object):

    hebrew_calendars = {}

    @classmethod
    def get_hebrew_calendar(cls, gregorian_year):
        """
        Build and cache the Hebrew calendar for the given Gregorian Year.
        """
        if gregorian_year not in cls.hebrew_calendars:
            # Build the hebrew calendar for year
            days = []
            current_date = date(gregorian_year, 1, 1)

            while current_date.year == gregorian_year:
                hebrew_date = GregorianDate(
                    year=current_date.year,
                    month=current_date.month,
                    day=current_date.day,
                ).to_heb()
                days.append(
                    (hebrew_date, current_date)
                )
                current_date += timedelta(days=1)
            # Store it in the class property
            cls.hebrew_calendars[gregorian_year] = days

        # Return the hebrew calendar
        return cls.hebrew_calendars[gregorian_year]

    @classmethod
    def search_hebrew_calendar(cls, gregorian_year, hebrew_month, hebrew_day):
        """
        Search for a specific Hebrew month and day in the Hebrew calendar.
        """
        calendar = cls.get_hebrew_calendar(gregorian_year)
        search = filter(lambda item: item[0].month == hebrew_month, calendar)
        search = filter(lambda item: item[0].day == hebrew_day, search)
        for item in search:
            return item[1]

    @classmethod
    def get_rosh_hashanah(cls, year):
        """
        Return the gregorian date of the first day of Rosh Hashanah
        """
        return cls.search_hebrew_calendar(year, 7, 1)

    @classmethod
    def get_yom_kippur(cls, year):
        """
        Return the gregorian date of Yom Kippur.
        """
        return cls.search_hebrew_calendar(year, 7, 10)


@iso_register('US-FL')
class Florida(UnitedStates):
    """Florida"""
    include_thanksgiving_friday = True
    thanksgiving_friday_label = "Friday after Thanksgiving"
    include_columbus_day = False
    include_federal_presidents_day = False


class FloridaLegal(Florida):
    """Florida Legal Holidays"""
    FIXED_HOLIDAYS = Florida.FIXED_HOLIDAYS + (
        (2, 15, 'Susan B. Anthony Day'),
        (4, 2, 'Pascua Florida Day'),
        (6, 14, 'Flag Day'),
    )
    include_mardi_gras = True
    include_lincoln_birthday = True
    include_federal_presidents_day = True
    include_good_friday = True
    include_confederation_day = True
    include_jefferson_davis_birthday = True
    include_columbus_day = True
    columbus_day_label = "Columbus Day and Farmers' Day"
    include_election_day_every_year = True

    def __init__(self, *args, **kwargs):
        super(FloridaLegal, self).__init__(*args, **kwargs)
        warnings.warn(
            "Florida's laws separate the definitions between paid versus legal"
            " holidays. Be warned that Florida Legal specific Holidays are not"
            " paid holidays."
        )

    def get_confederate_day(self, year):
        """
        Confederation memorial day is on the April 26th for Florida Legal.
        """
        return (date(year, 4, 26), "Confederate Memorial Day")

    def get_jefferson_davis_birthday(self, year):
        """
        Jefferson Davis Birthday appears to be a fixed holiday (June 3rd)
        """
        return (date(year, 6, 3), "Jefferson Davis Birthday")


class FloridaCircuitCourts(HebrewHolidays, Florida):
    """Florida Circuits Courts"""
    include_federal_presidents_day = True
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(FloridaCircuitCourts, self).get_variable_days(year)

        days.append((
            self.get_rosh_hashanah(year),
            "Rosh Hashanah"
        ))

        days.append((
            self.get_yom_kippur(year),
            "Yom Kippur"
        ))

        return days


class FloridaMiamiDade(Florida):
    """Miami-Dade, Florida"""
    include_federal_presidents_day = True
    include_columbus_day = True
