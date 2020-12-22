from unittest import TestCase
import warnings

from ..core import Calendar
from ..exceptions import ISORegistryError
from ..registry import IsoRegistry


class RegionCalendar(Calendar):
    'Region'


class SubRegionCalendar(Calendar):
    'Sub Region'


class NotACalendarClass:
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

    def test_get(self):
        # get() is the new name for `get_calendar_class()`
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE-SR', self.subregion)
        calendar_class = registry.get('RE')
        self.assertEqual(calendar_class, RegionCalendar)
        # Subregion
        calendar_class = registry.get('RE-SR')
        self.assertEqual(calendar_class, SubRegionCalendar)
        # Unknown code/region
        self.assertIsNone(registry.get('XX'))

    def test_get_calendar_class_alias(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        self.assertEqual(
            registry.get('RE'),
            registry.get_calendar_class('RE')
        )

    def test_get_calendar_class_deprecation(self):
        registry = IsoRegistry(load_standard_modules=False)
        with warnings.catch_warnings(record=True) as w:
            # Cause all warnings to always be triggered.
            warnings.simplefilter("always")
            # Trigger a warning.
            registry.get_calendar_class("RE")
            # Verify some things
            self.assertEqual(len(w), 1)
            warning = w[0]
            self.assertTrue(issubclass(warning.category, DeprecationWarning))
            self.assertIn("deprecated", str(warning.message))

    def test_get_subregions(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE-SR', self.subregion)
        registry.register('OR-SR', self.subregion)
        subregions = registry.get_subregions('RE')
        # Only one sub-region here
        self.assertEqual(1, len(subregions))
        self.assertIn('RE-SR', subregions)

    def test_get_calendars(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE-SR', self.subregion)
        registry.register('OR-SR', self.subregion)
        calendars = registry.get_calendars(['RE'], include_subregions=True)
        self.assertEqual(2, len(calendars))
        self.assertIn('RE', calendars)
        self.assertIn('RE-SR', calendars)
        calendars = registry.get_calendars(['RE'], include_subregions=False)
        self.assertEqual(1, len(calendars))
        self.assertIn('RE', calendars)

    def test_get_calendars_unknown(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        calendars = registry.get_calendars(['XX'])
        self.assertEqual(calendars, {})

    def test_get_calendars_with_subregions(self):
        registry = IsoRegistry(load_standard_modules=False)
        registry.register('RE', self.region)
        registry.register('RE2', self.region)
        registry.register('RE-SR', self.subregion)
        calendars = registry.get_calendars(
            ['RE2', "RE-SR"], include_subregions=True)
        self.assertEqual(2, len(calendars))
        self.assertIn('RE2', calendars)
        self.assertIn('RE-SR', calendars)
        calendars = registry.get_calendars(
            ['RE2', "RE-SR"], include_subregions=False)
        self.assertEqual(2, len(calendars))
        self.assertIn('RE2', calendars)
        self.assertIn('RE-SR', calendars)

        # Only a subregion
        calendars = registry.get_calendars(["RE-SR"], include_subregions=True)
        self.assertEqual(1, len(calendars))
        self.assertIn('RE-SR', calendars)

    def test_get_calendars_empty_arg(self):
        registry = IsoRegistry(load_standard_modules=False)
        # 3 regions, one sub-region
        registry.register('RE', self.region)
        registry.register('RE2', self.region)
        registry.register('RE3', self.region)
        registry.register('RE-SR', self.subregion)
        # Empty arg, no subregions
        calendars = registry.get_calendars([], include_subregions=False)
        self.assertEqual(len(calendars), 3)
        self.assertEqual(set({"RE", "RE2", "RE3"}), set(calendars.keys()))
        # Empty arg, with subregions
        calendars = registry.get_calendars([], include_subregions=True)
        self.assertEqual(len(calendars), 4)
        self.assertEqual(
            set({"RE", "RE2", "RE3", "RE-SR"}),
            set(calendars.keys())
        )

    def test_get_calendars_no_arg(self):
        registry = IsoRegistry(load_standard_modules=False)
        # 3 regions, one sub-region
        registry.register('RE', self.region)
        registry.register('RE2', self.region)
        registry.register('RE3', self.region)
        registry.register('RE-SR', self.subregion)

        # Should be equivalent to [] + no subregions
        calendars = registry.get_calendars()
        self.assertEqual(len(calendars), 3)
        self.assertEqual(set({"RE", "RE2", "RE3"}), set(calendars.keys()))

        # Should be equivalent to [] + include subregions
        calendars = registry.get_calendars(include_subregions=True)
        self.assertEqual(len(calendars), 4)
        self.assertEqual(
            set({"RE", "RE2", "RE3", "RE-SR"}),
            set(calendars.keys()))
