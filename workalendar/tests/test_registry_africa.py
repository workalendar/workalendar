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
        classes = (v for k, v in registry.region_registry.items())
        classes = list(classes)
        self.assertIn(Algeria, classes)
        self.assertIn(Benin, classes)
        self.assertIn(IvoryCoast, classes)
        self.assertIn(Madagascar, classes)
        self.assertIn(SaoTomeAndPrincipe, classes)
        self.assertIn(SouthAfrica, classes)
