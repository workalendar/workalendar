
ephem.Angle
===========

PyEphem measures all angles in radians.
But rather than simply returning angles as bare Python floats,
it returns each of them as an ``ephem.Angle``
which can print itself out in a more attractive format
than do raw floating-point numbers.

The vast majority of angles print as degrees.
For example,
the declination of Jupiter will print itself attractively
as degrees, minutes of arc, and seconds of arc:

    >>> import ephem
    >>> j = ephem.Jupiter('1994/7/16 20:13:16')
    >>> print j.dec
    -12:09:28.2

But the real value is always in radians,
which you can view by using ``repr()``::

    print repr(j.dec)  # => -0.21219402907256785

The only kind of angle which does not use degrees for display
is right ascension,
which instead traditionally breaks the celestial equator
into twenty-four “hours” which are each fifteen degress wide.

    >>> print j.ra
    14:12:45.77

As with PyEphem dates,
doing math with a PyEphem angle results in an unadorned float being returned.

    >>> type(j.dec)
    <type 'ephem.Angle'>
    >>> a = j.dec + 3.14
    >>> type(a)
    <type 'float'>

If you want to display the result of a computation
as an attractively formatted angle,
you can convert the float back to a PyEphem angle type
using either the ``degrees()`` function
or, for right ascension, the ``hours()`` function.
For example,
here are the results of adding fifteen degrees
to both Jupiter's declination and right ascension;
whereas the declination simply moves north by fifteen degrees
(passing north across the celestial equator into positive numbers),
the right ascension calls fifteen additional degrees “one hour” of motion:

    >>> import math
    >>> fifteen_degrees = ephem.degrees(math.pi / 12.)
    >>> print j.dec, ephem.degrees(j.dec + fifteen_degrees)
    -12:09:28.2 2:50:31.8
    >>> print j.ra, ephem.hours(j.ra + fifteen_degrees)
    14:12:45.77 15:12:45.77

Often when adding or subtracting with angles,
you will get a very large or small result
that you will want to normalize back to a respectable angle.
PyEphem angles offer two ways to make this convenient:
a ``norm`` attribute that returns the angle
normalized to the interval [0, 2π)
and a ``znorm`` attribute that returns the angle
normalized to the interval (-π, π] centered on zero.

    >>> circle = 2 * math.pi

::

    >>> a = + fifteen_degrees
    >>> print a, a.norm, a.znorm
    15:00:00.0 15:00:00.0 15:00:00.0

::

    >>> a = - fifteen_degrees
    >>> print a, a.norm, a.znorm
    -15:00:00.0 345:00:00.0 -15:00:00.0

::

    >>> a = ephem.degrees(circle - fifteen_degrees)
    >>> print a, a.norm, a.znorm
    345:00:00.0 345:00:00.0 -15:00:00.0
    
::

    >>> a = ephem.degrees(circle + fifteen_degrees)
    >>> print a, a.norm, a.znorm
    375:00:00.0 15:00:00.0 15:00:00.0
    
::

    >>> a = ephem.degrees(- circle + fifteen_degrees)
    >>> print a, a.norm, a.znorm
    -345:00:00.0 15:00:00.0 15:00:00.0

::

    >>> a = ephem.degrees(- circle - fifteen_degrees)
    >>> print a, a.norm, a.znorm
    -375:00:00.0 345:00:00.0 -15:00:00.0

Note that you cannot instantiate a raw ``Angle``:

    >>> ephem.Angle()
    Traceback (most recent call last):
     ...
    TypeError: you can only create an ephem.Angle through ephem.degrees() or ephem.hours()
