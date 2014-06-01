===============================
Right Ascension and Declination
===============================

.. _XEphem: http://www.clearskyinstitute.com/xephem/

There are several different ways
of specifying the position of an object
against the background of stars and constellations,
so every PyEphem “body”,
whether a planet, comet, asteroid, or star,
returns three sets of coordinates when you ask it to compute its position.
Briefly, these are:

* ``a_ra``, ``a_dec`` — **Astrometric Geocentric Position**
  for the star atlas ``epoch`` you've specified
* ``g_ra``, ``g_dec`` — **Apparent Geocentric Position**
  for the epoch-of-date
* ``ra``, ``dec`` — **Apparent Topocentric Position**
  for the epoch-of-date

Actually, the third position,
the“Apparent Topocentric” position,
is only computed if you provide PyEphem with an ``Observer`` to work with.
If you provide only a date for ``compute()`` instead,
then ``ra`` and ``dec`` will have the same values as ``g_ra`` and ``g_dec``.
The Greek prefix *topo-* means *place*,
and a *topocentric* position reveals where a body will appear in the sky
when viewed from a particular *place* on the Earth's surface.

The names ``ra`` and ``dec`` are short for *right ascension*
and *declination*,
which serve as longitude and latitude for the sky,
telling us where admist the stars and constellations an object appears.
See any introduction to astronomy
if you need to learn how they are defined;
the description below describes how the three versions
of right ascension and declination returned by PyEphem differ.

How the three positions differ
==============================

The easiest way to define what each kind of coordinate means
is to trace how PyEphem computes a body's position,
and show how it generates each of the values in turn.
PyEphem performs its computations using routines from ``libastro``,
which contains the high-precision astronomy routines
used in the `XEphem`_ graphical astronomy application.

* To begin with,
  PyEphem figures out where both the body and the Earth are located
  for the exact date and time you have asked about,
  and then compares the two positions
  to work out both the body's distance from the Earth
  and also the direction in which it lies.

* For bodies in the Solar System,
  like planets, comets, and asteroids,
  PyEphem converts the distance from the Earth to the body
  into the *light travel time*
  that light from the body requires to reach us,
  and re-computes the object's position
  for that many minutes earlier than the actual date and time you specified.
  For example, as I write this, Jupiter is about 3,100 light-seconds,
  or more than 51 light-minutes,
  from the earth:

  >>> import ephem
  >>> j = ephem.Jupiter('2007/12/6')
  >>> print j.earth_distance * ephem.meters_per_au / ephem.c, "seconds"
  3098.61793563 seconds

  This means that we on Earth are not actually seeing Jupiter
  as it really is at this moment;
  instead, we are seeing an image of where Jupiter was 51 minutes ago.
  So if I ask PyEphem for Jupiter's position,
  it will begin by computing its location at this moment as a “first try”,
  will discover that Jupiter is currently 51 light-minutes away,
  and then will re-compute Jupiter's position for 51 minutes ago
  since that is the position at which we will actually see Jupiter.

* Having compensated for light-travel time,
  PyEphem now knows the “star-atlas position” of the body,
  and checks for which star-atlas ``epoch``
  you want coordinates expressed in —
  which is supplied by the ``epoch`` attribute
  if you passed an ``Observer`` to ``compute()``
  or by the ``epoch=`` keyword if you have merely passed a date.
  (Both default to the standard date ``2000/1/1.5``
  if you do not specify your own value).
  PyEphem takes a copy of the body's coordinates,
  performs *precession* to determine what those coordinates were called
  in the ``epoch`` you have chosen,
  and stores the result in:

  * ``a_ra`` and ``a_dec`` — the **Astrometric Geocentric Position**

* Next,
  PyEphem adjusts the body's position for *relativistic deflection*,
  which is the slight nudge that gravity
  gives to light that passes very close to the Sun.
  This only affects objects within about 10° of the Sun
  and which lie on the far side of it from the Earth.

* Next, PyEphem adjusts the body's position for *nutation*,
  which is really not an adjustment to the body's apparent location at all,
  but a correction for the fact that the platform from which we observe —
  the Earth —
  wobbles over the span of months and years.
  If you want to point a very accurate telescope at an object,
  then you have to account for this wobble in the Earth's pole.
  (Star atlas coordinates always ignore this,
  and pretend that the Earth's pole doesn't have this slight wobble,
  which is why the “Astrometric” coordinates above
  don't have to include this correction.)

* Next, PyEphem adjusts the body's position
  for the *aberration of light*,
  the fact that the motion of the Earth through space
  causes a slight slant to the light reaching us from other objects,
  in the same way that driving through rain or snow
  will make the precipitation look like it is coming down diagonally,
  from in front of you,
  instead of looking like it is coming straight down from overhead.
  (PyEphem skips this step for the Moon,
  since the Moon travels with the Earth through space.)

* Having made all of these adjustments,
  PyEphem is now confident that it knows
  the direction in which the object *appears* to lie from the Earth,
  so it stores the computed position in:

  * ``g_ra`` and ``g_dec`` — the **Apparent Geocentric Position**

* If you provided an ``Observer`` to the body's ``compute()`` method,
  then PyEphem has a few last steps to perform
  to determine where the objects appears from that specific location.
  Otherwise, if you only provided a date, then the computation stops here
  (and ``ra`` and ``dec``
  are given the same values as ``g_ra`` and ``g_dec``).

* The first adjustment that PyEphem makes
  based on the location of the ``Observer``
  is to correct for *parallax*.
  This is needed because all of the previous steps
  computed where the body lies
  when viewed from the location of the Earth itself in its orbit —
  that is, from the Earth's exact center,
  which is why the previous coordinate sets
  were all named “Geocentric”
  (the Greek prefix *geo-* means *Earth*).
  But someone on the Earth's surface
  is more than 6,300 kilometers away from the Earth's center,
  which will shift, very slightly, the position of Solar System bodies
  against the background of stars
  (and will move nearby bodies like the Moon,
  or an artificial Earth satellite, even more).
  The parallax correction adjusts for this.

* Finally,
  the very atmosphere through which we view the sky
  acts as a lens that displaces the positions of bodies
  when they get close to the horizon.
  PyEphem has to correct for this *refraction*
  both in order to give you a more accurate idea
  of where to point your telescope,
  and to be able to make correct predictions of rising and setting times.
  But doing this calculation accurately is difficult,
  because the atmosphere's optical properties vary
  depending both on its temperature
  and on the amount of moisture the air is holding!
  PyEphem does its best to estimate the result,
  using the ``Observer`` attributes ``temp`` and ``pressure``.
  These default to 25°C and 1010 millibar
  if you do not specify more specific values;
  set the ``pressure`` to zero
  if you want PyEphem to ignore the effects of atmospheric refraction.

* PyEphem is now done,
  and produces its final set of coordinates:

  * ``ra`` and ``dec`` — the **Apparent Topocentric Position**
  * ``alt`` and ``az`` — the same position, measured from the horizon

Note that no *precession* was applied
to either of the final two sets of coordinates,
but only to the first.
This means that only the “Astrometric” position
will correspond to the lines in your star atlas.
The other positions are what are called “epoch-of-date” coordinates,
and are measured
off of the orientation of the celestial pole and the celestial equator
for the very day of the observation itself.
