"""
Working day tools
"""
from copy import copy
import warnings
from calendar import monthrange
from datetime import date, timedelta, datetime
from pathlib import Path
import sys

import convertdate
from dateutil import easter
from lunardate import LunarDate

from .exceptions import (
    UnsupportedDateType, CalendarError,
    ICalExportRangeError, ICalExportTargetPathError
)
from . import __version__

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)
ISO_MON, ISO_TUE, ISO_WED, ISO_THU, ISO_FRI, ISO_SAT, ISO_SUN = range(1, 8)


class classproperty:

    def __init__(self, getter):
        self.getter = getter
        self.__doc__ = getter.__doc__

    def __get__(self, instance, owner):
        return self.getter(owner)


def cleaned_date(day, keep_datetime=False):
    """
    Return a "clean" date type.

    * keep a `date` unchanged
    * convert a datetime into a date,
    * convert any "duck date" type into a date using its `date()` method.
    """
    if not isinstance(day, (date, datetime)):
        raise UnsupportedDateType(
            f"`{day}` is of unsupported type ({type(day)})"
        )
    if not keep_datetime:
        if hasattr(day, 'date') and callable(day.date):
            day = day.date()
    return day


def daterange(start, end):
    """
    Yield days from ``start`` to ``end`` including both of them.

    If start and end are in opposite order, they'll be swapped silently.
    """
    # Swap if necessary
    if start > end:
        end, start = start, end
    day = start
    while day <= end:
        yield day
        day += timedelta(days=1)


