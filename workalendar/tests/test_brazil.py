from datetime import date
from unittest import TestCase

from . import GenericCalendarTest
from ..america import (
    Brazil, BrazilSaoPauloState,
    BrazilAcre, BrazilAlagoas, BrazilAmapa, BrazilAmazonas, BrazilBahia,
    BrazilCeara, BrazilDistritoFederal, BrazilEspiritoSanto, BrazilGoias,
    BrazilMaranhao, BrazilMinasGerais, BrazilMatoGrosso, BrazilMatoGrossoDoSul,
    BrazilPara, BrazilParaiba, BrazilPernambuco, BrazilPiaui, BrazilParana,
    BrazilRioDeJaneiro, BrazilRioGrandeDoNorte, BrazilRioGrandeDoSul,
    BrazilRondonia, BrazilRoraima, BrazilSantaCatarina, BrazilSergipe,
    BrazilTocantins,
    # Cities
    BrazilSaoPauloCity, BrazilVitoriaCity, BrazilVilaVelhaCity,
    BrazilCariacicaCity, BrazilGuarapariCity, BrazilSerraCity,
    BrazilRioBrancoCity, BrazilMaceioCity, BrazilManausCity, BrazilMacapaCity,
    BrazilSalvadorCity, BrazilFortalezaCity, BrazilGoianiaCity,
    BrazilBeloHorizonteCity, BrazilCampoGrandeCity, BrazilCuiabaCity,
    BrazilBelemCity, BrazilJoaoPessoaCity, BrazilRecifeCity,
    BrazilTeresinaCity, BrazilCuritibaCity, BrazilNatalCity,
    BrazilPortoVelhoCity, BrazilBoaVistaCity, BrazilPortoAlegreCity,
    BrazilChapecoCity, BrazilFlorianopolisCity, BrazilJoinvilleCity,
    BrazilAracajuCity, BrazilSorocabaCity, BrazilPalmasCity,
    # Banks
    BrazilBankCalendar,
)
from ..america.brazil import IBGE_REGISTER, IBGE_TUPLE


class BrazilTest(GenericCalendarTest):
    cal_class = Brazil
    test_include_consciencia_negra = False
    test_include_immaculate_conception = False

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

    def test_consciencia_negra(self):
        # Consciência Negra day is not a national holiday
        # It's triggered in the appropriate classes, so this test needs to
        # be overwritten.
        month, day = self.cal.consciencia_negra_day
        consciencia_negra_day = date(self.year, month, day)
        holidays = self.cal.holidays_set(self.year)
        if self.test_include_consciencia_negra:
            # Included where needed
            self.assertIn(consciencia_negra_day, holidays)
        else:
            # By default, not in the holidays.
            self.assertNotIn(consciencia_negra_day, holidays)

    def test_immaculate_conception(self):
        # Immaculate Conception is not a national holiday
        # It's triggered in the appropriate classes, so this test needs to
        # be overwritten.
        immaculate_conception_day = date(self.year, 12, 8)
        holidays = dict(self.cal.holidays(self.year))
        if self.test_include_immaculate_conception:
            # Included where needed
            self.assertIn(immaculate_conception_day, holidays)
            # Test its label
            self.assertEqual(
                holidays[immaculate_conception_day],
                "Dia de Nossa Senhora da Conceição")
        else:
            # By default, not in the holidays.
            self.assertNotIn(immaculate_conception_day, holidays)


class BrazilAcreTest(BrazilTest):
    cal_class = BrazilAcre

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 23), holidays)  # Dia do evangélico
        self.assertIn(date(2017, 6, 15), holidays)  # niversário do Acre
        self.assertIn(date(2017, 9, 5), holidays)  # Dia da Amazônia
        # Assinatura do Tratado de Petrópolis
        self.assertIn(date(2017, 11, 17), holidays)
        # Início da Revolução Acreana
        self.assertIn(date(2017, 8, 6), holidays)


class BrazilAlagoasTest(BrazilTest):
    cal_class = BrazilAlagoas
    test_include_consciencia_negra = True

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 24), holidays)  # São João
        self.assertIn(date(2017, 6, 29), holidays)  # São Pedro
        # Emancipação política de Alagoas
        self.assertIn(date(2017, 9, 16), holidays)
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra


