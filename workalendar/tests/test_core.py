from unittest.mock import patch
from datetime import date
from datetime import datetime
from unittest import TestCase

import pandas

from . import CoreCalendarTest, GenericCalendarTest
from ..core import (
    MON, TUE, THU, FRI, WED, SAT, SUN,
    ISO_TUE, ISO_FRI,
    Calendar, LunarMixin, WesternCalendar,
    CalverterMixin, IslamicMixin, JalaliMixin,
    daterange,
)
from ..exceptions import UnsupportedDateType, CalendarError


class CalendarTest(CoreCalendarTest):

    def test_private_variables(self):
        self.assertTrue(hasattr(self.cal, '_holidays'))
        private_holidays = self.cal._holidays
        self.assertTrue(isinstance(private_holidays, dict))
        self.cal.holidays(2011)
        self.cal.holidays(2012)
        private_holidays = self.cal._holidays
        self.assertTrue(isinstance(private_holidays, dict))
        self.assertIn(2011, self.cal._holidays)
        self.assertIn(2012, self.cal._holidays)

    def test_year(self):
        holidays = self.cal.holidays()
        self.assertTrue(isinstance(holidays, (tuple, list)))
        self.assertEqual(self.cal._holidays[self.year], holidays)

    def test_another_year(self):
        holidays = self.cal.holidays(2011)
        self.assertTrue(isinstance(holidays, (tuple, list)))
        self.assertEqual(self.cal._holidays[2011], holidays)

    def test_is_working_day(self):
        self.assertRaises(
            NotImplementedError,
            self.cal.is_working_day, date(2012, 1, 1))

    def test_nth_weekday(self):
        # first monday in january 2013
        self.assertEqual(
            Calendar.get_nth_weekday_in_month(2013, 1, MON),
            date(2013, 1, 7)
        )
        # second monday in january 2013
        self.assertEqual(
            Calendar.get_nth_weekday_in_month(2013, 1, MON, 2),
            date(2013, 1, 14)
        )
        # let's test the limits
        # Jan 1st is a TUE
        self.assertEqual(
            Calendar.get_nth_weekday_in_month(2013, 1, TUE),
            date(2013, 1, 1)
        )
        # There's no 6th MONday
        self.assertEqual(
            Calendar.get_nth_weekday_in_month(2013, 1, MON, 6),
            None
        )

    def test_nth_weekday_start(self):
        # first thursday after 18th april
        start = date(2013, 4, 18)
        self.assertEqual(
            Calendar.get_nth_weekday_in_month(2013, 4, THU, start=start),
            date(2013, 4, 18)
        )
        # first friday after 18th april
        start = date(2013, 4, 18)
        self.assertEqual(
            Calendar.get_nth_weekday_in_month(2013, 4, FRI, start=start),
            date(2013, 4, 19)
        )

    def test_last_weekday(self):
        # last monday in january 2013
        self.assertEqual(
            Calendar.get_last_weekday_in_month(2013, 1, MON),
            date(2013, 1, 28)
        )
        # last thursday
        self.assertEqual(
            Calendar.get_last_weekday_in_month(2013, 1, THU),
            date(2013, 1, 31)
        )

    def test_get_next_weekday_after(self):
        # the first monday after Apr 1 2015
        self.assertEqual(
            Calendar.get_first_weekday_after(date(2015, 4, 1), MON),
            date(2015, 4, 6)
        )

        # the first tuesday after Apr 14 2015
        self.assertEqual(
            Calendar.get_first_weekday_after(date(2015, 4, 14), TUE),
            date(2015, 4, 14)
        )

    def test_get_iso_week_date(self):
        # Find the MON of the week 1 in 2021
        self.assertEqual(
            Calendar.get_iso_week_date(2021, 1),
            date(2021, 1, 4)
        )
        # Find the FRI of the week 1 in 2021
        self.assertEqual(
            Calendar.get_iso_week_date(2021, 1, ISO_FRI),
            date(2021, 1, 8)
        )

        # Find the TUE of the week 44 in 2021
        self.assertEqual(
            Calendar.get_iso_week_date(2021, 44, ISO_TUE),
            date(2021, 11, 2)
        )

    # Remove this test when dropping support for Python 3.7
    @patch('workalendar.core.sys')
    def test_get_iso_week_date_patched(self, mock_sys):
        # The Python 3.6-3.7 backport should always work
        mock_sys.version_info = (3, 6, 0)
        self.assertEqual(
            Calendar.get_iso_week_date(2021, 44, ISO_TUE),
            date(2021, 11, 2)
        )


