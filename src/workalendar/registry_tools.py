"""
Tools to update the ISO registry.
"""


def iso_register(iso_code):
    """
    Registers Calendar class as country or region in IsoRegistry.

    Registered country must set class variables ``iso`` using this decorator.

    >>> from workalendar.core import Calendar
    >>> @iso_register('MC-MR')
    >>> class MyRegion(Calendar):
    >>>     'My Region'

    Region calendar is then retrievable from registry:

    >>> calendar = registry.get('MC-MR')
    """
    def wrapper(cls):
        cls.__iso_code = (iso_code, cls.__name__)
        return cls
    return wrapper
