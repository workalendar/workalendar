"""
Astronomical functions

Computed years spread from 30 years before and after the release year.
"""
import datetime
import gzip
import json
import pathlib
from typing import Tuple

TZAwareDate = datetime.date

# In 2021, Skyfield cannot compute ephemeris after date 2053-10-08 23:58:51Z UT
YEAR_INTERVAL = 30
TIME_ZONES = (
    'America/Santiago',
    'Asia/Hong_Kong',
    'Asia/Taipei',
    'Asia/Tokyo',
)
pre_computed_equinoxes_path = \
    pathlib.Path(__file__).parent / 'equinoxes.json.gz'
pre_computed_solar_terms_path = \
    pathlib.Path(__file__).parent / 'solar_terms.json.gz'

try:
    # Before Python 3.7, date.fromisoformat does not exist
    datetime.date.fromisoformat

    def fromisoformat(iso):
        return datetime.date.fromisoformat(iso)
except AttributeError:  # pre-3.7
    def fromisoformat(iso):
        try:
            if not iso or '-' not in iso:
                raise ValueError
            parts = [int(x) for x in iso.split('-')]
            if len(parts) != 3:
                raise ValueError
            return datetime.date(year=parts[0], month=parts[1], day=parts[2])
        except ValueError:
            raise ValueError(f"Invalid isoformat string: '{iso}'")


def create_astronomical_data(progress=None):
    from .skyfield_astronomy import (
        calculate_equinoxes as real_calculate_equinoxes
    )
    from .skyfield_astronomy import (
        solar_term as real_solar_term
    )
    if progress is None:
        progress = lambda it: it  # noqa: E731
    current_year = datetime.date.today().year
    first_year = current_year - YEAR_INTERVAL
    last_year = current_year + YEAR_INTERVAL
    years = range(first_year, last_year + 1)
    equinoxes = dict()
    solar_terms = dict()
    for i, time_zone in enumerate(TIME_ZONES, 1):
        print(f"{time_zone} {i}/{len(TIME_ZONES)}")
        equinoxes[time_zone] = dict()
        equinoxes_tz = equinoxes[time_zone]
        solar_terms[time_zone] = dict()
        solar_terms_tz = solar_terms[time_zone]
        for year in progress(years):
            equinoxes_tz[year] = tuple(
                equinox.isoformat()
                for equinox in real_calculate_equinoxes(year, time_zone)
            )
            solar_terms_tz[year] = dict()
            for degrees in range(15, 360, 15):
                solar_terms_tz[year][degrees] = \
                    real_solar_term(year, degrees, time_zone).isoformat()
    with gzip.open(pre_computed_equinoxes_path, 'wb') as f:
        f.write(json.dumps(equinoxes, ensure_ascii=False).encode('utf-8'))
    with gzip.open(pre_computed_solar_terms_path, 'wb') as f:
        f.write(json.dumps(solar_terms, ensure_ascii=False).encode('utf-8'))


def calculate_equinoxes(
    year: int,
    timezone: str = 'UTC',
) -> Tuple[TZAwareDate, TZAwareDate]:
    """
    calculate equinox with time zone.
    returns a 2-tuple with vernal and autumn equinoxes.
    """
    equinoxes = json.loads(gzip.decompress(
        pre_computed_equinoxes_path.read_bytes()
    ).decode('utf-8'))
    try:
        result = equinoxes[timezone][str(year)]
    except KeyError:
        raise NotImplementedError(
            f"The year {year} and timezone {timezone} are not pre-computed"
        )
    return tuple(fromisoformat(equinox) for equinox in result)


def solar_term(year: int, degrees: int, timezone: str = 'UTC') -> TZAwareDate:
    if not 15 <= degrees < 345 or degrees % 15 != 0:
        raise ValueError(
            "The degrees should be between 15 and 345 by step of 15"
        )
    solar_terms = json.loads(gzip.decompress(
        pre_computed_solar_terms_path.read_bytes()
    ).decode('utf-8'))
    try:
        solar_terms_per_tz_and_year = solar_terms[timezone][str(year)]
    except KeyError:
        raise NotImplementedError(
            f"The year {year} and timezone {timezone} are not pre-computed"
        )
    return fromisoformat(
        solar_terms_per_tz_and_year[str(degrees)]
    )
