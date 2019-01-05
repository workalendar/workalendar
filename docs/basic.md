# Basic usage

[Home](index.md) / [Advanced usage](advanced.md) / [ISO Registry](iso-registry.md)

Here are basic examples of what Calendra can do for you. As an integrator or a simple Calendra user, you will use these methods to retrieve calendars, and get basic outputs for a given date.

## Get holidays for a given country and year

```python
>>> from calendra.europe import France
>>> cal = France()
>>> cal.holidays(2012)
[(datetime.date(2012, 1, 1), 'New year'),
 (datetime.date(2012, 4, 9), 'Easter Monday'),
 (datetime.date(2012, 5, 1), 'Labour Day'),
 (datetime.date(2012, 5, 8), 'Victory in Europe Day'),
 (datetime.date(2012, 5, 17), 'Ascension Day'),
 (datetime.date(2012, 5, 28), 'Whit Monday'),
 (datetime.date(2012, 7, 14), 'Bastille Day'),
 (datetime.date(2012, 8, 15), 'Assumption of Mary to Heaven'),
 (datetime.date(2012, 11, 1), "All Saints' Day"),
 (datetime.date(2012, 11, 11), 'Armistice Day'),
 (datetime.date(2012, 12, 25), 'Christmas')]
```

As you can see, the output is a simple list of tuples, with the first member being a `datetime.date` object, and the second one is the holiday label as a string. By design, we have chosen to stick to basic types so you can use them in your application and eventually compose your personal classes using them.

## Know if a day is a holiday or not

```python
>>> from datetime import date
>>> from calendra.europe import France
>>> cal = France()
>>> cal.is_working_day(date(2012, 12, 25))  # it's Christmas
False
>>> cal.is_working_day(date(2012, 12, 30))  # it's a Sunday
False
>>> cal.is_working_day(date(2012, 12, 26))  # No Boxing day in France
True
```

## Compute the "nth" working day after a given date

That was the basic use-case that started this library development: to answer to the following question:

> This task is due in 5 working days, starting of today. Can we calculate that?

In the following example, we want to calculate 5 working days after December the 23rd 2012.

| Date | Weekday | Working Day? | Count |
|:-----|:-------:|:------------:|:-----:|
| 23rd |   SUN   |      No      |   0   |
| 24th |   MON   |     Yes      |  +1   |
| 25th |   TUE   |  No (XMas)   |   -   |
| 26th |   WED   |     Yes      |  +2   |
| 27th |   THU   |     Yes      |  +3   |
| 28th |   FRI   |     Yes      |  +4   |
| 29th |   SAT   | No (weekend) |   -   |
| 30th |   SUN   | No (weekend) |   -   |
| 31th |   MON   |     Yes      |  +5   |

```python
>>> from datetime import date
>>> from calendra.europe import France
>>> cal = France()
>>> cal.add_working_days(date(2012, 12, 23), 5)
datetime.date(2012, 12, 31)
```

If we had requested the 6th day after the 23rd, it would have been January 2nd, 2013, because January 1st is New Year's Day.

## Calculate the number or working days between two given days

Let's say you want to know how many working days there are between April 2nd and June 17th of 2018, in France. Use the following:

```python
>>> from datetime import date
>>> from calendra.europe import France
>>> cal = France()
>>> cal.get_working_days_delta(date(2018, 4, 2), date(2018, 6, 17))
50
```

## Standard date(time) types only, please!

For your convenience, we allow both `datetime.date` and `datetime.datetime` types (and their subclasses) when using the core functions.

**WARNING**: We'll only allow "dates" types coming from the Python standard library. If you're manipulating types from external library. Trying to pass a non-standard argument will result in raising a ``UnsupportedDateType`` error.

Example:

```python
>>> from datetime import date, datetime
>>> from calendra.europe import France
>>> cal = France()
>>> cal.is_working_day(datetime(2012, 12, 25, 14, 0, 39))
False
>>> cal.add_working_days(datetime(2012, 12, 23, 14, 0, 39), 5)
datetime.datetime(2012, 12, 31)
```

If you really need it, you can use the ``add_working_days()`` with an option that will keep the ``datetime`` type:

```python
>>> from datetime import date, datetime
>>> from calendra.europe import France
>>> cal = France()
>>> cal.add_working_days(datetime(2012, 12, 23, 14, 0, 39), 5, keep_datetime=True)
datetime.datetime(2012, 12, 31, 14, 0, 39)
```

[Home](index.md) / [Advanced usage](advanced.md) / [ISO Registry](iso-registry.md)
