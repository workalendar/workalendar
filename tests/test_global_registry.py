from unittest import TestCase

from workalendar.registry import registry


class GlobalRegistry(TestCase):

    def test_name(self):
        classes = (v for k, v in registry.region_registry.items())
        classes = list(classes)
        for klass in classes:
            # All classes have a `name` class property
            self.assertTrue(hasattr(klass, 'name'))
            # All classes have a non-empty name
            self.assertTrue(klass.name)
            # All those properties are equivalent to the class docstring
            self.assertEqual(klass.name, klass.__doc__)
