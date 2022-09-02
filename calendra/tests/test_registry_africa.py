from unittest import TestCase

from ..africa import (
    Algeria,
    Benin,
    IvoryCoast,
    Madagascar,
    SaoTomeAndPrincipe,
    SouthAfrica,
)
from ..registry import registry


class RegistryAfrica(TestCase):
    def test_africa(self):
        classes = set(registry.region_registry.values())
        self.assertIn(Algeria, classes)
        self.assertIn(Benin, classes)
        self.assertIn(IvoryCoast, classes)
        self.assertIn(Madagascar, classes)
        self.assertIn(SaoTomeAndPrincipe, classes)
        self.assertIn(SouthAfrica, classes)
