.. image:: https://img.shields.io/pypi/v/calendra.svg
   :target: https://pypi.org/project/calendra

.. image:: https://img.shields.io/pypi/pyversions/calendra.svg

.. image:: https://img.shields.io/travis/jaraco/calendra/master.svg
   :target: https://travis-ci.org/jaraco/calendra

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/calendra/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/calendra/branch/master

.. image:: https://readthedocs.org/projects/calendra/badge/?version=latest
   :target: https://calendra.readthedocs.io/en/latest/?badge=latest

Overview
========

Calendra is a Python module that offers classes able to handle calendars,
list legal / religious holidays and gives working-day-related computation
functions.

History
=======

Calendra is a fork of `Workalendar <https://github.com/peopledoc/workalendar>`_
designed to be more extensible and introspectable, adding interfaces where
`Workalendar is philosophically opposed for the sake of simplicity
<https://github.com/peopledoc/workalendar/pull/79>`_.

What can Calendra do that Workalendar cannot?

- Provides descriptions for holidays for the "day indicated" for each
  Holiday (such as '3rd Monday in August').
- Keeps distinct the indicated and observed dates for Holidays, such
  that it's possible to determine on what day a given holiday is observed.
- Allows the number of Holidays in a calendar year to be counted.
- Consolidates observance logic in the core code rather than requiring
  each calendar implementation to implement its own.

Status
======

The project is stable and in production use. Calendra follows the principles
of `semver <https://semver.org>`_ for released verisons.

Usage sample
============

.. code-block:: python

    >>> from datetime import date
    >>> from calendra.europe import France
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

For a more complete documentation and advanced usage, go to
`the official workalendar documentation <https://peopledoc.github.io/workalendar>`_.

External dependencies
=====================

You may want to install ``python-dev`` and/or ``python3-dev`` on your machine to
either run the installation or run tests via tox.

Workalendar has been tested on Python 2.7, 3.4, 3.5, 3.6, 3.7.

Tests
=====

Travis status:

.. image:: https://api.travis-ci.org/jaraco/calendra.png


To run test, just install tox with ``pip install tox`` and run::

    tox

from the command line.


Available Calendars
===================

Europe
------

* Austria
* Belgium
* Bulgaria
* Croatia
* Cyprus
* Czech Republic
* Denmark
* Estonia
* European Central Bank
* Finland
* France
* France (Alsace / Moselle)
* Germany
* Greece
* Hungary
* Iceland
* Ireland
* Italy
* Latvia
* Lithuania
* Luxembourg
* Malta
* Netherlands
* Norway
* Poland
* Portugal
* Romania
* Russia
* Slovakia
* Sweden
* United Kingdom (incl. Northern Ireland)
* Spain (incl. Catalonia)
* Slovenia
* Switzerland
  * Vaud

America
-------

* Brazil (all states, cities and for bank transactions, except the city of Viana)
* Chile
* Colombia
* Mexico
* Panama
* United States of America (including state holidays)
* Canada (including provincial and territory holidays)

Asia
----

* Hong Kong
* Japan
* Malaysia
* Qatar
* Singapore
* South Korea
* Taiwan

Oceania
-------

* Australia (incl. its different states)
* Marshall Islands

Africa
------

* Algeria
* Angola
* Benin
* Ivory Coast
* Madagascar
* São Tomé
* South Africa

And more to come (I hope!)

Caveats
=======

Please take note that some calendars are not 100% accurate. The most common
example is the Islamic calendar, where some computed holidays are not exactly on
the same official day decided by religious authorities, and this may vary
country by country. Whenever it's possible, try to adjust your results with
the official data provided by the adequate authorities.

Contributing
============

Please read our `CONTRIBUTING.rst <https://github.com/jaraco/calandra/blob/master/CONTRIBUTING.rst>`_
document to discover how you can contribute to ``calendra``. Pull-requests
are very welcome.

License
=======

This library is published under the terms of the MIT License. Please check the
LICENSE file for more details.
