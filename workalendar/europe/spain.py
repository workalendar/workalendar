from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('ES')
class Spain(WesternCalendar):
    'Spain'

    # Christian holidays
    include_epiphany = True
    include_good_friday = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True

    # Civil holidays
    include_labour_day = True
    labour_day_label = "Día del trabajador"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (10, 12, "Fiesta nacional de España"),
        (12, 6, "Día de la Constitución Española")
    )


@iso_register('ES-AN')
class Andalusia(Spain):
    "Andalusia"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (2, 28, "Andalusian National Day"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-AR')
class Aragon(Spain):
    "Aragon"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (4, 23, "Aragonese National Day"),
        (12, 20, "Aragon Ombudsman Day"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-CL')
class CastileAndLeon(Spain):
    "Castile and León"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (4, 23, "Día de Castilla y León"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-CM')
class CastillaLaMancha(Spain):
    "Castilla-La Mancha"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (5, 31, "Día de la Región Castilla-La Mancha"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-CN')
class CanaryIslands(Spain):
    "Canary Islands"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (5, 30, "Día de Canarias"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-CT')
class Catalonia(Spain):
    "Catalonia"

    include_easter_monday = True
    include_boxing_day = True
    boxing_day_label = "Sant Esteve"

    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (9, 11, "Diada nacional de Catalunya"),
    )


@iso_register('ES-EX')
class Extremadura(Spain):
    "Extremadura"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (9, 8, "Día de Extremadura"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-GA')
class Galicia(Spain):
    "Galicia"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (5, 17, "Día das Letras Galegas"),
        (7, 25, "Santiago Apóstol o Día da Patria Galega"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday
