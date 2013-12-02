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

This is barely beta. Please consider this module as a work in progres.

Usage sample
============

::

    >>> from datetime import date
    >>> from workalendar.europe import FranceCalendar
    >>> cal = FranceCalendar()
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


Tests
=====

Travis status:

.. image:: https://api.travis-ci.org/novapost/workalendar.png


To run test, just install nose with ``pip install nose`` and run::

    nosetests

from the command line.

Available Calendars
===================

Europe
------

* Czech Republic
* France
* Iceland
* United Kingdom
* Northern Ireland

America
-------

* United States of America

Asia
----

* South Korea

Oceania
-------

* Australia

And more to come (I hope!)


License
=======

This library is published under the terms of the MIT License. Please check the
LICENSE file for more details.
