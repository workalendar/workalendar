PyEphem CHANGELOG
=================

Version 3.7.5.2 (2013 December 21)
----------------------------------

- The ``separation()`` function will no longer allow hardware floating
  point rounding errors to produce a non-zero result when a position is
  compared to itself, nor return a ``NaN`` result (which one user
  reports seeing as the angle ``1389660529:33:00.8`` degrees).
  `(GitHub #31) <https://github.com/brandon-rhodes/pyephem/issues/31>`_

- PyEphem routines no longer ignore the microseconds of ``datetime``
  objects provided as input.
  `(GitHub #29) <https://github.com/brandon-rhodes/pyephem/issues/29>`_

- PyEphem is now more careful to raise an exception if angles are
  specified using strings that contain invalid characters.

- The Earth-satellite attributes ``ra`` and ``dec`` are now correctly
  referenced to the epoch-of-date, instead of being expressed in J2000
  like the astrometric attributes.

Version 3.7.5.1 (2011 November 24)
----------------------------------

- Upgraded the underlying astronomy library to 3.7.5.

- **Incompatible Change**: the transit functions are now symmetric with
  the rising and setting functions: while they still return the date and
  time of the event, they do *not* alter the ``.date`` attribute of the
  Observer which gets passed to them.  This brings their behavior into
  line with the documentation.
  `(Launchpad #861526) <https://bugs.launchpad.net/pyephem/+bug/861526>`_

- ``Date('1986-2-9')`` now means February 9th instead of meaning “the
  beginning of 1986, minus two months, minus nine days.”
  `(Launchpad #792321) <https://bugs.launchpad.net/pyephem/+bug/792321>`_

- Earth satellite positions are now computed to six additional digits,
  in an attempt to eliminate small jumps in position that some users
  were observing in their figures.
  `(Launchpad #812906) <https://bugs.launchpad.net/pyephem/+bug/812906>`_

- Coordinate pair creation no longer leaks memory.
  `(Launchpad #798155) <https://bugs.launchpad.net/pyephem/+bug/798155>`_

Version 3.7.4.1 (2011 January 5)
---------------------------------

- Renamed the ``Observer.long`` attribute to ``lon`` after realizing
  that the official syllabification of “longitude” is “lon·gi·tude.”
  Also changed ``Body`` objects so that ``hlong`` is ``hlon`` instead.
  The old names will always be supported for compatibility with older
  programs.

- Upgraded the underlying astronomy library to 3.7.4.

- **Bugfix:** repaired the ``separation()`` function so that it no
  longer leaks memory; thanks to Enno Middelburg for the bug report!

- **Bugfix:** completely rebuilt the geographic data used by ``city()``
  after Giacomo Boffi pointed out several errors.

Version 3.7.3.4 (2009 April 30)
-------------------------------

- Added a new ``next_pass()`` method to ``Observer`` that searches for
  when a satellite next rises, culminates, and sets.

- Added a ``compute_pressure()`` method to ``Observer`` which computes
  the standard atmospheric pressure at the observer's current elevation.
  This function now gets called automatically on new ``city()`` objects
  before they are returned to the user.

- Corrected the altitude of San Francisco as returned by ``city()``.

- Improved the copyright message so that two more authors are credited.

Version 3.7.3.3 (2008 October 3)
--------------------------------

- Added ``cmsI`` and ``cmsII`` attributes to ``Jupiter`` to provide the
  central meridian longitude in both System I and System II.

- **Bugfix**: Saturn was returning the wrong values for its earthward
  and sunward angle tilt.

Version 3.7.3.2 (2008 July 2)
-----------------------------

- **Bugfix**: the rising and setting functions, if called repeatedly,
  would sometimes get hung up on a single answer which they would return
  over and over again instead of progressing to the next rising or
  setting.  They should now always progress instead of getting stuck.

Version 3.7.3.1 (2008 July 1)
-----------------------------

- **Bugfix**: the rising and setting functions were attempting to
  achieve such high precision that users sometimes found circumstances
  under which they would not complete at all!  They now stop and return
  an answer once they are withing a half-second of the real time of
  rising, transit, or setting, which solves the problem without damaging
  the quality of the results when tested against the Naval Observatory.

