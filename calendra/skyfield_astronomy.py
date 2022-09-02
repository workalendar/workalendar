"""
Astronomical functions
"""
from math import pi, radians, tau
try:
    # As of Python 3.9, included in the stdlib
    from zoneinfo import ZoneInfo
except ImportError:  # pre-3.9
    from backports.zoneinfo import ZoneInfo
from skyfield.api import Loader
from skyfield import almanac
from skyfield_data import get_skyfield_data_path
from datetime import date, timedelta


# Parameter for the newton method to converge towards the closest solution
# to the function. By default it'll be an approximation of a 10th of a second.
hour = 1 / 24
minute = hour / 60
second = minute / 60
newton_precision = second / 10


def calculate_equinoxes(year, timezone='UTC'):
    """ calculate equinox with time zone """
    tz = ZoneInfo(timezone)

    load = Loader(get_skyfield_data_path())
    ts = load.timescale()
    planets = load('de421.bsp')

    t0 = ts.utc(year, 1, 1)
    t1 = ts.utc(year, 12, 31)
    datetimes, _ = almanac.find_discrete(t0, t1, almanac.seasons(planets))
    vernal_equinox = datetimes[0].astimezone(tz).date()
    autumn_equinox = datetimes[2].astimezone(tz).date()
    return vernal_equinox, autumn_equinox


def get_current_longitude(current_date, earth, sun):
    """
    Return the ecliptic longitude, in radians.
    """
    astrometric = earth.at(current_date).observe(sun)
    latitude, longitude, _ = astrometric.ecliptic_latlon(epoch='date')
    return longitude.radians


def newton(f, x0, x1, precision=newton_precision,
           **func_kwargs):
    """Return an x-value at which the given function reaches zero.

    Stops and declares victory once the x-value is within ``precision``
    of the solution, which defaults to a half-second of clock time.
    """
    f0, f1 = f(x0, **func_kwargs), f(x1, **func_kwargs)
    while f1 and abs(x1 - x0) > precision and f1 != f0:
        new_x1 = x1 + (x1 - x0) / (f0 / f1 - 1)
        x0, x1 = x1, new_x1
        f0, f1 = f1, f(x1, **func_kwargs)
    return x1


def newton_angle_function(t, ts, target_angle, body1, body2):
    """
    Compute the longitude of body2 relative to body1

    In our case, it's Earth & Sun, but it could be used as any other
    combination of solar system planets/bodies.
    """
    # We've got a float which is the `tt`
    sky_tt = ts.tt_jd(t)
    longitude = get_current_longitude(sky_tt, body1, body2)
    result = target_angle - longitude
    if result > pi:
        result = result - pi
    if result < -pi:
        result = result + pi
    return result


def solar_term(year, degrees, timezone='UTC'):
    """
    Returns the date of the solar term for the given longitude
    and the given year.

    Solar terms are used for Chinese and Taiwanese holidays
    (e.g. Qingming Festival in Taiwan).

    More information:
    - https://en.wikipedia.org/wiki/Solar_term
    - https://en.wikipedia.org/wiki/Qingming

    This function is adapted from the following topic:
    https://answers.launchpad.net/pyephem/+question/110832
    """
    # Target angle as radians
    target_angle = radians(degrees)

    load = Loader(get_skyfield_data_path())
    planets = load('de421.bsp')
    earth = planets['earth']
    sun = planets['sun']
    ts = load.timescale()
    tz = ZoneInfo(timezone)

    jan_first = ts.utc(date(year, 1, 1))
    current_longitude = get_current_longitude(jan_first, earth, sun)

    # Find approximately the right time of year.
    difference = (target_angle - current_longitude) % tau
    # Here we have an approximation of the number of julian days to go
    date_delta = 365.25 * difference / tau
    # convert to "tt" and reconvert it back to a Time object
    t0 = ts.tt_jd(jan_first.tt + date_delta)

    # Using datetimes to compute the next step date
    t0_plus_one_minute = t0.utc_datetime() + timedelta(minutes=1)
    # Back to Skyfield Time objects
    t0_plus_one_minute = ts.utc(t0_plus_one_minute)

    # Julian day for the starting date
    t0 = t0.tt
    # Adding one minute to have a second boundary
    t0_plus_one_minute = t0_plus_one_minute.tt
    # Newton method to converge towards the target angle
    t = newton(
        newton_angle_function, t0, t0_plus_one_minute,
        precision=newton_precision,
        # Passed as kwargs to the angle function
        ts=ts,
        target_angle=target_angle,
        body1=earth,
        body2=sun,
    )
    # Here we have a float to convert to julian days.
    t = ts.tt_jd(t)
    # To convert to datetime
    t = t.utc_datetime()
    # Convert in the timezone
    result = t.astimezone(tz)
    return result.date()
