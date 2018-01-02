# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
"""
West Virginia

Christmas Eve and New Years Eve are considered as half-holidays. By default,
they're not included as "non-working days". If for your personal use you want
to include them, you may just have to create a class like this:

.. code::

    class WestVirginiaIncludeEves(WestVirginia):
        west_virginia_include_christmas_eve = True
        west_virginia_include_nye = True

"""
from datetime import date

from .core import UnitedStates


class WestVirginia(UnitedStates):
    """West Virginia"""
    include_thanksgiving_friday = True
    include_election_day_even = True
    election_day_label = "Election Day / Susan B. Anthony Day"

    # West Virginia specific "half-holidays"
    west_virginia_include_christmas_eve = False
    west_virginia_include_nye = False
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (6, 20, "West Virgina Day"),
    )
    shift_exceptions = (
        (12, 24),
        (12, 31),
    )

    def get_fixed_holidays(self, year):
        days = super(WestVirginia, self).get_fixed_holidays(year)
        if self.west_virginia_include_christmas_eve:
            days.append(
                (date(year, 12, 24), "Christmas Eve")
            )
        if self.west_virginia_include_nye:
            days.append(
                (date(year, 12, 31), "New Years Eve")
            )
        return days
