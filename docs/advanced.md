# Advanced usage

[Home](index.md) / [Basic usage](basic.md) / [ISO Registry](iso-registry.md)

The following examples will better suit people willing to contribute to Calendra or building their custom calendars. They use primitives and methods attached to the core Calendar class to enable computation of complex holidays, that is to say dates that are not fixed, not related to religious calendars (Christmas always happens on December 25th, right?).

## Find the following working day after a date

It's a bit like a shortcut function to find the next working day after the given date.

Please note that if the day you're entering is already a working day, that'll be the returned result.

```python
>>> from datetime import date, datetime
>>> from calendra.europe import France
>>> cal = France()
>>> cal.find_following_working_day(date(2018, 7, 6))  # It's FRI
datetime.date(2018, 7, 6)
>>> cal.find_following_working_day(date(2018, 7, 7))  # SAT => next MON
datetime.date(2018, 7, 9)
```

**WARNING**: this function doesn't take into account the existing holidays in the calendar. If you need this, use the ``add_working_days()`` function as described in the [Basic usage document](basic.md).

## Find the 4th Thursday in November

That's a puzzling question that we needed to address when we had to implement United States of America holidays calendars. Thanksgiving day, for example, which is on the 4th Thursday in November (Thanksgiving Friday is the day after this thursday)... and many others, are defined as:

> the ``nth`` ``Weekday name`` of the month of ``Month name``

Or even better for Election day, which is:

> the Tuesday next after the first Monday in the month of November.

We've got you covered with static methods in the core ``Calendar`` class.

```python
>>> from calendra.core import Calendar, THU
>>> Calendar.get_nth_weekday_in_month(2018, 11, THU)  # by default, find the first
datetime.date(2018, 11, 2)
>>> Calendar.get_nth_weekday_in_month(2018, 11, THU, 4)  # Thanksgiving
datetime.date(2018, 11, 23)
```

If you want to find the 2nd Monday after the 4th of July, you can use the ``start`` argument:

```python
>>> from datetime import date
>>> from calendra.core import Calendar, MON
>>> Calendar.get_nth_weekday_in_month(
  2018,  # Year
  7,     # Month
  MON,   # Monday
  2,     # The 2nd one
  start=date(2018, 7, 9))
datetime.date(2018, 7, 16)
```

## Find the last Monday in the Month

This one was a bit trickier, because it may happen that you have 4 or 5 `weekday name` in the same month. e.g: during the month of July 2018, you have 5 Mondays (2nd, 9th, 16th, 23rd, 30th), but only 4 Saturdays (7th, 14th, 21st, 28th).

Same as above, there's a static method in the ``Calendar`` class:

```python
>>> from calendra.core import Calendar, MON, FRI
>>> Calendar.get_last_weekday_in_month(2018, 7, MON)
datetime.date(2018, 7, 30)
>>> Calendar.get_last_weekday_in_month(2018, 7, FRI)
datetime.date(2018, 7, 27)
```

## Find the first Monday after a given date

Colombia, as an example, states that the Epiphany Day is set to the "First Monday after the 6th of January". You may use the following function to find this specific formula:

```python
>>> from calendra.core import Calendar, MON
>>> from datetime import date
>>> jan_6th = date(2018, 1, 6)  # It's a Saturday
>>> Calendar.get_first_weekday_after(jan_6th, MON)
datetime.date(2018, 1, 8)
```

[Home](index.md) / [Basic usage](basic.md) / [ISO Registry](iso-registry.md)
