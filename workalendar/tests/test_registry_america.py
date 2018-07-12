# -*- coding: utf-8 -*-
from unittest import TestCase

from workalendar.america import (
    Brazil, BrazilAcre, BrazilAlagoas, BrazilAmapa, BrazilAmazonas,
    BrazilBahia, BrazilCeara, BrazilDistritoFederal, BrazilEspiritoSanto,
    BrazilGoias, BrazilMaranhao, BrazilMatoGrosso, BrazilMatoGrossoDoSul,
    BrazilPara, BrazilParaiba, BrazilPernambuco, BrazilPiaui,
    BrazilRioDeJaneiro, BrazilRioGrandeDoNorte, BrazilRioGrandeDoSul,
    BrazilRondonia, BrazilRoraima, BrazilSantaCatarina, BrazilSaoPauloState,
    BrazilSergipe, BrazilTocantins,
)
from workalendar.america import (
    Canada,
    Ontario,
    Quebec,
    BritishColumbia,
    Alberta,
    Saskatchewan,
    Manitoba,
    NewBrunswick,
    NovaScotia,
    PrinceEdwardIsland,
    Newfoundland,
    Yukon,
    NorthwestTerritories,
    Nunavut,

)
from workalendar.america import Chile, Colombia, Mexico, Panama

from workalendar.registry import registry


class RegistryAmerica(TestCase):

    def _check_brazil_states(self, classes):
        self.assertIn(BrazilAcre, classes)
        self.assertIn(BrazilAlagoas, classes)
        self.assertIn(BrazilAmapa, classes)
        self.assertIn(BrazilAmazonas, classes)
        self.assertIn(BrazilBahia, classes)
        self.assertIn(BrazilCeara, classes)
        self.assertIn(BrazilDistritoFederal, classes)
        self.assertIn(BrazilEspiritoSanto, classes)
        self.assertIn(BrazilGoias, classes)
        self.assertIn(BrazilMaranhao, classes)
        self.assertIn(BrazilMatoGrosso, classes)
        self.assertIn(BrazilMatoGrossoDoSul, classes)
        self.assertIn(BrazilPara, classes)
        self.assertIn(BrazilParaiba, classes)
        self.assertIn(BrazilPernambuco, classes)
        self.assertIn(BrazilPiaui, classes)
        self.assertIn(BrazilRioDeJaneiro, classes)
        self.assertIn(BrazilRioGrandeDoNorte, classes)
        self.assertIn(BrazilRioGrandeDoSul, classes)
        self.assertIn(BrazilRondonia, classes)
        self.assertIn(BrazilRoraima, classes)
        self.assertIn(BrazilSantaCatarina, classes)
        self.assertIn(BrazilSaoPauloState, classes)
        self.assertIn(BrazilSergipe, classes)
        self.assertIn(BrazilTocantins, classes)

    def _check_canada_provinces(self, classes):
        self.assertIn(Ontario, classes)
        self.assertIn(Quebec, classes)
        self.assertIn(BritishColumbia, classes)
        self.assertIn(Alberta, classes)
        self.assertIn(Saskatchewan, classes)
        self.assertIn(Manitoba, classes)
        self.assertIn(NewBrunswick, classes)
        self.assertIn(NovaScotia, classes)
        self.assertIn(PrinceEdwardIsland, classes)
        self.assertIn(Newfoundland, classes)
        self.assertIn(Yukon, classes)
        self.assertIn(NorthwestTerritories, classes)
        self.assertIn(Nunavut, classes)

    def test_america(self):
        classes = (v for k, v in registry.region_registry.items())
        classes = list(classes)
        self.assertIn(Brazil, classes)
        self._check_brazil_states(classes)

        self.assertIn(Canada, classes)
        self._check_canada_provinces(classes)

        self.assertIn(Chile, classes)
        self.assertIn(Colombia, classes)
        self.assertIn(Mexico, classes)
        self.assertIn(Panama, classes)

    def test_brazil_subregion(self):
        classes = (v for k, v in registry.get_subregions('BR').items())
        classes = list(classes)
        self._check_brazil_states(classes)

    def test_canada_subregion(self):
        classes = (v for k, v in registry.get_subregions('CA').items())
        classes = list(classes)
        self._check_canada_provinces(classes)
