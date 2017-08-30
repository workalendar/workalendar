# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.registry import iso_register


@iso_register('DE')
class Germany(WesternCalendar, ChristianMixin):
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


@iso_register('DE-BW')
class BadenWurttemberg(Germany):
    name = "Baden-Wuerttemberg"

    include_epiphany = True
    include_corpus_christi = True
    include_all_saints = True


@iso_register('DE-BY')
class Bavaria(Germany):
    name = 'Bavaria'

    include_epiphany = True
    include_corpus_christi = True
    include_all_saints = True
    include_assumption = True


@iso_register('DE-BE')
class Berlin(Germany):
    name = 'Berlin'


@iso_register('DE-BB')
class Brandenburg(Germany):
    name = 'Brandenburg'

    include_easter_sunday = True
    include_reformation_day = True


@iso_register('DE-HB')
class Bremen(Germany):
    name = 'Bremen'


@iso_register('DE-HH')
class Hamburg(Germany):
    name = 'Hamburg'


@iso_register('DE-HE')
class Hesse(Germany):
    name = 'Hesse'

    include_corpus_christi = True


@iso_register('DE-MV')
class MecklenburgVorpommern(Germany):
    name = 'Mecklenburg-Western Pomerania'

    include_reformation_day = True


@iso_register('DE-NI')
class LowerSaxony(Germany):
    name = 'Lower Saxony'


@iso_register('DE-NW')
class NorthRhineWestphalia(Germany):
    name = 'North Rhine-Westphalia'

    include_corpus_christi = True
    include_all_saints = True


@iso_register('DE-RP')
class RhinelandPalatinate(Germany):
    name = 'Rhineland-Palatinate'

    include_corpus_christi = True
    include_all_saints = True


@iso_register('DE-SL')
class Saarland(Germany):
    name = 'Saarland'

    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True


@iso_register('DE-SN')
class Saxony(Germany):
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


@iso_register('DE-ST')
class SaxonyAnhalt(Germany):
    name = 'Saxony-Anhalt'

    include_epiphany = True
    include_reformation_day = True


@iso_register('DE-SH')
class SchleswigHolstein(Germany):
    name = 'Schleswig-Holstein'


@iso_register('DE-TH')
class Thuringia(Germany):
    name = 'Thuringia'

    include_reformation_day = True
