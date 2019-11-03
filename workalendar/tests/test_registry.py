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


class MockCalendarTest(TestCase):

    def setUp(self):
        self.region = RegionCalendar
        self.subregion = SubRegionCalendar

    def test_register(self):
        registry = IsoRegistry(load_standard_modules=False)
        self.assertEqual(0, len(registry.region_registry.items()))
        registry.register('RE', self.region)
        self.assertEqual(1, len(registry.region_registry.items()))
        self.assertEqual(RegionCalendar, registry.region_registry['RE'])

    def test_get_calendar_class(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        calendar_class = registry.get_calendar_class('RE')
        self.assertEqual(calendar_class, RegionCalendar)

    def test_get_subregions(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE-SR', self.subregion)
        registry.register('OR-SR', self.subregion)
        subregions = registry.get_subregions('RE')
        self.assertIn('RE-SR', subregions)
        self.assertEqual(1, len(subregions))

    def test_get_items(self):
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

    def test_register_non_calendar(self):
        registry = IsoRegistry(load_standard_modules=False)
        with self.assertRaises(ISORegistryError):
            registry.register("NAC", NotACalendarClass)
