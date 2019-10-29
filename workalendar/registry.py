# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from importlib import import_module
import re


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

    IBGE_LIST = {
        'AC': 'BR-IBGE-12',  # Brazil Acre state
        'AL': 'BR-IBGE-27',  # Brazil Alagoas state
        'AP': 'BR-IBGE-16',  # Brazil Amapa state
        'AM': 'BR-IBGE-13',  # Brazil Amazonas state
        'BA': 'BR-IBGE-29',  # Brazil Bahia state
        'CE': 'BR-IBGE-23',  # Brazil Ceará state
        'DF': 'BR-IBGE-53',  # Brazil Distrito Federal state
        'ES': 'BR-IBGE-32',  # Brazil Espirito Santo state
        'GO': 'BR-IBGE-52',  # Brazil Goiás state
        'MA': 'BR-IBGE-21',  # Brazil Maranhão state
        'MG': 'BR-IBGE-31',  # Brazil Minas Gerais state
        'MT': 'BR-IBGE-51',  # Brazil Mato Grosso state
        'MS': 'BR-IBGE-50',  # Brazil Mato Grosso do Sul state
        'PA': 'BR-IBGE-15',  # Brazil Pará state
        'PB': 'BR-IBGE-25',  # Brazil Paraíba state
        'PE': 'BR-IBGE-26',  # Brazil Pernambuco state
        'PI': 'BR-IBGE-22',  # Brazil Piauí state
        'PR': 'BR-IBGE-41',  # Brazil Paraná state
        'RJ': 'BR-IBGE-33',  # Brazil Rio de Janeiro state
        'RN': 'BR-IBGE-24',  # Brazil Rio Grande do Norte state
        'RS': 'BR-IBGE-43',  # Brazil Rio Grande do Sul state
        'RO': 'BR-IBGE-11',  # Brazil Rondônia state
        'RR': 'BR-IBGE-14',  # Brazil Roraima state
        'SC': 'BR-IBGE-42',  # Brazil Santa Catarina state
        'SP': 'BR-IBGE-35',  # Brazil São Paulo state
        'SE': 'BR-IBGE-28',  # Brazil Sergipe state
        'TO': 'BR-IBGE-17',  # Brazil Tocantins state
    }

    def __init__(self, load_standard_modules=True):
        self.region_registry = dict()
        if load_standard_modules:
            for module_name in self.STANDARD_MODULES:
                module = 'workalendar.{}'.format(module_name)
                all_classes = getattr(import_module(module), '__all__')
                self.load_module_from_items(module, all_classes)

    def register(self, iso_code, cls):
        """
        Store the ``cls`` in the region_registry.
        """
        if type(iso_code) == tuple:
            for code in iso_code:
                self.region_registry[code] = cls
        else:
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
            if code_elements[1] == 'IBGE':
                if iso_code[:10] in self.region_registry:
                    code = iso_code[:10]
                else:
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
        items = dict()
        code_elements, is_subregion = self._code_elements(iso_code)
        # iso_code is a brazilian state
        if is_subregion and code_elements[1] in self.IBGE_LIST:
            iso_code = self.IBGE_LIST[code_elements[1]]

        # iso_code is a IBGE code brazilian state
        if re.search('BR-IBGE-..', iso_code):
            for key, value in self.region_registry.items():
                if re.search(iso_code + '.+', key):
                    items[key] = value
        else:
            for key, value in self.region_registry.items():
                code_elements, is_subregion = self._code_elements(key)
                if is_subregion and code_elements[0] == iso_code\
                        and code_elements[1] != 'IBGE':
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
        items = dict()
        for code in region_codes:
            try:
                items[code] = self.region_registry[code]
            except KeyError:
                continue
            if include_subregions:
                items.update(self.get_subregions(code))
        return items


registry = IsoRegistry()
