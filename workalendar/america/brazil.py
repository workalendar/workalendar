# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import timedelta

from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON


class Brazil(WesternCalendar, ChristianMixin):
    "Brazil"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 21, "Tiradentes' Day"),
        (5, 1, "Labour Day"),
        (9, 7, "Independence Day"),
        (10, 12, "Our Lady of Aparecida"),
        (11, 2, "All Souls' Day"),
        (11, 15, "Republic Day"),
    )

    def get_carnaval(self, year):
        """
        Return the third day of Carnaval (Tuesday)

        This day is shared holidays by several Brazil states.
        """
        return self.get_easter_sunday(year) - timedelta(days=47)


class BrazilAcre(Brazil):
    "Brazil Acre State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (1, 23, "Dia do evangélico"),
        (6, 15, "Aniversário do Acre"),
        (9, 5, "Dia da Amazônia"),
        (11, 17, "Assinatura do Tratado de Petrópolis"),
    )


class BrazilAlagoas(Brazil):
    "Brazil Alagoas State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (6, 24, "São João"),
        (6, 29, "São Pedro"),
        (9, 16, "Emancipação política de Alagoas"),
        (11, 20, "Consciência Negra")
    )


class BrazilAmapa(Brazil):
    "Brazil Amapá State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (3, 19, "Dia de São José"),
        (7, 25, "São Tiago"),
        (10, 5, "Criação do estado"),
        (11, 20, "Consciência Negra"),
    )


class BrazilAmazonas(Brazil):
    "Brazil Amazonas State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (9, 5, "Elevação do Amazonas á categoria de província"),
        (11, 20, "Consciência Negra"),
        (12, 8, "Dia de Nossa Senhora da Conceição"),
    )


class BrazilBahia(Brazil):
    "Brazil Bahia State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 2, "Independência da Bahia"),
    )


class BrazilCeara(Brazil):
    "Brazil Ceará State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (3, 19, "São José"),
        (3, 23, "Data Manga do Ceará")
    )


class BrazilDistritoFederal(Brazil):
    "Brazil Distrito Federal State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (4, 21, "Fundação de Brasília"),
        (11, 30, "Dia do Evangélico"),
    )


class BrazilEspiritoSanto(Brazil):
    "Brazil Espírito Santo State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (10, 28, "Dia do Servidor Público"),
    )


class BrazilGoias(Brazil):
    "Brazil Goiás State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (10, 28, "Dia do Servidor Público"),
    )


class BrazilMaranhao(Brazil):
    "Brazil Maranhão State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 28, "Adesão do Maranhão á independência do Brasil"),
        (12, 8, "Dia de Nossa Senhora da Conceição"),
    )


class BrazilMatoGrosso(Brazil):
    "Brazil Mato Grosso State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (11, 29, "Consciência Negra"),
    )


class BrazilMatoGrossoDoSul(Brazil):
    "Brazil Mato Grosso do Sul State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (10, 11, "Criação do estado"),
    )


class BrazilPara(Brazil):
    "Brazil Pará State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (8, 15, "Adesão do Grão-Pará á independência do Brasil"),
    )


class BrazilParaiba(Brazil):
    "Brazil Paraíba State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (8, 5, "Fundação do Estado"),
    )


class BrazilPernambuco(Brazil):
    "Brazil Pernambuco State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (6, 24, "São João"),
    )


class BrazilPiaui(Brazil):
    "Brazil Piauí State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (3, 13, "Dia da Batalha do Jenipapo"),
        (10, 19, "Dia do Piauí"),
    )


class BrazilRioDeJaneiro(Brazil):
    "Brazil Rio de Janeiro State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (4, 23, "Dia de São Jorge"),
        (10, 28, "Dia do Funcionário Público"),
        (11, 20, "Dia da Consciência Negra"),
        (12, 8, "Dia de Nossa Senhora da Conceição"),
    )

    def get_dia_do_comercio(self, year):
        """
        Return Dia do Comércio variable date

        It happens on the 3rd Monday of october.
        """
        return BrazilRioDeJaneiro.get_nth_weekday_in_month(year, 10, MON, 3)

    def get_variable_days(self, year):
        days = super(BrazilRioDeJaneiro, self).get_variable_days(year)
        days.append((self.get_carnaval(year), "Carnaval"))
        days.append((self.get_dia_do_comercio(year), "Dia do Comércio"))
        return days


class BrazilRioGrandeDoNorte(Brazil):
    "Brazil Rio Grande do Norte State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (6, 29, "Dua de São Pedro"),
        (10, 3, "Mártires de Cunhaú e Uruaçuu"),
    )


class BrazilRioGrandeDoSul(Brazil):
    "Brazil Rio Grande do Sul State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (9, 20, "Revolução Farroupilha"),
    )


class BrazilRondonia(Brazil):
    "Brazil Rondônia State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (1, 4, "Criação do estado"),
        (6, 18, "Dia do Evangélico"),
    )


class BrazilRoraima(Brazil):
    "Brazil Roraima State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (10, 5, "Criação de Roraima"),
    )


class BrazilSantaCatarina(Brazil):
    "Brazil Santa Catarina State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (8, 11, "Criação da capitania, separando-se de SP"),
    )


class BrazilSaoPauloState(Brazil):
    "Brazil São Paulo State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 9, "Constitutional Revolution of 1932"),
    )


class BrazilSaoPauloCity(BrazilSaoPauloState):
    "Brazil São Paulo City"
    FIXED_HOLIDAYS = BrazilSaoPauloState.FIXED_HOLIDAYS + (
        (1, 25, "Anniversary of the city of São Paulo"),
        (11, 20, "Dia da Consciência Negra")
    )
    include_easter_sunday = True
    include_corpus_christi = True
    include_good_friday = True
    good_friday_label = "Sexta-feira da Paixão"

    def get_variable_days(self, year):
        days = super(BrazilSaoPauloCity, self).get_variable_days(year)
        days.append((self.get_carnaval(year), "Carnaval"))
        return days


class BrazilSergipe(Brazil):
    "Brazil Sergipe State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 8, "Autonomia política de Sergipe"),
    )


class BrazilTocantins(Brazil):
    "Brazil Tocantins State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (1, 1, "Instalação de Tocantins"),
        (9, 8, "Nossa Senhora da Natividade"),
        (10, 5, "Criação de Tocantins"),
    )


class BrazilVitoriaCity(Brazil):
    "Brazil Vitória City"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (4, 24, "Nossa Senhora da Penha"),  # Our Lady of Pain?
        (9, 8, "Nossa Senhora da Vitória"),  # Our Lady of Vitória
    )
    include_corpus_christi = True
    include_good_friday = True
    good_friday_label = "Paixão do Cristo"


class BrazilVilaVelhaCity(Brazil):
    "Brazil Vila Velha City"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (5, 23, "Colonização do Solo Espírito-santense"),
    )


class BrazilCariacicaCity(Brazil):
    "Brazil Cariacica City"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (4, 13, "Nossa Senhora da Penha"),
        (6, 24, "São João Batista / Aniversãrio de Cariacica"),
    )
    include_corpus_christi = True
    include_good_friday = True
    good_friday_label = "Paixão do Cristo"


class BrazilGuarapariCity(Brazil):
    "Brazil Guarapari City"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (6, 29, "São Pedro"),
        (9, 19, "Emancipação de Guarapari"),
        (11, 29, "Consciência Negra"),
        (12, 8, "Nossa Senhora Conceição"),
    )
