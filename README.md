# Workalendar

[![license](http://img.shields.io/pypi/l/workalendar.svg)](https://github.com/workalendar/workalendar/blob/master/LICENSE)
[![pypi](http://img.shields.io/pypi/v/workalendar.svg)](https://pypi.python.org/pypi/workalendar)
[![conda](https://img.shields.io/conda/v/conda-forge/workalendar?color=blue&logo=anaconda)](https://anaconda.org/conda-forge/workalendar)

## Overview

Workalendar is a Python module that offers classes able to handle calendars, list legal / religious holidays and gives working-day-related computation functions.

## Installation

**With pip**

```sh
pip install workalendar
```

**With conda**

```sh
conda install -c conda-forge workalendar
```

### Extra dependencies

**Note: NEW in v16.0.0**

If the calendar(s) you want to work with requires astronomical computations (such as Asian calendars needing equinoxes or solar terms), Workalendar will provide pre-computed values within the year range from 1991 to 2051.

However, if you want to use astronomical libraries to compute the calendar yourself, you'll need to install the `[astronomy]` extra dependency like this:

```sh
pip install workalendar[astronomy]
```

If you had previously installed the `skyfield` and `skyfield-data` packages, they'll be used to compute the calendars. If you want to benefit from the "astronomical cache", and eventually benefit from performance gains, you'll have to **uninstall** those packages first to fallback to pre-computed files.

## Status

This library is ready for production, although we may warn eventual users: some calendars may not be up-to-date, and this library doesn't cover all the existing countries on earth (yet).

If you spot any bug or wish to add a calendar, please refer to the [Contributing doc](docs/contributing.md).

## Usage sample

```python
>>> from datetime import date
>>> from workalendar.europe import France
>>> cal = France()
>>> cal.holidays(2012)
[(datetime.date(2012, 1, 1), 'New year'),
 (datetime.date(2012, 4, 9), 'Easter Monday'),
 (datetime.date(2012, 5, 1), 'Labour Day'),
 (datetime.date(2012, 5, 8), 'Victory in Europe Day'),
 (datetime.date(2012, 5, 17), 'Ascension Day'),
 (datetime.date(2012, 5, 28), 'Whit Monday'),
 (datetime.date(2012, 7, 14), 'Bastille Day'),
 (datetime.date(2012, 8, 15), 'Assumption of Mary to Heaven'),
 (datetime.date(2012, 11, 1), "All Saints' Day"),
 (datetime.date(2012, 11, 11), 'Armistice Day'),
 (datetime.date(2012, 12, 25), 'Christmas')]
>>> cal.is_working_day(date(2012, 12, 25))  # it's Christmas
False
>>> cal.is_working_day(date(2012, 12, 30))  # it's Sunday
False
>>> cal.is_working_day(date(2012, 12, 26))
True
>>> cal.add_working_days(date(2012, 12, 23), 5)  # 5 working days after Xmas
datetime.date(2012, 12, 31)
```

For a more complete documentation and advanced usage, go to [the official workalendar documentation](https://workalendar.github.io/workalendar).

## External dependencies

**Workalendar will require you to use Python 3.7+.**

Workalendar is tested on Python 3.7, 3.8, 3.9, 3.10, 3.11, and on Linux (Ubuntu), Mac OS and Windows using Github actions.

### Conditional dependencies

As of v15.0.0:

* If you're using \*Nix and Python 3.7, 3.8, the package `backports.zoneinfo` is required
* If you're using Windows and Python 3.7, 3.8, the package `tzdata` is *also* a requirement (with the `backports.zoneinfo`).
* If you're using Python 3.9+, the stdlib `zoneinfo` package will be used.

## Tests

CI status:

[![Github action status](https://github.com/workalendar/workalendar/workflows/CI/badge.svg)](https://github.com/workalendar/workalendar/actions?query=workflow%3ACI)

To run test, just install tox with `pip install tox` and run:

```
tox
```

from the command line.

## Available Calendars

### Europe

- Austria
- Belarus
- Belgium
- Bulgaria
- Cayman Islands
- Croatia
- Cyprus
- Czech Republic
- Denmark
- Estonia
- European Central Bank
- Finland
- France
- France (Alsace / Moselle)
- Georgia
- Germany
- Greece
- Guernsey
- Hungary
- Iceland
- Ireland
- Italy
- Latvia
- Lithuania
- Luxembourg
- Malta
- Monaco
- Netherlands (optionally with school holidays and carnival)
- Norway
- Poland
- Portugal
- Romania
- Russia
- Serbia
- Slovakia
- Slovenia
- Spain (Andalusia, Aragon, Castile and León, Castilla-La Mancha, Canary Islands, Extremadura, Galicia, Balearic Islands, La Rioja, Community of Madrid, Murcia, Navarre, Asturias, Basque Country, Cantabria, Valencian Community)
- Sweden
- Switzerland (Aargau, Appenzell Innerrhoden, Appenzell Ausserrhoden, Bern, Basel-Landschaft, Basel-Stadt, Fribourg, Geneva, Glarus, Graubünden, Jura, Luzern, Neuchâtel, Nidwalden, Obwalden, St. Gallen, Schaffhausen, Solothurn, Schwyz, Thurgau, Ticino, Uri, Vaud, Valais, Zug, Zurich)
- Turkey
- Ukraine
- United Kingdom (incl. Northern Ireland, Scotland and all its territories)

### America

- Argentina
- Barbados
- Brazil (all states, cities and for bank transactions, except the city of Viana)
- Canada (including provincial and territory holidays)
- Chile
- Colombia
- El Salvador
- Mexico
- Panama
- Paraguay
- United States of America
  - State holidays for all the 50 States
  - American Samoa
  - Chicago, Illinois
  - Guam
  - Suffolk County, Massachusetts
  - California Education, Berkeley, San Francisco, West Hollywood
  - Florida Legal and Florida Circuit Courts, Miami-Dade
  - Federal Reserve System

### Asia

- China
- Hong Kong
- Israel
- Japan
- JapanBank
- Kazakhstan
- Malaysia
- Philippines
- Qatar
- Singapore
- South Korea
- Taiwan

### Oceania

- Australia (incl. its different states)
- Marshall Islands
- New Zealand

### Africa

- Algeria
- Angola
- Benin
- Ivory Coast
- Kenya
- Madagascar
- Mozambique
- Nigeria
- São Tomé
- South Africa
- Tunisia

And more to come (I hope!)

## Caveats

Please take note that some calendars are not 100% accurate. The most common example is the Islamic calendar, where some computed holidays are not exactly on the same official day decided by religious authorities, and this may vary country by country. Whenever it's possible, try to adjust your results with the official data provided by the adequate authorities.

Some countries have some holidays based on ephemerids and equinoxes. Those are computed for the previous and next 30 years to prevent big computations and dependencies.

## Contributing

Please read our [contributing.md](https://github.com/workalendar/workalendar/blob/master/docs/contributing.md) document to discover how you can contribute to `workalendar`. Pull-requests are very welcome.

## History

This project was born in 2013, as an answer to the question "how do we calculate *this date + 5 working days*?". It was a use-case for [PeopleDoc](https://www.people-doc.fr/), in their ticketing application, for calculating SLAs. And it began as a small open-source library, for France and the USA at first.

Thanks to PeopleDoc, this project grew and eventually became a world-wide library, with the help of dozens of contributors.

As of June 2021, this project has moved to its own organization.

## License

This library is published under the terms of the MIT License. Please check the LICENSE file for more details.
