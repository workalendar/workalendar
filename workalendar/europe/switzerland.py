from datetime import date, timedelta
from ..core import WesternCalendar, ChristianMixin, SUN
from ..registry_tools import iso_register


@iso_register('CH')
class Switzerland(WesternCalendar, ChristianMixin):
    'Switzerland'

    # ChristianMixin entries common to (most) cantons - opt out
    include_good_friday = True  # not in TI, VS
    include_easter_sunday = True
    include_easter_monday = True  # not in VS
    include_ascension = True
    include_whit_sunday = True
    include_whit_monday = True  # not in VS
    include_christmas = True
    include_boxing_day = True  # not in GE, NE, VS, VD

    # ChristianMixin entries with varying observance - opt in
    include_epiphany = False
    include_corpus_christi = False
    include_assumption = False
    include_all_saints = False
    include_immaculate_conception = False

    # Swiss entries with varying observance - opt in
    include_berchtolds_day = False
    include_st_josephs_day = False
    include_labour_day = False

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (8, 1, "National Holiday"),
    )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        if self.include_berchtolds_day:
            days.append((date(year, 1, 2), "Berchtold's Day"))
        if self.include_st_josephs_day:
            days.append((date(year, 3, 19), "St Joseph's Day"))
        if self.include_labour_day:
            days.append((date(year, 5, 1), "Labour Day"))
        return days


@iso_register('CH-AG')
class Aargau(Switzerland):
    'Aargau'

    include_berchtolds_day = True
    include_corpus_christi = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-AI')
class AppenzellInnerrhoden(Switzerland):
    'Appenzell Innerrhoden'

    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-AR')
class AppenzellAusserrhoden(Switzerland):
    'Appenzell Ausserrhoden'

    include_labour_day = True


@iso_register('CH-BE')
class Bern(Switzerland):
    'Bern'

    include_berchtolds_day = True


@iso_register('CH-BL')
class BaselLandschaft(Switzerland):
    'Basel-Landschaft'

    include_labour_day = True


@iso_register('CH-BS')
class BaselStadt(Switzerland):
    'Basel-Stadt'

    include_labour_day = True


@iso_register('CH-FR')
class Fribourg(Switzerland):
    'Fribourg'

    include_berchtolds_day = True
    include_labour_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-GE')
class Geneva(Switzerland):
    'Geneva'

    include_boxing_day = False

    FIXED_HOLIDAYS = Switzerland.FIXED_HOLIDAYS + (
        (12, 31, "Creation of Geneva Republic"),
    )

    def get_genevan_fast(self, year):
        "Thursday following the first Sunday of September"
        first_sunday = self.get_nth_weekday_in_month(year, 9, SUN)
        # The following thursday is 4 days after
        return (
            first_sunday + timedelta(days=4),
            "Genevan Fast"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_genevan_fast(year))
        return days


@iso_register('CH-GL')
class Glarus(Switzerland):
    'Glarus (Glaris)'

    include_berchtolds_day = True
    include_all_saints = True

    FIXED_HOLIDAYS = Switzerland.FIXED_HOLIDAYS + (
        (4, 3, "Näfels Ride"),
    )


@iso_register('CH-GR')
class Graubunden(Switzerland):
    'Graubünden (Grisons)'

    include_epiphany = True
    include_st_josephs_day = True
    include_corpus_christi = True
    include_immaculate_conception = True


@iso_register('CH-JU')
class Jura(Switzerland):
    'Jura'

    include_berchtolds_day = True
    include_labour_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_boxing_day = False

    FIXED_HOLIDAYS = Switzerland.FIXED_HOLIDAYS + (
        (6, 23, "Independence Day"),
    )


@iso_register('CH-LU')
class Luzern(Switzerland):
    'Luzern'

    include_berchtolds_day = True
    include_epiphany = True
    include_st_josephs_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-NE')
class Neuchatel(Switzerland):
    'Neuchâtel'

    include_boxing_day = False
    include_berchtolds_day = True
    include_labour_day = True

    FIXED_HOLIDAYS = Switzerland.FIXED_HOLIDAYS + (
        (3, 1, "Republic Day"),
    )


@iso_register('CH-NW')
class Nidwalden(Switzerland):
    'Nidwalden'

    include_st_josephs_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-OW')
class Obwalden(Switzerland):
    'Obwalden'

    include_berchtolds_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True

    FIXED_HOLIDAYS = Switzerland.FIXED_HOLIDAYS + (
        (9, 25, "Saint Nicholas of Flüe Day"),
    )


@iso_register('CH-SG')
class StGallen(Switzerland):
    'St. Gallen'

    include_all_saints = True


@iso_register('CH-SH')
class Schaffhausen(Switzerland):
    'Schaffhausen'

    include_berchtolds_day = True
    include_labour_day = True


@iso_register('CH-SO')
class Solothurn(Switzerland):
    'Solothurn'

    include_berchtolds_day = True
    include_st_josephs_day = True
    include_labour_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-SZ')
class Schwyz(Switzerland):
    'Schwyz'

    include_epiphany = True
    include_st_josephs_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-TG')
class Thurgau(Switzerland):
    'Thurgau'

    include_berchtolds_day = True
    include_labour_day = True


@iso_register('CH-TI')
class Ticino(Switzerland):
    'Ticino'

    include_good_friday = False
    include_epiphany = True
    include_st_josephs_day = True
    include_labour_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True

    FIXED_HOLIDAYS = Switzerland.FIXED_HOLIDAYS + (
        (6, 29, "Saints Peter and Paul"),
    )


@iso_register('CH-UR')
class Uri(Switzerland):
    'Uri'

    include_epiphany = True
    include_st_josephs_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-VD')
class Vaud(Switzerland):
    'Vaud'

    include_berchtolds_day = True
    include_boxing_day = False

    def get_federal_thanksgiving_monday(self, year):
        "Monday following the 3rd sunday of September"
        third_sunday = self.get_nth_weekday_in_month(year, 9, SUN, 3)
        return (
            third_sunday + timedelta(days=1),
            "Federal Thanksgiving Monday"
        )

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.append(self.get_federal_thanksgiving_monday(year))
        return days


@iso_register('CH-VS')
class Valais(Switzerland):
    'Valais'

    include_good_friday = False
    include_easter_monday = False
    include_whit_monday = False
    include_st_josephs_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True
    include_boxing_day = False


@iso_register('CH-ZG')
class Zug(Switzerland):
    'Zug'

    include_berchtolds_day = True
    include_corpus_christi = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True


@iso_register('CH-ZH')
class Zurich(Switzerland):
    'Zürich'

    include_berchtolds_day = True
    include_labour_day = True
