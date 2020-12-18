from ..core import WesternCalendar


class EuropeanCentralBank(WesternCalendar):
    "European Central Bank"
    # Civil holidays
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (12, 26, "St. Stephen's Day"),
    )

    # Christian holidays
    include_good_friday = True
    include_easter_monday = True
