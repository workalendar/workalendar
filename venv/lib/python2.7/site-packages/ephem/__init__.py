# The core functionalty of PyEphem lives in the C-language _libastro
# module, which packages the astronomy routines from XEphem as
# convenient Python types.

import ephem._libastro as _libastro
from math import pi

__version__ = '3.7.5.2'

twopi = pi * 2.
halfpi = pi / 2.
quarterpi = pi / 4.
eighthpi = pi / 8.

degree = twopi / 360.
arcminute = degree / 60.
arcsecond = arcminute / 60.
half_arcsecond = arcsecond / 2.
tiny = arcsecond / 360.

c = 299792458.  # exact speed of light in meters/second
meters_per_au = _libastro.meters_per_au
earth_radius = _libastro.earth_radius
moon_radius = _libastro.moon_radius
sun_radius = _libastro.sun_radius

B1900 = 2415020.3135 - _libastro.MJD0
B1950 = 2433282.4235 - _libastro.MJD0
J2000 = _libastro.J2000

# We make available several basic types from _libastro.

Angle = _libastro.Angle
degrees = _libastro.degrees
hours = _libastro.hours

Date = _libastro.Date
hour = 1. / 24.
minute = hour / 60.
second = minute / 60.

default_newton_precision = second / 10.

delta_t = _libastro.delta_t
julian_date = _libastro.julian_date

Body = _libastro.Body
Planet = _libastro.Planet
PlanetMoon = _libastro.PlanetMoon
FixedBody = _libastro.FixedBody
EllipticalBody = _libastro.EllipticalBody
ParabolicBody = _libastro.ParabolicBody
HyperbolicBody = _libastro.HyperbolicBody
EarthSatellite = _libastro.EarthSatellite

readdb = _libastro.readdb
readtle = _libastro.readtle
constellation = _libastro.constellation
separation = _libastro.separation
now = _libastro.now

millennium_atlas = _libastro.millennium_atlas
uranometria = _libastro.uranometria
uranometria2000 = _libastro.uranometria2000

# We also create a Python class ("Mercury", "Venus", etcetera) for
# each planet and moon for which _libastro offers specific algorithms.

for index, classname, name in _libastro.builtin_planets():
    exec '''
class %(name)s(_libastro.%(classname)s):
    "Create a Body instance representing %(name)s"
    __planet__ = %(index)r
''' % dict(name=name, classname=classname, index=index)

del index, classname, name

# We now replace two of the classes we have just created, because
# _libastro actually provides separate types for two of the bodies.

Jupiter = _libastro.Jupiter
Saturn = _libastro.Saturn
Moon = _libastro.Moon

# Newton's method.

def newton(f, x0, x1, precision=default_newton_precision):
    """Return an x-value at which the given function reaches zero.

    Stops and declares victory once the x-value is within ``precision``
    of the solution, which defaults to a half-second of clock time.

    """
    f0, f1 = f(x0), f(x1)
    while f1 and abs(x1 - x0) > precision and f1 != f0:
        x0, x1 = x1, x1 + (x1 - x0) / (f0/f1 - 1)
        f0, f1 = f1, f(x1)
    return x1

# Find equinoxes and solstices.

_sun = Sun()                    # used for computing equinoxes

def holiday(d0, motion, offset):
    """Function that assists the finding of equinoxes and solstices."""

    def f(d):
        _sun.compute(d)
        return (_sun.ra + eighthpi) % quarterpi - eighthpi
    d0 = Date(d0)
    _sun.compute(d0)
    angle_to_cover = motion - (_sun.ra + offset) % motion
    if abs(angle_to_cover) < tiny:
        angle_to_cover = motion
    d = d0 + 365.25 * angle_to_cover / twopi
    return date(newton(f, d, d + hour))

def previous_vernal_equinox(date):
    """Return the date of the previous vernal equinox."""
    return holiday(date, -twopi, 0)

def next_vernal_equinox(date):
    """Return the date of the next vernal equinox."""
    return holiday(date, twopi, 0)

def previous_summer_solstice(date):
    """Return the date of the previous summer solstice."""
    return holiday(date, -twopi, pi + halfpi)

def next_summer_solstice(date):
    """Return the date of the next summer solstice."""
    return holiday(date, twopi, pi + halfpi)

def previous_autumnal_equinox(date):
    """Return the date of the previous autumnal equinox."""
    return holiday(date, -twopi, pi)

def next_autumnal_equinox(date):
    """Return the date of the next autumnal equinox."""
    return holiday(date, twopi, pi)

def previous_winter_solstice(date):
    """Return the date of the previous winter solstice."""
    return holiday(date, -twopi, halfpi)

def next_winter_solstice(date):
    """Return the date of the next winter solstice."""
    return holiday(date, twopi, halfpi)

