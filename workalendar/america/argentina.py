from datetime import timedelta, date
from ..core import (
    WesternCalendar, ChristianMixin,
    MON, TUE, WED, THU, FRI, SAT
)
from ..registry_tools import iso_register


@iso_register('AR')
class Argentina(WesternCalendar, ChristianMixin):
    'Argentina'

    include_good_friday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 24, "Día Nacional de la Memoria por la Verdad y la Justicia"),
        (5, 1, "Día del Trabajador"),
        (5, 25, "Día de la Revolución de Mayo"),
        (6, 20, "Día Paso a la Inmortalidad del General Manuel Belgrano"),
        (7, 9, "Día de la Independencia"),
        (12, 8, "Día de la Inmaculada Concepción de María"),
    )

    def get_general_guemes_day(self, year):
        """
        Día Paso a la Inmortalidad del General Martín Miguel de Güemes.

        Happens on June 17th, except:

        * if it happens on a THU, it's shifted to the next MON.
        * if it happens on a WED, it's shifted to the MON before this date.
        """
        general_guemes_day = date(year, 6, 17)

        if general_guemes_day.weekday() == THU:
            general_guemes_day = Argentina.get_first_weekday_after(
                date(year, 6, 17), MON)
        elif general_guemes_day.weekday() == WED:
            # Monday of the same week
            general_guemes_day = general_guemes_day - timedelta(days=2)
        else:
            general_guemes_day

        return (general_guemes_day,
                "Día Paso a la Inmortalidad del " +
                "General Martín Miguel de Güemes")

    def get_general_martin_day(self, year):
        """
        Día Paso a la Inmortalidad del Gral. José de San Martín

        Third MON of August.
        """
        general_martin_day = Argentina.get_nth_weekday_in_month(
            year, 8, MON, 3
        )

        return (general_martin_day,
                "Día Paso a la Inmortalidad del " +
                "Gral. José de San Martín")

    def get_soberania_day(self, year):
        """
        Día de la Soberanía Nacional

        Happens on the 3rd MON of November after the first Friday.
        """
        first_friday_november = Argentina.get_nth_weekday_in_month(
            year, 11, FRI, 1
        )

        soberania_day = Argentina.get_nth_weekday_in_month(
            year, 11, MON, n=3, start=first_friday_november
        )

        return (soberania_day, "Día de la Soberanía Nacional")

    def get_diversidad_day(self, year):
        """
        Día del Respeto a la Diversidad Cultural

        The pivot date is the 12th of October.

        * If it happens on a TUE, it's shifter on the 11th of Oct.
        * If it happens on a WED, THU, FRI or SAT, it's shifted on the first
          MON after this date.
        * Else, it's on the 12th of October.
        """
        diversidad_day = date(year, 10, 12)

        if (diversidad_day.weekday() == WED or
                diversidad_day.weekday() == THU or
                diversidad_day.weekday() == FRI or
                diversidad_day.weekday() == SAT):
            diversidad_day = Argentina.get_first_weekday_after(
                date(year, 10, 12), MON
            )
        elif diversidad_day.weekday() == TUE:
            diversidad_day = diversidad_day - timedelta(days=1)
        else:
            diversidad_day

        return (diversidad_day,
                "Día del Respeto a la Diversidad Cultural")

    def get_malvinas_day(self, year):
        """
        Día de las Malvinas

        In honour of the Veterans and the Fallen of the Malvinas war.
        https://en.wikipedia.org/wiki/Malvinas_Day

        In 2020, it was shifted to March 31st because of
        the coronavirus crisis.
        """
        label = "Día del Veterano y de los Caídos en la Guerra de Malvinas"
        if year == 2020:
            day = date(year, 3, 31)
        else:
            day = date(year, 4, 2)
        return (day, label)

    def get_variable_days(self, year):

        days = super().get_variable_days(year)
        days.append(
            (self.get_easter_sunday(year) - timedelta(days=48),
                "Carnival Lunes"))

        days.append(
            (self.get_easter_sunday(year) - timedelta(days=47),
                "Carnival"))

        days.append(
            self.get_malvinas_day(year))

        days.append(
            (self.get_general_guemes_day(year)))

        days.append(
            (self.get_general_martin_day(year)))

        days.append(
            (self.get_soberania_day(year)))

        days.append(
            (self.get_diversidad_day(year)))

        return days