class BrazilAmapaTest(BrazilTest):
    cal_class = BrazilAmapa
    test_include_consciencia_negra = True

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
        self.assertIn(date(2017, 9, 13), holidays)  # Aniversário da Amapá


class BrazilAmazonasTest(BrazilTest):
    cal_class = BrazilAmazonas
    test_include_consciencia_negra = True
    test_include_immaculate_conception = True

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Elevação do Amazonas á categoria de província
        self.assertIn(date(2017, 9, 5), holidays)
        self.assertIn(date(2017, 11, 20), holidays)  # Consciência Negra
        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)
        # Label test
        holidays = self.cal.holidays(2017)


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
        self.assertIn(date(2017, 3, 25), holidays)  # Aniversário do Ceará


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
    test_include_immaculate_conception = True

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Adesão do Maranhão á independência do Brasil
        self.assertIn(date(2017, 7, 28), holidays)
        # Dia de Nossa Senhora da Conceição
        self.assertIn(date(2017, 12, 8), holidays)


class BrazilMinasGeraisTest(BrazilTest):
    cal_class = BrazilMinasGerais

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Aniversário de Minas Geraisl
        self.assertIn(date(2017, 4, 21), holidays)


class BrazilMatoGrossoTest(BrazilTest):
    cal_class = BrazilMatoGrosso
    test_include_consciencia_negra = True

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
    test_include_immaculate_conception = True

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Adesão do Grão-Pará á independência do Brasil
        self.assertIn(date(2017, 8, 15), holidays)


class BrazilParaibaTest(BrazilTest):
    cal_class = BrazilParaiba

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 8, 5), holidays)  # Fundação do Estado
        # Homenagem à memória do ex-presidente João Pessoa
        self.assertIn(date(2017, 7, 26), holidays)


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


class BrazilParanaTest(BrazilTest):
    cal_class = BrazilParana

    def test_year_2017_state(self):
        holidays = self.cal.holidays_set(2017)
        # Aniversário do Paraná
        self.assertIn(date(2017, 12, 19), holidays)


class BrazilRioDeJaneiroTest(BrazilTest):
    cal_class = BrazilRioDeJaneiro
    test_include_consciencia_negra = True
    test_include_immaculate_conception = True

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

    def test_carnaval_label(self):
        holidays = self.cal.holidays(2017)
        holidays_dict = dict(holidays)
        label_carnaval = holidays_dict[date(2017, 2, 28)]
        self.assertEqual(label_carnaval, "Carnaval")


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
        # Dia de Santa Catarina de Alexandria
        self.assertIn(date(2017, 11, 25), holidays)


class SaoPauloStateTest(BrazilTest):
    cal_class = BrazilSaoPauloState

    def test_year_2013_state(self):
        holidays = self.cal.holidays_set(2013)
        # Revolução Constitucionalista de 1932
        self.assertIn(date(2013, 7, 9), holidays)
        # Revolução Constitucionalista de 1932
        self.assertIn(date(2013, 7, 9), holidays)


class SaoPauloCityTest(SaoPauloStateTest):
    cal_class = BrazilSaoPauloCity
    test_include_consciencia_negra = True

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

    def test_carnaval_label(self):
        holidays = self.cal.holidays(2013)
        holidays_dict = dict(holidays)
        label_carnaval = holidays_dict[date(2013, 2, 12)]
        self.assertEqual(label_carnaval, "Carnaval")


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
        # Autonomia do estado de Tocantins
        self.assertIn(date(2017, 3, 18), holidays)


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
    test_include_consciencia_negra = True
    test_include_immaculate_conception = True

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
    test_include_immaculate_conception = True

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

    def test_carnaval_label(self):
        holidays = self.cal.holidays(2017)
        holidays_dict = dict(holidays)
        label_carnaval = holidays_dict[date(2017, 2, 28)]
        self.assertEqual(label_carnaval, "Carnaval")


class BrazilRioBrancoCityTest(BrazilAcreTest):
    """
    Rio Branco is in the Acre state
    """
    cal_class = BrazilRioBrancoCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Rio Branco
        self.assertIn(date(2017, 12, 28), holidays)


class BrazilMaceioCityTest(BrazilAlagoasTest):
    """
    Maceió is in the Alagoas state
    """
    cal_class = BrazilMaceioCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Maceió
        self.assertIn(date(2017, 12, 5), holidays)


class BrazilManausCityTest(BrazilAmazonasTest):
    """
    Manaus is in the Amazonas state
    """
    cal_class = BrazilManausCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Manaus
        self.assertIn(date(2017, 10, 24), holidays)


class BrazilMacapaCityTest(BrazilAmapaTest):
    """
    Macapá is in the Amapá state
    """
    cal_class = BrazilMacapaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Macapá
        self.assertIn(date(2017, 2, 4), holidays)


class BrazilSalvadorCityTest(BrazilBahiaTest):
    """
    Salvador is in the Bahia state
    """
    cal_class = BrazilSalvadorCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Salvador
        self.assertIn(date(2017, 3, 29), holidays)


class BrazilFortalezaCityTest(BrazilCearaTest):
    """
    Fortaleza is in the Ceará state
    """
    cal_class = BrazilFortalezaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Fortaleza
        self.assertIn(date(2017, 4, 13), holidays)


class BrazilGoianiaCityTest(BrazilGoiasTest):
    """
    Goiânia is in the Goiás state
    """
    cal_class = BrazilGoianiaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Goiânia
        self.assertIn(date(2017, 10, 24), holidays)


class BrazilBeloHorizonteCityTest(BrazilMinasGeraisTest):
    """
    Belo Horizonte is in the Minas Gerais state
    """
    cal_class = BrazilBeloHorizonteCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Belo Horizonte
        self.assertIn(date(2017, 12, 12), holidays)


class BrazilCampoGrandeCityTest(BrazilMatoGrossoDoSulTest):
    """
    Campo Grande is in the Mato Grosso do Sul state
    """
    cal_class = BrazilCampoGrandeCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Campo Grande
        self.assertIn(date(2017, 8, 26), holidays)


class BrazilCuiabaCityTest(BrazilMatoGrossoTest):
    """
    Cuiabá is in the Mato Grosso state
    """
    cal_class = BrazilCuiabaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Cuiabá
        self.assertIn(date(2017, 4, 8), holidays)


class BrazilBelemCityTest(BrazilParaTest):
    """
    Belém is in the Pará state
    """
    cal_class = BrazilBelemCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Belém
        self.assertIn(date(2017, 1, 12), holidays)


class BrazilJoaoPessoaCityTest(BrazilParaibaTest):
    """
    João Pessoa is in the Paraíba state
    """
    cal_class = BrazilJoaoPessoaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de João Pessoa
        self.assertIn(date(2017, 8, 5), holidays)


class BrazilRecifeCityTest(BrazilPernambucoTest):
    """
    Recife is in the Pernambuco state
    """
    cal_class = BrazilRecifeCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Recife
        self.assertIn(date(2017, 3, 12), holidays)


class BrazilTeresinaCityTest(BrazilPiauiTest):
    """
    Teresina is in the Piauí state
    """
    cal_class = BrazilTeresinaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Teresina
        self.assertIn(date(2017, 8, 16), holidays)


class BrazilCuritibaCityTest(BrazilParanaTest):
    """
    Curitiba is in the Paraná state
    """
    cal_class = BrazilCuritibaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Curitiba
        self.assertIn(date(2017, 3, 29), holidays)


class BrazilNatalCityTest(BrazilRioGrandeDoNorteTest):
    """
    Natal is in the Rio Grande do Norte state
    """
    cal_class = BrazilNatalCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Natal
        self.assertIn(date(2017, 12, 25), holidays)


class BrazilPortoVelhoCityTest(BrazilRondoniaTest):
    """
    Porto Velho is in the Rio Grande do Norte state
    """
    cal_class = BrazilPortoVelhoCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Porto Velho
        self.assertIn(date(2017, 10, 2), holidays)


class BrazilBoaVistaCityTest(BrazilRoraimaTest):
    """
    Boa Vista is in the Roraima state
    """
    cal_class = BrazilBoaVistaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Boa Vista
        self.assertIn(date(2017, 6, 9), holidays)


class BrazilPortoAlegreCityTest(BrazilRioGrandeDoSulTest):
    """
    Porto Alegre is in the Rio Grande do Sul state
    """
    cal_class = BrazilPortoAlegreCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Porto Alegre
        self.assertIn(date(2017, 3, 26), holidays)


class BrazilChapecoCityTest(BrazilSantaCatarinaTest):
    """
    Chapecó is in the Santa Catarina state
    """
    cal_class = BrazilChapecoCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Chapecó
        self.assertIn(date(2017, 8, 25), holidays)


class BrazilFlorianopolisCityTest(BrazilSantaCatarinaTest):
    """
    Florianópolis is in the Santa Catarina state
    """
    cal_class = BrazilFlorianopolisCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Florianópolis
        self.assertIn(date(2017, 3, 23), holidays)


class BrazilJoinvilleCityTest(BrazilSantaCatarinaTest):
    """
    Joinville is in the Santa Catarina state
    """
    cal_class = BrazilJoinvilleCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Joinville
        self.assertIn(date(2017, 3, 9), holidays)


class BrazilAracajuCityTest(BrazilSergipeTest):
    """
    Aracajú is in the Sergipe state
    """
    cal_class = BrazilAracajuCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Aracajú
        self.assertIn(date(2017, 3, 17), holidays)


class BrazilSorocabaCityTest(SaoPauloStateTest):
    """
    Sorocaba is in the São Paulo state
    """
    cal_class = BrazilSorocabaCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Sorocaba
        self.assertIn(date(2017, 8, 15), holidays)


class BrazilPalmasCityTest(BrazilTocantinsTest):
    """
    Palmas is in the Tocantins state
    """
    cal_class = BrazilPalmasCity

    def test_year_2017_city(self):
        holidays = self.cal.holidays_set(2017)
        # Fixed days
        # Aniversário de Palmas
        self.assertIn(date(2017, 5, 20), holidays)


class BrazilBankCalendarTest(BrazilTest):
    cal_class = BrazilBankCalendar

    def test_year_2017_holidays(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # New year
        self.assertIn(date(2017, 2, 27), holidays)  # Monday carnaval
        self.assertIn(date(2017, 2, 28), holidays)  # Tuesday carnaval
        self.assertIn(date(2017, 3, 1), holidays)  # Ash wednesday
        self.assertIn(date(2017, 4, 14), holidays)  # Good friday
        self.assertIn(date(2017, 4, 21), holidays)  # Tiradentes
        self.assertIn(date(2017, 5, 1), holidays)  # Labour day
        self.assertIn(date(2017, 6, 15), holidays)  # Corpus Christi
        self.assertIn(date(2017, 9, 7), holidays)  # Independence day
        self.assertIn(date(2017, 10, 12), holidays)  # Our Lady Aparecida
        self.assertIn(date(2017, 11, 2), holidays)  # All Souls' Day
        self.assertIn(date(2017, 11, 15), holidays)  # Republic day
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2017, 12, 29), holidays)  # Last working day of year
        self.assertEqual(14, len(holidays))

    def test_year_2017_find_next_working_day_for_new_year(self):
        new_year = date(2017, 1, 1)
        working_day = self.cal.find_following_working_day(new_year)
        self.assertEqual(working_day, date(2017, 1, 2))

    def test_year_2017_find_next_working_day_for_monday_carnaval(self):
        monday_carnaval = date(2017, 2, 27)
        working_day = self.cal.find_following_working_day(monday_carnaval)
        self.assertEqual(working_day, date(2017, 3, 2))

    def test_year_2017_find_next_working_day_for_tuesday_carnaval(self):
        tuesday_carnaval = date(2017, 2, 28)
        working_day = self.cal.find_following_working_day(tuesday_carnaval)
        self.assertEqual(working_day, date(2017, 3, 2))

    def test_year_2017_find_next_working_day_for_good_friday(self):
        good_friday = date(2017, 4, 14)
        working_day = self.cal.find_following_working_day(good_friday)
        self.assertEqual(working_day, date(2017, 4, 17))

    def test_year_2017_find_next_working_day_for_tiradentes(self):
        tiradentes = date(2017, 4, 21)
        working_day = self.cal.find_following_working_day(tiradentes)
        self.assertEqual(working_day, date(2017, 4, 24))

    def test_year_2017_find_next_working_day_for_labour_day(self):
        labour_day = date(2017, 5, 1)
        working_day = self.cal.find_following_working_day(labour_day)
        self.assertEqual(working_day, date(2017, 5, 2))

    def test_year_2017_find_next_working_day_for_corpus_christi(self):
        corpus_christi = date(2017, 6, 15)
        working_day = self.cal.find_following_working_day(corpus_christi)
        self.assertEqual(working_day, date(2017, 6, 16))

    def test_year_2017_find_next_working_day_for_independence_day(self):
        independence_day = date(2017, 9, 7)
        working_day = self.cal.find_following_working_day(independence_day)
        self.assertEqual(working_day, date(2017, 9, 8))

    def test_year_2017_find_next_working_day_for_our_lady_aparecida(self):
        our_lady_aparecida = date(2017, 10, 12)
        working_day = self.cal.find_following_working_day(our_lady_aparecida)
        self.assertEqual(working_day, date(2017, 10, 13))

    def test_year_2017_find_next_working_day_for_our_all_souls(self):
        all_souls = date(2017, 11, 2)
        working_day = self.cal.find_following_working_day(all_souls)
        self.assertEqual(working_day, date(2017, 11, 3))

    def test_year_2017_find_next_working_day_for_our_republic_day(self):
        republic_day = date(2017, 11, 15)
        working_day = self.cal.find_following_working_day(republic_day)
        self.assertEqual(working_day, date(2017, 11, 16))

    def test_year_2017_find_next_working_day_for_our_christmas_day(self):
        christmas_day = date(2017, 12, 25)
        working_day = self.cal.find_following_working_day(christmas_day)
        self.assertEqual(working_day, date(2017, 12, 26))

    def test_year_2017_find_next_working_day_for_last_day(self):
        # last day of year for only internal bank transactions
        last_day = date(2017, 12, 29)
        working_day = self.cal.find_following_working_day(last_day)
        self.assertEqual(working_day, date(2018, 1, 2))

    def test_year_2017_find_next_working_day_for_already_working_day(self):
        already_working_day = date(2017, 7, 25)
        working_day = self.cal.find_following_working_day(already_working_day)
        self.assertEqual(working_day, date(2017, 7, 25))

    def test_carnaval_label(self):
        holidays = self.cal.holidays(2017)
        holidays_dict = dict(holidays)
        label_carnaval = holidays_dict[date(2017, 2, 28)]
        self.assertEqual(label_carnaval, "Tuesday carnaval")

    def test_shift_last_day_of_the_year(self):
        # New Year's eve is on SAT
        holidays = self.cal.holidays_set(2022)
        # Shifted to the FRI before
        self.assertIn(date(2022, 12, 30), holidays)
        self.assertNotIn(date(2022, 12, 29), holidays)

        # New Year's eve is on SUN
        holidays = self.cal.holidays_set(2017)
        # Shifted to the FRI before
        self.assertNotIn(date(2017, 12, 30), holidays)
        self.assertIn(date(2017, 12, 29), holidays)


class TestIBGERegister(TestCase):

    def test_register_length(self):
        # Each time another calendar will be added, this length should increase
        # This also fails when a key appears twice (typo mistake?)
        self.assertEqual(len(IBGE_REGISTER), len(IBGE_TUPLE))

    def test_no_duplicate(self):
        # Check if a class doesn't appear twice with different keys
        values = set(IBGE_REGISTER.values())
        self.assertEqual(len(IBGE_REGISTER.values()), len(values))

    def test_all_are_brazilian_classes(self):
        for key, value in IBGE_TUPLE:
            self.assertTrue(issubclass(value, Brazil))
