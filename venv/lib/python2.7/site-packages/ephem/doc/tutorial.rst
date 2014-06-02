====================
The PyEphem Tutorial
====================

Version 2007.November.1, for PyEphem version 3.7.2.2 and later.

The `PyEphem library`_ provides Python programmers
with access to the scientific-grade astronomical routines
used by the `XEphem`_ interactive astronomical ephemeris application;
its author, `Elwood Charles Downey`_, has generously granted permission
for PyEphem to be built upon his work.

After installing the module,
you can use it in Python with the statement:

.. _PyEphem library: http://rhodesmill.org/pyephem/
.. _XEphem: http://www.clearskyinstitute.com/xephem/
.. _Elwood Charles Downey: http://www.clearskyinstitute.com/resumes/ecdowney/resume.html

>>> import ephem

This tutorial assumes that you are familiar with astronomy,
but necessarily all of the issues surrounding astronomical calculation;
those who find its discussions tedious
will probably just want to read over its examples
to quickly familiarize themselves with how PyEphem works.

First Steps
-----------

PyEphem will compute the positions of celestial bodies on particular dates,
and can determine where in the sky they appear from any location on earth.

When using PyEphem,
you will usually create instances of the bodies that interest you,
compute their position for various dates and perhaps geographic locations,
and finally print or display the result.
For example,
to determine the location and brightness of Uranus
on the night it was discovered
we simply create a ``Uranus`` object
and ask where it was on the 13th of March, 1781:

>>> u = ephem.Uranus()
>>> u.compute('1781/3/13')
>>> print u.ra, u.dec, u.mag
5:35:45.28 23:32:54.1 5.6
>>> print ephem.constellation(u)
('Tau', 'Taurus')

Calling ``compute()`` sets many attributes of a body,
beyond the right ascension, declination, and magnitude printed here;
see the `Quick Reference`_
for other attributes that ``compute()`` sets.
You see that measurements are formatted as an astronomer would expect:
dates are expressed as year, month, and day, delimited by slashes;
right ascension as hours of arc around the celestial equator;
and declination as degrees north of the equator.
The colons between the components of an angle are a compromise —
the more traditional 21°46′15.66′′ is not possible
with the symbols on a standard computer keyboard.

.. _Quick Reference: quick

The code above created and used only one instance of ``Uranus``,
but you can also have several going at once.
For example,
to determine how close Neptune and Jupiter lay
as Galileo famously observed them —
he was busy watching the Jovian moons he had discovered two years earlier
and, though Neptune had moved overnight, he dismissed it as a background star
and left its discovery to wait another two hundred years —
we create one instance of each planet and compare their positions:

>>> j = ephem.Jupiter('1612/12/28')
>>> n = ephem.Neptune('1612/12/28')
>>> print j.ra, j.dec, j.mag
11:48:20.52 2:41:13.6 -1.96
>>> print n.ra, n.dec, n.mag
11:49:15.77 2:37:04.5 7.92
>>> print ephem.separation(j, n)
0:14:24.6

Notice that, while in our first example
we created our ``Uranus`` instance
and called its ``compute()`` method as two separate steps,
we have here taken the shortcut of providing dates
as we created each planet;
in general, any arguments you provide when creating a planet
are used to ``compute()`` its initial position.
The ``separation()`` function
computes the angle in degrees between two bodies,
as measured by their right ascension and declination.
In this case,
the separation of 0°14′
was small enough to place both planets in Galileo's field of view.

You can even create several instances of the same body.
Let's compare how far Mars moves in one day at perihelion versus aphelion,
and verify that its speed is greater when closer to the Sun:

>>> def hpos(body): return body.hlon, body.hlat
>>> ma0 = ephem.Mars('1976/05/21')    # ma: mars near aphelion
>>> ma1 = ephem.Mars('1976/05/22')
>>> print ephem.separation(hpos(ma0), hpos(ma1))
0:26:11.4
>>> mp0 = ephem.Mars('1975/06/13')    # mp: mars near perihelion
>>> mp1 = ephem.Mars('1975/06/14')
>>> print ephem.separation(hpos(mp0), hpos(mp1))
0:38:05.2

