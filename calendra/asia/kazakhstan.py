from datetime import date
from ..core import OrthodoxCalendar, IslamicCalendar
from ..registry_tools import iso_register


@iso_register('KZ')
class Kazakhstan(OrthodoxCalendar, IslamicCalendar):
    'Kazakhstan'

    "Sources: "
    "https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan"

    include_christmas = False
    include_christmas_eve = False

    include_new_years_day = True
    include_orthodox_christmas = False
    include_epiphany = False
    include_good_friday = False
    include_easter_saturday = False
    include_easter_sunday = False
    include_easter_monday = False

    include_prophet_birthday = False
    include_day_after_prophet_birthday = False
    include_start_ramadan = False
    include_eid_al_fitr = False
    length_eid_al_fitr = 1
    include_eid_al_adha = False
    length_eid_al_adha = 1
    include_day_of_sacrifice = True
    day_of_sacrifice_label = "Eid al-Adha"
    include_islamic_new_year = False
    include_laylat_al_qadr = False
    include_nuzul_al_quran = False

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (3, 8, "international Woman's Day"),
        (3, 21, "Nauryz Meyramy"),
        (3, 22, "Nauryz Meyramy"),
        (3, 23, "Nauryz Meyramy"),
        (5, 1, "Unity Day"),
        (5, 9, "Day Of Victory Over Fascism"),
        (7, 6, "Capital City Day"),
        (8, 30, "Constitution Day"),
        (12, 16, "Independence Day"),
        (12, 17, "Independence Day"),
    )

    def get_fixed_holidays(self, year):

        # Orthodox Christmas is an official holiday in Kazakhstan since 2007
        # see https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan
        self.include_orthodox_christmas = (year >= 2007)
        days = super(OrthodoxCalendar, self).get_fixed_holidays(year)
        if year >= 2013:
            # The 'Day of the First President' and the
            # 'Defender of the Faterland Day' are celebrated only since 2013
            # see https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan
            days.append((date(year, 12, 1), "Day of the First President"))
            days.append((date(year, 5, 7), "Defender of the Fatherland Day"))

        return days

    def get_variable_days(self, year):

        # Kurban Ait (Eid al-Adha in islamic calendar) is an official holiday
        # in Kazakhstan since 2007
        self.include_day_of_sacrifice = (year >= 2007)
        days = super(IslamicCalendar, self).get_variable_days(year)
        return days
