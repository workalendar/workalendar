from .core import UnitedStates
from ..registry_tools import iso_register

# FIXME: According to wikipedia, Kansas only has all federal holidays, except
# the Columbus Day and Washington's Birthday.
# Unfortunately, other sources mention XMas Eve for 2018, but not for other
# years.
# I'm a bit sad here...
#
# Sources to lookup, if you want to help:
# * http://www.admin.ks.gov/docs/default-source/ops/holidays/holidays2018.pdf
# * http://www.kansas.gov/employee/documents/2017calendar.pdf
# * https://publicholidays.us/kansas/2018-dates/
# * https://en.wikipedia.org/wiki/Public_holidays_in_the_United_States#Kansas
# * https://publicholidays.us/kansas/2018-dates/


@iso_register('US-KS')
class Kansas(UnitedStates):
    """Kansas"""
    include_federal_presidents_day = False
    include_columbus_day = False
