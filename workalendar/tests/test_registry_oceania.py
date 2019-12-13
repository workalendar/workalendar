from unittest import TestCase

from workalendar.registry import registry

# Australian territories;
from workalendar.oceania import (
    Australia,
    AustralianCapitalTerritory,
    MarshallIslands,
    NewSouthWales,
    NewZealand,
    NorthernTerritory,
    Queensland,
    SouthAustralia,
    Tasmania,
    Victoria,
    WesternAustralia,
)

# FIXME: There are no ISO code for Hobart city.
AUSTRALIAN_TERRITORIES = (
    AustralianCapitalTerritory,
    NewSouthWales,
    NorthernTerritory,
    Queensland,
    SouthAustralia,
    Tasmania,
    Victoria,
    WesternAustralia,
)


class RegistryOceania(TestCase):
    def test_oceania(self):
        classes = (v for k, v in registry.region_registry.items())
        classes = list(classes)
        self.assertIn(Australia, classes)
        self.assertIn(MarshallIslands, classes)
        self.assertIn(NewZealand, classes)
        for klass in AUSTRALIAN_TERRITORIES:
            self.assertIn(klass, classes)

    def test_australia_territories(self):
        # Get all the subregions
        classes = (v for k, v in registry.get_subregions("AU").items())
        classes = list(classes)
        for klass in AUSTRALIAN_TERRITORIES:
            self.assertIn(klass, classes)
