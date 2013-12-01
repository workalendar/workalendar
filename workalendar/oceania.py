from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON
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

