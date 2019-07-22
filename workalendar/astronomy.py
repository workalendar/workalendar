"""
Astronomical functions
"""
from math import pi
import pytz
import ephem


def calculate_equinoxes(year, timezone='UTC'):
    """ calculate equinox with time zone """
    tz = pytz.timezone(timezone)

    d1 = ephem.next_equinox(str(year))
    d = ephem.Date(str(d1))
    equinox1 = d.datetime() + tz.utcoffset(d.datetime())

    d2 = ephem.next_equinox(d1)
    d = ephem.Date(str(d2))
    equinox2 = d.datetime() + tz.utcoffset(d.datetime())

    return (equinox1.date(), equinox2.date())


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
    twopi = 2 * pi
    tz = pytz.timezone(timezone)

    # Find out the sun's current longitude.
    sun = ephem.Sun(ephem.Date(str(year)))
    # > Both hlon and hlat have a special meaning for the Sun and Moon.
    # > For a Sun body, they give the Earth's heliocentric longitude and
    # > latitude.
    current_longitude = sun.hlon - pi

    # Find approximately the right time of year.

    target_longitude = degrees * ephem.degree
    difference = (target_longitude - current_longitude) % twopi
    t0 = ephem.Date(str(year)) + 365.25 * difference / twopi

    # Zero in on the exact moment.

    def f(t):
        sun.compute(t)
        longitude = sun.hlon - pi
        return ephem.degrees(target_longitude - longitude).znorm

    d = ephem.Date(ephem.newton(f, t0, t0 + ephem.minute))
    solar_term = d.datetime() + tz.utcoffset(d.datetime())

    return solar_term.date()
