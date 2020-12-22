"""
Tools to update the ISO registry.
"""
from calendra.registry import registry


def iso_register(iso_code):
    """
    Registers Calendar class as country or region in IsoRegistry.

    Registered country must set class variables ``iso`` using this decorator.

    >>> from calendra.core import Calendar
    >>> @iso_register('MC-MR')
    ... class MyRegion(Calendar):
    ...     'My Region'

    Region calendar is then retrievable from registry:

    >>> calendar = registry.get_calendar_class('MC-MR')
    """

    def wrapper(cls):
        registry.register(iso_code, cls)
        return cls
    return wrapper
