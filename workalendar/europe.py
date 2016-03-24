# -*- coding: utf-8 -*-
from datetime import date, timedelta
from workalendar.core import WesternCalendar, ChristianMixin, OrthodoxMixin
from workalendar.core import THU, MON, FRI, SAT


class CzechRepublic(WesternCalendar, ChristianMixin):
    "Czech Republic"
    include_easter_monday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 1, "Restoration Day of the Independent Czech State"),
        (5, 1, "Labour Day"),
        (5, 8, "Liberation Day"),
        (7, 5, "Saints Cyril and Methodius Day"),
        (7, 6, "Jan Hus Day"),
        (9, 28, "St. Wenceslas Day (Czech Statehood Day)"),
        (10, 28, "Independent Czechoslovak State Day"),
        (11, 17, "Struggle for Freedom and Democracy Day"),
        (12, 24, "Christmas Eve"),
        (12, 26, "St. Stephen's Day (The Second Christmas Day)"),
    )


class Denmark(WesternCalendar, ChristianMixin):
    "Denmark"
    include_palm_sunday = True
    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost Sunday"
    include_whit_monday = True
    whit_monday_label = "Pentecost Monday"
    include_boxing_day = True
    boxing_day_label = "Second Day of Christmas"
    include_christmas_eve = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (6, 5, "Constitution Day"),
        (12, 31, "New Year's Eve")
    )

    def get_store_bededag(self, year):  # 'great prayer day'
        easter_sunday = self.get_easter_sunday(year)
        return easter_sunday + timedelta(days=26)

    def get_variable_days(self, year):
        days = super(Denmark, self).get_variable_days(year)
        days.append((self.get_store_bededag(year), "Store Bededag"))
        return days


class Slovakia(WesternCalendar, ChristianMixin):
    "Slovakia"
    include_epiphany = True
    include_easter_monday = True
    include_good_friday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 1, "Day of the Establishment of the Slovak Republic"),
        (5, 1, "Labour Day"),
        (5, 8, "Liberation Day"),
        (7, 5, "Saints Cyril and Methodius Day"),
        (8, 29, "Slovak National Uprising anniversary"),
        (9, 1, "Day of the Constitution of the Slovak Republic"),
        (9, 15, "Day of Blessed Virgin Mary, patron saint of Slovakia"),
        (11, 1, "All Saints’ Day"),
        (11, 17, "Struggle for Freedom and Democracy Day"),
        (12, 24, "Christmas Eve"),
        (12, 25, "Christmas Day"),
        (12, 26, "St. Stephen's Day (The Second Christmas Day)"),
    )


class Sweden(WesternCalendar, ChristianMixin):
    "Sweden"
    include_epiphany = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost"
    # Christmas Eve is not a holiday but not a work day either
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = "Second Day of Christmas"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 6, "National Day"),
        # New Year's Eve is not a holiday but not a work day either
        (12, 31, "New Year's Eve")
    )

    # Midsummer Eve is not a holiday but not a work day either
    def get_midsummer_eve(self, year):
        date_eve = Sweden.get_nth_weekday_in_month(
            year, 6, FRI, start=date(year, 6, 19))
        return date_eve

    def get_midsummer_day(self, year):
        date_eve = Sweden.get_nth_weekday_in_month(
            year, 6, SAT, start=date(year, 6, 20))
        return date_eve

    def get_variable_all_saints(self, year):
        all_saints = date(year, 10, 31)
        if all_saints.weekday() != SAT:
            all_saints = Sweden.get_nth_weekday_in_month(
                year, 11, SAT)
        return all_saints

    def get_variable_days(self, year):
        days = super(Sweden, self).get_variable_days(year)
        days.append((self.get_midsummer_day(year), "Midsummer's Day"))
        days.append((self.get_midsummer_eve(year), "Midsummer's Eve"))
        days.append((self.get_variable_all_saints(year), "All Saints"))
        return days