Here we wanted to measure the motion of Mars around the Sun,
but ``separation()`` normally compares
the right ascension and declination of two bodies —
which would measure the motion of Mars across the sky
of the moving platform of our earth.
So instead of giving ``separation()`` the Mars instances themselves,
we specifically provided
the heliocentric longitude and latitude of each instance,
revealing how far Mars moved around the Sun
regardless of how this motion appeared from earth.

In general ``separation()`` can measure the angle
between any pair of spherical coordinates,
so long as the elements of each coordinate are spherical longitude
(angle around the sphere)
followed by spherical latitude
(angle above or below its equator).
Each pair should be provided as a two-item sequence like a tuple or list.
Appropriate coordinate pairs include right ascension and declination;
heliocentric longitude and latitude;
azimuth and altitude;
and even the geographic longitude and latitude of two locations on earth.

Computing With Angles
---------------------

Sometimes you may want to perform computations with times and angles.
Strings like ``'7:45:45.15'`` are attractive when printed,
but cumbersome to add and multiply;
so PyEphem also makes times and angles available as floating-point numbers
for more convenient use in mathematical formulae.

All angles returned by PyEphem are actually measured in radians.
Let us return to our first example above,
and examine the results in more detail:

>>> u = ephem.Uranus('1871/3/13')
>>> print str(u.dec)
22:04:47.4
>>> print float(u.dec)
0.385365877213
>>> print u.dec + 1
1.38536587721

The rule is that angles become strings when printed or given to ``str()``,
but otherwise act like Python floating point numbers.
Note that the format operator ``%`` can return either value,
depending on whether you use ``%s`` or one of the numeric formats:

>>> print "as a string: %s, as a float: %f" % (u.dec, u.dec)
as a string: 22:04:47.4, as a float: 0.385366

As an example computation,
we can verify Kepler's Second Law of planetary motion —
that a line drawn from a planet to the sun
will sweep out equal areas over equal periods of time.
We have already computed two positions for Mars near its aphelion
that are one day apart
(and defined a helpful ``hpos()`` function; see above).
We can estimate the actual distance it moved in space that day
by multiplying its angular motion in radians by its distance from the Sun:

>>> aph_angle = ephem.separation(hpos(ma0), hpos(ma1))
>>> aph_distance = aph_angle * ma0.sun_distance
>>> print aph_distance
0.0126911122281

So, it moved nearly 0.013 AU in a single day (about 1.9 million kilometers).
A line drawn between it and the sun would have, roughly,
filled in a triangle whose base is 0.013 AU,
whose height is the distance to the Sun,
and whose area is therefore:

>>> aph_area = aph_distance * ma0.sun_distance / 2.
>>> print aph_area
0.0105710807908

According to Kepler our results should be the same
for any other one-day period for which we compute this;
we can try using the two Mars positions from near perihelion:

>>> peri_angle = ephem.separation(hpos(mp0), hpos(mp1))
>>> peri_distance = peri_angle * mp0.sun_distance
>>> peri_area = peri_distance * mp0.sun_distance / 2.
>>> print peri_area      # the area, to high precision, is the same!
0.0105712665517

Despite the fact that Mars moves twenty percent faster at perihelion,
the area swept out — to quite high precision — is identical,
just as Kepler predicted.
Some of the tiny difference between the two numbers we got
results from our having approximated sectors of its orbit as triangles;
the rest comes from the pertubations of other planets
and other small sources of irregularity in its motion.

When you use an angle in mathematical operations,
Python will return normal floats that lack the special power
of printing themselves as degrees or hours or arc.
To turn radian measures back into printable angles,
PyEphem supplies both a ``degrees()`` and an ``hours()`` function.
For example:

