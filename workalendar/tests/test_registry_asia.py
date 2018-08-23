# -*- coding: utf-8 -*-
from unittest import TestCase

from workalendar.asia import (
    HongKong,
    Japan,
    Malaysia,
    Qatar,
    Singapore,
    SouthKorea,
    Taiwan,
)

from workalendar.registry import registry


class RegistryAsia(TestCase):
    def test_asia(self):
        classes = (v for k, v in registry.region_registry.items())
        classes = list(classes)
        self.assertIn(HongKong, classes)
        self.assertIn(Japan, classes)
        self.assertIn(Malaysia, classes)
        self.assertIn(Qatar, classes)
        self.assertIn(Singapore, classes)
        self.assertIn(SouthKorea, classes)
        self.assertIn(Taiwan, classes)
