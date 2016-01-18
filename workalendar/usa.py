# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin, Calendar
from workalendar.core import SUN, MON, TUE, WED, THU, FRI, SAT

NONE, NEAREST_WEEKDAY, MONDAY = range(3)


class UnitedStates(WesternCalendar, ChristianMixin):
    "United States of America"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 4, 'Independence Day'),
        (11, 11, 'Veterans Day'),
    )

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_variable_days(self, year):
        # usual variable days
        days = super(UnitedStates, self).get_variable_days(year)
        days += [
            (UnitedStates.get_nth_weekday_in_month(year, 1, MON, 3),
                'Martin Luther King, Jr. Day'),

            (UnitedStates.get_nth_weekday_in_month(year, 2, MON, 3),
                "Washington's Birthday"),

            (UnitedStates.get_last_weekday_in_month(year, 5, MON),
                "Memorial Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 9, MON),
                "Labor Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 10, MON, 2),
                "Colombus Day"),

            (UnitedStates.get_nth_weekday_in_month(year, 11, THU, 4),
                "Thanksgiving Day"),
        ]
        # Inauguration day
        if UnitedStates.is_presidential_year(year - 1):
            inauguration_day = date(year, 1, 20)
            if inauguration_day.weekday() == SUN:
                inauguration_day = date(year, 1, 21)
            days.append((inauguration_day, "Inauguration Day"))
        return days


class FloatToNearestWeekdayMixin(Calendar):
    "Float Saturady to Friday, Sunday to Monday"
    def float(self, holidays, year=0):
        new_holidays = []
        holiday_lookup = [x[0] for x in holidays]
        for holiday in holidays:
            if holiday[0].weekday() == SAT:
                new_holidays.append((holiday[0] - timedelta(days=1),
                                     holiday[1] + " (Observed)"))
            elif holiday[0].weekday() == SUN:
                new_holidays.append((holiday[0] + timedelta(days=1),
                                     holiday[1] + " (Observed)"))

        if year > 0 and date(year + 1, 1, 1).weekday() == SAT:
            new_holidays.append((date(year, 12, 31,),
                                 "New Years Day (Observed)"))

        year = holiday_lookup[0].year
        if (date(year, 12, 25) in holiday_lookup and
                date(year, 12, 24) in holiday_lookup and
                date(year, 12, 25).weekday() == SAT):
            new_holidays.append((date(year, 12, 23),
                                 "Christmas Eve (Observed)"))
        if (date(year, 12, 25) in holiday_lookup and
                date(year, 12, 24) in holiday_lookup and
                date(year, 12, 25).weekday() == MON):
            new_holidays.append((date(year, 12, 26),
                                 "Christmas Eve (Observed)"))
            new_holidays.append((date(year, 12, 27),
                                 "Christmas Day (Observed)"))
        return holidays + new_holidays


class WashingtonsBirthdayInDecemberMixin(Calendar):
    """Floating observance, to give long weekend at christmas"""
    def get_washington_birthday(self, year,
                                label="Washington's Birthday (Observed)"):
        christmas_day = date(year, 12, 25).weekday()
        if christmas_day == MON:
            day = (date(year, 12, 26), label)  # TUE
        elif christmas_day == TUE:
            day = (date(year, 12, 24), label)  # MON
        elif christmas_day == WED:
            day = (date(year, 12, 24), label)  # TUE
        elif christmas_day == THU:
            day = (date(year, 12, 26), label)  # FRI
        elif christmas_day == FRI:
            day = (date(year, 12, 24), label)  # THU
        elif christmas_day == SAT:
            day = (date(year, 12, 23), label)  # THU
        else:  # christmas_day == SUN:
            day = (date(year, 12, 23), label)  # FRI
        return day


class CesarChavezDayMixin(Calendar):
    """31st of March, float to 1st April if Monday"""
    def get_chavez_day(self, year):
        days = [(date(year, 3, 31), "Cesar Chavez Day")]
        if date(year, 3, 31).weekday() == SUN:
            days += [(date(year, 4, 1), "Cesar Chavez Day (Observed)")]
        return days


class MardiGrasMixin(ChristianMixin):
    """Tuesday before Ash Wednesday"""
    def get_mardis_gras(self, year):
        sunday = self.get_easter_sunday(year)
        return (sunday - timedelta(days=47), "Mardi Gras")


class DayAfterChristmasNoFloatMixin(Calendar):
    """26th of December - but doesn't ever float"""
    def get_day_after_christmas(self, year):
        days = (date(year, 12, 26), "Day After Christmas")
        return days


