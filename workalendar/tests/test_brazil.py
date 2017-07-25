# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.america import (
    Brazil, BrazilSaoPauloState,
    BrazilAcre, BrazilAlagoas, BrazilAmapa, BrazilAmazonas, BrazilBahia,
    BrazilCeara, BrazilDistritoFederal, BrazilEspiritoSanto, BrazilGoias,
    BrazilMaranhao, BrazilMatoGrosso, BrazilMatoGrossoDoSul, BrazilPara,
    BrazilParaiba, BrazilPernambuco, BrazilPiaui, BrazilRioDeJaneiro,
    BrazilRioGrandeDoNorte, BrazilRioGrandeDoSul, BrazilRondonia,
    BrazilRoraima, BrazilSantaCatarina, BrazilSergipe, BrazilTocantins,
    # Cities
    BrazilSaoPauloCity, BrazilVitoriaCity, BrazilVilaVelhaCity,
    BrazilCariacicaCity, BrazilGuarapariCity, BrazilSerraCity,
    # Banks
    BrazilBankCalendar
)


class BrazilTest(GenericCalendarTest):
    cal_class = Brazil

    def test_year_2013_federal(self):
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

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 23), holidays)  # Dia do evangélico
        self.assertIn(date(2017, 6, 15), holidays)  # niversário do Acre
        self.assertIn(date(2017, 9, 5), holidays)  # Dia da Amazônia
        # Assinatura do Tratado de Petrópolis
        self.assertIn(date(2017, 11, 17), holidays)


class BrazilAlagoasTest(BrazilTest):
    cal_class = BrazilAlagoas

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 24), holidays)  # São João
        self.assertIn(date(2017, 6, 29), holidays)  # São Pedro
        # Emancipação política de Alagoas
        self.assertIn(date(2017, 9, 16), holidays)
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra


class BrazilAmapaTest(BrazilTest):
    cal_class = BrazilAmapa

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Dia de São José
        sao_jose = date(2017, 3, 19)
        self.assertIn(sao_jose, holidays)
        # Check its label
        self.assertEqual(
            self.cal.get_holiday_label(sao_jose), "Dia de São José")

        self.assertIn(date(2017, 7, 25), holidays)  # São Tiago
        self.assertIn(date(2017, 10, 5), holidays)  # Criação do estado
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra


class BrazilAmazonasTest(BrazilTest):
    cal_class = BrazilAmazonas

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Elevação do Amazonas á categoria de província
        self.assertIn(date(2017, 9, 5), holidays)
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra
        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)


class BrazilBahiaTest(BrazilTest):
    cal_class = BrazilBahia

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 7, 2), holidays)  # Independência da Bahia


class BrazilCearaTest(BrazilTest):
    cal_class = BrazilCeara

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 3, 19), holidays)  # São José
        self.assertIn(date(2017, 3, 23), holidays)  # Data Manga do Ceará


class BrazilDistritoFederalTest(BrazilTest):
    cal_class = BrazilDistritoFederal

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 4, 21), holidays)  # Fundação de Brasília
        self.assertIn(date(2017, 11, 30), holidays)  # Dia do Evangélico


class BrazilEspiritoSantoTest(BrazilTest):
    cal_class = BrazilEspiritoSanto

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 28), holidays)  # Dia do Servidor Público


class BrazilGoiasTest(BrazilTest):
    cal_class = BrazilGoias

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 28), holidays)  # Dia do Servidor Público


class BrazilMaranhaoTest(BrazilTest):
    cal_class = BrazilMaranhao

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Adesão do Maranhão á independência do Brasil
        self.assertIn(date(2017, 7, 28), holidays)
        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)


class BrazilMatoGrossoTest(BrazilTest):
    cal_class = BrazilMatoGrosso

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 11, 29), holidays)  # Consciência Negra


class BrazilMatoGrossoDoSulTest(BrazilTest):
    cal_class = BrazilMatoGrossoDoSul

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 11), holidays)  # Criação do estado


class BrazilParaTest(BrazilTest):
    cal_class = BrazilPara

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Adesão do Grão-Pará á independência do Brasil
        self.assertIn(date(2017, 8, 15), holidays)