# Common synonyms.

next_spring_equinox = next_vernal_equinox
previous_spring_equinox = previous_vernal_equinox

next_fall_equinox = next_autumn_equinox = next_autumnal_equinox
previous_fall_equinox = previous_autumn_equinox = previous_autumnal_equinox

# More-general functions that find any equinox or solstice.

def previous_equinox(date):
    """Return the date of the previous equinox."""
    return holiday(date, -pi, 0)

def next_equinox(date):
    """Return the date of the next equinox."""
    return holiday(date, pi, 0)

def previous_solstice(date):
    """Return the date of the previous solstice."""
    return holiday(date, -pi, halfpi)

def next_solstice(date):
    """Return the date of the next solstice."""
    return holiday(date, pi, halfpi)

# Find phases of the Moon.

_moon = Moon()                  # used for computing Moon phases

def _find_moon_phase(d0, motion, target):
    """Function that assists the finding of moon phases."""

    def f(d):
        _sun.compute(d)
        _moon.compute(d)
        slon = _libastro.eq_ecl(d, _sun.g_ra, _sun.g_dec)[0]
        mlon = _libastro.eq_ecl(d, _moon.g_ra, _moon.g_dec)[0]
        return (mlon - slon - antitarget) % twopi - pi
    antitarget = target + pi
    d0 = Date(d0)
    f0 = f(d0)
    angle_to_cover = (- f0) % motion
    if abs(angle_to_cover) < tiny:
        angle_to_cover = motion
    d = d0 + 29.53 * angle_to_cover / twopi
    return date(newton(f, d, d + hour))

def previous_new_moon(date):
    """Return the date of the previous New Moon."""
    return _find_moon_phase(date, -twopi, 0)

def next_new_moon(date):
    """Return the date of the next New Moon."""
    return _find_moon_phase(date, twopi, 0)

def previous_first_quarter_moon(date):
    """Return the date of the previous First Quarter Moon."""
    return _find_moon_phase(date, -twopi, halfpi)

def next_first_quarter_moon(date):
    """Return the date of the next First Quarter Moon."""
    return _find_moon_phase(date, twopi, halfpi)

def previous_full_moon(date):
    """Return the date of the previous Full Moon."""
    return _find_moon_phase(date, -twopi, pi)

def next_full_moon(date):
    """Return the date of the next Full Moon."""
    return _find_moon_phase(date, twopi, pi)

def previous_last_quarter_moon(date):
    """Return the date of the previous Last Quarter Moon."""
    return _find_moon_phase(date, -twopi, pi + halfpi)

def next_last_quarter_moon(date):
    """Return the date of the next Last Quarter Moon."""
    return _find_moon_phase(date, twopi, pi + halfpi)

# We provide a Python extension to our _libastro "Observer" class that
# can search for circumstances like transits.

class CircumpolarError(ValueError): pass
class NeverUpError(CircumpolarError): pass
class AlwaysUpError(CircumpolarError): pass