class LunarCalendarTest(TestCase):

    def test_lunar_new_year(self):
        self.assertEqual(
            LunarMixin.lunar(2014, 1, 1),
            date(2014, 1, 31)
        )


class MockCalendar(Calendar):

    def holidays(self, year=None):
        return tuple((
            (date(year, 12, 25), 'Christmas'),
            (date(year, 1, 1), 'New year'),
        ))

    def get_weekend_days(self):
        return []  # no week-end, yes, it's sad


class MockCalendarTest(CoreCalendarTest):
    cal_class = MockCalendar

    def test_holidays_set(self):
        self.assertIn(
            date(self.year, 12, 25), self.cal.holidays_set(self.year))

        self.assertIn(
            date(self.year, 1, 1), self.cal.holidays_set(self.year))

    def test_sorted_dates(self):
        holidays = list(self.cal.holidays(self.year))
        day, label = holidays.pop()
        for next_day, label in holidays:
            self.assertTrue(day <= next_day)
            day = next_day

    def test_add_workingdays_simple(self):
        # day is out of non-working-day
        self.assertEqual(
            self.cal.add_working_days(date(self.year, 12, 20), 0),
            date(self.year, 12, 20)
        )
        self.assertEqual(
            self.cal.add_working_days(date(self.year, 12, 20), 1),
            date(self.year, 12, 21)
        )

    def test_add_workingdays_on_holiday(self):
        # day is in holidays
        self.assertEqual(
            self.cal.add_working_days(date(self.year, 12, 25), 0),
            date(self.year, 12, 25)
        )
        self.assertEqual(
            self.cal.add_working_days(date(self.year, 12, 24), 1),
            date(self.year, 12, 26)
        )
        self.assertEqual(
            self.cal.add_working_days(date(self.year, 12, 24), 2),
            date(self.year, 12, 27)
        )

    def test_add_workingdays_span(self):
        day = date(self.year, 12, 20)
        # since this calendar has no weekends, we'll just have a 2-day-shift
        self.assertEqual(
            self.cal.add_working_days(day, 20),
            date(self.year + 1, 1, 11)
        )

    def test_add_working_days_exceptions(self):
        day = date(self.year, 12, 20)
        christmas = date(self.year, 12, 25)
        boxing = date(self.year, 12, 26)
        # exceptional workday
        self.assertEqual(
            self.cal.add_working_days(day, 20, extra_working_days=[christmas]),
            date(self.year + 1, 1, 10)
        )
        # exceptional holiday + exceptional workday
        self.assertEqual(
            self.cal.add_working_days(day, 20,
                                      extra_working_days=[christmas],
                                      extra_holidays=[boxing]),
            date(self.year + 1, 1, 11)
        )

    def test_add_exceptions(self):
        december_20th = date(self.year, 12, 20)
        christmas = date(self.year, 12, 25)
        # target_working_day *is* a working day
        target_working_day = self.cal.add_working_days(december_20th, 1)
        # Add extra working days
        extra_working_days = [christmas]
        # add extra holidays
        extra_holidays = [target_working_day]
        self.assertFalse(self.cal.is_working_day(christmas))
        self.assertTrue(
            self.cal.is_working_day(christmas,
                                    extra_working_days=extra_working_days))

        self.assertTrue(self.cal.is_working_day(target_working_day))
        self.assertFalse(
            self.cal.is_working_day(target_working_day,
                                    extra_holidays=extra_holidays))
        # test is_holiday
        self.assertTrue(self.cal.is_holiday(christmas))

    def test_get_holiday_label(self):
        self.assertEqual(
            self.cal.get_holiday_label(date(2014, 1, 1)), 'New year')
        self.assertIsNone(
            self.cal.get_holiday_label(date(2014, 1, 2)))

    def test_add_working_days_backwards(self):
        day = date(self.year, 1, 3)
        # since this calendar has no weekends, we'll just have a 1-day-shift
        self.assertEqual(
            self.cal.add_working_days(day, -7),
            date(self.year - 1, 12, 26)
        )
        self.assertEqual(
            self.cal.sub_working_days(day, 7),
            date(self.year - 1, 12, 26)
        )
        # Negative argument to sub_working_days -> converted to positive.
        self.assertEqual(
            self.cal.sub_working_days(day, -7),
            date(self.year - 1, 12, 26)
        )


