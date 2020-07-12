import os
import os.path
import warnings
from datetime import date
from unittest import TestCase, skipIf

from ..core import Calendar


class GenericCalendarTest(TestCase):
    cal_class = Calendar

    def setUp(self):
        super().setUp()
        warnings.simplefilter('ignore')
        self.year = date.today().year
        self.cal = self.cal_class()

    # test for ical export that runs on every calendar
    @skipIf(cal_class == Calendar, reason='Calendar has no holidays.')
    def test_ical_export(self):
        """Check that an iCal file can be created according to iCal spec."""
        holidays = self.cal.holidays(2020) + self.cal.holidays(2021)
        test_file_name = '%s_failed_test' % self.cal_class.name
        test_file_name = os.path.join(
            os.path.dirname(__file__), 'failed_ical_exports', test_file_name)
        self.cal.export_to_ical(target_path=test_file_name,
                                period=[2020, 2021])
        with open(test_file_name) as ics_file:
            # check header
            assert ics_file.readline() == 'BEGIN:VCALENDAR\n'
            assert ics_file.readline() == 'VERSION:2.0\n'
            assert ics_file.readline().startswith(
                'PRODID:-//workalendar//ical ')
            # check new year
            assert ics_file.readline() == 'BEGIN:VEVENT\n'
            if not self.cal.shift_new_years_day:
                assert ics_file.readline() == 'SUMMARY:New year\n'
                assert ics_file.readline() == 'DTSTART;VALUE=DATE:20200101\n'
                assert ics_file.readline().startswith(
                    'DTSTAMP;VALUE=DATE-TIME:')
                first_uid_line = ics_file.readline()
                uid_lines = [first_uid_line]
                assert first_uid_line.startswith('UID:')
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
            assert remaining_lines[-3].startswith('UID:2021')
            # check last few lines of file
            assert remaining_lines[-2] == 'END:VEVENT\n'
            assert remaining_lines[-1] == 'END:VCALENDAR\n'
        # A standard iCal extension should have been added automatically:
        test_file_name += '.ics'
        # Remove the .ics file if this test passes
        os.remove(test_file_name)