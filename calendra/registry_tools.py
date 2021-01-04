"""
Tools to update the ISO registry.
"""


def iso_register(iso_code):
    """
    Registers Calendar class as country or region in IsoRegistry.

    Registered country must set class variables ``iso`` using this decorator.

    >>> from calendra.core import Calendar
    >>> from calendra.registry import registry
    >>> from calendra.registry_tools import iso_register
    >>> @iso_register('MC-MR')
    ... class MyRegion(Calendar):
    ...     'My Region'

    Region calendar is then retrievable from registry:

    >>> calendar = registry.get('MC-MR')
    """

    def wrapper(cls):
        from calendra.registry import registry
        registry.register(iso_code, cls)
        return cls
    return wrapper