class IslamicMixinTest(CoreCalendarTest):
    cal_class = IslamicMixin

    def test_year_conversion(self):
        days = self.cal.converted(2013)
        self.assertEqual(len(days), 365)


class JalaliMixinTest(CoreCalendarTest):
    cal_class = JalaliMixin

    def test_year_conversion(self):
        days = self.cal.converted(2013)
        self.assertEqual(len(days), 365)


class CalverterClassNoConversionMethod(CalverterMixin):
    pass


class NoConversionMethodTest(TestCase):
    def test_no_conversion_method(self):
        with self.assertRaises(NotImplementedError):
            CalverterClassNoConversionMethod()


class IncludeLaylatAlQadr(IslamicMixin):
    include_laylat_al_qadr = True


class DoesNotIncludeLaylatAlQadr(IslamicMixin):
    include_laylat_al_qadr = False


class LaylatAlQadrTest(TestCase):

    def test_warning_laylat_al_qadr(self):
        cal = IncludeLaylatAlQadr()
        with patch('warnings.warn') as patched:
            cal.get_islamic_holidays()
        patched.assert_called_with(
            'The Islamic holiday named Laylat al-Qadr is decided by the '
            'religious authorities. It is not possible to compute it. '
            "You'll have to add it manually."
        )

    def test_no_warning_laylat_al_qadr(self):
        cal = DoesNotIncludeLaylatAlQadr()
        with patch('warnings.warn') as patched:
            cal.get_islamic_holidays()
        patched.assert_not_called()


class MockChristianCalendar(WesternCalendar):
    # WesternCalendar inherits from ChristianMixin
    pass


class MockChristianCalendarTest(CoreCalendarTest):
    cal_class = MockChristianCalendar

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(date(2014, 1, 6), holidays)  # Epiphany
        self.assertNotIn(date(2014, 3, 3), holidays)  # Clean Monday
        self.assertNotIn(date(2014, 3, 5), holidays)  # Ash Wednesday
        self.assertNotIn(date(2014, 3, 25), holidays)  # Annunciation
        self.assertNotIn(date(2014, 4, 17), holidays)  # Holy Thursday
        self.assertNotIn(date(2014, 4, 18), holidays)  # 'Good Friday
        self.assertNotIn(date(2014, 4, 19), holidays)  # Easter sat
        self.assertNotIn(date(2014, 4, 20), holidays)  # Easter Sun
        self.assertNotIn(date(2014, 4, 21), holidays)  # Easter Mon
        self.assertNotIn(date(2014, 5, 29), holidays)  # Ascension
        self.assertNotIn(date(2014, 6, 8), holidays)   # Whit Sunday
        self.assertNotIn(date(2014, 6, 9), holidays)   # Whit Monday
        self.assertNotIn(date(2014, 6, 19), holidays)  # Corp. Christi
        self.assertNotIn(date(2014, 8, 15), holidays)  # Assumption
        self.assertNotIn(date(2014, 11, 1), holidays)  # All Saints
        self.assertNotIn(date(2014, 12, 8), holidays)  # Imm. Conc.
        self.assertNotIn(date(2014, 12, 24), holidays)  # Xmas Eve
        self.assertNotIn(date(2014, 12, 26), holidays)  # Boxing Day

        # The only Christian day that is a holiday for every calendar
        self.assertIn(date(2014, 12, 25), holidays)  # XMas

        # Only 2 days: Jan 1st and Christmas
        self.assertEqual(len(holidays), 2)