class Finland(WesternCalendar, ChristianMixin):
    "Finland"
    include_epiphany = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    whit_sunday_label = 'Pentecost'
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = "St. Stephen's Day"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (12, 6, "Independence Day"),
    )

    def get_midsummer_eve(self, year):
        date_eve = Finland.get_nth_weekday_in_month(
            year, 6, FRI, start=date(year, 6, 19))
        return date_eve

    def get_midsummer_day(self, year):
        date_eve = Finland.get_nth_weekday_in_month(
            year, 6, SAT, start=date(year, 6, 20))
        return date_eve

    def get_variable_all_saints(self, year):
        all_saints = date(year, 10, 31)
        if all_saints.weekday() != SAT:
            all_saints = Finland.get_nth_weekday_in_month(
                year, 11, SAT)
        return all_saints

    def get_variable_days(self, year):
        days = super(Finland, self).get_variable_days(year)
        days.append((self.get_midsummer_eve(year), "Midsummer's Eve"))
        days.append((self.get_midsummer_day(year), "Midsummer's Day"))
        days.append((self.get_variable_all_saints(year), "All Saints"))
        return days


class France(WesternCalendar, ChristianMixin):
    "France"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_all_saints = True
    include_assumption = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (5, 8, "Victory in Europe Day"),
        (7, 14, "Bastille Day"),
        (11, 11, "Armistice Day"),
    )


class Luxembourg(WesternCalendar, ChristianMixin):
    "Luxembourg"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_all_saints = True
    include_assumption = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 23, "Luxembourg National Holiday"),
    )


class Netherlands(WesternCalendar, ChristianMixin):
    "Netherlands"
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 5, "Liberation Day"),
        (12, 31, "New Year's Eve"),
    )

    def get_kingsday(self, year):
        """27 April unless this is a Sunday in which case it is the 26th """
        if (date(year, 4, 27).weekday() != 6):
            return date(year, 4, 27)
        return date(year, 4, 26)

    def get_variable_days(self, year):
        days = super(Netherlands, self).get_variable_days(year)
        days += [
            (
                self.get_kingsday(year),
                "King's Day")
        ]
        return days


class FranceAlsaceMoselle(France):
    "France Alsace/Moselle"
    include_good_friday = True
    include_boxing_day = True


class Greece(OrthodoxMixin, WesternCalendar):
    "Greece"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 25, "Independence Day"),
        (5, 1, "Labour Day"),
        (10, 28, "Ohi Day"),
    )
    include_epiphany = True
    include_clean_monday = True
    include_annunciation = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost"
    include_whit_monday = True
    include_assumption = True
    include_boxing_day = True
    boxing_day_label = "Glorifying Mother of God"


class Hungary(WesternCalendar, ChristianMixin):
    "Hungary"
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost Sunday"
    include_whit_monday = True
    whit_monday_label = "Pentecost Monday"
    include_boxing_day = True
    boxing_day_label = "Second Day of Christmas"
    include_all_saints = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 15, "National Day"),
        (5, 1, "Labour Day"),
        (8, 20, "St Stephen's Day"),
        (10, 23, "National Day"),
    )


class Iceland(WesternCalendar, ChristianMixin):
    "Iceland"
    include_holy_thursday = True
    include_good_friday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_christmas_eve = True
    include_boxing_day = True
    boxing_day_label = "St Stephen's Day"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (6, 17, "Icelandic National Day"),
        (12, 31, "New Year's Eve"),
    )

    def get_first_day_of_summer(self, year):
        """It's the first thursday *after* April, 18th.
        If April the 18th is a thursday, then it jumps to the 24th.
        """
        return WesternCalendar.get_nth_weekday_in_month(
            year, 4, THU,
            start=date(year, 4, 19))

    def get_variable_days(self, year):
        days = super(Iceland, self).get_variable_days(year)
        days += [
            (
                self.get_first_day_of_summer(year),
                "First day of summer"),
            (
                Iceland.get_nth_weekday_in_month(year, 8, MON),
                "Commerce Day"),
        ]
        return days