class ChristianMixin:
    EASTER_METHOD = None  # to be assigned in the inherited mixin
    include_epiphany = False
    include_clean_monday = False
    include_annunciation = False
    include_fat_tuesday = False
    # Fat tuesday forced to `None` to make sure this value is always set
    # We've seen that there was a wide variety of labels.
    fat_tuesday_label = None
    include_ash_wednesday = False
    ash_wednesday_label = "Ash Wednesday"
    include_palm_sunday = False
    include_holy_thursday = False
    holy_thursday_label = "Holy Thursday"
    include_good_friday = False
    good_friday_label = "Good Friday"
    include_easter_monday = False
    include_easter_saturday = False
    easter_saturday_label = "Easter Saturday"
    include_easter_sunday = False
    include_all_saints = False
    include_immaculate_conception = False
    immaculate_conception_label = "Immaculate Conception"
    include_christmas = True
    christmas_day_label = "Christmas Day"
    include_christmas_eve = False
    include_ascension = False
    include_assumption = False
    include_whit_sunday = False
    whit_sunday_label = 'Whit Sunday'
    include_whit_monday = False
    whit_monday_label = 'Whit Monday'
    include_corpus_christi = False
    include_boxing_day = False
    boxing_day_label = "Boxing Day"
    include_all_souls = False

    def get_fat_tuesday(self, year):
        if not self.fat_tuesday_label:
            raise CalendarError(
                "Improperly configured: please provide a "
                "`fat_tuesday_label` value")
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=47)

    def get_ash_wednesday(self, year):
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=46)

    def get_palm_sunday(self, year):
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=7)

    def get_holy_thursday(self, year):
        "Return the date of the last thursday before easter"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=3)

    def get_good_friday(self, year):
        "Return the date of the last friday before easter"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=2)

    def get_clean_monday(self, year):
        "Return the clean monday date"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=48)

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

    def get_whit_sunday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=49)

    def get_corpus_christi(self, year):
        return self.get_easter_sunday(year) + timedelta(days=60)

    def shift_christmas_boxing_days(self, year):
        """ When Christmas and/or Boxing Day falls on a weekend, it is rolled
            forward to the next weekday.
        """
        christmas = date(year, 12, 25)
        boxing_day = date(year, 12, 26)
        boxing_day_label = f"{self.boxing_day_label} Shift"
        results = []
        if christmas.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(christmas)
            results.append((shift, "Christmas Shift"))
            results.append((shift + timedelta(days=1), boxing_day_label))
        elif boxing_day.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(boxing_day)
            results.append((shift, boxing_day_label))
        return results

    def get_variable_days(self, year):  # noqa
        "Return the christian holidays list according to the mixin"
        days = super().get_variable_days(year)
        if self.include_epiphany:
            days.append((date(year, 1, 6), "Epiphany"))
        if self.include_clean_monday:
            days.append((self.get_clean_monday(year), "Clean Monday"))
        if self.include_annunciation:
            days.append((date(year, 3, 25), "Annunciation"))
        if self.include_fat_tuesday:
            days.append(
                (self.get_fat_tuesday(year), self.fat_tuesday_label)
            )
        if self.include_ash_wednesday:
            days.append(
                (self.get_ash_wednesday(year), self.ash_wednesday_label)
            )
        if self.include_palm_sunday:
            days.append((self.get_palm_sunday(year), "Palm Sunday"))
        if self.include_holy_thursday:
            days.append(
                (self.get_holy_thursday(year), self.holy_thursday_label)
            )
        if self.include_good_friday:
            days.append((self.get_good_friday(year), self.good_friday_label))
        if self.include_easter_saturday:
            days.append(
                (self.get_easter_saturday(year), self.easter_saturday_label)
            )
        if self.include_easter_sunday:
            days.append((self.get_easter_sunday(year), "Easter Sunday"))
        if self.include_easter_monday:
            days.append((self.get_easter_monday(year), "Easter Monday"))
        if self.include_assumption:
            days.append((date(year, 8, 15), "Assumption of Mary to Heaven"))
        if self.include_all_saints:
            days.append((date(year, 11, 1), "All Saints Day"))
        if self.include_all_souls:
            days.append((date(year, 11, 2), "All Souls Day"))
        if self.include_immaculate_conception:
            days.append((date(year, 12, 8), self.immaculate_conception_label))
        if self.include_christmas:
            days.append((date(year, 12, 25), self.christmas_day_label))
        if self.include_christmas_eve:
            days.append((date(year, 12, 24), "Christmas Eve"))
        if self.include_boxing_day:
            days.append((date(year, 12, 26), self.boxing_day_label))
        if self.include_ascension:
            days.append((
                self.get_ascension_thursday(year), "Ascension Thursday"))
        if self.include_whit_monday:
            days.append((self.get_whit_monday(year), self.whit_monday_label))
        if self.include_whit_sunday:
            days.append((self.get_whit_sunday(year), self.whit_sunday_label))
        if self.include_corpus_christi:
            days.append((self.get_corpus_christi(year), "Corpus Christi"))
        return days


class WesternMixin(ChristianMixin):
    """
    General usage calendar for Western countries.

    (chiefly Europe and Northern America)

    """
    EASTER_METHOD = easter.EASTER_WESTERN
    WEEKEND_DAYS = (SAT, SUN)


class OrthodoxMixin(ChristianMixin):
    EASTER_METHOD = easter.EASTER_ORTHODOX
    WEEKEND_DAYS = (SAT, SUN)

    include_orthodox_christmas = True
    # This label should be de-duplicated if needed
    orthodox_christmas_day_label = "Christmas"

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)
        if self.include_orthodox_christmas:
            days.append(
                (date(year, 1, 7), self.orthodox_christmas_day_label)
            )
        return days


class LunarMixin:
    """
    Calendar ready to compute luncar calendar days
    """
    @staticmethod
    def lunar(year, month, day):
        return LunarDate(year, month, day).toSolarDate()


