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
        (6, 24, "La revetlla de Sant Joan, Nit de Sant Joan"),
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


@iso_register('ES-IB')
class BalearicIslands(Spain):
    "Balearic Islands"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (3, 1, "Dia de les Illes Balears"),
    )
    # Christian holidays
    include_holy_thursday = True  # Also called Maundy thursday
    include_easter_monday = True


@iso_register('ES-RI')
class LaRioja(Spain):
    "La Rioja"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (6, 9, "Dia de La Rioja"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-MD')
class CommunityofMadrid(Spain):
    "Community of Madrid"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (5, 2, "Fiesta de la Comunidad de Madrid"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-MC')
class Murcia(Spain):
    "Region of Murcia"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (6, 9, "Día de la Región de Murcia"),
        (3, 19, "San José"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-NA')
class Navarre(Spain):
    "Navarre"
    # Christian holidays
    include_holy_thursday = True  # Also called Maundy thursday
    include_easter_monday = True


@iso_register('ES-AS')
class Asturias(Spain):
    "Asturias"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (9, 8, "Día de Asturias"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-PV')
class BasqueCountry(Spain):
    "Basque Country"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (10, 25, "Euskadi Eguna"),
    )
    # Christian holidays
    include_holy_thursday = True  # Also called Maundy thursday
    include_easter_monday = True


@iso_register('ES-CB')
class Cantabria(Spain):
    "Cantabria"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (9, 15, "Día de Cantabria o Día de La Montaña"),
    )
    # Christian holiday
    include_holy_thursday = True  # Also called Maundy thursday


@iso_register('ES-VC')
class ValencianCommunity(Spain):
    "Valencian Community"
    FIXED_HOLIDAYS = Spain.FIXED_HOLIDAYS + (
        (3, 19, "San José"),
        (10, 9, "Dia de la Comunitat Valenciana"),
    )
    # Christian holiday
    include_easter_monday = True
