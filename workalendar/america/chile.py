from datetime import date

from ..core import WesternCalendar, MON, TUE, WED, THU, FRI, SAT
from ..astronomy import solar_term
from ..registry_tools import iso_register


# https://www.feriados.cl
# http://www.feriadoschilenos.cl

@iso_register('CL')
class Chile(WesternCalendar):
    "Chile"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 21, "Navy Day"),
        (9, 18, "National holiday"),
        (9, 19, "Army holiday"),
        (12, 31, "Banking Holiday"),
    )
    # Civil holidays
    # Labor day (Law 2.200 and Law 18.018)
    include_labour_day = True

    # Christian holidays
    # Holy Week (Law 2.977)
    include_good_friday = True
    include_easter_saturday = True
    # Assumption (Law 2.977)
    include_assumption = True
    # All Saints (Law 2.977)
    include_all_saints = True
    # Immaculate Conception (Law 2.977)
    include_immaculate_conception = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)

        # Indigenous Peoples (Law 21.357)
        indigenous_peoples_day = date(year, 6, 21)
        if year == 2021:
            days.append((indigenous_peoples_day, 'Indigenous Peoples Day'))
        elif year > 2021:
            june_solstice = solar_term(year, 90, 'America/Santiago')
            days.append((june_solstice, 'Indigenous Peoples Day'))

        # Saint Peter and Saint Paul (Law 18.432)
        peter_paul = date(year, 6, 29)
        if year < 2000:
            days.append((peter_paul, 'Saint Peter and Saint Paul'))
        else:
            # floating monday (Law 19.668)
            if peter_paul.weekday() in [TUE, WED, THU]:
                days.append((Chile.get_nth_weekday_in_month(year, 6, MON, 4),
                            'Saint Peter and Saint Paul'))
            elif peter_paul.weekday() == FRI:
                days.append((date(year, 7, 2), 'Saint Peter and Saint Paul'))
            else:
                days.append((peter_paul, 'Columbus Day'))

        # Our Lady of Mount Carmel (Law 20.148)
        if year >= 2007:
            days.append((date(year, 7, 16), "Our Lady of Mount Carmel"))

        # National Bridge Days (Law 20.215)
        if year >= 2007:
            september_17 = date(year, 9, 17)
            if september_17.weekday() == MON:
                days.append((september_17, '"Bridge" holiday'))
            september_20 = date(year, 9, 20)
            if september_20.weekday() == FRI:
                days.append((september_20, '"Bridge" holiday'))

        # Additional Friday (Law 20.983)
        if year >= 2017:
            september_18 = date(year, 9, 18)
            if (september_18.weekday() == SAT):
                days.append((september_17, '"Bridge" holiday'))

        # Meeting of the two Worlds (Law 3.810)
        columbus_day = date(year, 10, 12)
        if year < 2000:
            days.append((columbus_day, 'Columbus Day'))
        else:
            # floating monday (Law 19.668)
            if columbus_day.weekday() in [TUE, WED, THU]:
                days.append((Chile.get_nth_weekday_in_month(year, 10, MON, 2),
                            'Columbus Day'))
            elif columbus_day.weekday() == FRI:
                days.append((date(year, 10, 15), 'Columbus Day'))
            else:
                days.append((columbus_day, 'Columbus Day'))

        # Reformation Day (Law 20.299)
        if year >= 2008:
            reformation_day = date(year, 10, 31)
            if reformation_day.weekday() == WED:
                reformation_day = date(year, 11, 2)
            elif reformation_day.weekday() == TUE:
                reformation_day = date(year, 10, 27)

            days.append((reformation_day, "Reformation Day"))

        return days
