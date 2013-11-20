===========
Workalendar
===========

Overview
========

Workalendar is a Python module that offers classes able to handle calendars,
list legal / religious holidays and gives workday-related computation functions.

Status
======

This is barely beta. Please consider this module as a work in progres.

Usage sample
============

::

    >>> from datetime import date
    >>> from workalendar.europe import FranceCalendar
    >>> cal = FranceCalendar()
    >>> cal.get_calendar_holidays(2012)
    set([datetime.date(2012, 5, 17),
         datetime.date(2012, 11, 11),
         datetime.date(2012, 11, 1),
         datetime.date(2012, 5, 8),
         datetime.date(2012, 5, 28),
         datetime.date(2012, 7, 14),
         datetime.date(2012, 5, 1),
         datetime.date(2012, 4, 9),
         datetime.date(2012, 1, 1),
         datetime.date(2012, 8, 15),
         datetime.date(2012, 12, 25)])
    >>> cal.is_workday(date(2012, 12, 25))  # it's Christmas
    False
    >>> cal.is_workday(date(2012, 12, 30))  # it's Sunday
    False
    >>> cal.is_workday(date(2012, 12, 26))
    True

License
=======

This library is published under the terms of the MIT License. Please check the
LICENSE file for more details.
