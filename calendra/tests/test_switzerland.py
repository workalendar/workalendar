from datetime import date

from . import GenericCalendarTest
from ..europe import (
    Aargau, AppenzellInnerrhoden, AppenzellAusserrhoden, Bern, BaselLandschaft,
    BaselStadt, Fribourg, Geneva, Glarus, Graubunden, Jura, Luzern, Neuchatel,
    Nidwalden, Obwalden, StGallen, Schaffhausen, Solothurn, Schwyz, Thurgau,
    Ticino, Uri, Vaud, Valais, Zug, Zurich
)


class AargauTest(GenericCalendarTest):
    cal_class = Aargau

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class AppenzellInnerrhodenTest(GenericCalendarTest):
    cal_class = AppenzellInnerrhoden

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class AppenzellAusserrhodenTest(GenericCalendarTest):
    cal_class = AppenzellAusserrhoden

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class BernTest(GenericCalendarTest):
    cal_class = Bern

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class BaselLandschaftTest(GenericCalendarTest):
    cal_class = BaselLandschaft

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class BaselStadtTest(GenericCalendarTest):
    cal_class = BaselStadt

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class FribourgTest(GenericCalendarTest):
    cal_class = Fribourg

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class GenevaTest(GenericCalendarTest):
    cal_class = Geneva

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        # Jeune Genevois, only in Geneva
        self.assertIn(date(2020, 9, 10), holidays)
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        # Restoration day - Geneva
        self.assertIn(date(2020, 12, 31), holidays)

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        # Jeune Genevois, only in Geneva
        self.assertIn(date(2021, 9, 9), holidays)
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        # Restoration day - Geneva
        self.assertIn(date(2021, 12, 31), holidays)


class GlarusTest(GenericCalendarTest):
    cal_class = Glarus

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        # Only in Glarus/Glaris
        self.assertIn(date(2020, 4, 3), holidays)   # Näfels Day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        # Only in Glarus/Glaris
        self.assertIn(date(2021, 4, 3), holidays)   # Näfels Day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class GraubundenTest(GenericCalendarTest):
    cal_class = Graubunden

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class JuraTest(GenericCalendarTest):
    cal_class = Jura

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        # Independance day - Only in Jura
        self.assertIn(date(2020, 6, 23), holidays)
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 25), holidays)  # XMas

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        # Independance day - Only in Jura
        self.assertIn(date(2021, 6, 23), holidays)
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 25), holidays)  # XMas


class LuzernTest(GenericCalendarTest):
    cal_class = Luzern

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class NeuchatelTest(GenericCalendarTest):
    cal_class = Neuchatel

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 3, 1), holidays)  # Republic Day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 3, 1), holidays)  # Republic Day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas


class NidwaldenTest(GenericCalendarTest):
    cal_class = Nidwalden

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class ObwaldenTest(GenericCalendarTest):
    cal_class = Obwalden

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 9, 25), holidays)  # Saint Nicholas of Flüe
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 9, 25), holidays)  # Saint Nicholas of Flüe
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class StGallenTest(GenericCalendarTest):
    cal_class = StGallen

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class SchaffhausenTest(GenericCalendarTest):
    cal_class = Schaffhausen

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class SolothurnTest(GenericCalendarTest):
    cal_class = Solothurn

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class SchwyzTest(GenericCalendarTest):
    cal_class = Schwyz

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class ThurgauTest(GenericCalendarTest):
    cal_class = Thurgau

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class TicinoTest(GenericCalendarTest):
    cal_class = Ticino

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        # St Peter & St Paul - Only in Ticino
        self.assertIn(date(2020, 6, 29), holidays)
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        # St Peter & St Paul - Only in Ticino
        self.assertIn(date(2021, 6, 29), holidays)
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class UriTest(GenericCalendarTest):
    cal_class = Uri

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class VaudTest(GenericCalendarTest):
    cal_class = Vaud

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        # Lundi du Jeûne - Only in Vaud
        self.assertIn(date(2020, 9, 21), holidays)
        self.assertIn(date(2020, 12, 25), holidays)  # XMas

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        # Lundi du Jeûne - Only in Vaud
        self.assertIn(date(2021, 9, 20), holidays)
        self.assertIn(date(2021, 12, 25), holidays)  # XMas


class ValaisTest(GenericCalendarTest):
    cal_class = Valais

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 3, 19), holidays)  # St Joseph
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas


class ZugTest(GenericCalendarTest):
    cal_class = Zug

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints
        self.assertIn(date(2020, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 6, 3), holidays)  # Corpus Christi
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 8, 15), holidays)  # Assumption
        self.assertIn(date(2021, 11, 1), holidays)  # All Saints
        self.assertIn(date(2021, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day


class ZurichTest(GenericCalendarTest):
    cal_class = Zurich

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New years day
        self.assertIn(date(2020, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen's day

    def test_year_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New years day
        self.assertIn(date(2021, 1, 2), holidays)  # Berchtolds
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 13), holidays)  # Ascension day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 1), holidays)  # Swiss National Day
        self.assertIn(date(2021, 12, 25), holidays)  # XMas
        self.assertIn(date(2021, 12, 26), holidays)  # St Stephen's day