class PatriotsDayMixin(Calendar):
    """3rd Monday of April"""
    def get_patriots_day(self, year):
        days = (self.get_nth_weekday_in_month(year, 4, MON, 3),
                "Patriots Day")
        return days


class ConfederateMemorialDayMixin(Calendar):
    """4th Monday of April"""
    def get_confederate_day(self, year):
        return (Alabama.get_nth_weekday_in_month(year, 4, MON, 4),
                "Confederate Day")


class ThanksgivingFridayMixin(Calendar):
    "4th Friday in November"
    def get_thanksgiving_friday(self, year, label="Thanksgiving Friday"):
        return (self.get_nth_weekday_in_month(year, 11, FRI, 4), label)


class Alabama(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
              ConfederateMemorialDayMixin):
    "Alabama"
    def get_variable_days(self, year):
        days = super(Alabama, self).get_variable_days(year)
        days = super(Alabama, self).float(days)
        days = days + [self.get_confederate_day(year)]
        days = days + [(Alabama.get_nth_weekday_in_month(year, 6, MON, 1),
                        "Jefferson Davis Birthday")]
        return days

    def get_fixed_holidays(self, year):
        days = super(Alabama, self).get_fixed_holidays(year)
        days = super(Alabama, self).float(days, year)
        return days


class Alaska(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Alaska"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (10, 18, 'Alaska Day'),
    )

    def get_variable_days(self, year):
        days = super(Alaska, self).get_variable_days(year)
        days = super(Alaska, self).float(days)
        days = days + [(Alabama.get_last_weekday_in_month(year, 3, MON),
                        "Seward's Day")]
        return days

    def get_fixed_holidays(self, year):
        days = super(Alaska, self).get_fixed_holidays(year)
        days = super(Alaska, self).float(days, year)
        return days


