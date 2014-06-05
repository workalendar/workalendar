
ephem.Date
==========

PyEphem uses a simple floating point number
to represent the date and time inside of its astronomy routines.
While it would have been possible for PyEphem to conceal this
by always converting dates into Python's native ``datetime`` type
before returning them,
doing so — besides being slower —
would have incurred a slight rounding error in every date returned,
and the accumulation of this error could have caused problems
for users who need high precision.
So PyEphem provides its own ``ephem.Date`` type,
which preserves the full precision of the dates it uses internally.

The ``ephem.Date`` type simply subclasses the Python ``float``
to provide it with some extra features.
The most important is that it displays itself as a date when printed
(and also when formatted with ``%s``,
and when converted with the ``str()`` function):

    >>> import ephem
    >>> d = ephem.Date('1984/05/30 16:23:45.12')
    >>> print d
    1984/5/30 16:23:45

But behind the scenes,
each date is really a Python floating point number:

    >>> isinstance(d, float)
    True
    >>> print 'Behind the date %s is the number %f.' % (d, d)
    Behind the date 1984/5/30 16:23:45 is the number 30831.183161.

Time zones
----------

PyEphem's ``Date`` type itself does *not* support time zones.
All PyEphem dates are expressed in Universal Time (UTC),
which is similar to Standard Time in Greenwich, England.
But if you need a time displayed in your local timezone,
then you can use the PyEphem ``localtime`` function,
which takes a PyEphem date
and returns a Python ``datetime`` giving your local time.

    >>> lt = ephem.localtime(d)
    >>> print lt
    1984-05-30 12:23:45.000002
    >>> print repr(lt)
    datetime.datetime(1984, 5, 30, 12, 23, 45, 2)

The output of this code will differ
depending on the time zone in which you live.
Since I am in the Eastern time zone,
the ``time.localtime()`` call above
subtracted four hours from 16:23,
and returned 12:23 Eastern Daylight Time.
(Note that Daylight Time was chosen because the date fell in May;
had the date been in the winter, Standard Time would have been used.)

Conversions
-----------

PyEphem dates can be converted to and from
several other representations.

Strings
  As illustrated in the opening section above,
  dates can be initialized with strings,
  and can display themselves as strings on demand.

    >>> d = ephem.Date('1984/05/30 16:23:45.12')
    >>> print d
    1984/5/30 16:23:45

  The string you provide when creating a date
  can omit some of the numbers at the end.
  In fact, the only you have to specify is the year!
  The month, if not provided, defaults to January;
  the day defaults to the first of the month;
  and hours, minutes, and seconds default to zero.

    >>> print ephem.Date('1984/05/30 16')
    1984/5/30 16:00:00

    >>> print ephem.Date('1984')
    1984/1/1 00:00:00

  Note that the string output does not include fractional seconds;
  you will have to use one of the other conversions, below,
  if you need to be that precise.

Datetime objects
  When creating an ``ephem.Date``,
  you can specify the date
  as either a ``date`` or ``datetime`` object
  from the ``datetime`` standard Python module.
  You can also ask a PyEphem date to convert itself the other direction
  by calling its ``datetime()`` method.

    >>> from datetime import date, datetime
    >>> print ephem.Date(datetime(2005, 4, 18, 22, 19))
    2005/4/18 22:18:59

    >>> d = ephem.Date('2000/12/25 12:41:16')
    >>> d.datetime()
    datetime.datetime(2000, 12, 25, 12, 41, 15, 999999)

  In those last two commands,
  note that slight round-off error has converted sixteen seconds
  to 15.999999 seconds!
  The inevitability of such errors
  is why PyEphem exposes its own date type
  instead of returning Python ``datetime`` objects automatically.

Tuples
  PyEphem can return a date as a six-element tuple
  giving the year, month, day, hour, minute, and seconds,
  where the seconds include any fractions of a second.
  You can also provide such a tuple when creating a PyEphem date.

    >>> timetuple = (1984, 5, 30, 12, 23, 45)
    >>> print ephem.Date(timetuple)
    1984/5/30 12:23:45

    >>> d = ephem.Date('2001/12/14 16:07:57')
    >>> print d.tuple()
    (2001, 12, 14, 16, 7, 57.00000002514571)

  Several functions in the Python standard module ``time``
  will accept the time formatted as one of these six-element tuples.
  This feature was used in the *Time Zones* section, above,
  to convert a PyEphem date into local time.

Triples
  There may be occasions where you need to manipulate the year and month
  but do not need to break the day into hours and minutes.
  In these cases,
  you can provide a three-item tuple (a “triple” of values)
  when creating a PyEphem date,
  and receive one back by calling the ``triple()`` method.

    >>> timetriple = (1998, 2, 26.691458333334594)
    >>> print ephem.Date(timetriple)
    1998/2/26 16:35:42

    >>> d = ephem.Date('1996/4/17 22:37:11.5')
    >>> print d.triple()
    (1996, 4, 17.94249421296263)

Floats
  Finally,
  since a PyEphem date is really just a floating-point number,
  so you can manually supply the value you want it to have.

    >>> print ephem.Date(37238.1721875)
    2001/12/14 16:07:57

    >>> d = ephem.Date('2000/12/25 12:41:16')
    >>> print float(d)
    36884.0286574

  For more information on what the floating point number means
  when interpreted as a date,
  see the next section.

Calculating with dates
----------------------

PyEphem dates are encoded as the “Dublin Julian Day”,
which is the number of days (including any fraction)
that have passed since the last day of 1899, at noon.
From there, increasing the value by one moves to the next day: 

    >>> print ephem.Date(0)
    1899/12/31 12:00:00
    >>> print ephem.Date(1)
    1900/1/1 12:00:00
    >>> print ephem.Date(2)
    1900/1/2 12:00:00

Negative numbers are also perfectly legitimate,
and count backwards from the same reference point:

    >>> print ephem.Date(-1)
    1899/12/30 12:00:00
    >>> print ephem.Date(-2)
    1899/12/29 12:00:00

Fractions of a day, of course,
move the time forward by hours within a single day.
Note that doing math on a date returns a simple Python float,
which you have to re-cast to an XEphem date
if you want to display it:

    >>> n = ephem.Date(7) + 0.5
    >>> print n
    7.5
    >>> print ephem.Date(n)
    1900/1/8 00:00:00

To make math with dates more convenient,
PyEphem provides constants ``hour``, ``minute``, and ``second``
that represent those three fractions of a day.

    >>> print ephem.Date(n + ephem.hour)
    1900/1/8 01:00:00
    >>> print ephem.Date(n + ephem.minute)
    1900/1/8 00:01:00
    >>> print ephem.Date(n + ephem.second)
    1900/1/8 00:00:01
    >>> print ephem.Date(n + 12 * ephem.hour + 36 * ephem.minute)
    1900/1/8 12:36:00
