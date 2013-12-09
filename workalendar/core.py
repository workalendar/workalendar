"""Working day tools
"""
import warnings
from calendar import monthrange
from datetime import date, timedelta

from dateutil import easter
from lunardate import LunarDate
from calverter import Calverter

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


class Calendar(object):

    FIXED_HOLIDAYS = ()

    def __init__(self):
        self._holidays = {}

    def get_fixed_holidays(self, year):
        """Return the fixed days according to the FIXED_HOLIDAYS class property
        """
        days = []
        for month, day, label in self.FIXED_HOLIDAYS:
            days.append((date(year, month, day), label))
        return days

    def get_variable_days(self, year):
        return []

    def get_calendar_holidays(self, year):
        """Get calendar holidays.
        If you want to override this, please make sure that it **must** return
        a list of tuples (date, holiday_name)."""
        return self.get_fixed_holidays(year) + self.get_variable_days(year)

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

    def holidays_set(self, year=None):
        "Return a quick date index (set)"
        return set([day for day, label in self.holidays(year)])

    def get_weekend_days(self):
        """Return a list (or a tuple) of weekdays that are *not* working days.

        e.g: return (SAT, SUN,)

        """
        raise NotImplementedError("Your Calendar class must implement the"
                                  " `get_weekend_days` method")

    def is_working_day(self, day,
                       extra_working_days=None, extra_holidays=None):
        """Return True if it's a working day.
        In addition to the regular holidays, you can add exceptions.

        By providing ``extra_working_days``, you'll state that these dates
        **are** working days.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        Please note that the ``extra_working_days`` list has priority over the
        ``extra_holidays`` list.

        """
        # Extra lists exceptions
        if extra_working_days and day in extra_working_days:
            return True

        if extra_holidays and day in extra_holidays:
            return False

        # Regular rules
        if day.weekday() in self.get_weekend_days():
            return False
        if day in self.holidays_set(day.year):
            return False
        return True

    def add_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None):
        """Add `delta` working days to the date.

        By providing ``extra_working_days``, you'll state that these dates
        **are** working days.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        Please note that the ``extra_working_days`` list has priority over the
        ``extra_holidays`` list.
        """
        days = 0
        temp_day = day
        while days < delta:
            temp_day = temp_day + timedelta(days=1)
            if self.is_working_day(temp_day,
                                   extra_working_days=extra_working_days,
                                   extra_holidays=extra_holidays):
                days += 1
        return temp_day

    def find_following_working_day(self, day):
        "Looks for the following working day"
        while day.weekday() in self.get_weekend_days():
            day = day + timedelta(days=1)
        return day

    @staticmethod
    def get_nth_weekday_in_month(year, month, weekday, n=1, start=None):
        """Get the nth weekday in a given month. e.g:

        >>> # the 1st monday in Jan 2013
        >>> Calendar.get_nth_weekday_in_month(2013, 1, MON)
        datetime.date(2013, 1, 7)
        >>> # The 2nd monday in Jan 2013
        >>> Calendar.get_nth_weekday_in_month(2013, 1, MON, 2)
        datetime.date(2013, 1, 14)
        """
        day = date(year, month, 1)
        if start:
            day = start
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


class ChristianMixin(Calendar):
    EASTER_METHOD = None  # to be assigned in the inherited mixin
    include_epiphany = False
    include_holy_thursday = False
    include_good_friday = False
    include_easter_monday = False
    include_easter_saturday = False
    include_easter_sunday = False
    include_all_saints = False
    include_immaculate_conception = False
    include_christmas = True
    include_christmas_eve = False
    include_st_stephen = False
    include_ascension = False
    include_assumption = False
    include_whit_monday = False
    include_boxing_day = False

    def get_holy_thursday(self, year):
        "Return the date of the last thursday before easter"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=3)

    def get_good_friday(self, year):
        "Return the date of the last friday before easter"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=2)

    def get_easter_saturday(self, year):
        "Return the Easter Saturday date"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=1)

    def get_easter_sunday(self, year):
        "Return the date of the easter (sunday) -- following the easter method"
        return easter.easter(year, self.EASTER_METHOD)

    def get_easter_monday(self, year):
        "Return the date of the monday after easter"
        sunday = self.get_easter_sunday(year)
        return sunday + timedelta(days=1)

    def get_ascension_thursday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=39)

    def get_whit_monday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=50)

    def get_variable_days(self, year):
        "Return the christian holidays list according to the mixin"
        days = super(ChristianMixin, self).get_variable_days(year)
        if self.include_epiphany:
            days.append((date(year, 1, 6), "Epiphany"))
        if self.include_holy_thursday:
            days.append((self.get_holy_thursday(year), "Holy Thursday"))
        if self.include_good_friday:
            days.append((self.get_good_friday(year), "Good Friday"))
        if self.include_easter_saturday:
            days.append((self.get_easter_saturday(year), "Easter Saturday"))
        if self.include_easter_sunday:
            days.append((self.get_easter_sunday(year), "Easter Sunday"))
        if self.include_easter_monday:
            days.append((self.get_easter_monday(year), "Easter Monday"))
        if self.include_assumption:
            days.append((date(year, 8, 15), "Assumption of Mary to Heaven"))
        if self.include_all_saints:
            days.append((date(year, 11, 1), "All Saints Day"))
        if self.include_immaculate_conception:
            days.append((date(year, 12, 8), "Immaculate Conception"))
        if self.include_christmas:
            days.append((date(year, 12, 25), "Christmas Day"))
        if self.include_christmas_eve:
            days.append((date(year, 12, 24), "Christmas Eve"))
        if self.include_st_stephen:
            days.append((date(year, 12, 26), "St Stephen's Day"))
        if self.include_boxing_day:
            days.append((date(year, 12, 26), "Boxing Day"))
        if self.include_ascension:
            days.append((
                self.get_ascension_thursday(year), "Ascension Thursday"))
        if self.include_whit_monday:
            days.append((self.get_whit_monday(year), "Whit Monday"))
        return days