>>> print peri_angle * 2
0.0221584026149
>>> print ephem.degrees(peri_angle * 2)
1:16:10.5

You may find that your angle arithmetic often returns angles
that are less than zero or that exceed twice pi.
You can access the ``norm`` attribute of an angle
to force it into this range:

>>> deg = ephem.degrees
>>> print deg(deg('270') + deg('180'))
450:00:00.0
>>> print deg(deg('270') + deg('180')).norm
90:00:00.0

Computing With Dates
--------------------

PyEphem only processes and returns dates that are in Universal Time (UT),
which is simliar to Standard Time in Greenwich, England,
on the Earth's Prime Meridian.
If you need to display a PyEphem time in your own timezone,
use the ``localtime()`` function,
which returns a Python ``datetime`` object:

>>> d = ephem.Date('1984/12/21 15:00')
>>> ephem.localtime(d)
datetime.datetime(1984, 12, 21, 10, 0, 0, 4)
>>> print ephem.localtime(d).ctime()
Fri Dec 21 10:00:00 1984

As you can see from this result,
I am writing this *Tutorial* in the Eastern Time zone,
which in the winter is five hours earlier than the time in Greenwich.

PyEphem actually represents dates
as the number of days since noon on 1899 December 31.
While you will probably not find
the absolute value of this number very interesting,
the fact that it is counted in days
means you can move one day forward or backward
by adding or subtracting one.
The rules described above for angles hold for floats as well:
you can create them with ``ephem.Date()``,
but after doing arithmetic on them
you must pass them back through ``ephem.Date()``
to turn them back into dates:

>>> d = ephem.Date('1950/2/28')
>>> print d + 1
18321.5
>>> print ephem.Date(d + 1)
1950/3/1 00:00:00

The ``ephem`` module provides three constants
``hour``, ``minute``, and ``second``,
which can be added or subtracted from dates
to increment or decrement them by the desired amount.

You can specify dates in several formats;
not only can the strings that specify them
use either floating point days or provide hours, minutes, and seconds,
but you can also provide the components of the date in a tuple.
The following assignments are all equivalent:

>>> d = ephem.Date(34530.34375)
>>> d = ephem.Date('1994/7/16.84375')
>>> d = ephem.Date('1994/7/16 20:15')
>>> d = ephem.Date((1994, 7, 16.84375))
>>> d = ephem.Date((1994, 7, 16, 20, 15, 0))

And to complement the fact that you can specify dates as a tuple,
two methods are provided for extracting the date as a tuple:
``triple()`` returns a year, month, and floating point day,
while ``tuple()`` provides everything down to floating point seconds.
After any of the above calls,
the date can be examined as:

>>> print 'as a float: %f\nas a string: "%s"' % (d, d)
as a float: 34530.343750
as a string: "1994/7/16 20:15:00"
>>> print d.triple()
(1994, 7, 16.84375)
>>> print d.tuple()
(1994, 7, 16, 20, 15, 0.0)

Any PyEphem function argument that requires an angle or date
will accept any of the representations shown above;
so you could, for instance,
give a three-element tuple
directly to ``compute()`` for the date,
rather than having to pass the tuple through the
``Date()`` function before using it
(though the latter approach would also work).

Computations for Particular Observers
-------------------------------------

The examples so far have determined
the position of bodies against the background of stars,
and their location in the solar system.
But to observe a body we need to know more —
whether it is visible from our latitude,
when it rises and sets,
and the height it achieves above our horizon.
In return for this more detailed information,
PyEphem quite reasonably demands to know our position on the earth's surface;
we can provide this through an object called an ``Observer``:

>>> gatech = ephem.Observer()
>>> gatech.lon, gatech.lat = '-84.39733', '33.775867'

When the ``Observer`` is provided to ``compute()``
instead of a simple date and epoch,
PyEphem has enough information
to determine where in the sky the body appears.
Fill in the ``date`` and ``epoch`` fields of the ``Observer``
with the values you would otherwise provide to ``compute()``;
the epoch defaults to the year 2000 if you do not set it yourself.
As an example, we can examine the 1984 eclipse of the sun from Atlanta:

