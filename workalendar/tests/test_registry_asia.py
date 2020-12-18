from unittest import TestCase

from ..asia import (
    China,
    HongKong,
    Japan,
    Malaysia,
    Qatar,
    Singapore,
    SouthKorea,
    Taiwan,
)

from ..registry import registry


class RegistryAsia(TestCase):
    def test_asia(self):
        classes = set(registry.region_registry.values())
        self.assertIn(China, classes)
        self.assertIn(HongKong, classes)
        self.assertIn(Japan, classes)
        self.assertIn(Malaysia, classes)
        self.assertIn(Qatar, classes)
        self.assertIn(Singapore, classes)
        self.assertIn(SouthKorea, classes)
        self.assertIn(Taiwan, classes)
