import itertools
from datetime import date, timedelta

from more_itertools import recipes


class Holiday(date):
    """
    A named holiday with an indicated date, name, and additional keyword
    attributes.

    >>> nyd = Holiday(date(2014, 1, 1), "New year")

    But if New Year's Eve is also a holiday, and it too falls on a weekend,
    many calendars will have that holiday fall back to the previous friday:

    >>> from dateutil import relativedelta as rd
    >>> nye = Holiday(date(2014, 12, 31), "New year's eve",
    ...     observance_shift=dict(weekday=rd.FR(-1)))

    For compatibility, a Holiday may be treated like a tuple of (date, label)

    >>> nyd[0] == date(2014, 1, 1)
    True
    >>> nyd[1]
    'New year'
    >>> d, label = nyd
    """

    def __new__(cls, date, *args, **kwargs):
        return super().__new__(
            cls, date.year, date.month, date.day)

    def __init__(self, date, name='Holiday', **kwargs):
        self.name = name
        vars(self).update(kwargs)

    def __getitem__(self, n):
        """
        for compatibility as a two-tuple
        """
        tp = self, self.name
        return tp[n]

    def __iter__(self):
        """
        for compatibility as a two-tuple
        """
        tp = self, self.name
        return iter(tp)

    def replace(self, *args, **kwargs):
        replaced = super().replace(*args, **kwargs)
        vars(replaced).update(vars(self))
        return replaced

    def __add__(self, other):
        orig = date(self.year, self.month, self.day)
        return Holiday(orig + other, **vars(self))

    def __sub__(self, other):
        orig = date(self.year, self.month, self.day)
        return Holiday(orig - other, **vars(self))

    def nearest_weekday(self, calendar):
        """
        Return the nearest weekday to self.
        """
        weekend_days = calendar.get_weekend_days()
        deltas = (timedelta(n) for n in itertools.count())
        candidates = recipes.flatten(
            (self - delta, self + delta)
            for delta in deltas
        )
        matches = (
            day for day in candidates
            if day.weekday() not in weekend_days
        )
        return next(matches)

    @classmethod
    def _from_fixed_definition(cls, item):
        """For backward compatibility, load Holiday object from an item of
        FIXED_HOLIDAYS class property, which might be just a tuple of
        month, day, label.
        """
        if isinstance(item, tuple):
            month, day, label = item
            any_year = 2000
            item = Holiday(date(any_year, month, day), label)
        return item

    @classmethod
    def _from_resolved_definition(cls, item, **kwargs):
        """For backward compatibility, load Holiday object from a two-tuple
        or existing Holiday instance.
        """
        if isinstance(item, tuple):
            item = Holiday(*item, **kwargs)
        return item


class SeriesShiftMixin:
    """
    "Series" holidays like the two Islamic Eid's or Chinese Spring Festival span
    multiple days. If one of these days encounters a non-zero observance_shift,
    apply that shift to all subsequent members of the series.
    """

    def get_calendar_holidays(self, year):
        """
        Ensure that all events are observed in the order indicated.
        """
        days = super().get_calendar_holidays(year)
        holidays = sorted(map(Holiday._from_resolved_definition, days))
        from more_itertools import pairwise
        for a, b in pairwise(holidays):
            b.observe_after = a
        return holidays