>>> gatech.date = '1984/5/30 16:22:56'   # 12:22:56 EDT
>>> sun, moon = ephem.Sun(), ephem.Moon()
>>> sun.compute(gatech)
>>> moon.compute(gatech)
>>> print sun.alt, sun.az
70:08:39.2 122:11:26.4
>>> print moon.alt, moon.az
70:08:39.5 122:11:26.0

For those unfamiliar with azimuth and altitude:
they describe position in the sky by measuring angle around the horizon,
then angle above the horizon.
To locate the Sun and Moon in this instance,
you would begin by facing north and then turn right 122°,
bringing you almost around to the southeast
(which lies 125° around the sky from north);
and by looking 70° above that point on the horizon —
fairly high, given that 90° is directly overhead —
you would find the Sun and Moon.

Eclipses are classified as *partial*
when the Moon merely takes a bite out of the Sun;
*annular*
when the Moon passes inside the disc of the sun
to leave only a brilliant ring (Latin *annulus*) visible;
and *total* when the moon is large enough to cover the Sun completely.
To classify this eclipse we must compare the size of the Sun and Moon
to the distance between them.
Since each argument to ``separation()``
can be an arbitrary measure of spherical longitude and latitude,
we can provide azimuth and altitude:

>>> print ephem.separation((sun.az, sun.alt), (moon.az, moon.alt))
0:00:00.3
>>> print sun.size, moon.size, sun.size - moon.size
1892.91210938 1891.85778809 1.05432128906

The Sun's diameter is larger by 1.05′′,
so placing the Moon at its center
would leave an annulus of width
1.05′′ / 2 = 0.52′′
visible around the Moon's edge.
But, in fact, the center of the Moon lies 0.48 arc seconds
towards one edge of the sun —
not enough to move its edge outside the sun and make a partial eclipse,
but enough to make a quite lopsided annular eclipse,
whose annulus is 0.52′′ + 0.48 = 1.00′′
wide on one side
and a scant 0.52′′ - 0.48 = 0.04′′ on the other.

The sky positions computed by PyEphem
take into account the refraction of the atmosphere,
which bends upwards the images of bodies near the horizon.
During sunset, for example, the descent of the sun appears to slow
because the atmosphere bends its image upwards as it approaches the horizon:

>>> gatech.date = '1984/5/31 00:00'   # 20:00 EDT
>>> sun.compute(gatech)
>>> for i in range(8):
...     old_az, old_alt = sun.az, sun.alt
...     gatech.date += ephem.minute * 5.
...     sun.compute(gatech)
...     sep = ephem.separation((old_az, old_alt), (sun.az, sun.alt))
...     print gatech.date, sun.alt, sep
1984/5/31 00:05:00 6:17:36.8 1:08:48.1
1984/5/31 00:10:00 5:21:15.6 1:08:36.3
1984/5/31 00:15:00 4:25:31.6 1:08:20.0
1984/5/31 00:20:00 3:30:34.2 1:07:56.5
1984/5/31 00:25:00 2:36:37.8 1:07:22.7
1984/5/31 00:30:00 1:44:04.6 1:06:32.2
1984/5/31 00:35:00 0:53:28.7 1:05:17.0
1984/5/31 00:40:00 0:05:37.8 1:03:28.3

We see that the Sun's apparent angular speed
indeed decreased as it approached the horizon,
from around 1°08′ to barely 1°03′ each five minutes.

Since atmospheric refraction varies with temperature and pressure,
you can improve the accuracy of PyEphem
by providing these values from a local forecast,
or at least from average values for your location and season.
By default an ``Observer`` uses 15°C and 1010 mB,
the values for these parameters at sea level
in the standard atmosphere model used in aviation.
Setting the pressure to zero
directs PyEphem to simply ignore atmospheric refraction.