class ChineseNewYearMixin(LunarMixin):
    """
    Calendar including toolsets to compute the Chinese New Year holidays.
    """
    include_chinese_new_year_eve = False
    chinese_new_year_eve_label = "Chinese New Year's eve"
    # Chinese New Year will be included by default
    include_chinese_new_year = True
    chinese_new_year_label = 'Chinese New Year'
    # Some countries include the 2nd lunar day as a holiday
    include_chinese_second_day = False
    chinese_second_day_label = "Chinese New Year (2nd day)"
    include_chinese_third_day = False
    chinese_third_day_label = "Chinese New Year (3rd day)"
    shift_sunday_holidays = False
    # Some calendars roll a starting Sunday CNY to Sat
    shift_start_cny_sunday = False

    def get_chinese_new_year(self, year):
        """
        Compute Chinese New Year days. To return a list of holidays.

        By default, it'll at least return the Chinese New Year holidays chosen
        using the following options:

        * ``include_chinese_new_year_eve``
        * ``include_chinese_new_year`` (on by default)
        * ``include_chinese_second_day``

        If the ``shift_sunday_holidays`` option is on, the rules are the
        following.

        * If the CNY1 falls on MON-FRI, there's not shift.
        * If the CNY1 falls on SAT, the CNY2 is shifted to the Monday after.
        * If the CNY1 falls on SUN, the CNY1 is shifted to the Monday after,
          and CNY2 is shifted to the Tuesday after.
        """
        days = []

        lunar_first_day = ChineseNewYearMixin.lunar(year, 1, 1)
        # Chinese new year's eve
        if self.include_chinese_new_year_eve:
            days.append((
                lunar_first_day - timedelta(days=1),
                self.chinese_new_year_eve_label
            ))
        # Chinese new year (is included by default)
        if self.include_chinese_new_year:
            days.append((lunar_first_day, self.chinese_new_year_label))

        if self.include_chinese_second_day:
            lunar_second_day = lunar_first_day + timedelta(days=1)
            days.append((
                lunar_second_day,
                self.chinese_second_day_label
            ))
        if self.include_chinese_third_day:
            lunar_third_day = lunar_first_day + timedelta(days=2)
            days.append((
                lunar_third_day,
                self.chinese_third_day_label
            ))

        if self.shift_sunday_holidays:
            if lunar_first_day.weekday() == SUN:
                if self.shift_start_cny_sunday:
                    days.append(
                        (lunar_first_day - timedelta(days=1),
                         "Chinese Lunar New Year shift"),
                    )
                else:
                    if self.include_chinese_third_day:
                        shift_day = lunar_third_day
                    else:
                        shift_day = lunar_second_day
                    days.append(
                        (shift_day + timedelta(days=1),
                         "Chinese Lunar New Year shift"),
                    )
            if (lunar_second_day.weekday() == SUN
                    and self.include_chinese_third_day):
                days.append(
                    (lunar_third_day + timedelta(days=1),
                     "Chinese Lunar New Year shift"),
                )
        return days

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend(self.get_chinese_new_year(year))
        return days

    def get_shifted_holidays(self, dates):
        """
        Taking a list of existing holidays, yield a list of 'shifted' days if
        the holiday falls on SUN.
        """
        for holiday, label in dates:
            if holiday.weekday() == SUN:
                yield (
                    holiday + timedelta(days=1),
                    f'{label} shift'
                )

    def get_calendar_holidays(self, year):
        """
        Take into account the eventual shift to the next MON if any holiday
        falls on SUN.
        """
        # Unshifted days are here:
        days = super().get_calendar_holidays(year)
        if self.shift_sunday_holidays:
            days_to_inspect = copy(days)
            for day_shifted in self.get_shifted_holidays(days_to_inspect):
                days.append(day_shifted)
        return days


class CalverterMixin:
    conversion_method = None
    ISLAMIC_HOLIDAYS = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.conversion_method is None:
            raise NotImplementedError

    def converted(self, year):
        current = date(year, 1, 1)
        delta = timedelta(days=1)
        days = []
        while current.year == year:
            days.append(
                self.conversion_method.from_gregorian(
                    current.year,
                    current.month,
                    current.day
                )
            )
            current += delta
        return days

    def calverted_years(self, year):
        converted = self.converted(year)
        return sorted({y for y, m, d in converted})

    def get_islamic_holidays(self):
        return self.ISLAMIC_HOLIDAYS

    def get_delta_islamic_holidays(self, year):
        """
        Return the delta to add/substract according to the year or customs.

        By default, to return None or timedelta(days=0)
        """
        return None

    def get_variable_days(self, year):
        warnings.warn('Please take note that, due to arbitrary decisions, '
                      'this Islamic calendar computation may be wrong.')
        days = super().get_variable_days(year)
        years = self.calverted_years(year)
        for month, day, label in self.get_islamic_holidays():
            for y in years:
                g_date = self.conversion_method.to_gregorian(y, month, day)
                holiday = date(*g_date)

                # Only add a delta if necessary
                delta = self.get_delta_islamic_holidays(year)
                if delta:
                    holiday += delta

                if holiday.year == year:
                    days.append((holiday, label))
        return days


