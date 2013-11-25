"""Workday tools
"""
from calendar import monthrange
from datetime import date, timedelta

from dateutil import easter
from lunardate import LunarDate

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


class Calendar(object):

    EASTER_METHOD = 3  # 3 is 'Western'
    FIXED_DAYS = ()

    def __init__(self):
        self._holidays = {}

    def get_fixed_days(self, year):
        """Return the fixed days according to the FIXED_DAYS class property
        """
        days = []
        for month, day, label in self.FIXED_DAYS:
            days.append((date(year, month, day), label))
        return days

    def get_variable_days(self, year):
        return []

    def get_calendar_holidays(self, year):
        """Get calendar holidays.
        If you want to override this, please make sure that it **must** return
        a list of tuples (date, holiday_name)."""
        return self.get_fixed_days(year) + self.get_variable_days(year)

    def holidays(self, year=None):
        """Computes holidays (non-working days) for a given year.
        Return a 2-item tuple, composed of the date and a label."""
        if not year:
            year = date.today().year

        if year in self._holidays:
            return self._holidays[year]

        # Here we process the holiday specific calendar
        temp_calendar = tuple(self.get_calendar_holidays(year))

        # it is sorted
        self._holidays[year] = sorted(temp_calendar)
        return self._holidays[year]

    def holidays_dates(self, year=None):
        "Return a quick date index (set)"
        return set([day for day, label in self.holidays(year)])

    def get_weekend_days(self):
        """Return a list (or a tuple) of weekdays that are *not* workdays.

        e.g: return (SAT, SUN,)

        """
        raise NotImplementedError("Your Calendar class must implement the"
                                  " `get_weekend_days` method")

    def is_workday(self, day, extra_workdays=None, extra_holidays=None):
        """Return True if it's a workday.
        In addition to the regular holidays, you can add exceptions.

        By providing ``extra_workdays``, you'll state that these dates **are**
        workdays.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        Please note that the ``extra_workdays`` list has priority over the
        ``extra_holidays`` list.

        """
        # Extra lists exceptions
        if extra_workdays and day in extra_workdays:
            return True

        if extra_holidays and day in extra_holidays:
            return False

        # Regular rules
        if day.weekday() in self.get_weekend_days():
            return False
        if day in self.holidays_dates(day.year):
            return False
        return True

    def add_workdays(self, day, delta):
        "Add `delta` workdays to the date."
        days = 0
        temp_day = day
        while days < delta:
            temp_day = temp_day + timedelta(1)
            if self.is_workday(temp_day):
                days += 1
        return temp_day

    def get_easter_sunday(self, year):
        "Return the date of the easter (sunday) -- following the easter method"
        return easter.easter(year, self.EASTER_METHOD)

    def get_easter_monday(self, year):
        "Return the date of the monday after easter"
        sunday = self.get_easter_sunday(year)
        return sunday + timedelta(days=1)

    @staticmethod
    def get_nth_weekday_in_month(year, month, weekday, n=1):
        """Get the nth weekday in a given month. e.g:

        >>> # the 1st monday in Jan 2013
        >>> Calendar.get_nth_weekday_in_month(2013, 1, MON)
        datetime.date(2013, 1, 7)
        >>> # The 2nd monday in Jan 2013
        >>> Calendar.get_nth_weekday_in_month(2013, 1, MON, 2)
        datetime.date(2013, 1, 14)
        """
        day = date(year, month, 1)
        counter = 0
        while True:
            if day.month != month:
                # Don't forget to break if "n" is too big
                return None
            if day.weekday() == weekday:
                counter += 1
            if counter == n:
                break
            day = day + timedelta(days=1)
        return day

    @staticmethod
    def get_last_weekday_in_month(year, month, weekday):
        """Get the last weekday in a given month. e.g:

        >>> # the last monday in Jan 2013
        >>> Calendar.get_last_weekday_in_month(2013, 1, MON)
        datetime.date(2013, 1, 28)
        """
        day = date(year, month, monthrange(year, month)[1])
        while True:
            if day.weekday() == weekday:
                break
            day = day - timedelta(days=1)
        return day


class WesternCalendar(Calendar):
    """
    General usage calendar for Western countries.

    (chiefly Europe and Northern America)

    """
    EASTER_METHOD = 3  # 3 is 'Western'
    WEEK_END_DAYS = (SAT, SUN)

    FIXED_DAYS = (
        (1, 1, 'New year'),
        (12, 25, "Christmas"),
    )

    def get_weekend_days(self):
        "Week-end days are SATurday and SUNday."
        return self.WEEK_END_DAYS


class LunarCalendar(Calendar):
    """Calendar that include lunar days
    """
    FIXED_DAYS = (
        (1, 1, 'Lunar new year'),
    )

    @staticmethod
    def lunar(year, month, day):
        return LunarDate(year, month, day).toSolarDate()