class Observer(_libastro.Observer):
    """
    Observers instances allow you to compute positions of celestial bodies.
    No parameters to init are taken.
    Includes a position on the Earth's surface, a time, a temperature, and a pressure.
    Needed by the compute() method of Body instances.
    Defaults:
     time: now
     temperature: 15 degrees Celsius
     pressure: 1010 mBar
     elevation, lat, long: 0
     epoch: 2000
    """
    __slots__ = [ 'name' ]
    elev = _libastro.Observer.elevation

    def __repr__(self):
        """Return a useful textual representation of this Observer."""
        return ('<ephem.Observer date=%r epoch=%r'
                ' lon=%s lat=%s elevation=%sm'
                ' horizon=%s temp=%sC pressure=%smBar>'
                % (str(self.date), str(self.epoch),
                   self.lon, self.lat, self.elevation,
                   self.horizon, self.temp, self.pressure))

    def compute_pressure(self):
        """Set the atmospheric pressure for the current elevation."""
        # Formula from the ISA Standard Atmosphere
        self.pressure = (1013.25 * (1 - 0.0065 * self.elevation / 288.15)
                         ** 5.2558761132785179)

    def _compute_transit(self, body, start, sign, offset):
        """Internal function used to compute transits."""

        if isinstance(body, EarthSatellite):
            raise TypeError(
                'the next and previous transit methods do not'
                ' support earth satellites because of their speed;'
                ' please use the higher-resolution next_pass() method'
                )

        def f(d):
            self.date = d
            body.compute(self)
            return degrees(offset - sidereal_time() + body.g_ra).znorm

        if start is not None:
            self.date = start
        sidereal_time = self.sidereal_time
        body.compute(self)
        ha = sidereal_time() - body.g_ra
        ha_to_move = (offset - ha) % (sign * twopi)
        if abs(ha_to_move) < tiny:
            ha_to_move = sign * twopi
        d = self.date + ha_to_move / twopi
        result = Date(newton(f, d, d + minute))
        return result

    def _previous_transit(self, body, start=None):
        """Find the previous passage of a body across the meridian."""

        return self._compute_transit(body, start, -1., 0.)

    def _next_transit(self, body, start=None):
        """Find the next passage of a body across the meridian."""

        return self._compute_transit(body, start, +1., 0.)

    def _previous_antitransit(self, body, start=None):
        """Find the previous passage of a body across the anti-meridian."""

        return self._compute_transit(body, start, -1., pi)

    def _next_antitransit(self, body, start=None):
        """Find the next passage of a body across the anti-meridian."""

        return self._compute_transit(body, start, +1., pi)

    def previous_transit(self, body, start=None):
        """Find the previous passage of a body across the meridian."""

        original_date = self.date
        d = self._previous_transit(body, start)
        self.date = original_date
        return d

    def next_transit(self, body, start=None):
        """Find the next passage of a body across the meridian."""

        original_date = self.date
        d = self._next_transit(body, start)
        self.date = original_date
        return d

    def previous_antitransit(self, body, start=None):
        """Find the previous passage of a body across the anti-meridian."""

        original_date = self.date
        d = self._previous_antitransit(body, start)
        self.date = original_date
        return d

    def next_antitransit(self, body, start=None):
        """Find the next passage of a body across the anti-meridian."""

        original_date = self.date
        d = self._next_antitransit(body, start)
        self.date = original_date
        return d

    def disallow_circumpolar(self, declination):
        """Raise an exception if the given declination is circumpolar.

        Raises NeverUpError if an object at the given declination is
        always below this Observer's horizon, or AlwaysUpError if such
        an object would always be above the horizon.

        """
        if abs(self.lat - declination) >= halfpi:
            raise NeverUpError('The declination %s never rises'
                               ' above the horizon at latitude %s'
                               % (declination, self.lat))
        if abs(self.lat + declination) >= halfpi:
            raise AlwaysUpError('The declination %s is always'
                                ' above the horizon at latitude %s'
                                % (declination, self.lat))

    def _riset_helper(self, body, start, use_center, rising, previous):
        """Internal function for finding risings and settings."""

        if isinstance(body, EarthSatellite):
            raise TypeError(
                'the rising and settings methods do not'
                ' support earth satellites because of their speed;'
                ' please use the higher-resolution next_pass() method'
                )

        def visit_transit():
            d = (previous and self._previous_transit(body)
                 or self._next_transit(body)) # if-then
            if body.alt + body.radius * use_radius - self.horizon <= 0:
                raise NeverUpError('%r transits below the horizon at %s'
                                   % (body.name, d))
            return d

        def visit_antitransit():
            d = (previous and self._previous_antitransit(body)
                 or self._next_antitransit(body)) # if-then
            if body.alt + body.radius * use_radius - self.horizon >= 0:
                raise AlwaysUpError('%r is still above the horizon at %s'
                                    % (body.name, d))
            return d

        # Determine whether we should offset the result for the radius
        # of the object being measured, or instead pretend that rising
        # and setting happens when its center crosses the horizon.
        if use_center:
            use_radius = 0.0
        else:
            use_radius = 1.0

        # Save self.date so that we can restore it before returning.
        original_date = self.date

        # Start slightly to one side of the start date, to prevent
        # repeated calls from returning the same solution over and over.
        if start is not None:
            self.date = start
        if previous:
            self.date -= default_newton_precision
        else:
            self.date += default_newton_precision

        # Take a big leap towards the solution, then Newton takes us home.
        body.compute(self)
        heading_downward = (rising == previous) # "==" is inverted "xor"
        if heading_downward:
            on_lower_cusp = (body.alt + body.radius * use_radius
                             - self.horizon > tiny)
        else:
            on_lower_cusp = (body.alt + body.radius * use_radius
                             - self.horizon < - tiny)

        az = body.az
        on_right_side_of_sky = ((rising == (az < pi)) # inverted "xor"
                                or (az < tiny
                                    or pi - tiny < az < pi + tiny
                                    or twopi - tiny < az))

        if on_lower_cusp and on_right_side_of_sky:
            d0 = self.date
        elif heading_downward:
            d0 = visit_transit()
        else:
            d0 = visit_antitransit()
        if heading_downward:
            d1 = visit_antitransit()
        else:
            d1 = visit_transit()

        def f(d):
            self.date = d
            body.compute(self)
            return body.alt + body.radius * use_radius - self.horizon

        d = (d0 + d1) / 2.
        result = Date(newton(f, d, d + minute))
        self.date = original_date
        return result

    def previous_rising(self, body, start=None, use_center=False):
        """Move to the given body's previous rising, returning the date."""
        return self._riset_helper(body, start, use_center, True, True)

    def previous_setting(self, body, start=None, use_center=False):
        """Move to the given body's previous setting, returning the date."""
        return self._riset_helper(body, start, use_center, False, True)

    def next_rising(self, body, start=None, use_center=False):
        """Move to the given body's next rising, returning the date."""
        return self._riset_helper(body, start, use_center, True, False)

    def next_setting(self, body, start=None, use_center=False):
        """Move to the given body's next setting, returning the date."""
        return self._riset_helper(body, start, use_center, False, False)

    def next_pass(self, body):
        """Return the next rising, culmination, and setting of a satellite."""

        if not isinstance(body, EarthSatellite):
            raise TypeError(
                'the next_pass() method is only for use with'
                ' EarthSatellite objects because of their high speed'
                )

        return _libastro._next_pass(self, body)

