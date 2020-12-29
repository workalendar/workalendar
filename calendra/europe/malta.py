from ..core import WesternCalendar
from ..registry_tools import iso_register


@iso_register('MT')
class Malta(WesternCalendar):
    'Malta'

    # Christian holidays
    include_good_friday = True
    include_assumption = True
    include_immaculate_conception = True
    include_christmas = True

    # Civil holidays
    include_labour_day = True
    labour_day_label = "Worker's Day"  # (Jum il-Ħaddiem)
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        # National Holidays
        (3, 31, "Freedom Day"),            # (Jum il-Ħelsien)
        (6, 7, "Sette Giugno"),
        (9, 8, "Victory Day"),             # (Jum il-Vitorja)
        (9, 21, "Independence Day"),       # (Jum l-Indipendenza)
        (12, 13, "Republic Day"),          # (Jum ir-Repubblika)
        # Public Holidays
        (2, 10, "Feast of Saint Paul's Shipwreck"),
        (3, 19, "Feast of Saint Joseph"),  # (San Ġużepp)
        (6, 29, "Feast of Saint Peter & Saint Paul"),  # (L-Imnarja)
    )
