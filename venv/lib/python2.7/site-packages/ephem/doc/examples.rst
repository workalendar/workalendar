
Example Scripts
===============

Here are a few samples scripts
that show how to use PyEphem to perform simple tasks.

hale_bopp_ephemeris.py
----------------------

The following script prints out an ephemeris.

.. testcode::

 import ephem

 hb = ephem.readdb(
     'C/1995 O1 (Hale-Bopp),e,89.4245,282.4515,130.5641,183.6816,'
     '0.0003959,0.995026,0.1825,07/06.0/1998,2000,g -2.0,4.0'
     )

 here = ephem.Observer()
 here.lat, here.lon, here.elev = '33:45:10', '-84:23:37', 320.0

 print "Hale-Bopp: date, right ascension, declination, and magnitude:"

 here.date = ephem.date('1997/2/15')
 end = ephem.date('1997/5/15')
 while here.date < end:
     hb.compute(here)
     print here.date, hb.ra, hb.dec, hb.mag
     here.date += 5

.. testoutput::

    Hale-Bopp: date, right ascension, declination, and magnitude:
    1997/2/15 00:00:00 20:20:49.11 23:17:34.2 0.0
    1997/2/20 00:00:00 20:39:29.29 26:38:56.6 -0.31
    1997/2/25 00:00:00 21:01:27.07 30:15:40.6 -0.62
    1997/3/2 00:00:00 21:27:38.03 34:02:02.9 -0.92
    1997/3/7 00:00:00 21:59:04.35 37:47:03.6 -1.19
    1997/3/12 00:00:00 22:36:38.57 41:12:54.8 -1.42
    1997/3/17 00:00:00 23:20:28.94 43:55:38.2 -1.6
    1997/3/22 00:00:00 0:09:11.83 45:30:21.2 -1.72
    1997/3/27 00:00:00 0:59:34.63 45:41:07.9 -1.76
    1997/4/1 00:00:00 1:47:38.29 44:29:10.8 -1.74
    1997/4/6 00:00:00 2:30:23.60 42:11:38.0 -1.65
    1997/4/11 00:00:00 3:06:42.92 39:12:15.1 -1.5
    1997/4/16 00:00:00 3:36:55.11 35:52:30.5 -1.3
    1997/4/21 00:00:00 4:01:57.98 32:27:45.2 -1.06
    1997/4/26 00:00:00 4:22:55.70 29:07:19.0 -0.8
    1997/5/1 00:00:00 4:40:44.44 25:56:03.3 -0.52
    1997/5/6 00:00:00 4:56:08.73 22:55:55.0 -0.23
    1997/5/11 00:00:00 5:09:42.34 20:07:08.7 0.05

jovian_moon_chart.py
----------------------

This script prints out where the Jovian moons are around Jupiter
for the next few days.

.. testcode::

 import ephem

 moons = ((ephem.Io(), 'i'),
          (ephem.Europa(), 'e'),
          (ephem.Ganymede(), 'g'),
          (ephem.Callisto(), 'c'))

 # How to place discrete characters on a line that actually represents
 # the real numbers -maxradii to +maxradii.

 linelen = 65
 maxradii = 30.

 def put(line, character, radii):
     if abs(radii) > maxradii:
         return
     offset = radii / maxradii * (linelen - 1) / 2
     i = int(linelen / 2 + offset)
     line[i] = character

 interval = ephem.hour * 3
 now = ephem.now()
 now -= now % interval

 t = now
 while t < now + 2:
     line = [' '] * linelen
     put(line, 'J', 0)
     for moon, character in moons:
         moon.compute(t)
         put(line, character, moon.x)
     print str(ephem.date(t))[5:], ''.join(line).rstrip()
     t += interval

 print 'East is to the right;',
 print ', '.join([ '%s = %s' % (c, m.name) for m, c in moons ])

.. testoutput::

    3/2 12:00:00                         g e     J   i                    c
    3/2 15:00:00                        ge       J    i                    c
    3/2 18:00:00                      g e        J     i                   c
    3/2 21:00:00                     g e         J    i                    c
    3/3 00:00:00                    g  e         J  i                       c
    3/3 03:00:00                   g   e         Ji                         c
    3/3 06:00:00                  g    e       i J                          c
    3/3 09:00:00                  g     e   i    J                          c
    3/3 12:00:00                 g       e i     J                          c
    3/3 15:00:00                 g        ie     J                          c
    3/3 18:00:00                 g         i e   J                          c
    3/3 21:00:00                 g           i e J                          c
    3/4 00:00:00                 g             i e                          c
    3/4 03:00:00                  g              Jie                        c
    3/4 06:00:00                  g              J  ie                      c
    3/4 09:00:00                   g             J    ie                   c
    East is to the right; i = Io, e = Europa, g = Ganymede, c = Callisto
