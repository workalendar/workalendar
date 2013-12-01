from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON, TUE
from datetime import date


class AustraliaCalendar(WesternCalendar, ChristianMixin):
    "Australia base calendar"
    include_good_friday = True
    include_easter_monday = True
    include_queens_birthday = False
    include_labour_day_october = False

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 26, "Australia Day"),
        (4, 25, "Anzac Day"),
    )

    def get_canberra_day(self, year):
        return (
            AustraliaCalendar.get_nth_weekday_in_month(year, 3, MON, 2),
            "Canberra Day"
        )

    def get_queens_birthday(self, year):
        return (
            AustraliaCalendar.get_nth_weekday_in_month(year, 6, MON, 2),
            "Queen's Birthday"
        )

    def get_labour_day_october(self, year):
        return (
            AustraliaCalendar.get_nth_weekday_in_month(year, 10, MON),
            'Labour Day'
        )

    def get_variable_days(self, year):
        # usual variable days
        days = super(AustraliaCalendar, self).get_variable_days(year)
        if self.include_queens_birthday:
            days.append(self.get_queens_birthday(year))
        if self.include_labour_day_october:
            days.append(self.get_labour_day_october(year))
        return days


class AustraliaCapitalTerritoryCalendar(AustraliaCalendar):
    include_easter_saturday = True
    include_queens_birthday = True
    include_labour_day_october = True
    include_boxing_day = True

    def get_family_community_day(self, year):
        # Since this day is picked unsing the school year calendar, there's no
        # mathematical way yet to provide it surely

        # TODO: Family & Community Day was celebrated on the first Tuesday of
        # November in 2007, 2008 and 2009
        if year == 2010:
            day = date(2010, 9, 27)
        elif year == 2011:
            day = date(2011, 10, 10)
        elif year == 2012:
            day = date(2012, 10, 8)
        elif year == 2013:
            day = date(2013, 9, 30)
        elif year == 2014:
            day = date(2014, 9, 29)
        else:
            raise Exception("Year %d is not implemented, Sorry" % year)
        return (day, "Family & Community Day")

    def get_variable_days(self, year):
        days = super(AustraliaCapitalTerritoryCalendar, self) \
            .get_variable_days(year)
        days += [
            self.get_canberra_day(year),
            self.get_family_community_day(year),
        ]
        return days


class AustraliaNewSouthWalesCalendar(AustraliaCalendar):
    include_queens_birthday = True
    include_easter_saturday = True
    include_easter_sunday = True
    include_labour_day_october = True
    include_boxing_day = True


class AustraliaNorthernTerritoryCalendar(AustraliaCalendar):
    include_easter_saturday = True
    include_queens_birthday = True
    include_boxing_day = True

    def get_may_day(self, year):
        return (
            AustraliaNorthernTerritoryCalendar.get_nth_weekday_in_month(
                year, 5, MON),
            "May Day"
        )

    def get_picnic_day(self, year):
        return (
            AustraliaNorthernTerritoryCalendar.get_nth_weekday_in_month(
                year, 8, MON),
            "Picnic Day"
        )

    def get_variable_days(self, year):
        days = super(AustraliaNorthernTerritoryCalendar, self) \
            .get_variable_days(year)
        days += [
            self.get_may_day(year),
            self.get_picnic_day(year),
        ]
        return days


class AustraliaQueenslandCalendar(AustraliaCalendar):
    include_easter_saturday = True
    include_queens_birthday = True
    include_boxing_day = True

    def get_labour_day_may(self, year):
        return (
            AustraliaNorthernTerritoryCalendar.get_nth_weekday_in_month(
                year, 5, MON),
            "Labour Day"
        )

    def get_variable_days(self, year):
        days = super(AustraliaQueenslandCalendar, self) \
            .get_variable_days(year)
        days += [
            self.get_labour_day_may(year),
        ]
        return days


class SouthAustraliaCalendar(AustraliaCalendar):
    include_easter_saturday = True
    include_queens_birthday = True
    include_labour_day_october = True

    def get_adelaides_cup(self, year):
        return (
            SouthAustraliaCalendar.get_nth_weekday_in_month(
                year, 3, MON, 2),
            "Adelaide's cup"
        )

    def get_proclamation_day(self, year):
        return (date(year, 12, 26), "Proclamation Day")

    def get_variable_days(self, year):
        days = super(SouthAustraliaCalendar, self) \
            .get_variable_days(year)
        days += [
            self.get_adelaides_cup(year),
            self.get_proclamation_day(year),
        ]
        return days


class TasmaniaCalendar(AustraliaCalendar):
    include_queens_birthday = True
    include_boxing_day = True

    @property
    def has_recreation_day(self):
        return True

    def get_eight_hours_day(self, year):
        return (
            TasmaniaCalendar.get_nth_weekday_in_month(year, 3, MON, 2),
            "Eight hours Day"
        )

    def get_recreation_day(self, year):
        return (
            TasmaniaCalendar.get_nth_weekday_in_month(year, 11, MON),
            "Recreation Day"
        )

    def get_variable_days(self, year):
        days = super(TasmaniaCalendar, self).get_variable_days(year)
        days.append(self.get_eight_hours_day(year))
        if self.has_recreation_day:
            days.append(self.get_recreation_day(year))
        return days


class HobartCalendar(TasmaniaCalendar):

    @property
    def has_recreation_day(self):
        return False

    def get_hobart(self, year):
        return (
            HobartCalendar.get_nth_weekday_in_month(year, 2, MON, 2),
            "Royal Hobart Regatta"
        )

    def get_variable_days(self, year):
        days = super(HobartCalendar, self).get_variable_days(year)
        days.append(self.get_hobart(year))
        return days


class VictoriaCalendar(AustraliaCalendar):
    include_easter_saturday = True
    include_queens_birthday = True
    include_boxing_day = True

    def get_labours_day_in_march(self, year):
        return (
            VictoriaCalendar.get_nth_weekday_in_month(year, 3, MON, 2),
            "Labour Day"
        )

    def get_melbourne_cup(self, year):
        return (
            VictoriaCalendar.get_nth_weekday_in_month(year, 11, TUE),
            "Melbourne Cup"
        )

    def get_variable_days(self, year):
        days = super(VictoriaCalendar, self).get_variable_days(year)
        days.append(self.get_labours_day_in_march(year))
        days.append(self.get_melbourne_cup(year))
        return days


class WesternAustraliaCalendar(AustraliaCalendar):
    include_boxing_day = True

    def get_labours_day_in_march(self, year):
        return (
            WesternAustraliaCalendar.get_nth_weekday_in_month(year, 3, MON),
            "Labour Day"
        )

    def get_western_australia_day(self, year):
        return (
            WesternAustraliaCalendar.get_nth_weekday_in_month(year, 6, MON),
            "Western Australia Day"
        )

    def get_variable_days(self, year):
        # It is not possible to surely compute Queen's Birthday holiday in
        # The western Australia territory, since it's based on the Governor
        # Decision (it is typically the last Monday of September or the first
        # Monday of October)

        days = super(WesternAustraliaCalendar, self).get_variable_days(year)
        days.append(self.get_labours_day_in_march(year))
        days.append(self.get_western_australia_day(year))
        return days
