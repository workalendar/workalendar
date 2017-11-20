===========
Workalendar
===========

Overview
========

Workalendar is a Python module that offers classes able to handle calendars,
list legal / religious holidays and gives working-day-related computation
functions.

Status
======

This library is ready for production, although we may warn eventual users: some calendars may not be up-to-date, and this library doesn't cover all the existing countries on earth (yet).

If you spot any bug or wish to add a calendar, please refer to the `Contributing doc <CONTRIBUTING.rst>`_.

Usage sample
============

.. code-block:: python

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


External dependencies
=====================

You may want to install ``python-dev`` and/or ``python3-dev`` on your machine to
either run the installation or run tests via tox.


Tests
=====

Travis status:

.. image:: https://api.travis-ci.org/peopledoc/workalendar.png


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
* Luxembourg
* Malta
* Netherlands
* Norway
* Poland
* Portugal
* Romania
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

Please read our `CONTRIBUTING.rst <https://github.com/peopledoc/workalendar/blob/master/CONTRIBUTING.rst>`_
document to discover how you can contribute to ``workalendar``. Pull-requests
are very welcome.

License
=======

This library is published under the terms of the MIT License. Please check the
LICENSE file for more details.