Once PyEphem knows your location it can also work out
when bodies rise, cross your meridian, and set each day.
These computations can be fairly involved,
since planets continue their journey among the stars
even as the rotation of the earth brings them across the sky;
PyEphem has to internally re-compute their position several times
before it finds the exact circumstances of rising or setting.
But this is taken care of automatically,
leaving you to simply ask:

>>> print gatech.next_setting(sun)
1984/5/31 00:42:21
>>> print sun.alt, sun.az
-0:15:46.4 297:20:44.3

Functions also exist for finding risings, transits, and —
just for completeness —
the moment of “anti-transit” when the object lies along the meridian
directly under your feet.
See the section on `transit, rising, and setting`_
in the Quick Reference for more details.

.. _transit, rising, and setting: quick#transit-rising-setting

Loading Bodies From Catalogues
------------------------------

So far we have dealt with the planets, the Sun, and the Moon —
major bodies whose orbits PyEphem already knows in great detail.
But for minor bodies, like comets and asteroids,
you must aquire and load the orbital parameters yourself.

Understand that because the major planets constantly perturb
the other bodies in the solar system, including each other,
it requires great effort —
years of observation yielding formulae with dozens or hundreds of terms —
to predict the position of a body accurately over decades or centuries.
For a comet or asteroid,
astronomers find it more convenient
to describe its orbit as perfect ellipse, parabola, or hyperbola,
and then issue new orbital parameters as its orbit changes.

The PyEphem home page provides links to several
`online catalogs`_ of orbital elements.
Once you have obtained elements for a particular body,
simply provide them to PyEphem's ``readdb()`` function
in `ephem database format`_ and the resulting object is ready to use:

>>> yh = ephem.readdb("C/2002 Y1 (Juels-Holvorcem),e,103.7816," +
...    "166.2194,128.8232,242.5695,0.0002609,0.99705756,0.0000," +
...    "04/13.2508/2003,2000,g  6.5,4.0")
>>> yh.compute('2003/4/11')
>>> print yh.name
C/2002 Y1 (Juels-Holvorcem)
>>> print yh.ra, yh.dec
0:22:44.58 26:49:48.1
>>> print ephem.constellation(yh), yh.mag
('And', 'Andromeda') 5.96

.. _online catalogs: http://rhodesmill.org/pyephem/catalogs
.. _ephem database format: http://www.clearskyinstitute.com/xephem/help/xephem.html#mozTocId468501

(Unfortunately, the library upon which PyEphem is build
truncates object names to twenty characters, as you can see.)
Each call to ``readdb()`` returns an object appropriate
for the orbit specified in the database entry;
in this case it has returned an ``EllipticalBody``:

>>> print yh # doctest: +ELLIPSIS
<ephem.EllipticalBody 'C/2002 Y1 (Juels-Holvorcem)' at 0x...>

For objects for which you cannot find an entry in ephem database format,
you can always create the appropriate kind of object
and then fill in its orbital parameters yourself;
see the `Quick Reference`_ for their names and meanings.
By calling the ``writedb()`` function of a PyEphem object,
you can even get it to generate its own database entry
for archiving or distribution.

.. _Quick Reference: quick

There is one other database format with which PyEphem is familiar:
the NORAD Two-Line Element format (TLE) used for earth satellites.
Here are some recent elements for the International Space Station.

>>> iss = ephem.readtle("ISS (ZARYA)",
...  "1 25544U 98067A   03097.78853147  .00021906  00000-0  28403-3 0  8652",
...  "2 25544  51.6361  13.7980 0004256  35.6671  59.2566 15.58778559250029")
>>> gatech.date = '2003/3/23'
>>> iss.compute(gatech)
>>> print iss.rise_time, iss.transit_time, iss.set_time
2003/3/23 00:00:44 2003/3/23 00:03:22 2003/3/23 00:06:00

