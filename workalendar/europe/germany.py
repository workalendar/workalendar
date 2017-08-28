# -*- coding: utf-8 -*-
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin


class Germany(WesternCalendar, ChristianMixin):
    "Germany"
    iso = 'DE'
    name = 'Germany'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (10, 3, "Day of German Unity"),
    )

    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_good_friday = True
    include_boxing_day = True
    boxing_day_label = "Second Christmas Day"
    # German-specific holiday
    include_reformation_day = False

    def get_reformation_day(self, year):
        """
        Reformation Day is a fixed date.

        It's handled via the variable_days because it can be activated
        depending on the Länder or the year (see #150).
        """
        day = date(year, 10, 31)
        return (day, "Reformation Day")

    def get_variable_days(self, year):
        days = super(Germany, self).get_variable_days(year)
        if self.include_reformation_day or year == 2017:
            days.append(self.get_reformation_day(year))
        return days


class BadenWurttemberg(Germany):
    "Baden-Württemberg"
    iso = 'DE-BW'
    name = "Baden-Wuerttemberg"

    include_epiphany = True
    include_corpus_christi = True
    include_all_saints = True


class Bavaria(Germany):
    "Bavaria"
    iso = 'DE-BY'
    name = 'Bavaria'

    include_epiphany = True
    include_corpus_christi = True
    include_all_saints = True
    include_assumption = True


class Berlin(Germany):
    "Berlin"
    iso = 'DE-BE'
    name = 'Berlin'


class Brandenburg(Germany):
    "Brandenburg"
    iso = 'DE-BB'
    name = 'Brandenburg'

    include_easter_sunday = True
    include_reformation_day = True


class Bremen(Germany):
    "Bremen"
    iso = 'DE-HB'
    name = 'Bremen'


class Hamburg(Germany):
    "Hamburg"
    iso = 'DE-HH'
    name = 'Hamburg'


class Hesse(Germany):
    "Hesse"
    iso = 'DE-HE'
    name = 'Hesse'

    include_corpus_christi = True


class MecklenburgVorpommern(Germany):
    "Mecklenburg-Vorpommern"
    iso = 'DE-MV'
    name = 'Mecklenburg-Western Pomerania'

    include_reformation_day = True


class LowerSaxony(Germany):
    "Lower Saxony"
    iso = 'DE-NI'
    name = 'Lower Saxony'


class NorthRhineWestphalia(Germany):
    "North Rhine-Westphalia"
    iso = 'DE-NW'
    name = 'North Rhine-Westphalia'

    include_corpus_christi = True
    include_all_saints = True


class RhinelandPalatinate(Germany):
    "Rhineland-Palatinate"
    iso = 'DE-RP'
    name = 'Rhineland-Palatinate'

    include_corpus_christi = True
    include_all_saints = True


class Saarland(Germany):
    "Saarland"
    iso = 'DE-SL'
    name = 'Saarland'

    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True


class Saxony(Germany):
    "Saxony"
    iso = 'DE-SN'
    name = 'Saxony'

    include_reformation_day = True

    def get_repentance_day(self, year):
        "Wednesday before November 23"
        day = date(year, 11, 22)
        while day.weekday() != 2:  # 2=Wednesday
            day -= timedelta(days=1)
        return (day, "Repentance Day")

    def get_variable_days(self, year):
        days = super(Saxony, self).get_variable_days(year)
        days.append(self.get_repentance_day(year))
        return days


class SaxonyAnhalt(Germany):
    "Saxony-Anhalt"
    iso = 'DE-ST'
    name = 'Saxony-Anhalt'

    include_epiphany = True
    include_reformation_day = True


class SchleswigHolstein(Germany):
    "Schleswig-Holstein"
    iso = 'DE-SH'
    name = 'Schleswig-Holstein'


class Thuringia(Germany):
    "Thuringia"
    iso = 'DE-TH'
    name = 'Thuringia'

    include_reformation_day = True
