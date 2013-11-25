from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.core import Calendar, MON, TUE, THU, LunarCalendar


class CalendarTest(GenericCalendarTest):

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
        self.assertTrue(isinstance(holidays, set))
        self.assertEquals(self.cal._holidays[self.year], holidays)

    def test_another_year(self):
        holidays = self.cal.holidays(2011)
        self.assertTrue(isinstance(holidays, set))
        self.assertEquals(self.cal._holidays[2011], holidays)

    def test_is_working_day(self):
        self.assertRaises(
            NotImplementedError,
            self.cal.is_working_day, date(2012, 1, 1))

    def test_nth_weekday(self):
        # first monday in january 2013
        self.assertEquals(
            Calendar.get_nth_weekday_in_month(2013, 1, MON),
            date(2013, 1, 7)
        )
        # second monday in january 2013
        self.assertEquals(
            Calendar.get_nth_weekday_in_month(2013, 1, MON, 2),
            date(2013, 1, 14)
        )
        # let's test the limits
        # Jan 1st is a TUE
        self.assertEquals(
            Calendar.get_nth_weekday_in_month(2013, 1, TUE),
            date(2013, 1, 1)
        )
        # There's no 6th MONday
        self.assertEquals(
            Calendar.get_nth_weekday_in_month(2013, 1, MON, 6),
            None
        )

    def test_last_weekday(self):
        # last monday in january 2013
        self.assertEquals(
            Calendar.get_last_weekday_in_month(2013, 1, MON),
            date(2013, 1, 28)
        )
        # last thursday
        self.assertEquals(
            Calendar.get_last_weekday_in_month(2013, 1, THU),
            date(2013, 1, 31)
        )


class LunarCalendarTest(GenericCalendarTest):
    cal_class = LunarCalendar

    def test_new_year(self):
        self.assertEquals(
            self.cal.lunar(2014, 1, 1),
            date(2014, 1, 31)
        )


class MockCalendar(Calendar):

    def holidays(self, year=None):
        return set([date(year, 12, 25), date(year, 1, 1)])

    def get_weekend_days(self):
        return []  # no week-end, yes, it's sad


class MockCalendarTest(GenericCalendarTest):
    cal_class = MockCalendar

    def test_add_working_days_span(self):
        day = date(self.year, 12, 20)
        # since this calendar has no weekends, we'll just have a 2-day-shift
        self.assertEquals(
            self.cal.add_working_days(day, 20),
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
