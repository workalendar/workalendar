# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
"""
Virginia module

You may or may want not to treat the Day before Thanksgiving as a non-working
day by implementing the following class:

.. code::

    from workalenda.usa import Virginia as VirginiaBase

    class Virginia(VirginiaBase):
        include_thanksgiving_wednesday = False

"""
from ..core import WED, FRI
from ..registry import iso_register
from .core import UnitedStates


@iso_register('US-VA')
class Virginia(UnitedStates):
    """Virginia"""
    include_christmas_eve = True
    include_thanksgiving_friday = True
    include_boxing_day = True
    presidents_day_label = "George Washington Day"
    # Virginia specific. By default, it's treated as a holiday, but
    # you may chose to exclude it for you own uses. See the module doc.
    include_thanksgiving_wednesday = True

    def get_variable_days(self, year):
        days = super(Virginia, self).get_variable_days(year)
        days.append(
            (self.get_nth_weekday_in_month(year, 1, FRI, 3),
             "Lee-Jackson Day")
        )
        if self.include_thanksgiving_wednesday:
            days.append(
                (self.get_nth_weekday_in_month(year, 11, WED, 4),
                 "Day before Thanksgiving (start at noon)")
            )

        return days