class NoWeekendCalendar(Calendar):
    """
    This calendar class has no WEEKEND_DAYS and no `get_weekend_days()` method.
    It has to fail when trying to fetch its weekend days / holidays
    """


class NoWeekendCalendarTest(CoreCalendarTest):
    cal_class = NoWeekendCalendar

    def test_weekend(self):
        day = date(2017, 5, 13)  # This is a Saturday
        with self.assertRaises(NotImplementedError):
            self.cal.is_working_day(day)
        day = date(2017, 5, 17)  # This is a Wednesday
        with self.assertRaises(NotImplementedError):
            self.cal.is_working_day(day)


class GenericCalendarTestTest(GenericCalendarTest):
    cal_class = NoWeekendCalendar

    def test_weekend_days(self):
        with self.assertRaises(AssertionError):
            super().test_weekend_days()


class WeekendOnWednesdayCalendar(Calendar):
    """
    This calendar class weekend days is on Wednesday and we don't overwrite
    the `get_weekend_days()` method. It should be fine.
    """
    WEEKEND_DAYS = (WED,)


class WeekendOnWednesdayCalendarTest(CoreCalendarTest):
    cal_class = WeekendOnWednesdayCalendar

    def test_weekend(self):
        day = date(2017, 5, 13)  # This is a Saturday
        self.assertTrue(self.cal.is_working_day(day))
        day = date(2017, 5, 17)  # This is a Wednesday
        self.assertFalse(self.cal.is_working_day(day))


class OverwriteGetWeekendDaysCalendar(Calendar):
    """
    This calendar class has no WEEKEND_DAYS and we overwrite
    its `get_weekend_days` method.
    Should work.
    """
    def get_weekend_days(self):
        return WED,


class OverwriteGetWeekendDaysCalendarTest(CoreCalendarTest):
    cal_class = OverwriteGetWeekendDaysCalendar

    def test_weekend(self):
        day = date(2017, 5, 13)  # This is a Saturday
        self.assertTrue(self.cal.is_working_day(day))
        day = date(2017, 5, 17)  # This is a Wednesday
        self.assertFalse(self.cal.is_working_day(day))


class NoHolidayCalendar(Calendar):
    include_new_years_day = False
    WEEKEND_DAYS = (SAT, SUN)


