from unittest import TestCase

from workalendar.registry import IsoRegistry
from workalendar.core import Calendar
from workalendar.exceptions import ISORegistryError


class RegionCalendar(Calendar):
    'Region'


class SubRegionCalendar(Calendar):
    'Sub Region'


class NotACalendarClass(object):
    "Not a Calendar"


class NonStandardRegistryTest(TestCase):

    def setUp(self):
        self.region = RegionCalendar
        self.subregion = SubRegionCalendar

    def test_region_registry(self):
        registry = IsoRegistry(load_standard_modules=False)
        self.assertEqual(0, len(registry.region_registry.items()))
        registry.register('RE', self.region)
        self.assertEqual(1, len(registry.region_registry.items()))
        self.assertEqual(RegionCalendar, registry.region_registry['RE'])

    def test_register_non_calendar(self):
        registry = IsoRegistry(load_standard_modules=False)
        with self.assertRaises(ISORegistryError):
            registry.register("NAC", NotACalendarClass)

    def test_get_calendar_class(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE-SR', self.subregion)
        calendar_class = registry.get_calendar_class('RE')
        self.assertEqual(calendar_class, RegionCalendar)
        # Subregion
        calendar_class = registry.get_calendar_class('RE-SR')
        self.assertEqual(calendar_class, SubRegionCalendar)
        # Unknown code/region
        self.assertIsNone(registry.get_calendar_class('XX'))

    def test_get_subregions(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE-SR', self.subregion)
        registry.register('OR-SR', self.subregion)
        subregions = registry.get_subregions('RE')
        # Only one sub-region here
        self.assertEqual(1, len(subregions))
        self.assertIn('RE-SR', subregions)

    def test_items(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE-SR', self.subregion)
        registry.register('OR-SR', self.subregion)
        items = registry.items(['RE'], include_subregions=True)
        self.assertEqual(2, len(items))
        self.assertIn('RE', items)
        self.assertIn('RE-SR', items)
        items = registry.items(['RE'], include_subregions=False)
        self.assertEqual(1, len(items))
        self.assertIn('RE', items)

    def test_items_unknown(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        items = registry.items(['XX'])
        self.assertEqual(items, {})

    def test_items_with_subregions(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE2', self.region)
        registry.register('RE-SR', self.subregion)
        items = registry.items(['RE2', "RE-SR"], include_subregions=True)
        self.assertEqual(2, len(items))
        self.assertIn('RE2', items)
        self.assertIn('RE-SR', items)
        items = registry.items(['RE2', "RE-SR"], include_subregions=False)
        self.assertEqual(2, len(items))
        self.assertIn('RE2', items)
        self.assertIn('RE-SR', items)

        # Only a subregion
        items = registry.items(["RE-SR"], include_subregions=True)
        self.assertEqual(1, len(items))
        self.assertIn('RE-SR', items)

    def test_items_empty_arg(self):
        registry = IsoRegistry(load_standard_modules=False)
        # 3 regions, one sub-region
        registry.register('RE', self.region)
        registry.register('RE2', self.region)
        registry.register('RE3', self.region)
        registry.register('RE-SR', self.subregion)
        items = registry.items([], include_subregions=False)
        self.assertEqual(len(items), 3)
        self.assertEqual(set({"RE", "RE2", "RE3"}), set(items.keys()))
        items = registry.items([], include_subregions=True)
        self.assertEqual(len(items), 4)
        self.assertEqual(set({"RE", "RE2", "RE3", "RE-SR"}), set(items.keys()))

    def test_items_no_arg(self):
        registry = IsoRegistry(load_standard_modules=False)
        # 3 regions, one sub-region
        registry.register('RE', self.region)
        registry.register('RE2', self.region)
        registry.register('RE3', self.region)
        registry.register('RE-SR', self.subregion)

        # Should be equivalent to [] + no subregions
        items_no_arg = registry.items()
        self.assertEqual(len(items_no_arg), 3)
        self.assertEqual(set({"RE", "RE2", "RE3"}), set(items_no_arg.keys()))

        # Should be equivalent to [] + include subregions
        items = registry.items(include_subregions=True)
        self.assertEqual(len(items), 4)
        self.assertEqual(set({"RE", "RE2", "RE3", "RE-SR"}), set(items.keys()))
