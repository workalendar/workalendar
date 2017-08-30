# -*- coding: utf-8 -*-
from functools import wraps


class IsoRegistry(object):
    """
    Registry for all calendars retrievable by ISO 3166-2 codes associated with countries
    where they are used as official calendars.

    Two letter codes are favored for any subdivisions.
    """

    def __init__(self):
        self.region_registry = {}
        self.subregion_registry = {}

    def _code_elements(self, iso_code):
        code_elements = iso_code.split('-')
        is_subregion = False
        if len(code_elements) > 1:
            is_subregion = True
        return code_elements, is_subregion

    def register(self, iso_code, cls):
        _, is_subregion = self._code_elements(iso_code)
        target_registry = self.subregion_registry if is_subregion else self.region_registry
        target_registry[iso_code] = cls

    def get_instance(self, iso_code):
        """
        Retrieves calendar associated with given ``iso_code``.

        If calendar of subdivision is not registered (for subdivision like ISO codes, e.g. GB-ENG)
        returns calendar of containing region (e.g. United Kingdom for ISO code GB) if it's available.

        :rtype: Calendar
        """
        code_elements, is_subregion = self._code_elements(iso_code)
        if is_subregion and iso_code in self.subregion_registry:
            return self.subregion_registry.get(iso_code)
        return self.region_registry.get(code_elements[0])

    def items(self):
        return self.region_registry.items() + self.subregion_registry.items()


registry = IsoRegistry()


def iso_register(iso_code):
    """
    Registers Calendar class as country or region in IsoRegistry.

    Registered country must set class variables ``iso`` and ``name``.

    >>> from workalendar.core import Calendar
    >>> from workalendar.registry import iso_register
    >>> @iso_register('MC-MR')
    >>> class MyRegion(Calendar):
    >>>     pass

    Region calendar is then retrievable from registry:

    >>> from workalendar.registry import registry
    >>> calendar = registry.get_instance('MC-MR')
    """
    def wrapper(cls):
        registry.register(iso_code, cls)
        return cls
    return wrapper


from workalendar.europe import *