class Arizona(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Arizona"""
    def get_variable_days(self, year):
        days = super(Arizona, self).get_variable_days(year)
        days = super(Arizona, self).float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Arizona, self).get_fixed_holidays(year)
        days = super(Arizona, self).float(days, year)
        return days


class Arkansas(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Arkansas"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(Arkansas, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Arkansas, self).get_fixed_holidays(year)
        days = super(Arkansas, self).float(days, year)
        return days


class California(UnitedStates, WesternCalendar, ThanksgivingFridayMixin,
                 FloatToNearestWeekdayMixin, CesarChavezDayMixin):
    """California"""
    def get_variable_days(self, year):
        days = super(California, self).get_variable_days(year)
        days += [self.get_thanksgiving_friday(year)]
        days += [(self.get_nth_weekday_in_month(year, 10, MON, 2),
                  "Indingenous People's Day")]
        days += self.get_chavez_day(year)
        return days

    def get_fixed_holidays(self, year):
        days = super(California, self).get_fixed_holidays(year)
        days = super(California, self).float(days, year)
        return days


class Colorado(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               CesarChavezDayMixin):
    """Colorado"""

    def get_variable_days(self, year):
        days = super(Colorado, self).get_variable_days(year)
        days += self.get_chavez_day(year)
        return days

    def get_fixed_holidays(self, year):
        days = super(Colorado, self).get_fixed_holidays(year)
        days = super(Colorado, self).float(days, year)
        return days


class Connecticut(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Connecticut"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
    )

    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Connecticut, self).get_variable_days(year)
        days = super(Connecticut, self).float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Connecticut, self).get_fixed_holidays(year)
        days = super(Connecticut, self).float(days, year)
        return days


class Delaware(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin):
    """Delaware"""

    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Delaware, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Delaware, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Florida(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Florida"""
    def get_variable_days(self, year):
        days = super(Florida, self).get_variable_days(year)
        days = super(Florida, self).float(days)
        days = days + [(Florida.get_nth_weekday_in_month(year, 11, FRI, 4),
                        "Friday after Thanksgiving")]
        return days

    def get_fixed_holidays(self, year):
        days = super(Florida, self).get_fixed_holidays(year)
        days = super(Florida, self).float(days, year)
        return days


class Georgia(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
              WashingtonsBirthdayInDecemberMixin, ConfederateMemorialDayMixin):
    """Georgia"""
    def get_variable_days(self, year):
        days = super(Georgia, self).get_variable_days(year)
        days = super(Georgia, self).float(days)
        days += [self.get_confederate_day(year)]
        days += [(Georgia.get_nth_weekday_in_month(year, 11, FRI, 4),
                  "Robert E. Lee's Birthday (Observed)")]
        days += [self.get_washington_birthday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Georgia, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Hawaii(UnitedStates, WesternCalendar):
    """Hawaii"""
    pass


class Idaho(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Idaho"""
    def get_variable_days(self, year):
        days = super(Idaho, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Idaho, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Illinois(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin):
    """Illinois"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
    )

    def get_variable_days(self, year):
        days = super(Illinois, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Illinois, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Indiana(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
              WashingtonsBirthdayInDecemberMixin, ThanksgivingFridayMixin):
    """Indiana"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Indiana, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_washington_birthday(year)]
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Indiana, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Iowa(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
           ThanksgivingFridayMixin):
    """Iowa"""
    def get_variable_days(self, year):
        days = super(Iowa, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Iowa, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Kansas(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
             ThanksgivingFridayMixin, DayAfterChristmasNoFloatMixin):
    """Kansas"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(Kansas, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [self.get_day_after_christmas(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Kansas, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Kentucky(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin, DayAfterChristmasNoFloatMixin):
    """Kentucky"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Kentucky, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [self.get_day_after_christmas(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Kentucky, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Louisiana(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                MardiGrasMixin):
    """Louisiana"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Louisiana, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_mardis_gras(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Louisiana, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Maine(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
            PatriotsDayMixin, ThanksgivingFridayMixin):
    """Maine"""

    def get_variable_days(self, year):
        days = super(Maine, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_patriots_day(year)]
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Maine, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Maryland(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin):
    """Maryland"""
    def get_variable_days(self, year):
        days = super(Maryland, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Maryland, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Massachusetts(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                    PatriotsDayMixin):
    """Massachusetts"""
    def get_variable_days(self, year):
        days = super(Massachusetts, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_patriots_day(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Massachusetts, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Michigan(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin):
    """Michigan"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(Michigan, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Michigan, self).get_fixed_holidays(year)
        days += [(date(year, 12, 31), "New Years Eve")]
        days = self.float(days, year)
        return days


class Minnesota(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                ThanksgivingFridayMixin):
    """Minnesota"""
    def get_variable_days(self, year):
        days = super(Minnesota, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Minnesota, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Mississippi(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                  ThanksgivingFridayMixin, ConfederateMemorialDayMixin):
    """Mississippi"""
    def get_variable_days(self, year):
        days = super(Mississippi, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_confederate_day(year)]
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Mississippi, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Missouri(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Missouri"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
        (5, 8, "Truman Day"),
    )

    def get_variable_days(self, year):
        days = super(Missouri, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Missouri, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Montana(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Montana"""

    def get_variable_days(self, year):
        days = super(Montana, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Montana, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Nebraska(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin):
    """Nebraska"""
    def get_variable_days(self, year):
        days = super(Nebraska, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [(self.get_last_weekday_in_month(year, 4, FRI),
                  "Arbor Day")]
        return days

    def get_fixed_holidays(self, year):
        days = super(Nebraska, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Nevada(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
             ThanksgivingFridayMixin):
    """Nevada"""
    def get_variable_days(self, year):
        days = super(Nevada, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [(self.get_last_weekday_in_month(year, 10, FRI),
                  "Nevada Day")]
        return days

    def get_fixed_holidays(self, year):
        days = super(Nevada, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class NewHampshire(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                   ThanksgivingFridayMixin):
    """NewHampshire"""
    def get_variable_days(self, year):
        days = super(NewHampshire, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(NewHampshire, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class NewJersey(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """NewJersey"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(NewJersey, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(NewJersey, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class NewMexico(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                ThanksgivingFridayMixin):
    """NewMexico"""
    def get_variable_days(self, year):
        days = super(NewMexico, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(NewMexico, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class NewYork(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """NewYork"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (2, 12, "Lincoln's Birthday"),
    )

    def get_variable_days(self, year):
        days = super(NewYork, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(NewYork, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class NorthCarolina(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                    ThanksgivingFridayMixin, DayAfterChristmasNoFloatMixin):
    """NorthCarolina"""
    include_good_friday = True
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(NorthCarolina, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [self.get_day_after_christmas(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(NorthCarolina, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class NorthDakota(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """NorthDakota"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(NorthDakota, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(NorthDakota, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Ohio(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Ohio"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (12, 1, "Rosa Parks Day"),
    )

    def get_variable_days(self, year):
        days = super(Ohio, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Ohio, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Oklahoma(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin):
    """Oklahoma"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(Oklahoma, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Oklahoma, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Oregon(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Oregon"""

    def get_variable_days(self, year):
        days = super(Oregon, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Oregon, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Pennsylvania(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                   ThanksgivingFridayMixin):
    """Pennsylvania"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Pennsylvania, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Pennsylvania, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class RhodeIsland(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """RhodeIsland"""

    def get_variable_days(self, year):
        days = super(RhodeIsland, self).get_variable_days(year)
        days = self.float(days)
        days += [(self.get_nth_weekday_in_month(year, 8, MON, 2),
                  "Victory Day")]
        return days

    def get_fixed_holidays(self, year):
        days = super(RhodeIsland, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class SouthCarolina(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                    ThanksgivingFridayMixin, DayAfterChristmasNoFloatMixin):
    """SouthCarolina"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (5, 10, "Confederate Memorial Day"),
    )
    include_good_friday = True
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(SouthCarolina, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [self.get_day_after_christmas(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(SouthCarolina, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class SouthDakota(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """SouthDakota"""
    def get_variable_days(self, year):
        days = super(SouthDakota, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(SouthDakota, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Tennessee(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                ThanksgivingFridayMixin):
    """Tennessee"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Tennessee, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Tennessee, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Texas(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
            CesarChavezDayMixin):
    """Texas"""
    include_good_friday = True

    def get_variable_days(self, year):
        days = super(Texas, self).get_variable_days(year)
        days = self.float(days)
        days += self.get_chavez_day(year)
        return days

    def get_fixed_holidays(self, year):
        days = super(Texas, self).get_fixed_holidays(year)
        days = self.float(days, year)
        days += [(date(year, 1, 19), "Confederate Heroes Day")]
        days += [(date(year, 3, 2), "Texas Independence Day")]
        days += [(date(year, 4, 21), "San Jacinto Day")]
        days += [(date(year, 6, 19), "Emancipation Day")]
        days += [(date(year, 8, 27), "Lyndon B. Jonhson Day")]
        return days


class Utah(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Utah"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (7, 24, "Pioneer Day"),
    )

    def get_variable_days(self, year):
        days = super(Utah, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Utah, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Vermont(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Vermont"""
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (8, 16, "Bennington Battle Day"),
    )

    def get_variable_days(self, year):
        days = super(Vermont, self).get_variable_days(year)
        days = self.float(days)
        days += [(self.get_nth_weekday_in_month(year, 3, TUE, 1),
                  "Town Meeting Day")]
        return days

    def get_fixed_holidays(self, year):
        days = super(Vermont, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class Virginia(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
               ThanksgivingFridayMixin, DayAfterChristmasNoFloatMixin):
    """Virginia"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(Virginia, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [(self.get_nth_weekday_in_month(year, 1, FRI, 3),
                  "Lee-Jackson Day")]
        days += [(self.get_nth_weekday_in_month(year, 11, WED, 4),
                  "Additional Thanksgiving Holiday")]
        return days

    def get_fixed_holidays(self, year):
        days = super(Virginia, self).get_fixed_holidays(year)
        days = self.float(days, year)
        days += [self.get_day_after_christmas(year)]
        return days


class Washington(UnitedStates, WesternCalendar, ThanksgivingFridayMixin,
                 FloatToNearestWeekdayMixin):
    """Washington"""
    def get_variable_days(self, year):
        days = super(Washington, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Washington, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days


class WestVirginia(UnitedStates, WesternCalendar, ThanksgivingFridayMixin,
                   FloatToNearestWeekdayMixin):
    """WestVirginia"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(WestVirginia, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        days += [(date(year, 6, 20), "West Virgina Day")]
        if date(year, 6, 20).weekday() == SUN:
            days += [(date(year, 6, 21), "West Virgina Day (Observed)")]

        return days

    def get_fixed_holidays(self, year):
        days = super(WestVirginia, self).get_fixed_holidays(year)
        days = self.float(days, year)
        days += [(date(year, 12, 31), "New Years Eve")]
        return days


class Wisconsin(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin,
                ThanksgivingFridayMixin):
    """Wisconsin"""
    include_christmas_eve = True

    def get_variable_days(self, year):
        days = super(Wisconsin, self).get_variable_days(year)
        days = self.float(days)
        days += [self.get_thanksgiving_friday(year)]
        return days

    def get_fixed_holidays(self, year):
        days = super(Wisconsin, self).get_fixed_holidays(year)
        days += [(date(year, 12, 31), "New Years Eve")]
        days = self.float(days, year)
        return days


class Wyoming(UnitedStates, WesternCalendar, FloatToNearestWeekdayMixin):
    """Wyoming"""
    def get_variable_days(self, year):
        days = super(Wyoming, self).get_variable_days(year)
        days = self.float(days)
        return days

    def get_fixed_holidays(self, year):
        days = super(Wyoming, self).get_fixed_holidays(year)
        days = self.float(days, year)
        return days