class BrazilParaibaTest(BrazilTest):
    cal_class = BrazilParaiba

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 8, 5), holidays)  # Fundação do Estado


class BrazilPernambucoTest(BrazilTest):
    cal_class = BrazilPernambuco

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 24), holidays)  # São João


class BrazilPiauiTest(BrazilTest):
    cal_class = BrazilPiaui

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Dia da Batalha do Jenipapo
        self.assertIn(date(2017, 3, 13), holidays)
        self.assertIn(date(2017, 10, 19), holidays)  # Dia do Piauí


class BrazilRioDeJaneiroTest(BrazilTest):
    cal_class = BrazilRioDeJaneiro

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 2, 28), holidays)  # Carnaval
        self.assertIn(date(2017, 4, 23), holidays)  # Dia de São Jorge
        self.assertIn(date(2017, 10, 16), holidays)  # Dia do Comércio
        # Dia do Funcionário Público
        self.assertIn(date(2017, 10, 28), holidays)
        # Dia da Consciência Negra
        consciencia_negra = date(2017, 11, 20)
        self.assertIn(consciencia_negra, holidays)
        # check its label
        self.assertEqual(
            self.cal.get_holiday_label(consciencia_negra),
            "Dia da Consciência Negra",
        )

        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)


class BrazilRioGrandeDoNorteTest(BrazilTest):
    cal_class = BrazilRioGrandeDoNorte

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Dua de São Pedro
        sao_pedro = date(2017, 6, 29)
        self.assertIn(sao_pedro, holidays)
        # Check the label
        self.assertEqual(
            self.cal.get_holiday_label(sao_pedro), "Dua de São Pedro"
        )
        # Mártires de Cunhaú e Uruaçuu
        self.assertIn(date(2017, 10, 3), holidays)


class BrazilRioGrandeDoSulTest(BrazilTest):
    cal_class = BrazilRioGrandeDoSul

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 9, 20), holidays)  # Revolução Farroupilha


class BrazilRondoniaTest(BrazilTest):
    cal_class = BrazilRondonia

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 4), holidays)  # Criação do estado
        self.assertIn(date(2017, 6, 18), holidays)  # Dia do Evangélico


class BrazilRoraimaTest(BrazilTest):
    cal_class = BrazilRoraima

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 10, 5), holidays)  # Criação de Roraima


class BrazilSantaCatarinaTest(BrazilTest):
    cal_class = BrazilSantaCatarina

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Criação da capitania, separando-se de SP
        self.assertIn(date(2017, 8, 11), holidays)


class SaoPauloStateTest(BrazilTest):
    cal_class = BrazilSaoPauloState

    def test_year_2013_state(self):
        holidays = self.cal.holidays_set(2013)
        # Revolução Constitucionalista de 1932
        self.assertIn(date(2013, 7, 9), holidays)


class SaoPauloCityTest(SaoPauloStateTest):
    cal_class = BrazilSaoPauloCity

    def test_year_2013_city(self):
        holidays = self.cal.holidays_set(2013)
        # Aniversário da Cidade de São Paulo
        self.assertIn(date(2013, 1, 25), holidays)
        self.assertIn(date(2013, 2, 12), holidays)  # Carnaval
        # Dia da Consciência Negra
        consciencia_negra = date(2013, 11, 20)
        self.assertIn(consciencia_negra, holidays)
        # check its label
        self.assertEqual(
            self.cal.get_holiday_label(consciencia_negra),
            "Dia da Consciência Negra",
        )
        self.assertIn(date(2013, 3, 31), holidays)  # Páscoa
        self.assertIn(date(2013, 5, 30), holidays)  # Corpus Christi

        # Variable day: Good Friday
        good_friday = date(2013, 3, 29)
        self.assertIn(good_friday, holidays)  # Sexta-feira da Paixão
        # Label test
        self.assertEqual(
            self.cal.get_holiday_label(good_friday),
            "Sexta-feira da Paixão",
        )


class BrazilSergipeTest(BrazilTest):
    cal_class = BrazilSergipe

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Autonomia política de Sergipe
        self.assertIn(date(2017, 7, 8), holidays)