class WorkingDaysDeltatest(TestCase):

    def test_zero(self):
        days = (
            date(2018, 12, 21),  # a Thursday
            date(2018, 12, 23),  # a Sunday
            date(2018, 12, 25),  # a holiday in Christian calendars
        )
        for day in days:
            cal = NoHolidayCalendar()
            self.assertEqual(cal.get_working_days_delta(day, day), 0)
            cal = MockChristianCalendar()
            self.assertEqual(cal.get_working_days_delta(day, day), 0)

    def test_no_holidays_simple(self):
        cal = NoHolidayCalendar()
        day1 = date(2018, 12, 21)
        day2 = date(2018, 12, 26)
        delta = cal.get_working_days_delta(day1, day2)
        # there are 3 days, because of the week-ends
        self.assertEqual(delta, 3)

        # No difference if you swap the two dates
        delta = cal.get_working_days_delta(day2, day1)
        self.assertEqual(delta, 3)

    def test_no_holidays_over_2_years(self):
        cal = NoHolidayCalendar()
        day1 = date(2018, 12, 21)
        day2 = date(2019, 1, 4)
        delta = cal.get_working_days_delta(day1, day2)
        # there are 10 days, because of the week-ends
        self.assertEqual(delta, 10)

        # No difference if you swap the two dates
        delta = cal.get_working_days_delta(day2, day1)
        self.assertEqual(delta, 10)

    def test_christian_simple(self):
        cal = MockChristianCalendar()
        day1 = date(2018, 12, 21)
        day2 = date(2018, 12, 26)
        delta = cal.get_working_days_delta(day1, day2)
        # there are 2 days, because of the week-end + Christmas Day
        self.assertEqual(delta, 2)

        # No difference if you swap the two dates
        delta = cal.get_working_days_delta(day2, day1)
        self.assertEqual(delta, 2)

    def test_christian_over_2_years(self):
        cal = MockChristianCalendar()
        day1 = date(2018, 12, 21)
        day2 = date(2019, 1, 4)
        delta = cal.get_working_days_delta(day1, day2)
        # there are 8 days, because of the week-ends + Xmas day + New Year
        self.assertEqual(delta, 8)

        # No difference if you swap the two dates
        delta = cal.get_working_days_delta(day2, day1)
        self.assertEqual(delta, 8)

    def test_with_datetimes(self):
        cal = MockChristianCalendar()
        day1 = datetime(2018, 12, 21)
        day2 = date(2018, 12, 26)
        delta = cal.get_working_days_delta(day1, day2)
        # there are 2 days, because of the week-end + Christmas Day
        self.assertEqual(delta, 2)

        # No difference if you swap the two dates
        delta = cal.get_working_days_delta(day2, day1)
        self.assertEqual(delta, 2)

    def test_with_including_first_day(self):
        # linked to #393
        cal = MockChristianCalendar()
        day1 = date(2018, 12, 24)  # December 24th: not holiday so working day
        day2 = date(2018, 12, 25)  # December 25th: Christmas

        # not including the first day, should return 0
        delta = cal.get_working_days_delta(day1, day2)
        self.assertEqual(delta, 0)

        # including the first day, should return 1
        delta = cal.get_working_days_delta(day1, day2, include_start=True)
        self.assertEqual(delta, 1)


class NoDocstring(Calendar):
    pass


class EmptyDocstring(Calendar):
    ""


class OneLineDocstring(Calendar):
    "One line"


class MultipleLineDocstring(Calendar):
    """Multiple line

    docstrings can span over multiple lines.
    """


class MultipleLineEmptyFirstDocstring(Calendar):
    """

    Multiple line empty first

    docstrings can span over multiple lines.
    """


class CalendarClassNameTest(TestCase):
    def test_no_docstring(self):
        self.assertEqual(NoDocstring.name, "NoDocstring")

    def test_empty_docstring(self):
        self.assertEqual(EmptyDocstring.name, "EmptyDocstring")

    def test_oneline_docstring(self):
        self.assertEqual(OneLineDocstring.name, "One line")

    def test_multiple_line_docstring(self):
        self.assertEqual(MultipleLineDocstring.name, "Multiple line")

    def test_multiple_line_empty_first_docstring(self):
        self.assertEqual(
            MultipleLineEmptyFirstDocstring.name, "Multiple line empty first"
        )


