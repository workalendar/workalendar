from .registry import registry
from workalendar.america import Brazil, BrazilBankCalendar


# Commemorative holidays list
COMMEMORATIVE_HOLIDAYS = [
    'Consciência Negra',
]


def brazil_all_holidays_set(year):
    "Returns all holidays in brazil with their respective type and coverage"

    holidays_set = []

    # Get brazilian national holidays
    cal = Brazil()
    for national_holidays in cal.holidays(year):
        if national_holidays in COMMEMORATIVE_HOLIDAYS:
            tipo_feriado = 'C'
        else:
            tipo_feriado = 'F'
        if [national_holidays, 'N', tipo_feriado] not in holidays_set:
            holidays_set.append([national_holidays, 'N', tipo_feriado])

    # Get brazilian bank holidays
    cal = BrazilBankCalendar()
    for bank_holidays in cal.holidays(year):
        if [bank_holidays, 'N', 'B'] not in holidays_set:
            holidays_set.append([bank_holidays, 'N', 'B'])

    # Get holidays from brazilian state
    for state in registry.get_subregions('BR'):

        cal_state = registry.get_calendar_class(state)()
        for state_holidays in cal_state.holidays(year):

            if [state_holidays, 'E', 'F'] not in holidays_set \
                    and [state_holidays, 'M', 'F'] not in holidays_set:
                holidays_set.append([state_holidays, 'E', 'F'])

        # Get brazilian municipal holidays
        for city in registry.get_subregions(state):

            cal_city = registry.get_calendar_class(city)()
            for city_holiday in cal_city.holidays(year):

                if [city_holiday, 'M', 'F'] not in holidays_set \
                        and [city_holiday, 'E', 'F'] not in holidays_set:
                    holidays_set.append([city_holiday, 'M', 'F'])
    return holidays_set