class Italy(WesternCalendar, ChristianMixin):
    "Italy"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 25, "Liberation Day"),
        (5, 1, "International Workers' Day"),
        (6, 2, "Republic Day"),
    )
    include_immaculate_conception = True
    include_epiphany = True
    include_easter_monday = True
    include_assumption = True
    include_all_saints = True
    include_assumption = True
    include_boxing_day = True
    boxing_day_label = "St Stephen's Day"


class Norway(WesternCalendar, ChristianMixin):
    "Norway"
    include_holy_thursday = True
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_whit_sunday = True
    include_boxing_day = True
    boxing_day_label = "St Stephen's Day"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (5, 17, "Constitution Day"),
    )


class Poland(WesternCalendar, ChristianMixin):
    "Poland"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 6, 'Trzech Kroli'),
        (5, 1, 'Labour Day'),
        (5, 3, 'Constitution Day'),
        (11, 11, 'Independence Day'),
    )
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    whit_sunday_label = "Pentecost Sunday"
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_boxing_day = True


class UnitedKingdom(WesternCalendar, ChristianMixin):
    "United Kingdom"
    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_boxing_day = True
    shift_new_years_day = True

    def get_early_may_bank_holiday(self, year):
        return (
            UnitedKingdom.get_nth_weekday_in_month(year, 5, MON),
            "Early May Bank Holiday"
        )

    def get_spring_bank_holiday(self, year):
        return (
            UnitedKingdom.get_last_weekday_in_month(year, 5, MON),
            "Spring Bank Holiday"
        )

    def get_late_summer_bank_holiday(self, year):
        return (
            UnitedKingdom.get_last_weekday_in_month(year, 8, MON),
            "Late Summer Bank Holiday"
        )

    def get_variable_days(self, year):
        days = super(UnitedKingdom, self).get_variable_days(year)
        days.append(self.get_early_may_bank_holiday(year))
        days.append(self.get_spring_bank_holiday(year))
        days.append(self.get_late_summer_bank_holiday(year))
        # Boxing day & XMas shift
        christmas = date(year, 12, 25)
        boxing_day = date(year, 12, 26)
        if christmas.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(christmas)
            days.append((shift, "Christmas Shift"))
            days.append((shift + timedelta(days=1), "Boxing Day Shift"))
        elif boxing_day.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(boxing_day)
            days.append((shift, "Boxing Day Shift"))
        return days


class UnitedKingdomNorthernIreland(UnitedKingdom):
    "Northern Ireland (UK)"
    def get_variable_days(self, year):
        days = super(UnitedKingdomNorthernIreland, self) \
            .get_variable_days(year)
        # St Patrick's day
        st_patrick = date(year, 3, 17)
        days.append((st_patrick, "Saint Patrick's Day"))
        if st_patrick.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(st_patrick),
                "Saint Patrick substitute"))

        # Battle of boyne
        battle_of_boyne = date(year, 7, 12)
        days.append((battle_of_boyne, "Battle of the Boyne"))
        if battle_of_boyne.weekday() in self.get_weekend_days():
            days.append((
                self.find_following_working_day(battle_of_boyne),
                "Battle of the Boyne substitute"))
        return days


class EuropeanCentralBank(WesternCalendar, ChristianMixin):
    "European Central Bank"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (12, 26, "St. Stephen's Day"),
    )

    include_good_friday = True
    include_easter_monday = True


class Belgium(WesternCalendar, ChristianMixin):
    "Belgium"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (7, 21, "National Day"),
        (11, 11, "Armistice of 1918"),
    )

    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True


class Germany(WesternCalendar, ChristianMixin):
    "Germany"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (10, 3, "Day of German Unity"),
    )

    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_good_friday = True
    include_boxing_day = True
    boxing_day_label = "Second Christmas Day"


class BadenWurttemberg(Germany):
    "Baden-Württemberg"

    include_epiphany = True
    include_corpus_christi = True
    include_all_saints = True


class Bavaria(Germany):
    "Bavaria"

    include_epiphany = True
    include_corpus_christi = True
    include_all_saints = True
    include_assumption = True


class Berlin(Germany):
    "Berlin"


