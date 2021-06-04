from unittest import TestCase
from ..europe import (
    Austria, Belgium, Bulgaria, Croatia, Cyprus, CzechRepublic, Estonia,
    Denmark, Finland, France,
    # FranceAlsaceMoselle,  # TODO: Should we add it to the registry?
    Greece, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Luxembourg,
    Malta, Monaco, Netherlands, Norway, Poland, Portugal, Romania, Russia,
    Slovakia, Slovenia,
    Sweden, UnitedKingdom,
    UnitedKingdomNorthernIreland,
)

# Spain & regions
from ..europe import (
    Spain, Andalusia, Aragon, Catalonia, CastileAndLeon, CastillaLaMancha,
    CanaryIslands, Extremadura, Galicia, BalearicIslands, LaRioja,
    CommunityofMadrid, Murcia, Navarre, Asturias, BasqueCountry, Cantabria,
    ValencianCommunity,
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

classes = set(registry.region_registry.values())

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

SPAIN_REGION_CLASSES = (
    Andalusia, Aragon, Catalonia, CastileAndLeon, CastillaLaMancha,
    CanaryIslands, Extremadura, Galicia, BalearicIslands, LaRioja,
    CommunityofMadrid, Murcia, Navarre, Asturias, BasqueCountry, Cantabria,
    ValencianCommunity,
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
        self.assertIn(Monaco, classes)
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
        for klass in SPAIN_REGION_CLASSES:
            self.assertIn(klass, classes)

    def test_germany_subregions(self):
        # Get all the subregions
        classes = set(registry.get_subregions('DE').values())
        for klass in GERMANY_REGION_CLASSES:
            self.assertIn(klass, classes)

    def test_switzerland_subregions(self):
        # Get all the subregions
        classes = set(registry.get_subregions('CH').values())
        for klass in SWITZERLAND_REGION_CLASSES:
            self.assertIn(klass, classes)

    def test_spain_subregions(self):
        # Get all the subregions
        classes = set(registry.get_subregions('ES').values())
        for klass in SPAIN_REGION_CLASSES:
            self.assertIn(klass, classes)

    def test_slovenia_code(self):
        # Source: https://github.com/workalendar/workalendar/pull/291
        self.assertEqual(registry.region_registry['SI'], Slovenia)
