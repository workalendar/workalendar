.. image:: https://img.shields.io/pypi/v/calendra.svg
   :target: https://pypi.org/project/calendra

.. image:: https://img.shields.io/pypi/pyversions/calendra.svg

.. image:: https://img.shields.io/pypi/dm/calendra.svg

.. image:: https://img.shields.io/travis/jaraco/calendra/master.svg
   :target: http://travis-ci.org/jaraco/calendra

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

Overview
========

Calendra is a Python module that offers classes able to handle calendars,
list legal / religious holidays and gives working-day-related computation
functions.

History
=======

Calendra is a fork of `Workalendar <https://github.com/novapost/workalendar>`_
designed to be more extensible and introspectable, adding interfaces where
`Workalendar is philosophically opposed for the sake of simplicity
<https://github.com/novapost/workalendar/pull/79>`_.

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


External dependencies
=====================

You may want to install ``python-dev`` and/or ``python3-dev`` on your machine to
either run the installation or run tests via tox.


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

* Belgium
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
* Italy
* Luxembourg
* Netherlands
* Norway
* Poland
* Portugal
* Slovakia
* Sweden
* United Kingdom (incl. Northern Ireland)
* Spain (incl. Catalonia)
* Slovenia
* Switzerland

America
-------

* Brazil (incl. São Paulo state and city)
* Chile
* Colombia
* Mexico
* Panama
* United States of America (including state holidays)
* Canada (including provincial and territory holidays)

Asia
----

* Japan
* Qatar
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

Please read our `CONTRIBUTING.rst <https://github.com/jaraco/calandra/blob/master/CONTRIBUTING.rst>`_
document to discover how you can contribute to ``calendra``. Pull-requests
are very welcome.

License
=======

This library is published under the terms of the MIT License. Please check the
LICENSE file for more details.
