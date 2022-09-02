from copy import copy
from datetime import timedelta, date

from ..core import IslamoWesternCalendar, SAT, SUN
from ..registry_tools import iso_register


@iso_register('KE')
class Kenya(IslamoWesternCalendar):
    "Kenya"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_good_friday = True
    include_easter_monday = True
    # Islamic holidays
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    shift_sunday_holidays = True

    # Explicitly assign these WE days, Kenya has adopted the western workweek
    WEEKEND_DAYS = (SAT, SUN)

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (6, 1, "Madaraka Day"),
        (10, 20, "Mashujaa Day"),
        (12, 12, "Jamhuri Day"),
        (12, 31, "New Years Eve"),
    )

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)

        if year >= 2020:
            days.append((date(year, 2, 11), 'Moi Memorial Day'))

        # Moi Day renamed
        huduma_day_label = "Moi Day"
        if year >= 2020:
            huduma_day_label = "Huduma Day"
        days.append((date(year, 10, 10), huduma_day_label))

        # Boxing day renamed
        boxing_day_label = "Boxing Day"
        if year >= 2020:
            boxing_day_label = "Utamaduni Day"
        days.append((date(year, 12, 26), boxing_day_label))

        return days

    def get_shifted_holidays(self, dates):
        """
        Taking a list of existing holidays, yield a list of 'shifted' days if
        the holiday falls on SUN, excluding the Islamic holidays.
        """
        for holiday, label in dates:
            if (holiday.weekday() == SUN and
                    label != self.eid_al_fitr_label and
                    label != self.day_of_sacrifice_label):
                yield (
                    holiday + timedelta(days=1),
                    f'{label} Shift'
                )

    def get_calendar_holidays(self, year):
        """
        Take into account the eventual shift to the next MON if any holiday
        falls on SUN.
        """
        # Unshifted days are here:
        days = super().get_calendar_holidays(year)
        if self.shift_sunday_holidays:
            days_to_inspect = copy(days)
            for day_shifted in self.get_shifted_holidays(days_to_inspect):
                days.append(day_shifted)
        return days
