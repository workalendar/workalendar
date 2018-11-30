"""
Core Workalendar Exceptions
"""


class CalendarError(Exception):
    """
    Base Calendar Error
    """


class UnsupportedDateType(CalendarError):
    """
    Raised when trying to use an unsupported date/datetime type.
    """