class IslamicMixin(CalverterMixin):

    WEEKEND_DAYS = (FRI, SAT)

    conversion_method = convertdate.islamic
    include_prophet_birthday = False
    include_day_after_prophet_birthday = False
    include_start_ramadan = False
    include_eid_al_fitr = False
    length_eid_al_fitr = 1
    eid_al_fitr_label = "Eid al-Fitr"
    include_eid_al_adha = False
    eid_al_adha_label = "Eid al-Adha"
    length_eid_al_adha = 1
    include_day_of_sacrifice = False
    day_of_sacrifice_label = "Eid al-Adha"
    include_islamic_new_year = False
    include_laylat_al_qadr = False
    include_nuzul_al_quran = False

    def get_islamic_holidays(self):
        """Return a list of Islamic (month, day, label) for islamic holidays.
        Please take note that these dates must be expressed using the Islamic
        Calendar"""
        days = list(super().get_islamic_holidays())

        if self.include_islamic_new_year:
            days.append((1, 1, "Islamic New Year"))
        if self.include_prophet_birthday:
            days.append((3, 12, "Prophet's Birthday"))
        if self.include_day_after_prophet_birthday:
            days.append((3, 13, "Day after Prophet's Birthday"))
        if self.include_start_ramadan:
            days.append((9, 1, "Start of ramadan"))
        if self.include_nuzul_al_quran:
            days.append((9, 17, "Nuzul Al-Qur'an"))
        if self.include_eid_al_fitr:
            for x in range(self.length_eid_al_fitr):
                days.append((10, x + 1, self.eid_al_fitr_label))
        if self.include_eid_al_adha:
            for x in range(self.length_eid_al_adha):
                days.append((12, x + 10, self.eid_al_adha_label))
        if self.include_day_of_sacrifice:
            days.append((12, 10, self.day_of_sacrifice_label))
        if self.include_laylat_al_qadr:
            warnings.warn("The Islamic holiday named Laylat al-Qadr is decided"
                          " by the religious authorities. It is not possible"
                          " to compute it. You'll have to add it manually.")
        return tuple(days)