class BrazilTocantinsTest(BrazilTest):
    cal_class = BrazilTocantins

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # Instalação de Tocantins
        # Nossa Senhora da Natividade
        self.assertIn(date(2017, 9, 8), holidays)
        self.assertIn(date(2017, 10, 5), holidays)  # Criação de Tocantins


class BrazilVitoriaCityTest(BrazilEspiritoSantoTest):
    """
    Vitória city is in the Espírito Santo state
    """
    cal_class = BrazilVitoriaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        self.assertIn(date(2017, 4, 24), holidays)  # Nossa Senhora da Penha
        self.assertIn(date(2017, 9, 8), holidays)  # Nossa Senhora da Vitória

        # Variable days: Corpus Christie
        corpus_christie = date(2017, 6, 15)
        self.assertIn(corpus_christie, holidays)

        # Variable days: Good friday
        good_friday = date(2017, 4, 14)
        self.assertIn(good_friday, holidays)
        # Test label
        self.assertEqual(
            self.cal.get_holiday_label(good_friday),
            "Paixão do Cristo",
        )


class BrazilVilaVelhaCityTest(BrazilEspiritoSantoTest):
    """
    Vila Velha city is in the Espírito Santo state
    """
    cal_class = BrazilVilaVelhaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Colonização do Solo Espírito-santense
        self.assertIn(date(2017, 5, 23), holidays)


class BrazilCariacicaCityTest(BrazilEspiritoSantoTest):
    """
    Cariacica city is in the Espírito Santo state
    """
    cal_class = BrazilCariacicaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        self.assertIn(date(2017, 4, 13), holidays)  # Nossa Senhora da Penha
        # São João Batista / Aniversãrio de Cariacica
        sao_joao = date(2017, 6, 24)
        self.assertIn(sao_joao, holidays)
        # Check São João label
        self.assertEqual(
            self.cal.get_holiday_label(sao_joao),
            "São João Batista / Aniversãrio de Cariacica"
        )

        # Variable days: Corpus Christie
        corpus_christie = date(2017, 6, 15)
        self.assertIn(corpus_christie, holidays)

        # Variable days: Good friday
        good_friday = date(2017, 4, 14)
        self.assertIn(good_friday, holidays)
        # Test label
        self.assertEqual(
            self.cal.get_holiday_label(good_friday),
            "Paixão do Cristo",
        )


class BrazilGuarapariCityTest(BrazilEspiritoSantoTest):
    """
    Guarapari city is in the Espírito Santo state
    """
    cal_class = BrazilGuarapariCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 29), holidays),  # São Pedro
        self.assertIn(date(2017, 9, 19), holidays),  # Emancipação de Guarapari
        self.assertIn(date(2017, 11, 29), holidays),  # Consciência Negra
        self.assertIn(date(2017, 12, 8), holidays),  # Nossa Senhora Conceição


class BrazilSerraCityTest(BrazilEspiritoSantoTest):
    """
    Serra city is in the Espírito Santo state
    """
    cal_class = BrazilSerraCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        self.assertIn(date(2017, 6, 29), holidays)  # São Pedro
        self.assertIn(date(2017, 12, 8), holidays)  # Nossa Senhora Conceição
        self.assertIn(date(2017, 12, 26), holidays)  # Dia do Serrano

        # Variable days: Carnaval (Monday & Tuesday)
        self.assertIn(date(2017, 2, 27), holidays)  # Monday
        self.assertIn(date(2017, 2, 28), holidays)  # Tuesday

        # Variable days: Ash Wednesday (Quarta-feira de cinzas)
        ash_wednesday = date(2017, 3, 1)
        self.assertIn(ash_wednesday, holidays)
        # Test label
        self.assertEqual(
            self.cal.get_holiday_label(ash_wednesday),
            "Quarta-feira de cinzas",
        )

        # Variable days: Good Friday (Paixão de Cristo)
        good_friday = date(2017, 4, 14)
        self.assertIn(good_friday, holidays)
        # Test label
        self.assertEqual(
            self.cal.get_holiday_label(good_friday),
            "Paixão do Cristo",
        )


