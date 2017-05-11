# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.america import (
    Brazil, BrazilSaoPauloState, BrazilSaoPauloCity,
    BrazilAcre
)


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


class BrazilAcreTest(BrazilTest):
    cal_class = BrazilAcre

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 23), holidays)  # Dia do evangélico
        self.assertIn(date(2017, 6, 15), holidays)  # niversário do Acre
        self.assertIn(date(2017, 9, 5), holidays)  # Dia da Amazônia
        # Assinatura do Tratado de Petrópolis
        self.assertIn(date(2017, 11, 17), holidays)


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
