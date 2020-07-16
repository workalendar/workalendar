import os
import os.path
import warnings
from datetime import date
from unittest import TestCase, SkipTest

from ..core import Calendar


class CoreCalendarTest(TestCase):
    cal_class = Calendar

    def setUp(self):
        super().setUp()
        self.year = date.today().year
        self.cal = self.cal_class()


class GenericCalendarTest(CoreCalendarTest):
    test_include_january_1st = True

    def setUp(self):
        super().setUp()
        warnings.simplefilter('ignore')

    def test_weekend_days(self):
        class_name = self.cal_class.__name__
        if class_name in ('Calendar',):
            return
        try:
            self.cal.get_weekend_days()
        except NotImplementedError:
            assert False, (self.cal, class_name)

    def test_january_1st(self):
        class_name = self.cal_class.__name__
        if class_name in ('Calendar',):
            return
        holidays = self.cal.holidays_set(self.year)
        if self.test_include_january_1st:
            self.assertIn(date(self.year, 1, 1), holidays)
        else:
            self.assertNotIn(date(self.year, 1, 1), holidays)

    # test for ical export that runs on every calendar
    def test_ical_export(self):
        """Check that an iCal file can be created according to iCal spec."""
        if self.cal_class == Calendar:
            raise SkipTest('Calendar has no holidays.')
        holidays = self.cal.holidays(2019) + self.cal.holidays(2020)
        cal_name = self.cal_class.name.replace('/', '')
        test_file_name = '%s_failed_test' % cal_name
        test_file_name = os.path.join(
            os.path.dirname(__file__), 'failed_ical_exports', test_file_name)
        self.cal.export_to_ical(target_path=test_file_name,
                                period=[2019, 2020])
        # A standard iCal extension should have been added automatically:
        test_file_name += '.ics'
        with open(test_file_name) as ics_file:
            # check header
            assert ics_file.readline() == 'BEGIN:VCALENDAR\n'
            assert ics_file.readline() == 'VERSION:2.0\n'
            assert ics_file.readline().startswith(
                'PRODID:-//workalendar//ical ')
            # check new year
            assert ics_file.readline() == 'BEGIN:VEVENT\n'
            first_event_name = holidays[0][1]
            assert ics_file.readline() == 'SUMMARY:%s\n' % first_event_name
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
        # Remove the .ics file if this test passes
        os.remove(test_file_name)
