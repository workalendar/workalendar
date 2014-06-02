
PyEphem Reference
=================

The official documentation.

.. class:: Observer

 .. attribute:: pressure

 The atmospheric pressure that you would like PyEphem to use when
 computing how much objects are refracted at the horizon, which makes
 them appear higher (and thus rise earlier, and set later) than they
 really are.  You can change the default value of 1010.0 millibar if you
 know that the weather where you will be observing will be different.

 If you set the pressure to zero, then you will turn off the PyEphem
 refraction routine entirely.  This will make calculations near the
 horizon slightly faster, and will return the altitude that objects
 would have if the Earth had no atmosphere and you could see straight
 into space.