class Brandenburg(Germany):
    "Brandenburg"

    FIXED_HOLIDAYS = Germany.FIXED_HOLIDAYS + (
        (10, 31, "Reformation Day"),
    )


class Bremen(Germany):
    "Bremen"


class Hamburg(Germany):
    "Hamburg"


class Hesse(Germany):
    "Hesse"

    include_corpus_christi = True


class MecklenburgVorpommern(Germany):
    "Mecklenburg-Vorpommern"

    FIXED_HOLIDAYS = Germany.FIXED_HOLIDAYS + (
        (10, 31, "Reformation Day"),
    )


class LowerSaxony(Germany):
    "Lower Saxony"


class NorthRhineWestphalia(Germany):
    "North Rhine-Westphalia"

    include_corpus_christi = True
    include_all_saints = True


class RhinelandPalatinate(Germany):
    "Rhineland-Palatinate"

    include_corpus_christi = True
    include_all_saints = True


class Saarland(Germany):
    "Saarland"

    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True


class Saxony(Germany):
    "Saxony"

    FIXED_HOLIDAYS = Germany.FIXED_HOLIDAYS + (
        (10, 31, "Reformation Day"),
    )

    def get_repentance_day(self, year):
        "Wednesday before November 23"
        day = date(year, 11, 23)
        while day.weekday() != 2:  # 2=Wednesday
            day -= timedelta(days=1)
        return (day, "Repentance Day")

    def get_variable_days(self, year):
        days = super(Germany, self).get_variable_days(year)
        days.append(self.get_repentance_day(year))
        return days


class SaxonyAnhalt(Germany):
    "Saxony-Anhalt"

    FIXED_HOLIDAYS = Germany.FIXED_HOLIDAYS + (
        (10, 31, "Reformation Day"),
    )

    include_epiphany = True


class SchleswigHolstein(Germany):
    "Schleswig-Holstein"


class Thuringia(Germany):
    "Thuringia"

    FIXED_HOLIDAYS = Germany.FIXED_HOLIDAYS + (
        (10, 31, "Reformation Day"),
    )


class Portugal(WesternCalendar, ChristianMixin):
    "Portugal"
    include_good_friday = True
    include_easter_sunday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 25, "Dia da Liberdade"),
        (5, 1, "Dia do Trabalhador"),
        (6, 10, "Dia de Portugal"),
        (8, 15, "Assunção de Nossa Senhora"),
        (12, 8, "Imaculada Conceição"),
    )

    def get_variable_entrudo(self, year):
        easter_sunday = self.get_easter_sunday(year)
        return easter_sunday - timedelta(days=47)

    def get_variable_days(self, year):
        days = super(Portugal, self).get_variable_days(year)
        days.append((self.get_variable_entrudo(year), "Entrudo"))

        return days


class Spain(WesternCalendar, ChristianMixin):
    "Spain"
    include_epiphany = True
    include_immaculate_conception = True
    include_good_friday = True
    include_assumption = True
    include_all_saints = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, u"Día del trabajador"),
        (10, 12, u"Fiesta nacional de España"),
        (12, 6, u"Día de la Constitución Española")
    )


class Slovenia(WesternCalendar, ChristianMixin):
    "Slovenia"
    include_easter_sunday = True
    include_easter_monday = True
    include_whit_sunday = True
    include_assumption = True
    include_christmas = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 8, "Preseren Day, the Slovenian Cultural Holiday"),
        (4, 27, "Day of Uprising Against Occupation"),
        (5, 1, "Labour Day"),
        (5, 2, "Labour Day"),
        (6, 25, "Statehood Day"),
        (10, 31, "Reformation Day"),
        (11, 1, "Day of Remembrance of the Dead"),
        (12, 26, "Independence and Unity Day"),
    )


class Switzerland(WesternCalendar, ChristianMixin):
    "Switzerland"

    include_good_friday = True
    include_easter_sunday = True
    include_easter_monday = True
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True
    include_christmas = True
    include_boxing_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Berchtold's Day"),
        (5, 1, "Labour Day"),
        (8, 1, "National Holiday"),
    )