Note that earth satellites are fast movers —
in this case rising and setting in less than six minutes!
They can therefore have multiple risings and settings each day,
and the particular ones you get from ``rise_time`` and ``set_time``
depend on the particular time of day for which you ask.
Repeating the above query eight hours later gives complete different results:

>>> gatech.date = '2003/3/23 8:00'
>>> iss.compute(gatech)
>>> print iss.rise_time, iss.transit_time, iss.set_time
2003/3/23 08:03:41 2003/3/23 08:08:29 2003/3/23 08:13:16

When calling ``compute()`` for an earth satellite
you should provide an ``Observer``,
and not simply a date and epoch,
since its location is entirely dependent
upon the location from which you are observing.
PyEphem provides extra information about earth satellites,
beyond the ones available for other objects;
again, see the `Quick Reference`_ for details.

.. _Quick Reference: quick

Fixed Objects, Precession, and Epochs
-------------------------------------

The simplest kind of object to create from a catalog entry
are *fixed* objects,
for which a constant right ascension and declination are specified.
These include stars, nebulae, global clusters, and galaxies.
One example is Polaris, the North Star,
which lies at the end of Ursa Minor's tail:

>>> polaris = ephem.readdb("Polaris,f|M|F7,2:31:48.704,89:15:50.72,2.02,2000")
>>> print polaris.dec
Traceback (most recent call last):
 ...
RuntimeError: field dec undefined until first compute()

We are able to create the object successfully —
why should asking its position raise a runtime error?
The reason is that fixed objects, like planets,
have an undefined position and magnitude
until you call their ``compute()`` method
to determine their position for a particular date or ``Observer``:

>>> polaris.compute()    # uses the current time by default
>>> print polaris.a_dec
89:15:50.7
>>> print ephem.degrees(ephem.degrees('90') - polaris.a_dec)
0:44:09.3

Much better; we see that the `North Star` lies
less than forty-five arc minutes from the pole.
But why should we have to call ``compute()``
for something fixed —
something whose position is considered permanent,
and which should not move between one date and another?

The reason is that, while `fixed` stars and nebulae
are indeed nearly motionless over the span of human civilization,
the coordinate system by which we designate their positions
changes more rapidly.
Right ascension and declination are based
upon the orientation of the earth's pole —
but it turns out that the pole slowly revolves
(around the axis of the ecliptic plane)
like the axis of a whirling top,
completing each revolution in roughly 25,800 years.
This motion is called *precession*.
Because this makes the entire coordinate system shift slightly every year,
is not sufficient to state that Polaris lies at
2h31m right ascension and 89:15° declination;
you have to say in *which year*.

That is why the Polaris entry above ends with ``2000``;
this gives the year for which the coordinates are correct,
called the *epoch* of the coordinates.
Because the year 2000 is currently a very popular epoch
for quoting positions and orbital parameters,
``compute()`` uses it by default;
but we can provide an ``epoch=`` keyword parameter
to have the coordinates translated into those for another year:

>>> polaris.compute(epoch='2100')
>>> print polaris.a_dec
89:32:26.1

Thus we see that in another hundred years Polaris
will actually lie closer to the pole that it does today.
(The ``'2100'`` is the same year/month/day format you have seen already,
missing both its month and day
because we are not bothering to be that specific.)
If you enter subsequent years you will find
that 2100 is very nearly the closest approach of the pole to Polaris,
and that soon afterwards they move apart.
For much of the twenty-five thousand year journey the pole makes,
there are no stars very near;
we may have been lucky to have held the Age of Exploration
as the pole was approaching as convenient a star as Polaris.

Today a dim star in Draco named Thuban
lies more than twenty degrees from the pole:

>>> thuban = ephem.readdb("Thuban,f|V|A0,14:4:23.3,64:22:33,3.65,2000")
>>> thuban.compute()
>>> print thuban.a_dec
64:22:33.0

But in 2801 BC, as the Egyptians built the pyramids,
Thuban served as their pole star,
while Polaris lay further from their pole than Thuban lies from ours today:

