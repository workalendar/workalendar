from datetime import date

from ..astronomy import calculate_equinoxes, solar_term


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
