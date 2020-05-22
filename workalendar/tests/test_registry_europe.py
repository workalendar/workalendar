from unittest import TestCase
from ..europe import (
    Austria, Belgium, Bulgaria, Croatia, Cyprus, CzechRepublic, Estonia,
    Denmark, Finland, France,
    # FranceAlsaceMoselle,  # TODO: Should we add it to the registry?
    Greece, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Luxembourg,
    Malta, Netherlands, Norway, Poland, Portugal, Romania, Russia, Slovakia,
    Slovenia, Spain,
    # Catalonia,  # TODO: Add it to registry
    Sweden, UnitedKingdom,
    UnitedKingdomNorthernIreland,
)

# Switzerland
from ..europe import (
    Switzerland,
    Aargau, AppenzellInnerrhoden, AppenzellAusserrhoden, Bern, BaselLandschaft,
    BaselStadt, Fribourg, Geneva, Glarus, Graubunden, Jura, Luzern, Neuchatel,
    Nidwalden, Obwalden, StGallen, Schaffhausen, Solothurn, Schwyz, Thurgau,
    Ticino, Uri, Vaud, Valais, Zug, Zurich
)

# Germany
from ..europe import (
    Germany, BadenWurttemberg, Bavaria, Berlin, Brandenburg, Bremen,
    Hamburg, Hesse, MecklenburgVorpommern, LowerSaxony,
    NorthRhineWestphalia, RhinelandPalatinate, Saarland, Saxony,
    SaxonyAnhalt, SchleswigHolstein, Thuringia
)

from ..registry import registry

classes = (v for k, v in registry.region_registry.items())
classes = list(classes)

GERMANY_REGION_CLASSES = (
    BadenWurttemberg, Bavaria, Berlin, Brandenburg, Bremen,
    Hamburg, Hesse, MecklenburgVorpommern, LowerSaxony,
    NorthRhineWestphalia, RhinelandPalatinate, Saarland, Saxony,
    SaxonyAnhalt, SchleswigHolstein, Thuringia
)

SWITZERLAND_REGION_CLASSES = (
    Aargau, AppenzellInnerrhoden, AppenzellAusserrhoden, Bern, BaselLandschaft,
    BaselStadt, Fribourg, Geneva, Glarus, Graubunden, Jura, Luzern, Neuchatel,
    Nidwalden, Obwalden, StGallen, Schaffhausen, Solothurn, Schwyz, Thurgau,
    Ticino, Uri, Vaud, Valais, Zug, Zurich
)


class RegistryEurope(TestCase):
    def test_europe(self):
        self.assertIn(Austria, classes)
        self.assertIn(Belgium, classes)
        self.assertIn(Bulgaria, classes)
        self.assertIn(Croatia, classes)
        self.assertIn(Cyprus, classes)
        self.assertIn(CzechRepublic, classes)
        self.assertIn(Estonia, classes)
        self.assertIn(Denmark, classes)
        self.assertIn(Finland, classes)
        self.assertIn(France,  classes)
        self.assertIn(Greece, classes)
        self.assertIn(Hungary, classes)
        self.assertIn(Iceland, classes)
        self.assertIn(Ireland, classes)
        self.assertIn(Italy, classes)
        self.assertIn(Latvia, classes)
        self.assertIn(Lithuania, classes)
        self.assertIn(Luxembourg, classes)
        self.assertIn(Malta, classes)
        self.assertIn(Netherlands, classes)
        self.assertIn(Norway, classes)
        self.assertIn(Poland, classes)
        self.assertIn(Portugal, classes)
        self.assertIn(Romania, classes)
        self.assertIn(Russia, classes)
        self.assertIn(Slovakia, classes)
        self.assertIn(Slovenia, classes)
        self.assertIn(Spain,  classes)
        self.assertIn(Sweden, classes)
        self.assertIn(Switzerland, classes)
        self.assertIn(Vaud, classes)
        self.assertIn(Geneva, classes)
        self.assertIn(UnitedKingdom, classes)
        self.assertIn(UnitedKingdomNorthernIreland, classes)
        # Germany & Länders
        self.assertIn(Germany, classes)
        for klass in GERMANY_REGION_CLASSES:
            self.assertIn(klass, classes)
        for klass in SWITZERLAND_REGION_CLASSES:
            self.assertIn(klass, classes)

    def test_germany_subregion(self):
        # Get all the subregions
        classes = (v for k, v in registry.get_subregions('DE').items())
        classes = list(classes)
        for klass in GERMANY_REGION_CLASSES:
            self.assertIn(klass, classes)

    def test_switzerland_subregion(self):
        # Get all the subregions
        classes = (v for k, v in registry.get_subregions('CH').items())
        classes = list(classes)
        for klass in SWITZERLAND_REGION_CLASSES:
            self.assertIn(klass, classes)

    def test_slovenia_code(self):
        # Source: https://github.com/peopledoc/workalendar/pull/291
        self.assertEqual(registry.region_registry['SI'], Slovenia)