- Upgraded to the libastro from XEphem 3.7.3.

Version 3.7.2.4 (2008 June 12)
------------------------------

- **Incompatible Change**: After feedback from users, I have changed
  the ``Observer`` methods which find risings, settings, and transits,
  so that they do not change their Observer's ``.date`` attribute.  So
  the sequence:

  .. code-block:: python

     r1 = boston.next_rising(mars)
     r2 = boston.next_rising(mars)

  now computes the same value twice!  If you want a series of calls to
  each begin when the other left off, you can use the ``start=``
  parameter described in the next item:

  .. code-block:: python

     r1 = boston.next_rising(mars)
     r2 = boston.next_rising(mars, start=r1)

- Added an optional ``start=`` argument to the rising, setting, and
  transit ``Observer`` functions, that tells them from which date and
  time to begin their search.

- **Bugfix**: Rewrote planetary moon routines so that moons of Mars,
  Jupiter, Saturn, and Uranus now return appropriate data for years
  1999-2020.  (Each moon had been returning the unmodified position of
  its planet, because I was unsure whether I could distribute the moon
  data with PyEphem.)

- You can no longer create arbitrary attributes on an ``Observer``, to
  prevent users from accidentially saying things like
  ``here.longitude`` or ``here.lon`` when they mean ``here.long``.
  Create your own subclass of ``Observer`` if you need the power to
  set your own attributes.

- The ephem module now provides a ``__version__`` symbol.

- Added test suite that tests planet and planet moon positions
  against JPL ephemeris data (needs more work).

Version 3.7.2.3 (2008 January 8)
--------------------------------

- Three new classes ``Equatorial``, ``Ecliptic``, and ``Galactic``
  allow coordinates to be transformed between the three systems
  (ability to transform coordinates was requested by Aaron Parsons).

- Added constants for popular epochs ``B1900``, ``B1950``, and
  ``J2000``.

- Added named functions for every solstice and equinox (before, only
  the vernal equinox could be asked for specifically).

- Product tests have been moved inside of the ``ephem`` module itself,
  and can now be invoked simply by running:

  .. code-block:: bash

     $ python setup.py test

- **Bugfix**: ``Angle()`` can no longer be directly instantiated.

- **Bugfix**: San Francisco had the wrong coordinates in the cities
  database (pointed out by Randolph Bentson).

Version 3.7.2.2 (2007 December 9)
---------------------------------

- The phases of the moon can now be determined through the functions
  ``next_new_moon()``, ``next_full_moon()``, ``previous_new_moon()``,
  et cetera.

- Added a modest database of world cities; the ``city()`` function
  returns a new Observer on each call:

  .. code-block:: python

     observer = ephem.city('Boston')

- Using the old ``rise``, ``set``, and ``transit`` attributes on
  ``Body`` objects now causes a deprecation warning.

- **Bugfix**: the last release of PyEphem omitted the constants
  ``meters_per_au``, ``earth_radius``, ``moon_radius``, and
  ``sun_radius``; the constant ``c`` (the speed of light) is also now
  available.

Version 3.7.2.1 (2007 October 1)
--------------------------------

- Functions now exist to find equinoxes and solstices.

- Bodies now cleanly offer three different versions of their
  position, rather than making the user remember obscure rules for
  having each of these three values computed:

  * Astrometric geocetric right ascension and declination
  * Apparent geocentric right ascension and declination
  * Apparent topocentric right ascension and declination

- Bodies can now find their next or previous times of transit,
  anti-transit, rising, and setting.

- A ``localtime()`` function can convert PyEphem ``Date`` objects to
  local time.

- Now ``ephem.angle`` instances can survive unary ``+`` and ``-``
  without getting changed into plain floats.

- The ``elev`` Observer attribute has been renamed to ``elevation``.

- Observers now display useful information when printed.

- Added a much more extensive test suite, which, among other things,
  now compares results with the United States Naval Observatory,
  insisting upon arcsecond agreement.

- **Bugfix**: When a fixed body is repeatedly precessed to different
  dates, its original position will no longer accumulate error.