class TestAcceptableDateTypes(CoreCalendarTest):
    """
    Test cases about accepted date and datetime types.
    """
    cal_class = MockCalendar
    unsupported = ('hello', 1)

    def test_unsupported_type_is_working_day(self):
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.is_working_day(arg)

        # Extra holidays optional argument
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.is_working_day(
                    date(2018, 1, 1),
                    extra_holidays=[arg]
                )
        # Extra working days optional argument
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.is_working_day(
                    date(2018, 1, 1),
                    extra_working_days=[arg]
                )

    def test_unsupported_type_is_holiday(self):
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.is_holiday(arg)

        # Extra holidays optional argument
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.is_holiday(
                    date(2018, 1, 1),
                    extra_holidays=[arg]
                )

    def test_unsupported_type_holiday_label(self):
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.get_holiday_label(arg)

    def test_unsupported_type_add_sub_working_days(self):
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.add_working_days(arg, 1)

        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.sub_working_days(arg, 1)

        # Extra holidays optional argument
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.add_working_days(
                    date(2018, 1, 1), 1,
                    extra_holidays=[arg]
                )
        # Extra working days optional argument
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.add_working_days(
                    date(2018, 1, 1), 1,
                    extra_working_days=[arg]
                )
        # NOTE: no need to test "sub", they're calling each other.

    def test_unsupported_type_find_following_working_day(self):
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.find_following_working_day(arg)

    def test_unsupported_type_get_nth_weekday_in_month(self):
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.get_nth_weekday_in_month(2018, 1, MON, start=arg)

    def test_unsupported_type_get_working_days_delta(self):
        for arg in self.unsupported:
            with self.assertRaises(UnsupportedDateType):
                self.cal.get_working_days_delta(date(2018, 1, 1), arg)

            with self.assertRaises(UnsupportedDateType):
                self.cal.get_working_days_delta(arg, date(2018, 1, 1))

    def test_datetime(self):
        self.assertFalse(
            self.cal.is_working_day(datetime(2014, 1, 1)))
        self.assertTrue(
            self.cal.is_holiday(datetime(2014, 1, 1)))

    def test_add_working_days_datetime(self):
        # datetime inside, date outside
        self.assertEqual(
            self.cal.add_working_days(
                datetime(self.year, 12, 20, 12, 34, 56), 0),
            date(self.year, 12, 20)
        )
        self.assertEqual(
            self.cal.add_working_days(
                datetime(self.year, 12, 20, 12, 34, 56), 1),
            date(self.year, 12, 21)
        )

        # Use the `keep_datetime` option
        self.assertEqual(
            self.cal.add_working_days(
                datetime(self.year, 12, 20, 12, 34, 56),
                0, keep_datetime=True),
            datetime(self.year, 12, 20, 12, 34, 56)
        )
        self.assertEqual(
            self.cal.add_working_days(
                datetime(self.year, 12, 20, 12, 34, 56),
                1, keep_datetime=True),
            datetime(self.year, 12, 21, 12, 34, 56)
        )

    def test_sub_working_days_datetime(self):
        # datetime inside, date outside
        self.assertEqual(
            self.cal.sub_working_days(
                datetime(self.year, 12, 20, 12, 34, 56), 0),
            date(self.year, 12, 20)
        )
        self.assertEqual(
            self.cal.sub_working_days(
                datetime(self.year, 12, 20, 12, 34, 56), 1),
            date(self.year, 12, 19)
        )

        # Use the `keep_datetime` option
        self.assertEqual(
            self.cal.sub_working_days(
                datetime(self.year, 12, 20, 12, 34, 56),
                0, keep_datetime=True),
            datetime(self.year, 12, 20, 12, 34, 56)
        )
        self.assertEqual(
            self.cal.sub_working_days(
                datetime(self.year, 12, 20, 12, 34, 56),
                1, keep_datetime=True),
            datetime(self.year, 12, 19, 12, 34, 56)
        )

    def test_get_holiday_label_with_datetime(self):
        self.assertEqual(
            self.cal.get_holiday_label(datetime(2014, 1, 1)), 'New year')
        self.assertIsNone(
            self.cal.get_holiday_label(datetime(2014, 1, 2)))