class BrazilBankCalendarTest(BrazilTest):
    cal_class = BrazilBankCalendar

    def test_year_2017_holidays(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # New year
        self.assertIn(date(2017, 2, 27), holidays)  # Monday carnaval
        self.assertIn(date(2017, 2, 28), holidays)  # Tuesday carnaval
        self.assertIn(date(2017, 4, 14), holidays)  # Good friday
        self.assertIn(date(2017, 4, 21), holidays)  # Tiradentes
        self.assertIn(date(2017, 5, 1), holidays)  # Labour day
        self.assertIn(date(2017, 6, 15), holidays)  # Corpus Christi
        self.assertIn(date(2017, 9, 7), holidays)  # Independence day
        self.assertIn(date(2017, 10, 12), holidays)  # Our Lady Aparecida
        self.assertIn(date(2017, 11, 2), holidays)  # All Souls' Day
        self.assertIn(date(2017, 11, 15), holidays)  # Republic day
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas Day

    def test_year_2017_find_next_working_day_for_new_year(self):
        new_year = date(2017, 1, 1)
        working_day = self.cal.find_following_working_day(new_year)
        self.assertEquals(working_day, date(2017, 1, 2))

    def test_year_2017_find_next_working_day_for_monday_carnaval(self):
        monday_carnaval = date(2017, 2, 27)
        working_day = self.cal.find_following_working_day(monday_carnaval)
        self.assertEquals(working_day, date(2017, 3, 1))

    def test_year_2017_find_next_working_day_for_tuesday_carnaval(self):
        tuesday_carnaval = date(2017, 2, 28)
        working_day = self.cal.find_following_working_day(tuesday_carnaval)
        self.assertEquals(working_day, date(2017, 3, 1))

    def test_year_2017_find_next_working_day_for_good_friday(self):
        good_friday = date(2017, 4, 14)
        working_day = self.cal.find_following_working_day(good_friday)
        self.assertEquals(working_day, date(2017, 4, 17))

    def test_year_2017_find_next_working_day_for_tiradentes(self):
        tiradentes = date(2017, 4, 21)
        working_day = self.cal.find_following_working_day(tiradentes)
        self.assertEquals(working_day, date(2017, 4, 24))

    def test_year_2017_find_next_working_day_for_labour_day(self):
        labour_day = date(2017, 5, 1)
        working_day = self.cal.find_following_working_day(labour_day)
        self.assertEquals(working_day, date(2017, 5, 2))

    def test_year_2017_find_next_working_day_for_corpus_christi(self):
        corpus_christi = date(2017, 6, 15)
        working_day = self.cal.find_following_working_day(corpus_christi)
        self.assertEquals(working_day, date(2017, 6, 16))

    def test_year_2017_find_next_working_day_for_independence_day(self):
        independence_day = date(2017, 9, 7)
        working_day = self.cal.find_following_working_day(independence_day)
        self.assertEquals(working_day, date(2017, 9, 8))

    def test_year_2017_find_next_working_day_for_our_lady_aparecida(self):
        our_lady_aparecida = date(2017, 10, 12)
        working_day = self.cal.find_following_working_day(our_lady_aparecida)
        self.assertEquals(working_day, date(2017, 10, 13))

    def test_year_2017_find_next_working_day_for_our_all_souls(self):
        all_souls = date(2017, 11, 2)
        working_day = self.cal.find_following_working_day(all_souls)
        self.assertEquals(working_day, date(2017, 11, 3))

    def test_year_2017_find_next_working_day_for_our_republic_day(self):
        republic_day = date(2017, 11, 15)
        working_day = self.cal.find_following_working_day(republic_day)
        self.assertEquals(working_day, date(2017, 11, 16))

    def test_year_2017_find_next_working_day_for_our_christmas_day(self):
        christmas_day = date(2017, 12, 25)
        working_day = self.cal.find_following_working_day(christmas_day)
        self.assertEquals(working_day, date(2017, 12, 26))

    def test_year_2017_find_next_working_day_for_last_day(self):
        # last day of year for only internal bank transactions
        last_day = date(2017, 12, 29)
        working_day = self.cal.find_following_working_day(last_day)
        self.assertEquals(working_day, date(2018, 1, 2))

    def test_year_2017_find_next_working_day_for_already_working_day(self):
        already_working_day = date(2017, 7, 25)
        working_day = self.cal.find_following_working_day(already_working_day)
        self.assertEquals(working_day, date(2017, 7, 25))
