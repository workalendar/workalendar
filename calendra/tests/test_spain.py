from datetime import date

from . import GenericCalendarTest
from ..europe import (
    Spain, Andalusia, Aragon, Catalonia, CastileAndLeon, CastillaLaMancha,
    CanaryIslands, Extremadura, Galicia, BalearicIslands, LaRioja,
    CommunityofMadrid, Murcia, Navarre, Asturias, BasqueCountry, Cantabria,
    ValencianCommunity
)


class SpainTest(GenericCalendarTest):
    cal_class = Spain

    def test_common_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)    # New Year
        self.assertIn(date(2015, 1, 6), holidays)    # Epiphany
        self.assertIn(date(2015, 4, 3), holidays)    # Good Friday
        self.assertIn(date(2015, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2015, 8, 15), holidays)   # Assumption
        self.assertIn(date(2015, 10, 12), holidays)  # Nation Day
        self.assertIn(date(2015, 11, 1), holidays)   # All Saints
        self.assertIn(date(2015, 12, 6), holidays)   # Dia de la Constitución
        self.assertIn(date(2015, 12, 8), holidays)   # Immaculate conception
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas

    def test_common_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)    # New Year
        self.assertIn(date(2016, 1, 6), holidays)    # Epiphany
        self.assertIn(date(2016, 3, 25), holidays)   # Good Friday
        self.assertIn(date(2016, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2016, 8, 15), holidays)   # Assumption
        self.assertIn(date(2016, 10, 12), holidays)  # Nation Day
        self.assertIn(date(2016, 11, 1), holidays)   # All Saints
        self.assertIn(date(2016, 12, 6), holidays)   # Dia de la Constitución
        self.assertIn(date(2016, 12, 8), holidays)   # Immaculate conception
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "Día del trabajador")


class AndalusiaTest(SpainTest):
    cal_class = Andalusia

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 2, 28), holidays)  # Andalusian National Day
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 2, 28), holidays)  # Andalusian National Day
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertEqual(len(holidays), 12)


class AragonTest(SpainTest):
    cal_class = Aragon

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 4, 23), holidays)  # Regional Day
        self.assertIn(date(2019, 12, 20), holidays)  # Aragon Ombudsman Day
        self.assertEqual(len(holidays), 13)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 4, 23), holidays)  # Regional Day
        self.assertIn(date(2020, 12, 20), holidays)  # Aragon Ombudsman Day
        self.assertEqual(len(holidays), 13)


class CastileAndLeonTest(SpainTest):
    cal_class = CastileAndLeon

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 4, 23), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 4, 23), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)


class CastillaLaManchaTest(SpainTest):
    cal_class = CastillaLaMancha

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 5, 31), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 5, 31), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)


class CanaryIslandsTest(SpainTest):
    cal_class = CanaryIslands

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 5, 30), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 5, 30), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)


class CataloniaTest(SpainTest):
    cal_class = Catalonia

    def test_region_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 4, 6), holidays)  # Easter Monday
        # Diada nacional de Catalunya
        self.assertIn(date(2015, 9, 11), holidays)
        self.assertIn(date(2015, 12, 26), holidays)  # Sant Esteve
        self.assertEqual(len(holidays), 13)

    def test_region_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 3, 28), holidays)  # Easter Monday
        # Diada nacional de Catalunya
        self.assertIn(date(2016, 9, 11), holidays)
        self.assertIn(date(2016, 12, 26), holidays)  # Sant Esteve
        self.assertEqual(len(holidays), 13)

    def test_boxing_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(holidays[date(2020, 12, 26)], "Sant Esteve")


class ExtremaduraTest(SpainTest):
    cal_class = Extremadura

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 9, 8), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 9, 8), holidays)  # Regional Day
        self.assertEqual(len(holidays), 12)


class GaliciaTest(SpainTest):
    cal_class = Galicia

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 5, 17), holidays)  # Galician Literature Day
        self.assertIn(date(2019, 7, 25), holidays)  # Regional Day
        self.assertEqual(len(holidays), 13)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 5, 17), holidays)  # Galician Literature Day
        self.assertIn(date(2020, 7, 25), holidays)  # Regional Day
        self.assertEqual(len(holidays), 13)


class BalearicIslandsTest(SpainTest):
    cal_class = BalearicIslands

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 3, 1), holidays)  # Balearic National Day
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 4, 22), holidays)  # Easter Monday
        self.assertEqual(len(holidays), 13)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 3, 1), holidays)  # Balearic National Day
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertEqual(len(holidays), 13)


class LaRiojaTest(SpainTest):
    cal_class = LaRioja

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 6, 9), holidays)  # Dia de La Rioja
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 6, 9), holidays)  # Dia de La Rioja
        self.assertEqual(len(holidays), 12)


class CommunityofMadridTest(SpainTest):
    cal_class = CommunityofMadrid

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        # Fiesta de la Comunidad de Madrid
        self.assertIn(date(2019, 5, 2), holidays)
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        # Fiesta de la Comunidad de Madrid
        self.assertIn(date(2020, 5, 2), holidays)
        self.assertEqual(len(holidays), 12)


class MurciaTest(SpainTest):
    cal_class = Murcia

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 3, 19), holidays)  # San José
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 6, 9), holidays)  # Día de la Región de Murcia
        self.assertEqual(len(holidays), 13)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 3, 19), holidays)  # San José
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 6, 9), holidays)  # Día de la Región de Murcia
        self.assertEqual(len(holidays), 13)


class NavarreTest(SpainTest):
    cal_class = Navarre

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 4, 22), holidays)  # Easter Monday
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertEqual(len(holidays), 12)


class AsturiasTest(SpainTest):
    cal_class = Asturias

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 9, 8), holidays)  # Día de Asturias
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 9, 8), holidays)  # Día de Asturias
        self.assertEqual(len(holidays), 12)


class BasqueCountryTest(SpainTest):
    cal_class = BasqueCountry

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2019, 4, 22), holidays)  # Easter Monday
        self.assertIn(date(2019, 10, 25), holidays)  # Euskadi Eguna
        self.assertEqual(len(holidays), 13)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 10, 25), holidays)  # Euskadi Eguna
        self.assertEqual(len(holidays), 13)


class CantabriaTest(SpainTest):
    cal_class = Cantabria

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy/Holy Thursday
        # Día de Cantabria o Día de La Montaña
        self.assertIn(date(2019, 9, 15), holidays)
        self.assertEqual(len(holidays), 12)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 4, 9), holidays)  # Maundy/Holy Thursday
        # Día de Cantabria o Día de La Montaña
        self.assertIn(date(2020, 9, 15), holidays)
        self.assertEqual(len(holidays), 12)


class ValencianCommunityTest(SpainTest):
    cal_class = ValencianCommunity

    def test_region_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 3, 19), holidays)  # San José
        self.assertIn(date(2019, 4, 22), holidays)  # Easter Monday
        # Dia de la Comunitat Valenciana
        self.assertIn(date(2019, 10, 9), holidays)
        self.assertEqual(len(holidays), 13)

    def test_region_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 3, 19), holidays)  # San José
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        # Dia de la Comunitat Valenciana
        self.assertIn(date(2020, 10, 9), holidays)
        self.assertEqual(len(holidays), 13)
