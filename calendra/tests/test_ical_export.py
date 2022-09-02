import tempfile
from pathlib import Path

from ..core import Calendar
from ..exceptions import ICalExportRangeError, ICalExportTargetPathError

from . import CoreCalendarTest


class FakeCalendar(Calendar):
    """Fake Calendar"""


class IcalExportPeriodTest(CoreCalendarTest):
    cal_class = FakeCalendar

    def test_empty_range(self):
        # No period means 2000-2030
        result = self.cal._get_ical_period()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2000)
        self.assertEqual(result[1], 2030)
        # No period means 2000-2030
        result = self.cal._get_ical_period(period=())
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2000)
        self.assertEqual(result[1], 2030)
        # No period means 2000-2030
        result = self.cal._get_ical_period(period=[])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2000)
        self.assertEqual(result[1], 2030)

    def test_range_lists(self):
        # Period: 2010-2020
        result = self.cal._get_ical_period(period=[2010, 2020])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2010)
        self.assertEqual(result[1], 2020)

        # Bad period: 2020-2010 => Swap terms
        result = self.cal._get_ical_period(period=[2020, 2010])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2010)
        self.assertEqual(result[1], 2020)

        # Too long of a list => take the extremes
        result = self.cal._get_ical_period(period=[2010, 2015, 2020])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2010)
        self.assertEqual(result[1], 2020)

        # Assume that the range is only one year
        result = self.cal._get_ical_period(period=[2020, 2020])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2020)
        self.assertEqual(result[1], 2020)

    def test_range_tuples(self):
        # Period: 2010-2020
        result = self.cal._get_ical_period(period=(2010, 2020))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2010)
        self.assertEqual(result[1], 2020)

        # Bad period: 2020-2010 => Swap terms
        result = self.cal._get_ical_period(period=(2020, 2010))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2010)
        self.assertEqual(result[1], 2020)

        # Too long of a list => take the extremes
        result = self.cal._get_ical_period(period=(2010, 2015, 2020))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2010)
        self.assertEqual(result[1], 2020)

        # Assume that the range is only one year
        result = self.cal._get_ical_period(period=(2020, 2020))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 2020)
        self.assertEqual(result[1], 2020)

    def test_bad_ranges(self):
        # Bad period: String
        with self.assertRaises(ICalExportRangeError):
            self.cal._get_ical_period(period="something")

        # Bad period: Dict
        with self.assertRaises(ICalExportRangeError):
            self.cal._get_ical_period(period={"a": 2000, "b": "foobar"})

        # Bad period: List of non-integers
        with self.assertRaises(ICalExportRangeError):
            self.cal._get_ical_period(period=["foo", "bar"])

        # Bad period: Tuple of non-integers
        with self.assertRaises(ICalExportRangeError):
            self.cal._get_ical_period(period=("foo", "bar"))


class ICalExportTargetPath(CoreCalendarTest):
    cal_class = FakeCalendar

    def test_empty_path(self):
        with self.assertRaises(ICalExportTargetPathError):
            self.cal._get_ical_target_path("")

        with self.assertRaises(ICalExportTargetPathError):
            self.cal._get_ical_target_path(None)

    def test_target_is_directory(self):
        temp_dir = Path(tempfile.gettempdir()) / "failed_ical_tests"
        temp_dir.mkdir(parents=True, exist_ok=True)

        with self.assertRaises(ICalExportTargetPathError):
            self.cal._get_ical_target_path(temp_dir)

    def test_no_extension(self):
        # Relative paths
        self.assertEqual(self.cal._get_ical_target_path("a"), Path("a.ics"))
        self.assertEqual(
            self.cal._get_ical_target_path("a/b"),
            Path("a/b.ics")
        )
        # Absolute path
        self.assertEqual(
            self.cal._get_ical_target_path("/path/to/a"),
            Path("/path/to/a.ics")
        )

    def test_known_extensions(self):
        for ext in ('ical', 'ics', 'ifb', 'icalendar'):
            filename = Path(f"a.{ext}")
            self.assertEqual(
                self.cal._get_ical_target_path(filename),
                filename
            )

    def test_added_extensions(self):
        self.assertEqual(self.cal._get_ical_target_path('a.'), Path('a..ics'))
        self.assertEqual(
            self.cal._get_ical_target_path('a.txt'),
            Path('a.txt.ics')
        )
        self.assertEqual(
            self.cal._get_ical_target_path('.test'),
            Path('.test.ics')
        )