class PandasTimestampTest(CoreCalendarTest):
    cal_class = MockCalendar

    def test_panda_type_is_working_day(self):
        self.assertFalse(
            self.cal.is_working_day(pandas.to_datetime("2018-1-1"))
        )

        # Extra holidays optional argument
        self.assertFalse(
            self.cal.is_working_day(
                date(2018, 1, 2),
                extra_holidays=[pandas.to_datetime("2018-1-2")]
            )
        )
        # Extra working days optional argument
        self.assertTrue(
            self.cal.is_working_day(
                date(2018, 1, 1),
                extra_working_days=[pandas.to_datetime("2018-1-1")]
            )
        )

    def test_panda_type_is_holiday(self):
        self.assertTrue(self.cal.is_holiday(pandas.to_datetime("2018-1-1")))

        # Extra holidays optional argument
        self.assertTrue(
            self.cal.is_holiday(
                date(2018, 2, 1),
                extra_holidays=[pandas.to_datetime("2018-2-1")]
            )
        )

    def test_panda_type_holiday_label(self):
        label = self.cal.get_holiday_label(pandas.to_datetime("2018-1-1"))
        self.assertEqual(label, "New year")

    def test_panda_type_add_sub_working_days(self):
        day = pandas.to_datetime("2018-12-24")
        next_day = self.cal.add_working_days(day, 1)
        self.assertEqual(next_day, date(2018, 12, 26))

        previous_day = self.cal.sub_working_days(next_day, 1)
        self.assertEqual(previous_day, date(2018, 12, 24))

        next_day = self.cal.add_working_days(
            date(2018, 12, 24), 1,
            extra_holidays=[pandas.to_datetime("2018-12-26")]
        )
        self.assertEqual(next_day, date(2018, 12, 27))

        next_day = self.cal.add_working_days(
            date(2018, 12, 24), 1,
            extra_working_days=[pandas.to_datetime("2018-12-25")]
        )
        self.assertEqual(next_day, date(2018, 12, 25))

    def test_unsupported_type_find_following_working_day(self):
        following_day = self.cal.find_following_working_day(
            pandas.to_datetime("2018-1-1")
        )
        # No weekend days, the next day is "today"
        self.assertEqual(following_day, date(2018, 1, 1))

    def test_unsupported_type_get_nth_weekday_in_month(self):
        start = pandas.to_datetime("2018-1-4")
        monday = self.cal.get_nth_weekday_in_month(2018, 1, MON, start=start)
        self.assertEqual(monday, date(2018, 1, 8))

    def test_unsupported_type_get_working_days_delta(self):
        start, end = date(2018, 12, 23), pandas.to_datetime("2018-12-26")
        delta = self.cal.get_working_days_delta(start, end)
        self.assertEqual(delta, 2)
        delta = self.cal.get_working_days_delta(end, start)
        self.assertEqual(delta, 2)

        start, end = pandas.to_datetime("2018-12-23"), date(2018, 12, 26)
        delta = self.cal.get_working_days_delta(start, end)
        self.assertEqual(delta, 2)
        delta = self.cal.get_working_days_delta(end, start)
        self.assertEqual(delta, 2)


class MockCalendarNoFatTuesdayLabel(WesternCalendar):
    fat_tuesday_label = None


class FatTuesdayLabelTest(TestCase):

    def test_fat_tuesday_label(self):
        cal = MockCalendarNoFatTuesdayLabel()
        with self.assertRaises(CalendarError):
            cal.get_fat_tuesday(2020)


def test_daterange_start_end():
    start = date(2020, 4, 1)
    end = date(2020, 4, 10)
    date_list = list(daterange(start, end))
    assert date_list == [
        date(2020, 4, 1),
        date(2020, 4, 2),
        date(2020, 4, 3),
        date(2020, 4, 4),
        date(2020, 4, 5),
        date(2020, 4, 6),
        date(2020, 4, 7),
        date(2020, 4, 8),
        date(2020, 4, 9),
        date(2020, 4, 10),
    ]


def test_daterange_end_start():
    end = date(2020, 4, 1)
    start = date(2020, 4, 10)
    date_list = list(daterange(start, end))
    assert date_list == [
        date(2020, 4, 1),
        date(2020, 4, 2),
        date(2020, 4, 3),
        date(2020, 4, 4),
        date(2020, 4, 5),
        date(2020, 4, 6),
        date(2020, 4, 7),
        date(2020, 4, 8),
        date(2020, 4, 9),
        date(2020, 4, 10),
    ]


def test_daterange_same_date():
    # Stupid usecase, but nonetheless
    start = end = date(2020, 4, 1)
    date_list = list(daterange(start, end))
    assert date_list == [date(2020, 4, 1)]
