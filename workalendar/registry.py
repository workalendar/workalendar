# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import warnings
from collections import OrderedDict
from importlib import import_module


class IsoRegistry(object):
    """
    Registry for all calendars retrievable
    by ISO 3166-2 codes associated with countries
    where they are used as official calendars.

    Two letter codes are favored for any subdivisions.
    """

    STANDARD_MODULES = (
        # Europe Countries
        'europe',
        # United States of America
        'usa',
        # American continent outside of USA
        'america',
        # African continent
        'africa',
        # Asia
        'asia',
        # Oceania
        'oceania',
    )

    def __init__(self, load_standard_modules=True):
        warnings.warn(
            "The use of ``OrderedDict`` objects in the registry feature is "
            "about to be deprecated, in favor of plain ``dict`` objects",
            DeprecationWarning
        )
        self.region_registry = OrderedDict()
        if load_standard_modules:
            for module_name in self.STANDARD_MODULES:
                module = 'workalendar.{}'.format(module_name)
                all_classes = getattr(import_module(module), '__all__')
                self.load_module_from_items(module, all_classes)

    def register(self, iso_code, cls):
        """
        Store the ``cls`` in the region_registry.
        """
        self.region_registry[iso_code] = cls

    def load_module_from_items(self, module_name, items):
        """
        Load all registered classes in the registry
        """
        for item in items:
            cls = getattr(import_module(module_name), item)
            iso_stuff = getattr(cls, '__iso_code', None)
            if iso_stuff:
                iso_code, class_name = iso_stuff
                if iso_code and cls.__name__ == class_name:
                    self.register(iso_code, cls)

    def _code_elements(self, iso_code):
        code_elements = iso_code.split('-')
        is_subregion = False
        if len(code_elements) > 1:
            is_subregion = True
        return code_elements, is_subregion

    def get_calendar_class(self, iso_code):
        """
        Retrieve calendar class associated with given ``iso_code``.

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

    def items(self, region_codes, include_subregions=False):
        """
        Returns calendar classes for regions

        :param region_codes list of ISO codes for selected regions
        :param include_subregions boolean if subregions
        of selected regions should be included in result
        :rtype dict
        :return dict where keys are ISO codes strings
        and values are calendar classes
        """
        items = OrderedDict()
        for code in region_codes:
            try:
                items[code] = self.region_registry[code]
            except KeyError:
                continue
            if include_subregions:
                items.update(self.get_subregions(code))
        return items


registry = IsoRegistry()
