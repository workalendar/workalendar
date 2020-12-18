from unittest import TestCase

from ..registry import registry


class GlobalRegistry(TestCase):

    def test_name(self):
        for klass in registry.region_registry.values():
            # All classes have a `name` class property
            self.assertTrue(hasattr(klass, 'name'))
            # All classes have a non-empty name
            self.assertTrue(klass.name)
            # All those properties are equivalent to the class docstring
            self.assertEqual(klass.name, klass.__doc__)
