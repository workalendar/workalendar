
Rising, Transit, Setting
========================

Temperature and pressure; set to 0 to turn off

    >>> import ephem

Altitude you ask for

Naval Observatory Risings and Settings
--------------------------------------

One of the most famous and reliable sources of astronomical almanacs is
the United States Naval Observatory.  Ship captains were amongst the
earliest consumers of precision celestial data, since on the wide and
featureless expanses of the world's oceans you can often deduce your
position only by comparing the altitude of the stars and Sun and Moon
against the time given by the ship's clock.

If you want to compute rising and setting times that match the ones
given by the Navy in their *Astronomical Almanac*, then turn off
PyEphem's native mechanism for computing atmospheric refraction near the
horizon.  As explained above, you can do this simply by setting the
:attr:`~Observer.pressure` of your observer to zero.  Then, manually set
the horizon that you want to use to one that is exactly 34 arcminutes
lower than the normal horizon, to match the value by which the Navy
reckons that an object at the horizon is refracted:

    >>> atlanta = ephem.Observer()
    >>> atlanta.pressure = 0
    >>> atlanta.horizon = '-0:34'

Let's see if these values work!  Here are the rising and setting times
for the Sun and Moon in Atlanta today, as returned by the USNO web
site::

        Sunday
        6 September 2009      Eastern Daylight Time

                         SUN
        Begin civil twilight       6:50 a.m.
        Sunrise                    7:15 a.m.
        Sun transit                1:36 p.m.
        Sunset                     7:56 p.m.
        End civil twilight         8:21 p.m.

                         MOON
        Moonrise                   8:17 p.m. on preceding day
        Moon transit               2:37 a.m.
        Moonset                    9:05 a.m.
        Moonrise                   8:44 p.m.
        Moonset                   10:05 a.m. on following day

To get the same results, we simply need to use the Navy's longitude and
latitude for Atlanta (which their web page helpfully printed atop the
printout shown above) with the :class:`Observer` that we constructed
above with the correct pressure and horizon settings:

    >>> atlanta.lat, atlanta.lon = '33.8', '-84.4'
    >>> atlanta.date = '2009/09/06 17:00' # noon EST
    >>> print atlanta.previous_rising(ephem.Sun())
    2009/9/6 11:14:56
    >>> print atlanta.next_setting(ephem.Sun())
    2009/9/6 23:56:09
    >>> print atlanta.previous_rising(ephem.Moon())
    2009/9/6 00:16:31
    >>> print atlanta.next_setting(ephem.Moon())
    2009/9/7 14:05:29

As you can see, these values, given in Universal Time, match quite
precisely the USNO values given above in Eastern Daylight Time (which,
as you can see, runs four hours earlier).  So, simply use these settings
whenever you want your results to match those of the Navy.

Computing Twilight
------------------

You will note that the Navy printout in the previous section contains
another kind of information, besides simple risings and settings: it
specifies the beginning and end of *twilight*, which is the time during
the morning and evening when there is light but the Sun is still below
the horizon.

To compute the beginning and end of twilight, ask when the Sun reaches a
position several degrees below the horizon.  There are different horizon
values you should use depending on which twilight (civil, nautical, or
astronomical) you are interested in:

* Civil twilight uses the value –6 degrees.
* Nautical twilight uses the value –12 degrees.
* Astronomical twilight uses the value –18 degrees.

Note, however, that these twilight definitions specify the position of
the *center* of the Sun, while the rising and setting functions normally
pay attention to the top edge of an object instead.  To make them use
the Sun's center, simply set the ``use_center`` parameter to ``True``
when doing the calculation.  For example, here is how you would use the
:class:`Observer` created in the section above to calculate the civil
twilight in Atlanta:

    >>> atlanta.horizon = '-6'
    >>> print atlanta.previous_rising(ephem.Sun(), use_center=True)
    2009/9/6 10:49:40
    >>> print atlanta.next_setting(ephem.Sun(), use_center=True)
    2009/9/7 00:21:22

As you can see, these values match quite precisely the times given in
the table in the previous section for civil twilight.