# Time conversion.

def localtime(date):
    """Convert a PyEphem date into local time, returning a Python datetime."""
    import calendar, time, datetime
    timetuple = time.localtime(calendar.timegm(date.tuple()))
    return datetime.datetime(*timetuple[:7])

# Coordinate transformations.

class Coordinate(object):
    def __init__(self, *args, **kw):

        # Accept an optional "epoch" keyword argument.

        epoch = kw.pop('epoch', None)
        if epoch is not None:
            self.epoch = epoch = Date(epoch)
        if kw:
            raise TypeError('"epoch" is the only keyword argument'
                            ' you can use during %s instantiation'
                            % (type(self).__name__))

        # Interpret a single-argument initialization.

        if len(args) == 1:
            a = args[0]

            if isinstance(a, Body):
                a = Equatorial(a.a_ra, a.a_dec, epoch = a.a_epoch)

            for cls in (Equatorial, Ecliptic, Galactic):
                if isinstance(a, cls):

                    # If the user omitted an "epoch" keyword, then
                    # use the epoch of the other object.

                    if epoch is None:
                        self.epoch = epoch = a.epoch

                    # If we are initialized from another of the same
                    # kind of coordinate and epoch, simply copy the
                    # coordinates and epoch into this new object.

                    if isinstance(self, cls) and epoch == a.epoch:
                        self.set(*a.get())
                        return

                    # Otherwise, convert.

                    ra, dec = a.to_radec()
                    if epoch != a.epoch:
                        ra, dec = _libastro.precess(
                            a.epoch, epoch, ra, dec
                            )
                    self.from_radec(ra, dec)
                    return

            raise TypeError(
                'a single argument used to initialize %s() must be either'
                ' a coordinate or a Body, not an %r' % (type(a).__name__,)
                )

        # Two arguments are interpreted as (ra, dec) or (lon, lat).

        elif len(args) == 2:
            self.set(*args)
            if epoch is None:
                self.epoch = epoch = Date('2000')

        else:
            raise TypeError(
                'to initialize %s you must pass either a Body,'
                ' another coordinate, or two coordinate values,'
                ' but not: %r' % (type(self).__name__, args,)
                )

class Equatorial(Coordinate):
    def get(self):
        return self.ra, self.dec

    def set(self, ra, dec):
        self.ra, self.dec = hours(ra), degrees(dec)

    to_radec = get
    from_radec = set

class LonLatCoordinate(Coordinate):
    def set(self, lon, lat):
        self.lon, self.lat = degrees(lon), degrees(lat)

    def get(self):
        return self.lon, self.lat

class Ecliptic(LonLatCoordinate):
    def to_radec(self):
        return _libastro.ecl_eq(self.epoch, self.lon, self.lat)

    def from_radec(self, ra, dec):
        self.lon, self.lat = _libastro.eq_ecl(self.epoch, ra, dec)

class Galactic(LonLatCoordinate):
    def to_radec(self):
        return _libastro.gal_eq(self.epoch, self.lon, self.lat)

    def from_radec(self, ra, dec):
        self.lon, self.lat = _libastro.eq_gal(self.epoch, ra, dec)

# For backwards compatibility, provide lower-case names for our Date
# and Angle classes, and also allow "Lon" to be spelled "Long".

date = Date
angle = Angle
LongLatCoordinate = LonLatCoordinate

# Catalog boostraps.  Each of these functions imports a catalog
# module, then replaces itself with the function of the same name that
# lives inside of the catalog.

def star(name, *args, **kwargs):
    """Load the stars database and return a star."""
    global star
    import ephem.stars
    star = ephem.stars.star
    return star(name, *args, **kwargs)

def city(name):
    """Load the cities database and return a city."""
    global city
    import ephem.cities
    city = ephem.cities.city
    return city(name)