>>> thuban.compute(epoch='-2800')
>>> print thuban.a_dec
89:54:35.0
>>> polaris.compute(epoch='-2800')
>>> print polaris.a_dec
63:33:17.6

Realize that in these examples I have been lazy
by giving ``compute()`` an epoch without an actual date,
which requests the *current* position of each star
in the coordinates of another epoch.
This makes no difference for these fixed objects,
since their positions never change;
but when dealing with moving objects
one must always keep in mind the difference
between the date for which you want their position computed,
and the epoch in which you want those coordinates expressed.
Here are some example ``compute()`` calls,
beginning with one like the above but for a moving object:

``halley.compute(epoch='1066')``
 This is probably useless:
 it computes the current position of ``halley``,
 but returns coordinates relative
 to the direction the earth's axis was pointing in the year 1066.
 Unless you use a Conquest-era star atlas, this is not useful.

``halley.compute('1066', epoch='1066')``
 This is slightly more promising:
 it computes the position of ``halley`` in 1066
 and returns coordinates for the orientation of the earth in that year.
 This might help you visualize
 how the object was positioned above contemporary observers,
 who considered it an ill omen in the imminent conflict
 between King Harold of England and William the Bastard.
 But to plot this position against a background of stars,
 you would first have to recompute each star's position in 1066 coordinates.

``halley.compute('1066')``
 This is what you will probably use most often;
 you get the position of ``halley`` in the year 1066
 but expressed in the 2000 coordinates that your star atlas probably uses.

When planning to observe with an equatorial telescope,
you may want to use the current date as your epoch,
because the rotation of the sky above your telescope
is determined by where the pole points today,
not where it pointed in 2000 or some other convenient epoch.
Computing positions in the epoch of their date
is accomplished by simply providing the same argument for both date and epoch:

>>> j = ephem.Jupiter()
>>> j.compute(epoch=ephem.now())   # so both date and epoch are now
>>> print j.a_ra, j.a_dec # doctest: +SKIP
8:44:29.49 19:00:10.23
>>> j.compute('2003/3/25', epoch='2003/3/25')
>>> print j.a_ra, j.a_dec
8:43:32.82 19:03:32.5

Be careful when computing distances;
comparing two positions in the coordinates of their own epochs
will give slightly different results
than if the two were based on the same epoch:

>>> j1, j2 = ephem.Jupiter(), ephem.Jupiter()
>>> j1.compute('2003/3/1')
>>> j2.compute('2003/4/1')
>>> print ephem.separation(
...     (j1.a_ra, j1.a_dec),
...     (j2.a_ra, j2.a_dec))    # coordinates are both epoch 2000
1:46:35.9
>>> j1.compute('2003/3/1', '2003/3/1')
>>> j2.compute('2003/4/1', '2003/4/1')
>>> print ephem.separation(
...     (j1.a_ra, j1.a_dec),
...     (j2.a_ra, j2.a_dec))    # coordinates are both epoch-of-date
1:46:31.6

Comparing coordinates of the same epoch, as in the first call above,
measures motion against the background of stars;
comparing coordinates from different epochs, as in the second call,
measures motion against the slowly shifting coordinate system of the earth.
Users are most often interested in the first kind of measurement,
and stick with a single epoch the whole way through a computation.

It was for the sake of simplicity
that all of the examples in this section
simply provided dates as arguments to the ``compute()`` function.
If you are instead using an ``Observer`` argument,
then you specify the epoch through the observer's ``epoch`` variable,
not through the ``epoch=`` argument.
Observers use epoch 2000 by default.

Finally,
make sure you understand
that your choice of epoch only affects absolute position —
the right ascension and declination returned for objects —
*not* the azimuth and altitude of an object above an observer.
This is because the sun will hang in the same position over Atlanta
whether the star atlas with which you plot its position
has epoch 2000, or 1950, or even 1066 coordinates;
the epoch only affects how you name locations in the sky,
not how they are positioned with respect to you.