class CoreCalendar:

    FIXED_HOLIDAYS = ()
    WEEKEND_DAYS = ()

    def __init__(self):
        self._holidays = {}

    @classproperty
    def name(cls):
        class_name = cls.__name__
        if cls.__doc__:
            doc = cls.__doc__.split('\n')
            doc = map(lambda s: s.strip(), doc)
            return next(s for s in doc if s)
        return class_name

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

    def get_holiday_label(self, day):
        """Return the label of the holiday, if the date is a holiday"""
        day = cleaned_date(day)
        return {day: label for day, label in self.holidays(day.year)}.get(day)

    def holidays_set(self, year=None):
        "Return a quick date index (set)"
        return {day for day, label in self.holidays(year)}

    def get_weekend_days(self):
        """Return a list (or a tuple) of weekdays that are *not* working days.

        e.g: return (SAT, SUN,)

        """
        if self.WEEKEND_DAYS:
            return self.WEEKEND_DAYS
        else:
            raise NotImplementedError("Your Calendar class must provide "
                                      "WEEKEND_DAYS or implement the "
                                      "`get_weekend_days` method")

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
        day = cleaned_date(day)
        if extra_working_days:
            extra_working_days = tuple(map(cleaned_date, extra_working_days))
        if extra_holidays:
            extra_holidays = tuple(map(cleaned_date, extra_holidays))

        # Extra lists exceptions
        if extra_working_days and day in extra_working_days:
            return True

        # Regular rules
        if day.weekday() in self.get_weekend_days():
            return False

        return not self.is_holiday(day, extra_holidays=extra_holidays)

    def is_holiday(self, day, extra_holidays=None):
        """Return True if it's an holiday.
        In addition to the regular holidays, you can add exceptions.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        """
        day = cleaned_date(day)

        if extra_holidays:
            extra_holidays = tuple(map(cleaned_date, extra_holidays))

        if extra_holidays and day in extra_holidays:
            return True

        return day in self.holidays_set(day.year)

    def add_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        """Add `delta` working days to the date.

        You can provide either a date or a datetime to this function that will
        output a ``date`` result. You can alter this behaviour using the
        ``keep_datetime`` option set to ``True``.

        the ``delta`` parameter might be positive or negative. If it's
        negative, you may want to use the ``sub_working_days()`` method with
        a positive ``delta`` argument.

        By providing ``extra_working_days``, you'll state that these dates
        **are** working days.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        Please note that the ``extra_working_days`` list has priority over the
        ``extra_holidays`` list.
        """
        day = cleaned_date(day, keep_datetime)

        if extra_working_days:
            extra_working_days = tuple(map(cleaned_date, extra_working_days))

        if extra_holidays:
            extra_holidays = tuple(map(cleaned_date, extra_holidays))

        days = 0
        temp_day = day
        day_added = 1 if delta >= 0 else -1
        delta = abs(delta)
        while days < delta:
            temp_day = temp_day + timedelta(days=day_added)
            if self.is_working_day(temp_day,
                                   extra_working_days=extra_working_days,
                                   extra_holidays=extra_holidays):
                days += 1
        return temp_day

    def sub_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        """
        Substract `delta` working days to the date.

        This method is a shortcut / helper. Users may want to use either::

            cal.add_working_days(my_date, -7)
            cal.sub_working_days(my_date, 7)

        The other parameters are to be used exactly as in the
        ``add_working_days`` method.

        A negative ``delta`` argument will be converted into its absolute
        value. Hence, the two following calls are equivalent::

            cal.sub_working_days(my_date, -7)
            cal.sub_working_days(my_date, 7)

        As in ``add_working_days()`` you can set the parameter
        ``keep_datetime`` to ``True`` to make sure that if your ``day``
        argument is a ``datetime``, the returned date will also be a
        ``datetime`` object.

        """
        delta = abs(delta)
        return self.add_working_days(
            day, -delta,
            extra_working_days, extra_holidays, keep_datetime=keep_datetime)

    def find_following_working_day(self, day):
        """Looks for the following working day, if not already a working day.

        **WARNING**: this function doesn't take into account the calendar
        holidays, only the days of the week and the weekend days parameters.
        """
        day = cleaned_date(day)

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
        # If start is `None` or Falsy, no need to check and clean
        if start:
            start = cleaned_date(start)

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

    @staticmethod
    def get_iso_week_date(year, week_nb, weekday=ISO_MON):
        """
        Return the date of the weekday of the week number (ISO definition).

        **Warning:** in the ISO definition, the weeks start on MON, not SUN.

        By default, if you don't provide the ``weekday`` argument, it'll return
        the date of the MON of this week number.

        Example:

            >>> Calendar.get_iso_week_date(2021, 44)
            datetime.date(2021, 11, 1)

        For your convenience, the ISO weekdays are available via the
        ``workalendar.core`` module, like this:

            from workalendar.core import ISO_MON, ISO_TUE  # etc.

        i.e.: if you need to get the FRI of the week 44 of the year 2020,
        you'll have to use:

            from workalendar.core import ISO_FRI
            Calendar.get_iso_week_date(2020, 44, ISO_FRI)

        """
        if sys.version_info >= (3, 8, 0):
            # use the stock Python 3.8 function
            return date.fromisocalendar(year, week_nb, weekday)

        # else, use the backport
        # Adapted from https://stackoverflow.com/a/59200842
        jan_1st = date(year, 1, 1)
        _, jan_1st_week, jan_1st_weekday = jan_1st.isocalendar()
        base = 1 if jan_1st_week == 1 else 8
        delta = base - jan_1st_weekday + 7 * (week_nb - 1) + (weekday - 1)
        start = jan_1st + timedelta(days=delta)
        return start

    @staticmethod
    def get_first_weekday_after(day, weekday):
        """Get the first weekday after a given day. If the day is the same
        weekday, the same day will be returned.

        >>> # the first monday after Apr 1 2015
        >>> Calendar.get_first_weekday_after(date(2015, 4, 1), MON)
        datetime.date(2015, 4, 6)

        >>> # the first tuesday after Apr 14 2015
        >>> Calendar.get_first_weekday_after(date(2015, 4, 14), TUE)
        datetime.date(2015, 4, 14)
        """
        day_delta = (weekday - day.weekday()) % 7
        day = day + timedelta(days=day_delta)
        return day

    def get_working_days_delta(self, start, end, include_start=False,
                               extra_working_days=None, extra_holidays=None):
        """
        Return the number of working day between two given dates.
        The order of the dates provided doesn't matter.

        In the following example, there are 5 days, because of the week-end:

        >>> cal = WesternCalendar()  # does not include easter monday
        >>> day1 = date(2018, 3, 29)
        >>> day2 = date(2018, 4, 5)
        >>> cal.get_working_days_delta(day1, day2)
        5

        In France, April 1st 2018 is a holiday because it's Easter monday:

        >>> cal = France()
        >>> cal.get_working_days_delta(day1, day2)
        4

        This method should even work if your ``start`` and ``end`` arguments
        are datetimes.

        By default, if the day after you start is not a working day,
        the count will start at 0. If include_start is set to true,
        this day will be taken into account.

        Example:

        >>> from dateutil.parser import parse
        >>> cal = France()
        >>> day1 = parse('09/05/2018 00:01', dayfirst=True)
        >>> day2 = parse('10/05/2018 19:01', dayfirst=True) # holiday in france
        >>> cal.get_working_days_delta(day1, day2)
        0

        >>> cal.get_working_days_delta(day1, day2, include_start=True)
        1

        As in many other methods, you can use the ``extra_holidays`` and
        ``extra_working_days`` to exclude
        """
        start = cleaned_date(start)
        end = cleaned_date(end)

        if start == end:
            return 0

        if start > end:
            start, end = end, start

        # Starting count here
        is_working_day = self.is_working_day(
            start,
            extra_working_days=extra_working_days,
            extra_holidays=extra_holidays
        )
        count = 1 if include_start and is_working_day else 0
        while start < end:
            start += timedelta(days=1)
            is_working_day = self.is_working_day(
                start,
                extra_working_days=extra_working_days,
                extra_holidays=extra_holidays
            )
            if is_working_day:
                count += 1
        return count

    def _get_ical_period(self, period=None):
        """
        Return a usable period for iCal export

        Default period is [2000, 2030]
        """
        # Default value.
        if not period:
            period = [2000, 2030]

        # Make sure it's a usable iterable
        if type(period) not in (list, tuple):
            raise ICalExportRangeError(
                "Incorrect Range type. Must be list or tuple.")

        # Taking the extremes
        period = [min(period), max(period)]

        # check for internal types
        check_types = map(type, period)
        check_types = map(lambda x: x != int, check_types)
        if any(check_types):
            raise ICalExportRangeError(
                "Incorrect Range boundaries. Must be int.")

        return period

    def _get_ical_target_path(self, target_path):
        """
        Return target path for iCal export.

        Note
        ----
        If `target_path` does not have one of the extensions `.ical`, `.ics`,
        `.ifb`, or `.icalendar`, the extension `.ics` is appended to the path.
        Returns
        -------
        None.
        Examples
        --------
        >>> cal = Austria()
        >>> cal._get_ical_target_path('austria')  # -> austria.ics

        """

        if not target_path:
            raise ICalExportTargetPathError(
                "Incorrect target path. It must not be empty")

        target_path = Path(target_path)

        if target_path.is_dir():
            raise ICalExportTargetPathError(
                "Incorrect target path. It must not be a directory"
            )

        ical_extensions = ['.ical', '.ics', '.ifb', '.icalendar']
        if target_path.suffix not in ical_extensions:
            target_path = target_path.with_name(target_path.name + '.ics')
        return target_path

    def export_to_ical(self, period=[2000, 2030], target_path=None):
        """
        Export the calendar to iCal (RFC 5545) format.

        Parameters
        ----------
        period: [int, int]
            start and end year (inclusive) of calendar
            Default is [2000, 2030]

        target_path: str or pathlib.Path
            the name or path of the exported file. If this argument is missing,
            the function will return the ical content.

        """
        first_year, last_year = self._get_ical_period(period)
        if target_path:
            # Generate filename path before calculate the holidays
            target_path = self._get_ical_target_path(target_path)

        # fetch holidays
        holidays = []
        for year in range(first_year, last_year + 1):
            holidays.extend(self.holidays(year))

        # initialize icalendar
        ics = [
            'BEGIN:VCALENDAR',
            'VERSION:2.0',  # current RFC5545 version
            f'PRODID:-//workalendar//ical {__version__}//EN'
        ]
        dtstamp = f'DTSTAMP;VALUE=DATE-TIME:{datetime.utcnow():%Y%m%dT%H%M%SZ}'

        # add an event for each holiday
        for date_, name in holidays:
            ics.extend([
                'BEGIN:VEVENT',
                f'SUMMARY:{name}',
                f'DTSTART;VALUE=DATE:{date_:%Y%m%d}',
                dtstamp,
                f'UID:{date_}{name}@peopledoc.github.io/workalendar',
                'END:VEVENT',
            ])

        # add footer
        ics.append('END:VCALENDAR\n')  # last line with a trailing \n

        # Transform this list into text lines
        ics = "\n".join(ics)

        if target_path:
            # save iCal file
            with target_path.open('w+') as export_file:
                export_file.write(ics)
            return

        return ics


