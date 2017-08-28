# -*- coding: utf-8 -*-
from workalendar.europe import (
    Austria, Germany, BadenWurttemberg, Bavaria, Berlin, Brandenburg, Bremen, Hamburg, Hesse, MecklenburgVorpommern,
    LowerSaxony, NorthRhineWestphalia, RhinelandPalatinate, Saarland, Saxony, SaxonyAnhalt, SchleswigHolstein,
    Thuringia, Switzerland
)


class IsoRegistry(object):

    def __init__(self):
        self.region_registry = {}
        self.subregion_registry = {}

    def _code_elements(self, iso_code):
        code_elements = iso_code.split('-')
        is_subregion = False
        if len(code_elements) > 1:
            is_subregion = True
        return code_elements, is_subregion

    def register(self, cls):
        _, is_subregion = self._code_elements(cls.iso)
        target_registry = self.subregion_registry if is_subregion else self.region_registry
        target_registry[cls.iso] = cls

    def get_instance(self, iso_code):
        code_elements, is_subregion = self._code_elements(iso_code)
        if is_subregion and iso_code in self.subregion_registry:
            return self.subregion_registry.get(iso_code)
        return self.region_registry.get(code_elements[0])

    def items(self):
        return self.region_registry.items() + self.subregion_registry.items()


registry = IsoRegistry()
registry.register(Austria)
registry.register(Germany)
registry.register(BadenWurttemberg)
registry.register(Bavaria)
registry.register(Berlin)
registry.register(Brandenburg)
registry.register(Bremen)
registry.register(Hamburg)
registry.register(Hesse)
registry.register(MecklenburgVorpommern)
registry.register(LowerSaxony)
registry.register(NorthRhineWestphalia)
registry.register(RhinelandPalatinate)
registry.register(Saarland)
registry.register(Saxony)
registry.register(SaxonyAnhalt)
registry.register(SchleswigHolstein)
registry.register(Thuringia)
registry.register(Switzerland)


# class MetaRegistered(type):
#     def __new__(mcs, name, bases, class_dict):
#         cls = type.__new__(mcs, name, bases, class_dict)
#         registry.register(name, cls)
#         return cls
#
#
# class RegisteredMixin(object):
#     __metaclass__ = MetaRegistered


# from workalendar.registry import registry
# print registry.items()
