import os
import tempfile
import warnings
from datetime import date
from pathlib import Path
from unittest import TestCase
from platform import system

from freezegun import freeze_time

from ..core import Calendar
from .. import __version__


class CoreCalendarTest(TestCase):
    cal_class = Calendar
    kwargs = {}

    def setUp(self):
        super().setUp()
        self.year = date.today().year
        self.cal = self.cal_class(**self.kwargs)


class GenericCalendarTest(CoreCalendarTest):
    test_include_january_1st = True

    def setUp(self):
        super().setUp()
        warnings.simplefilter('ignore')

    def test_weekend_days(self):
        class_name = self.cal_class.__name__
        if class_name in ['Calendar']:
            return
        try:
            self.cal.get_weekend_days()
        except NotImplementedError:
            assert False, (self.cal, class_name)

    def test_january_1st(self):
        class_name = self.cal_class.__name__
        if class_name in ['Calendar']:
            return
        holidays = self.cal.holidays_set(self.year)
        if self.test_include_january_1st:
            self.assertIn(date(self.year, 1, 1), holidays)
        else:
            self.assertNotIn(date(self.year, 1, 1), holidays)

    def test_ical_export(self):
        """Check that an iCal file can be created according to iCal spec."""
        class_name = self.cal_class.__name__
        if class_name in ['Calendar']:
            return

        holidays = self.cal.holidays(2019) + self.cal.holidays(2020)

        temp_dir = Path(tempfile.gettempdir()) / "failed_ical_tests"
        temp_dir.mkdir(parents=True, exist_ok=True)
        test_file_fd, test_file_name = tempfile.mkstemp(
            prefix=f"{self.cal_class.__name__}_",
            suffix=".ics",
            dir=temp_dir,
        )
        test_path = Path(test_file_name)

        self.cal.export_to_ical(
            period=[2019, 2020],
            target_path=test_path,
        )
        # A standard iCal extension should have been added automatically:
        with test_path.open() as ics_file:
            # check header
            assert ics_file.readline() == 'BEGIN:VCALENDAR\n'
            assert ics_file.readline() == 'VERSION:2.0\n'
            prod_id_line = ics_file.readline()
            assert prod_id_line == (
                f'PRODID:-//workalendar//ical {__version__}//EN\n')
            # check new year
            assert ics_file.readline() == 'BEGIN:VEVENT\n'
            first_event_name = holidays[0][1]
            assert ics_file.readline() == f'SUMMARY:{first_event_name}\n'
            if self.test_include_january_1st:
                assert ics_file.readline() == 'DTSTART;VALUE=DATE:20190101\n'
                assert ics_file.readline().startswith(
                    'DTSTAMP;VALUE=DATE-TIME:')
                first_uid_line = ics_file.readline()
                uid_lines = [first_uid_line]
                assert first_uid_line.startswith('UID:2019')
                assert ics_file.readline() == 'END:VEVENT\n'
            else:
                uid_lines = []
            remaining_lines = ics_file.readlines()
            uid_lines += [line for line in remaining_lines
                          if line.startswith('UID:')]
            # check number of entries
            assert len(uid_lines) == len(holidays)
            # check that UIDs are unique within the calendar
            assert len(uid_lines) == len(set(uid_lines))
            # check that final year is included
            assert remaining_lines[-3].startswith('UID:2020')
            # check last few lines of file
            assert remaining_lines[-2] == 'END:VEVENT\n'
            assert remaining_lines[-1] == 'END:VCALENDAR\n'

        # Freeze time to make sure they both have the same timestamp
        with freeze_time():
            # Regenerate the file
            self.cal.export_to_ical(
                period=[2019, 2020],
                target_path=test_path,
            )
            # Not providing any target => returns the value as a string
            var_contents = self.cal.export_to_ical(period=[2019, 2020])

        file_contents = test_path.read_text()

        assert file_contents == var_contents

        # If platform is Windows close the temp file descriptor
        if system() == 'Windows':  # pragma: no cover
            os.close(test_file_fd)
        # Remove the .ics file if this test passes
        test_path.unlink()