Version 3.7.2a (2007 June)
--------------------------

- Upgraded to the libastro from XEphem 3.7.2.

- Should now compile under Windows!

- **Bugfix**: rewrote date-and-time parsing to avoid the use of
  ``sscanf()``, which was breaking under Windows and requiring the
  insertion of a leading space to succeed.

- Improved the error returned when a date string cannot be parsed,
  so that it now quotes the objectionable string (so you can tell
  which of several date strings on the same line gave an error!).

Version 3.7b  (2005 August 25)
------------------------------

- **Bugfix**: in the underlying library, earth satellite objects do
  not support ``SOLSYS`` attributes like ``sun_distance``; so
  ``EarthSatellite`` must inherit from ``Body`` rather than ``Planet``
  (and lose several attributes, which were returning nonsense values).

Version 3.7a  (2005 August 22)
------------------------------

- Upgraded to the libastro from XEphem 3.7.

- **Bugfix**: after creating an earth satellite and calling
  ``compute()``, some attributes (including ``sublat`` and
  ``sublong``) would always equal zero until you had accessed a more
  mainstream attribute (like ``ra`` or ``dec``); now, all attributes
  should return correct values on their first access.

- **Bugfix**: the ``sidereal_time()`` function of an ``Observer`` now
  returns a correct floating-point number that measures in radians,
  rather than a number in the range [0,1).

- The ``Observer`` now has an ``radec_of(az=, alt=)`` function that
  returns the right ascension and declination of a point in the sky.

- You can normalize an ``Angle`` into the range [0,2pi) by requesting
  the attribute ``.norm``.

- Earth satellite objects read in from TLE files now retain their
  TLE catalog number as an attribute ``catalog_number``.

- Uninitialized bodies now start off with ``None`` for their name,
  rather than the string ``"unnamed"``.

Version 3.6.4a  (2005 July 18)
------------------------------

- Upgraded to the libastro from XEphem 3.6.4, which:

  * No longer incorrectly applies relativistic deflection to
    objects on this side of the Sun, whose light will obviously not
    go past the sun and be deflected.

  * Now correctly handles earth satellites with a negative
    ``es_decay`` parameter.

- Added several functions to the module:

  * ``moon_phases()`` computes a new and full moon following a date.

  * ``delta_t()`` computes the difference between Terrestrial Time and
    Universal Time.

  * ``julian_date()`` computes the Julian Date for a ``date`` or
    ``Observer``.

  * ``millennium_atlas()`` and
    ``uranometria()`` and
    ``uranometria2000()`` determine the star atlas page on which a
    given location falls, given as right ascension and declination.

- Added a function to the Observer class, which takes no arguments:

  ``sidereal_time()`` computes the sidereal time for the Observer

- Each ``Observer`` now has a ``horizon`` attribute, with which you
  can specify the degrees altitude at which you define an object to be
  rising or setting.  Normally, all rising and setting times are
  computed for when the object appears to be exactly at the horizon
  (at zero degrees altitude).

Version 3.6.1a  (2004 November 25)
----------------------------------

- All major moons in the solar system are now supported.

- Added ``copy()`` method to bodies, that returns a new instance of
  the body which should be identical in all properties.

- Improved the definitions of body attributes, both in their
  docstrings and in the PyEphem Manual.

- Improved access to the orbital parameters by which the user
  defines bodies in ellipical, parabolic, and hyperbolic orbits, as
  well as artificial Earth satellites; users can now create such
  objects entirely through setting their parameters, without having
  to use the ``readdb()`` function to parse a definition of the object
  in Ephem database format.

- Source distribution now includes test suites, one of which
  actually checks to see whether your version of PyEphem produces
  the same output as the examples from the PyEphem Manual (two of
  which will fail).

- Following the same adjustment in the XEphem application, PyEphem
  now uses a default atmospheric pressure of 1010 millibar, rather
  than the old value of 1013, when computing the altitude of a body
  near the horizon.

- The ``constellation()`` function now correctly forces the
  computation of a body's ``ra`` and ``dec`` before determining the
  constellation in which the body lies.

- Code should produce cleaner compiles on many platforms.
