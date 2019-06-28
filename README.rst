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

If you spot any bug or wish to add a calendar, please refer to the `Contributing doc <contributing.md>`_.

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

For a more complete documentation and advanced usage, go to
`the official workalendar documentation <https://peopledoc.github.io/workalendar>`_.

External dependencies
=====================

You may want to install ``python-dev`` and/or ``python3-dev`` on your machine to
either run the installation or run tests via tox.

Workalendar has been tested on Python 2.7, 3.5, 3.6, 3.7.

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
* Cayman Islands
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
* Slovenia
* Spain (incl. Catalonia)
* Sweden
* Switzerland

  * Vaud

* Turkey
* United Kingdom (incl. Northern Ireland, Scotland and all its territories)

America
-------

* Barbados
* Brazil (all states, cities and for bank transactions, except the city of Viana)
* Canada (including provincial and territory holidays)
* Chile
* Colombia
* Mexico
* Panama
* Paraguay
* United States of America

  * State holidays for all the 50 States
  * American Samoa
  * Chicago, Illinois
  * Guam
  * Suffolk County, Massachusetts
  * California Education, Berkeley, San Francisco, West Hollywood
  * Florida Legal and Florida Circuit Courts, Miami-Dade

Asia
----

* China
* Hong Kong
* Israel
* Japan
* JapanBank
* Malaysia
* Qatar
* Singapore
* South Korea
* Taiwan

Oceania
-------

* Australia (incl. its different states)
* Marshall Islands
* New Zealand

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

Please read our `contributing.md <https://github.com/peopledoc/workalendar/blob/master/contributing.md>`_
document to discover how you can contribute to ``workalendar``. Pull-requests
are very welcome.

License
=======

This library is published under the terms of the MIT License. Please check the
LICENSE file for more details.