class WesternCalendar(Calendar):
    """
    General usage calendar for Western countries.

    (chiefly Europe and Northern America)

    """
    EASTER_METHOD = 3  # 3 is 'Western'
    WEEKEND_DAYS = (SAT, SUN)
    shift_new_years_day = False

    FIXED_HOLIDAYS = (
        (1, 1, 'New year'),
    )

    def get_weekend_days(self):
        "Week-end days are SATurday and SUNday."
        return self.WEEKEND_DAYS

    def get_variable_days(self, year):
        days = super(WesternCalendar, self).get_variable_days(year)
        new_year = date(year, 1, 1)
        if self.shift_new_years_day:
            if new_year.weekday() in self.get_weekend_days():
                days.append((
                    self.find_following_working_day(new_year),
                    "New Year shift"))
        return days


class LunarCalendar(Calendar):
    """Calendar including lunar days
    """
    FIXED_HOLIDAYS = (
        (1, 1, 'Lunar new year'),
    )

    @staticmethod
    def lunar(year, month, day):
        return LunarDate(year, month, day).toSolarDate()


class CalverterMixin(Calendar):
    conversion_method = None
    ISLAMIC_HOLIDAYS = ()

    def __init__(self, *args, **kwargs):
        super(CalverterMixin, self).__init__(*args, **kwargs)
        self.calverter = Calverter()
        if self.conversion_method is None:
            raise NotImplementedError

    def converted(self, year):
        conversion_method = getattr(
            self.calverter, 'jd_to_%s' % self.conversion_method)
        current = date(year, 1, 1)
        days = []
        while current.year == year:
            julian_day = self.calverter.gregorian_to_jd(
                current.year,
                current.month,
                current.day)
            days.append(conversion_method(julian_day))
            current = current + timedelta(days=1)
        return days

    def calverted_years(self, year):
        converted = self.converted(year)
        generator = (y for y, m, d in converted)
        return sorted(list(set(generator)))

    def get_islamic_holidays(self):
        return self.ISLAMIC_HOLIDAYS

    def get_variable_days(self, year):
        warnings.warn('Please take not that, due to arbitrary decisions, '
                      'this Islamic calendar computation may be wrong.')
        days = super(CalverterMixin, self).get_variable_days(year)
        years = self.calverted_years(year)
        conversion_method = getattr(
            self.calverter, '%s_to_jd' % self.conversion_method)
        for month, day, label in self.get_islamic_holidays():
                for y in years:
                    jd = conversion_method(y, month, day)
                    g_year, g_month, g_day = self.calverter.jd_to_gregorian(jd)
                    if g_year == year:
                        holiday = date(g_year, g_month, g_day)
                        days.append((holiday, label))
        return days


class IslamicMixin(CalverterMixin):
    conversion_method = 'islamic'
    include_prophet_birthday = False
    include_eid_al_fitr = False
    include_day_of_sacrifice = False
    include_day_of_sacrifice_label = "Eid al-Adha"
    include_islamic_new_year = False

    def get_islamic_holidays(self):
        """Return a list of Islamic (month, day, label) for islamic holidays.
        Please take note that these dates must be expressed using the Islamic
        Calendar"""
        days = list(super(IslamicMixin, self).get_islamic_holidays())

        if self.include_islamic_new_year:
            days.append((1, 1, "Islamic New Year"))
        if self.include_prophet_birthday:
            days.append((3, 12, "Prophet's Birthday"))
        if self.include_eid_al_fitr:
            days.append((10, 1, "Eid al-Fitr"))
        if self.include_day_of_sacrifice:
            days.append((12, 10, self.include_day_of_sacrifice_label))
        return tuple(days)


class JalaliMixin(CalverterMixin):
    conversion_method = 'jalali'
