# -*- coding: utf-8 -*-
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.america import Brazil, BrazilSaoPauloState
from workalendar.america import BrazilSaoPauloCity
from workalendar.america import Colombia
from workalendar.america import Mexico, Chile, Panama


class BrazilTest(GenericCalendarTest):
    cal_class = Brazil

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 4, 21), holidays)  # Tiradentes
        self.assertIn(date(2013, 5, 1), holidays)  # Dia do trabalhador
        self.assertIn(date(2013, 9, 7), holidays)  # Dia da Independência
        self.assertIn(date(2013, 10, 12), holidays)  # Nossa Senhora Aparecida
        self.assertIn(date(2013, 11, 2), holidays)  # Finados
        self.assertIn(date(2013, 11, 15), holidays)  # Proclamação da República
        self.assertIn(date(2013, 12, 25), holidays)  # Natal


class SaoPauloStateTest(BrazilTest):
    cal_class = BrazilSaoPauloState

    def test_regional_2013(self):
        holidays = self.cal.holidays_set(2013)
        # Revolução Constitucionalista de 1932
        self.assertIn(date(2013, 7, 9), holidays)


class SaoPauloCityTest(SaoPauloStateTest):
    cal_class = BrazilSaoPauloCity

    def test_city_2013(self):
        holidays = self.cal.holidays_set(2013)
        # Aniversário da Cidade de São Paulo
        self.assertIn(date(2013, 1, 25), holidays)
        self.assertIn(date(2013, 2, 12), holidays)  # Carnaval
        self.assertIn(date(2013, 11, 20), holidays)  # Dia da Consciência Negra
        self.assertIn(date(2013, 3, 29), holidays)  # Sexta-feira da Paixão
        self.assertIn(date(2013, 3, 31), holidays)  # Páscoa
        self.assertIn(date(2013, 5, 30), holidays)  # Corpus Christi


class ChileTest(GenericCalendarTest):
    cal_class = Chile

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 3, 30), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 21), holidays)
        self.assertIn(date(2013, 6, 29), holidays)
        self.assertIn(date(2013, 7, 16), holidays)
        self.assertIn(date(2013, 8, 15), holidays)
        self.assertIn(date(2013, 9, 18), holidays)
        self.assertIn(date(2013, 9, 19), holidays)
        self.assertIn(date(2013, 9, 20), holidays)
        self.assertIn(date(2013, 10, 12), holidays)
        self.assertIn(date(2013, 10, 31), holidays)
        self.assertIn(date(2013, 11, 1), holidays)
        self.assertIn(date(2013, 12, 8), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 31), holidays)

    def test_reformation_day(self):
        holidays = self.cal.holidays_set(2012)
        self.assertNotIn(date(2012, 10, 31), holidays)
        self.assertIn(date(2012, 11, 2), holidays)
        #
        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(date(2017, 10, 31), holidays)
        self.assertIn(date(2017, 10, 27), holidays)


class ColombiaTest(GenericCalendarTest):
    cal_class = Colombia

    def test_holidays_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 12), holidays)
        self.assertIn(date(2015, 3, 23), holidays)
        self.assertIn(date(2015, 3, 29), holidays)
        self.assertIn(date(2015, 4, 2), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 5), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 18), holidays)
        self.assertIn(date(2015, 6, 8), holidays)
        self.assertIn(date(2015, 6, 15), holidays)
        self.assertIn(date(2015, 6, 29), holidays)
        self.assertIn(date(2015, 7, 20), holidays)
        self.assertIn(date(2015, 8, 7), holidays)
        self.assertIn(date(2015, 8, 17), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 2), holidays)
        self.assertIn(date(2015, 11, 16), holidays)
        self.assertIn(date(2015, 12, 8), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertEqual(len(holidays), 20)


class MexicoTest(GenericCalendarTest):
    cal_class = Mexico

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 2, 4), holidays)  # Constitution day
        self.assertIn(date(2013, 3, 18), holidays)  # Benito Juárez's birthday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 9, 16), holidays)  # Independence day
        self.assertIn(date(2013, 11, 18), holidays)  # Revolution day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas

    def test_shift_to_monday(self):
        holidays = self.cal.holidays_set(2017)
        # New year on Sunday -> shift
        self.assertIn(date(2017, 1, 2), holidays)
        holidays = self.cal.holidays_set(2016)
        # XMas on sunday -> shift to monday
        self.assertIn(date(2016, 12, 26), holidays)
        # Same for Labour day
        self.assertIn(date(2016, 5, 2), holidays)

    def test_shift_to_friday(self):
        holidays = self.cal.holidays_set(2021)
        # January 1st 2022 is a saturday, so we shift to friday
        self.assertIn(date(2021, 12, 31), holidays)
        # Same for Labour day
        self.assertIn(date(2021, 4, 30), holidays)
        holidays = self.cal.holidays_set(2021)
        # December 25th, 2022 is a saturday, so we shift to friday
        self.assertIn(date(2021, 12, 24), holidays)


class PanamaTest(GenericCalendarTest):
    cal_class = Panama

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 1, 9), holidays)  # Martyrs day
        self.assertIn(date(2013, 2, 12), holidays)  # carnival tuesday
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 30), holidays)  # easter saturday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 11, 3), holidays)  # independence day
        self.assertIn(date(2013, 11, 5), holidays)  # colon day
        # Shout in Villa de los Santos
        self.assertIn(date(2013, 11, 10), holidays)
        self.assertIn(date(2013, 12, 2), holidays)  # Independence from spain
        self.assertIn(date(2013, 12, 8), holidays)  # mother day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
