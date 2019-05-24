from datetime import date
from unittest import TestCase

from workalendar.registry import IsoRegistry
from workalendar.core import Calendar


class RegionCalendar(Calendar):
    'Region'

    def holidays(self, year=None):
        return tuple((
            (date(year, 12, 25), 'Christmas'),
            (date(year, 1, 1), 'New year'),
        ))

    def get_weekend_days(self):
        return []  # no week-end, yes, it's sad


class SubRegionCalendar(Calendar):
    'Sub Region'

    def holidays(self, year=None):
        return tuple((
            (date(year, 12, 25), 'Christmas'),
            (date(year, 1, 1), 'New year'),
        ))

    def get_weekend_days(self):
        return []  # no week-end, yes, it's sad


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
