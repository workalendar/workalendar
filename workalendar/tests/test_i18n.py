import os
from datetime import date
from workalendar.europe import France


def test_i18n_france():
    calendar = France()
    holidays = calendar.holidays(2019)
    holidays = dict(holidays)

    language = os.getenv("LANGUAGE") or ""
    tox_env_name = os.getenv("TOX_ENV_NAME") or ""
    if language.startswith('fr'):   # We're checking French translations
        # This is only happening in "i18n" tests
        assert 'i18n' in tox_env_name, (
            "tests supposed to be run with "
            "TOX_ENV_NAME containing 'i18n'"
        )
        # Commented assertions are not translated yet.
        # assert holidays[date(2019, 1, 1)] == "Jour de l'an"
        # assert holidays[date(2013, 4, 1)] == "Lundi de Pâques"
        assert holidays[date(2019, 5, 1)] == "Fête du travail"
        assert holidays[date(2019, 5, 8)] == "Fête de la Victoire"
        # assert holidays[date(2019, 5, 9)] == "Jeudi de l'Ascension"
        # assert holidays[date(2019, 5, 20)] == "Lundi de Pentecôte"
        assert holidays[date(2019, 7, 14)] == "Fête nationale"
        # assert holidays[date(2019, 8, 15)] == "Assomption"
        # assert holidays[date(2019, 11, 1)] == "Toussaint"
        assert holidays[date(2019, 11, 11)] == "Armistice 1918"
        # assert holidays[date(2019, 12, 25)] == "Noël"
    else:
        # All other tests are using the LANG=C or en_US or whatever...
        assert 'i18n' not in tox_env_name
        # We'll just check this assertion, because it's the most common
        # fixed holiday in the world (without any religious origin)
        assert holidays[date(2019, 5, 1)] == "Labour Day"
