# -*- coding: utf-8 -*-
"""
Texas module
============

This module presents two classes to handle the way state holidays are managed
in Texas.

The :class:`TexasBase` class gathers all available holidays for Texas,
according to this document:
http://www.statutes.legis.state.tx.us/Docs/GV/htm/GV.662.htm

The :class:`Texas` class includes all national and state holidays, as described
in the said document. This should be the "default" Texas calendar class, to be
used in most cases.

But if state holidays are supposed to be observed by most of the workforces,
any employee can chose to skip one of these days and replace it by another.

If at some point you need to create a specific calendar class based on Texas
calendar, you can either use the :class:`TexasBase` class or directly the
:class:`Texas` class and overwrite/override the :method:`get_fixed_holidays()`
and/or :method:`get_variable_days()` to fit your needs.

Example:

.. code::

    class TexasCustom(TexasBase):
        # This will include the confederate heroes day
        texas_include_confederate_heroes = True

        FIXED_HOLIDAYS = TexasBase.FIXED_HOLIDAYS + (
            (7, 14, "Bastille Day!"),
        )

        def get_variable_days(self, year):
            days = super(TexasCustom, self).get_variable_days(year)
            days.append(
                (self.get_nth_weekday_in_month(year, 1, 15), "Special Day")
            )
            return days

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
from .core import UnitedStates


class TexasBase(UnitedStates):
    """Texas Base (w/o State holidays)"""
    include_columbus_day = False
    texas_include_confederate_heroes = False
    texas_include_independance_day = False
    texas_san_jacinto_day = False
    texas_emancipation_day = False
    texas_lyndon_johnson_day = False
    # Non-Texas-specific state holidays
    include_thanksgiving_friday = False
    include_christmas_eve = False
    include_boxing_day = False

    def get_fixed_holidays(self, year):
        days = super(TexasBase, self).get_fixed_holidays(year)
        if self.texas_include_confederate_heroes:
            days.append(
                (date(year, 1, 19), "Confederate Heroes Day")
            )

        if self.texas_include_independance_day:
            days.append(
                (date(year, 3, 2), "Texas Independence Day")
            )

        if self.texas_san_jacinto_day:
            days.append(
                (date(year, 4, 21), "San Jacinto Day")
            )

        if self.texas_emancipation_day:
            days.append(
                (date(year, 6, 19), "Emancipation Day in Texas"),
            )

        if self.texas_lyndon_johnson_day:
            days.append(
                (date(year, 8, 27), "Lyndon B. Jonhson Day"),
            )
        return days


class Texas(TexasBase):
    """Texas"""
    texas_include_confederate_heroes = True
    texas_include_independance_day = True
    texas_san_jacinto_day = True
    texas_emancipation_day = True
    texas_lyndon_johnson_day = True
    include_thanksgiving_friday = True
    include_christmas_eve = True
    include_boxing_day = True
