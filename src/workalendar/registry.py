from importlib import import_module

from .core import Calendar
from .exceptions import ISORegistryError


class IsoRegistry:
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
        self.region_registry = dict()
        if load_standard_modules:
            for module_name in self.STANDARD_MODULES:
                module = f'workalendar.{module_name}'
                all_classes = getattr(import_module(module), '__all__')
                self.load_module_from_items(module, all_classes)

    def register(self, iso_code, cls):
        """
        Store the ``cls`` in the region_registry.
        """
        if not issubclass(cls, Calendar):
            raise ISORegistryError(
                f"Class `{cls}` is not a Calendar class"
            )
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

    def get(self, iso_code):
        """
        Retrieve calendar class associated with given ``iso_code``.

        If calendar of subdivision is not registered
        (for subdivision like ISO codes, e.g. GB-ENG)
        returns calendar of containing region
        (e.g. United Kingdom for ISO code GB) if it's available.

        :rtype: Calendar
        """
        return self.region_registry.get(iso_code)

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
        for key, value in self.region_registry.items():
            if key.startswith(f"{iso_code}-"):
                items[key] = value
        return items

    def get_calendars(self, region_codes=None, include_subregions=False):
        """
        Returns calendar classes for regions

        :param region_codes list of ISO codes for selected regions. If empty,
                            the function will return all items from the
                            registry.
        :param include_subregions boolean if subregions
        of selected regions should be included in result
        :rtype dict
        :return dict where keys are ISO codes strings
        and values are calendar classes
        """
        if not region_codes:
            # Here it contains all subregions
            if include_subregions:
                return self.region_registry.copy()
            items = {k: v for k, v in self.region_registry.items()
                     if '-' not in k}
            return items

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
