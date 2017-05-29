# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.america import (
    Brazil, BrazilSaoPauloState, BrazilSaoPauloCity,
    BrazilAcre, BrazilAlagoas, BrazilAmapa, BrazilAmazonas, BrazilBahia,
    BrazilCeara, BrazilDistritoFederal, BrazilEspiritoSanto, BrazilGoias,
    BrazilMaranhao, BrazilMatoGrosso, BrazilMatoGrossoDoSul, BrazilPara,
    BrazilParaiba, BrazilPernambuco, BrazilPiaui, BrazilRioDeJaneiro,
    BrazilRioGrandeDoNorte, BrazilRioGrandeDoSul, BrazilRondonia,
    BrazilRoraima, BrazilSantaCatarina, BrazilSergipe,
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


class BrazilAlagoasTest(BrazilTest):
    cal_class = BrazilAlagoas

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 24), holidays)  # São João
        self.assertIn(date(2017, 6, 29), holidays)  # São Pedro
        # Emancipação política de Alagoas
        self.assertIn(date(2017, 9, 16), holidays)
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra


class BrazilAmapaTest(BrazilTest):
    cal_class = BrazilAmapa

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 3, 19), holidays)  # Dia de São José
        self.assertIn(date(2017, 7, 25), holidays)  # São Tiago
        self.assertIn(date(2017, 10, 5), holidays)  # Criação do estado
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra


class BrazilAmazonasTest(BrazilTest):
    cal_class = BrazilAmazonas

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # Elevação do Amazonas á categoria de província
        self.assertIn(date(2017, 9, 5), holidays)
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra
        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)


class BrazilBahiaTest(BrazilTest):
    cal_class = BrazilBahia

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 7, 2), holidays)  # Independência da Bahia


class BrazilCearaTest(BrazilTest):
    cal_class = BrazilCeara

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 3, 19), holidays)  # São José
        self.assertIn(date(2017, 3, 23), holidays)  # Data Manga do Ceará


class BrazilDistritoFederalTest(BrazilTest):
    cal_class = BrazilDistritoFederal

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 4, 21), holidays)  # Fundação de Brasília
        self.assertIn(date(2017, 11, 30), holidays)  # Dia do Evangélico


class BrazilEspiritoSantoTest(BrazilTest):
    cal_class = BrazilEspiritoSanto

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 28), holidays)  # Dia do Servidor Público


class BrazilGoiasTest(BrazilTest):
    cal_class = BrazilGoias

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 28), holidays)  # Dia do Servidor Público


class BrazilMaranhaoTest(BrazilTest):
    cal_class = BrazilMaranhao

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # Adesão do Maranhão á independência do Brasil
        self.assertIn(date(2017, 7, 28), holidays)
        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)


class BrazilMatoGrossoTest(BrazilTest):
    cal_class = BrazilMatoGrosso

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 11, 29), holidays)  # Consciência Negra


class BrazilMatoGrossoDoSulTest(BrazilTest):
    cal_class = BrazilMatoGrossoDoSul

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 11), holidays)  # Criação do estado


class BrazilParaTest(BrazilTest):
    cal_class = BrazilPara

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # Adesão do Grão-Pará á independência do Brasil
        self.assertIn(date(2017, 8, 15), holidays)


class BrazilParaibaTest(BrazilTest):
    cal_class = BrazilParaiba

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 8, 5), holidays)  # Fundação do Estado


class BrazilPernambucoTest(BrazilTest):
    cal_class = BrazilPernambuco

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 24), holidays)  # São João


class BrazilPiauiTest(BrazilTest):
    cal_class = BrazilPiaui

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # Dia da Batalha do Jenipapo
        self.assertIn(date(2017, 3, 13), holidays)
        self.assertIn(date(2017, 10, 19), holidays)  # Dia do Piauí


class BrazilRioDeJaneiroTest(BrazilTest):
    cal_class = BrazilRioDeJaneiro

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 2, 28), holidays)  # Carnaval
        self.assertIn(date(2017, 4, 23), holidays)  # Dia de São Jorge
        self.assertIn(date(2017, 10, 16), holidays)  # Dia do Comércio
        # Dia do Funcionário Público
        self.assertIn(date(2017, 10, 28), holidays)
        self.assertIn(date(2017, 11, 20), holidays)  # Dia da Consciência Negra
        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)


class BrazilRioGrandeDoNorteTest(BrazilTest):
    cal_class = BrazilRioGrandeDoNorte

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 29), holidays)  # Dua de São Pedro
        # Mártires de Cunhaú e Uruaçuu
        self.assertIn(date(2017, 10, 3), holidays)


class BrazilRioGrandeDoSulTest(BrazilTest):
    cal_class = BrazilRioGrandeDoSul

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 9, 20), holidays)  # Revolução Farroupilha


class BrazilRondoniaTest(BrazilTest):
    cal_class = BrazilRondonia

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 4), holidays)  # Criação do estado
        self.assertIn(date(2017, 6, 18), holidays)  # Dia do Evangélico


class BrazilRoraimaTest(BrazilTest):
    cal_class = BrazilRoraima

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 5), holidays)  # Criação de Roraima


class BrazilSantaCatarinaTest(BrazilTest):
    cal_class = BrazilSantaCatarina

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # Criação da capitania, separando-se de SP
        self.assertIn(date(2017, 8, 11), holidays)


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


class BrazilSergipeTest(BrazilTest):
    cal_class = BrazilSergipe

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # Autonomia política de Sergipe
        self.assertIn(date(2017, 7, 8), holidays)
