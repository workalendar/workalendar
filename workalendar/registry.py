# -*- coding: utf-8 -*-
from collections import OrderedDict


class IsoRegistry(object):
    """
    Registry for all calendars retrievable
    by ISO 3166-2 codes associated with countries
    where they are used as official calendars.

    Two letter codes are favored for any subdivisions.
    """

    def __init__(self):
        self.region_registry = OrderedDict()

    def _code_elements(self, iso_code):
        code_elements = iso_code.split('-')
        is_subregion = False
        if len(code_elements) > 1:
            is_subregion = True
        return code_elements, is_subregion

    def register(self, iso_code, cls):
        self.region_registry[iso_code] = cls

    def get_calendar_class(self, iso_code):
        """
        Retrieves calendar class associated with given ``iso_code``.

        If calendar of subdivision is not registered
        (for subdivision like ISO codes, e.g. GB-ENG)
        returns calendar of containing region
        (e.g. United Kingdom for ISO code GB) if it's available.

        :rtype: Calendar
        """
        code_elements, is_subregion = self._code_elements(iso_code)
        if is_subregion and iso_code not in self.region_registry:
            # subregion code not in region_registry
            code = code_elements[0]
        else:
            # subregion code in region_registry or is not a subregion
            code = iso_code
        return self.region_registry.get(code)

    def get_subregions(self, iso_code):
        """
        Returns subregion calendar classes for given region iso_code.

        >>> registry = IsoRegistry()
        >>> # assuming calendars registered are: DE, DE-HH, DE-BE
        >>> registry.get_subregions('DE')
        {'DE-HH': <class 'workalendar.europe.germany.Hamburg'>,
        'DE-BE': <class 'workalendar.europe.germany.Berlin'>}
        :rtype dict
        :return dict where keys are ISO codes strings
        and values are calendar classes
        """
        items = OrderedDict()
        for key, value in self.region_registry.items():
            code_elements, is_subregion = self._code_elements(key)
            if is_subregion and code_elements[0] == iso_code:
                items[key] = value
        return items

    def items(self, regions, include_subregions=False):
        """
        Returns calendar classes for regions

        :param regions list of ISO codes for selected regions
        :param include_subregions boolean if subregions
        of selected regions should be included in result
        :rtype dict
        :return dict where keys are ISO codes strings
        and values are calendar classes
        """
        items = OrderedDict()
        for region in regions:
            try:
                items[region] = self.region_registry[region]
            except KeyError:
                continue
            if include_subregions:
                items.update(self.get_subregions(region))
        return items


registry = IsoRegistry()


def iso_register(iso_code):
    """
    Registers Calendar class as country or region in IsoRegistry.

    Registered country must set class variables ``iso`` and ``name``.

    >>> from workalendar.core import Calendar
    >>> @iso_register('MC-MR')
    >>> class MyRegion(Calendar):
    >>>     pass

    Region calendar is then retrievable from registry:

    >>> calendar = registry.get_calendar_class('MC-MR')
    """
    def wrapper(cls):
        registry.register(iso_code, cls)
        return cls
    return wrapper


# right now only european countries are supported in the ISO registry
from workalendar.europe import *        # NoQA
