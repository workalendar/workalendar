#-*- coding: utf-8 -*-
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import SUN, MON, THU, SAT


class UnitedStatesCalendar(WesternCalendar, ChristianMixin):
    "USA calendar"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 4, 'Independence Day'),
        (11, 11, 'Veterans Day'),
    )

    @staticmethod
    def is_presidential_year(year):
        return (year % 4) == 0

    def get_variable_days(self, year):
        # usual variable days
        days = super(UnitedStatesCalendar, self).get_variable_days(year)
        days += [
            (WesternCalendar.get_nth_weekday_in_month(year, 1, MON, 3),
                'Martin Luther King, Jr. Day'),

            (WesternCalendar.get_nth_weekday_in_month(year, 2, MON, 3),
                "Washington's Birthday"),

            (WesternCalendar.get_last_weekday_in_month(year, 5, MON),
                "Memorial Day"),

            (WesternCalendar.get_nth_weekday_in_month(year, 9, MON),
                "Labor Day"),

            (WesternCalendar.get_nth_weekday_in_month(year, 10, MON, 2),
                "Colombus Day"),

            (WesternCalendar.get_nth_weekday_in_month(year, 11, THU, 4),
                "Thanksgiving Day"),
        ]
        # Inauguration day
        if UnitedStatesCalendar.is_presidential_year(year - 1):
            inauguration_day = date(year, 1, 20)
            if inauguration_day.weekday() == SUN:
                inauguration_day = date(year, 1, 21)
            days.append((inauguration_day, "Inauguration Day"))
        return days


class BrazilCalendar(WesternCalendar, ChristianMixin):
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 21, "Tiradentes' Day"),
        (5, 1, "Labour Day"),
        (9, 7, "Independance Day"),
        (10, 12, "Our Lady of Aparecida"),
        (11, 2, "All Souls' Day"),
        (11, 15, "Republic Day"),
    )


class BrazilSaoPaoloStateCalendar(BrazilCalendar):
    FIXED_HOLIDAYS = BrazilCalendar.FIXED_HOLIDAYS + (
        (7, 9, "Constitutional Revolution of 1932"),
    )


class BrazilSaoPaoloCityCalendar(BrazilSaoPaoloStateCalendar):
    FIXED_HOLIDAYS = BrazilSaoPaoloStateCalendar.FIXED_HOLIDAYS + (
        (1, 25, "Aniversary of the city of São Paulo"),
        (11, 20, "Dia da Consciência Negra")
    )
    include_easter_sunday = True

    def get_corpus_christi(self, year):
        return self.get_easter_sunday(year) + timedelta(days=60)

    def get_carnaval(self, year):
        return self.get_easter_sunday(year) - timedelta(days=47)

    def get_variable_days(self, year):
        days = super(BrazilSaoPaoloCityCalendar, self).get_variable_days(year)
        days.append((self.get_carnaval(year), "Carnaval"))
        days.append((self.get_good_friday(year), "Sexta-feira da Paixão"))
        days.append((self.get_corpus_christi(year), "Corpus Christi"))
        return days


class MexicoCalendar(WesternCalendar, ChristianMixin):
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (9, 16, "Independance Day"),
    )

    def get_variable_days(self, year):
        days = super(MexicoCalendar, self).get_variable_days(year)
        days.append(
            (MexicoCalendar.get_nth_weekday_in_month(year, 2, MON),
             "Constitution Day"))

        days.append(
            (MexicoCalendar.get_nth_weekday_in_month(year, 3, MON, 3),
             "Benito Juárez's birthday"))

        days.append(
            (MexicoCalendar.get_nth_weekday_in_month(year, 11, MON, 3),
             "Revolution Day"))

        return days

    def get_calendar_holidays(self, year):
        days = super(MexicoCalendar, self).get_calendar_holidays(year)
        # If any statutory day is on Sunday, the monday is off
        # If it's on a Saturday, the Friday is off
        for day, label in days:
            if day.weekday() == SAT:
                days.append((day - timedelta(days=1), "%s substitute" % label))
            elif day.weekday() == SUN:
                days.append((day + timedelta(days=1), "%s substitute" % label))
        return days
