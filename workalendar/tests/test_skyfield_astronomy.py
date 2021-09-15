import pytest
from datetime import date
from math import pi
from unittest.mock import patch

from skyfield.api import Loader
from skyfield_data import get_skyfield_data_path

from ..skyfield_astronomy import (
    calculate_equinoxes,
    solar_term,
    newton_angle_function,
)


def test_calculate_some_equinoxes():
    assert calculate_equinoxes(2010) == (date(2010, 3, 20), date(2010, 9, 23))
    assert calculate_equinoxes(2010, 'Asia/Taipei') == (
        date(2010, 3, 21), date(2010, 9, 23)
    )
    assert calculate_equinoxes(2013) == (date(2013, 3, 20), date(2013, 9, 22))
    assert calculate_equinoxes(2014) == (date(2014, 3, 20), date(2014, 9, 23))
    assert calculate_equinoxes(2020) == (date(2020, 3, 20), date(2020, 9, 22))


def test_qingming_festivals():
    assert solar_term(2001, 15) == date(2001, 4, 4)
    assert solar_term(2001, 15, 'Asia/Taipei') == date(2001, 4, 5)
    assert solar_term(2011, 15) == date(2011, 4, 5)
    assert solar_term(2014, 15) == date(2014, 4, 4)
    assert solar_term(2016, 15) == date(2016, 4, 4)
    assert solar_term(2017, 15) == date(2017, 4, 4)


def test_qingming_festivals_hk():
    assert solar_term(2018, 15, 'Asia/Hong_Kong') == date(2018, 4, 5)
    assert solar_term(2019, 15, 'Asia/Hong_Kong') == date(2019, 4, 5)
    assert solar_term(2020, 15, 'Asia/Hong_Kong') == date(2020, 4, 4)
    assert solar_term(2021, 15, 'Asia/Hong_Kong') == date(2021, 4, 4)


@pytest.fixture(scope='session')
def params_newton_angle():
    """
    Session-scoped fixture to "cache" the newton angle func parameters
    """
    load = Loader(get_skyfield_data_path())
    ts = load.timescale()
    planets = load('de421.bsp')
    earth = planets['earth']
    sun = planets['sun']

    jan_first = ts.utc(date(2021, 1, 1))
    t0 = ts.tt_jd(jan_first.tt).tt
    return t0, ts, earth, sun


def test_newton_angle_function_normal_range(params_newton_angle):
    """
    Test the newton angle func when the longitude is in the range [-pi, +pi].
    """
    t0, ts, earth, sun = params_newton_angle

    with patch('workalendar.skyfield_astronomy.get_current_longitude') \
            as patched:
        patched.return_value = pi
        assert newton_angle_function(t0, ts, 0, earth, sun) == -pi


def test_newton_angle_function_above_pi(params_newton_angle):
    """
    Test the newton angle function when the longitude is > +pi.

    This should not happen, but it was implemented in the function, so in order
    to make sure that the resulting angle is always in the range [-pi, +pi],
    we added these tests with those out of range values.
    """
    t0, ts, earth, sun = params_newton_angle

    with patch('workalendar.skyfield_astronomy.get_current_longitude') \
            as patched:
        patched.return_value = pi + 0.1
        expected = pytest.approx(-.1)
        assert newton_angle_function(t0, ts, 0, earth, sun) == expected


def test_newton_angle_function_below_minus_pi(params_newton_angle):
    """
    Test the newton angle function when the longitude is < -pi.

    This should not happen, but it was implemented in the function, so in order
    to make sure that the resulting angle is always in the range [-pi, +pi],
    we added these tests with those out of range values.
    """
    t0, ts, earth, sun = params_newton_angle

    with patch('workalendar.skyfield_astronomy.get_current_longitude') \
            as patched:
        patched.return_value = -pi - 0.1
        expected = pytest.approx(.1)
        assert newton_angle_function(t0, ts, 0, earth, sun) == expected