class Calendar(CoreCalendar):
    """
    The cornerstone of Earth calendars.

    Take care of the New Years Day, which is almost a worldwide holiday.
    """
    include_new_years_day = True
    include_new_years_eve = False
    shift_new_years_day = False
    include_labour_day = False
    labour_day_label = "Labour Day"

    def __init__(self, **kwargs):
        super().__init__()

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)
        if self.include_new_years_day:
            days.insert(0, (date(year, 1, 1), "New year"))
        if self.include_new_years_eve:
            days.append((date(year, 12, 31), "New Year's eve"))
        if self.include_labour_day:
            days.append((date(year, 5, 1), self.labour_day_label))
        return days

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        new_year = date(year, 1, 1)
        if self.include_new_years_day and self.shift_new_years_day:
            if new_year.weekday() in self.get_weekend_days():
                days.append((
                    self.find_following_working_day(new_year),
                    "New Year shift"))
        return days


class WesternCalendar(WesternMixin, Calendar):
    """
    A Christian calendar using Western definition for Easter.
    """


class OrthodoxCalendar(OrthodoxMixin, Calendar):
    """
    A Christian calendar using Orthodox definition for Easter.
    """


class ChineseNewYearCalendar(ChineseNewYearMixin, Calendar):
    """
    Chinese Calendar, using Chinese New Year computation.
    """
    # There are regional exceptions to those week-end days, to define locally.
    WEEKEND_DAYS = (SAT, SUN)


class IslamicCalendar(IslamicMixin, Calendar):
    """
    Islamic calendar
    """


class IslamoWesternCalendar(IslamicMixin, WesternMixin, Calendar):
    """
    Mix of Islamic and Western calendars.

    When countries have both Islamic and Western-Christian holidays.
    """
    FIXED_HOLIDAYS = Calendar.FIXED_HOLIDAYS
