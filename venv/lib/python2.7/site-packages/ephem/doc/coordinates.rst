
==========================
Coordinate Transformations
==========================

This document describes how to use PyEphem
to convert between equatorial, ecliptic, and galactic coordinates,
and how to convert coordinates between different epochs.

Celestial bodies in PyEphem
can directly express their coordinates in only two ways;
you can ask for their equatorial position,
which provides a right ascension and a declination
relative to the Earth's equator and poles,
or you can ask where they stand in the sky above a particular observer,
which yields an azimuth and an altitude.
(There are actually several versions of the equatorial position available;
see the :doc:`radec` document for details.)

But PyEphem does support two other coordinate systems,
which differ by which great circle they use as the equator of the sky:

Ecliptic Coordinates
  This involves a pair of coordinates,
  *ecliptic longitude* and *ecliptic latitude*,
  which measure position from the ecliptic —
  the plane in which the earth orbits around the sun,
  and thus, approximately,
  the plane in which all of the major planets orbit.

Galactic Coordinates
  The *galactic longitude* and *galactic latitude* of an object
  measure its location from the tilted plane that our own galaxy,
  the Milky Way, makes across our sky.

As explained below,
the user can either simply ask for a body's coordinates
to be re-expressed in either of these alternate systems,
or can convert freely between the three main systems of coordinate
without getting bodies involved at all.

Summary of coordinate transforms
================================

Before wading into all of the specific examples below
which outline many different ways of using PyEphem's coordinate engine,
we should summarize the basic rules of coordinate handling.

* There are three coordinate classes,
  instances of which have three attributes:

  | ``Equatorial`` coordinates have ``ra`` right ascension,
    ``dec`` declination, and an ``epoch``.
  | ``Ecliptic`` coordinates have ``lon`` longitude,
    ``lat`` latitude, and an ``epoch``.
  | ``Galactic`` coordinates have ``lon`` longitude,
    ``lat`` latitude, and an ``epoch``.

* You can instantiate any kind of coordinate
  by passing it a body, or a body together with an alternate epoch,
  and it will use the body's astrometric right ascension and declination::

   Ecliptic(mars)
   Ecliptic(mars, epoch='1950')

* You can instantiate any kind of coordinate
  by passing it any other coordinate,
  and can optionally provide an alternate epoch::

   Galactic(north_pole)
   Galactic(north_pole, epoch='1900')

* Finally, you can instantiate a coordinate
  by simply providing its parts manually
  (in the same order as they are listed in the first point above).
  If you do not specify an epoch,
  then J2000 is assumed::

   Equatorial('23:19:01.27', '-17:14:22.1')
   Equatorial('23:19:01.27', '-17:14:22.1', epoch='1950')

* If you call the ``get()`` method of any coordinate,
  then it will return the value of its two angles in a tuple,
  with the “big angle” (longitude or right ascension) first
  and then the “small angle” (latitude or declination) second.

All of the examples below
are constructed using some combination of the possibilities above.

Common Operations
=================

**Convert right ascension and declination to a different epoch**
  If you have, say, the position of Mars in J2000 coordinates,
  and now want the same position to be expressed in B1950 coordinates,
  then you could, of course, simply call ``compute()`` again
  with the other epoch.
  But you can also ask PyEphem to translate the coordinates directly:

  >>> import ephem
  >>> m = ephem.Mars('2003/08/27', epoch=ephem.J2000)
  >>> print m.a_ra, m.a_dec
  22:39:06.87 -15:41:53.2
  >>> p = ephem.Equatorial(m, epoch=ephem.B1950)
  >>> print p.ra, p.dec
  22:36:26.49 -15:57:31.6

  You can also convert raw coordinates to another epoch
  rather than the position of a body like Mars.
  For example, we can ask where the point in the sky
  that we call the North Pole in J2000 coordinates
  was back in 2500 BC, when the pyramids were being built,
  by manually typing ninety degrees for the declination:

  >>> north_pole = ephem.Equatorial('0', '90', epoch=ephem.J2000)
  >>> ancient_pole = ephem.Equatorial(north_pole, epoch='-2500')
  >>> print ancient_pole.ra, ancient_pole.dec
  22:05:17.60 65:45:47.5

**Find the position of a body in galactic or ecliptic coordinates**
  Pass the body to the ``Ecliptic`` or ``Galactic`` class:

  >>> import ephem
  >>> m = ephem.Mars('1990/12/13')
  >>> print m.a_ra, m.a_dec
  3:51:20.54 22:12:49.4

  >>> ecl = ephem.Ecliptic(m)
  >>> print ecl.lon, ecl.lat
  60:27:09.2 2:00:47.5

  >>> gal = ephem.Galactic(m)
  >>> print gal.lon, gal.lat
  168:47:15.2 -24:14:01.8

  The epoch of the resulting coordinates
  is the same as that used by the body for its astrometric coordinates:

  >>> print ecl.epoch
  2000/1/1 12:00:00

**Using Another Right Ascension and Declination**
  In the first above example,
  when we passed a body directly to ``Ecliptic()`` and ``Galactic()``,
  they automatically used the body's
  astrometric right ascension and declination.
  If for some particular application
  you want to use the apparent version of the coordinates instead,
  then use the alternative right ascension and declination
  to build your own ``Equatorial`` object:

  >>> import ephem
  >>> m = ephem.Mars('1980/2/25')
  >>> ma = ephem.Equatorial(m.ra, m.dec, epoch='1980/2/25')
  >>> me = ephem.Ecliptic(ma)
  >>> print me.lon, me.lat
  155:52:22.4 4:22:08.7
