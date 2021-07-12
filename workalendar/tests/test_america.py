from datetime import date

from ..america import (Argentina, Barbados, Chile, Colombia, Mexico, Panama,
                       Paraguay)
from . import GenericCalendarTest


class ArgentinaTest(GenericCalendarTest):
    cal_class = Argentina

    def test_holidays_2018(self):
        holidays = self.cal.holidays_set(2018)
        # 1. Año Nuevo
        self.assertIn(date(2018, 1, 1), holidays)
        # 2. Carnaval
        self.assertIn(date(2018, 2, 12), holidays)
        # 3. Carnaval
        self.assertIn(date(2018, 2, 13), holidays)
        # 4. Día de la Memoria
        self.assertIn(date(2018, 3, 24), holidays)
        # 5. Día del Veterano y de los Caídos en la Guerra de Malvinas
        self.assertIn(date(2018, 4, 2), holidays)
        # 6. Viernes Santo
        self.assertIn(date(2018, 3, 30), holidays)
        # 7. Día del Trabajador
        self.assertIn(date(2018, 5, 1), holidays)
        # 8. Día de la Revolución de Mayo
        self.assertIn(date(2018, 5, 25), holidays)
        # 9. Día Paso a la Inmortalidad del General Manuel Belgrano
        self.assertIn(date(2018, 6, 20), holidays)
        # 10. Día de la Independencia
        self.assertIn(date(2018, 7, 9), holidays)
        # 11. Inmaculada Concepción de María
        self.assertIn(date(2018, 12, 8), holidays)
        # 12. Navidad
        self.assertIn(date(2018, 12, 25), holidays)
        # variable days
        # 13. Día Paso a la Inmortalidad del General Martín Miguel de Güemes
        self.assertIn(date(2018, 6, 17), holidays)
        # 14. Paso a la Inmortalidad del General José de San Martín
        self.assertIn(date(2018, 8, 20), holidays)
        # 15. Día del Respeto a la Diversidad Cultural
        self.assertIn(date(2018, 10, 15), holidays)
        # 16. Día de la Soberanía Nacional
        self.assertIn(date(2018, 11, 19), holidays)

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)
        self.assertIn(date(2019, 3, 4), holidays)
        self.assertIn(date(2019, 3, 5), holidays)
        self.assertIn(date(2019, 3, 24), holidays)
        self.assertIn(date(2019, 4, 2), holidays)
        self.assertIn(date(2019, 4, 19), holidays)
        self.assertIn(date(2019, 5, 1), holidays)
        self.assertIn(date(2019, 5, 25), holidays)
        self.assertIn(date(2019, 6, 20), holidays)
        self.assertIn(date(2019, 7, 9), holidays)
        self.assertIn(date(2019, 12, 8), holidays)
        self.assertIn(date(2019, 12, 25), holidays)
        # variable days
        self.assertIn(date(2019, 6, 17), holidays)
        self.assertIn(date(2019, 8, 19), holidays)
        self.assertIn(date(2019, 10, 14), holidays)
        self.assertIn(date(2019, 11, 18), holidays)

    def test_holidays_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)
        self.assertIn(date(2020, 2, 24), holidays)
        self.assertIn(date(2020, 2, 25), holidays)
        self.assertIn(date(2020, 3, 24), holidays)
        # Special case: Argentina has shifted this holiday due to
        # Coronavirus lockdown in 2020.
        self.assertNotIn(date(2020, 4, 2), holidays)
        self.assertIn(date(2020, 3, 31), holidays)

        # Back to normal, I hope...
        self.assertIn(date(2020, 4, 10), holidays)
        self.assertIn(date(2020, 5, 1), holidays)
        self.assertIn(date(2020, 5, 25), holidays)
        self.assertIn(date(2020, 6, 20), holidays)
        self.assertIn(date(2020, 7, 9), holidays)
        self.assertIn(date(2020, 12, 8), holidays)
        self.assertIn(date(2020, 12, 25), holidays)
        # variable days
        self.assertIn(date(2020, 6, 15), holidays)
        self.assertIn(date(2020, 8, 17), holidays)
        self.assertIn(date(2020, 10, 12), holidays)
        self.assertIn(date(2020, 11, 23), holidays)

    def test_holidays_2021(self):
        # Testing it because June 17th happens on THU (general_guemes_day).
        holidays = self.cal.holidays_set(2021)
        # Not happening on June 17
        self.assertNotIn(date(2021, 6, 17), holidays)
        # Happens on the 1st MON after this date.
        self.assertIn(date(2021, 6, 20), holidays)

        # Also, Día del Respeto a la Diversidad Cultural is shifted
        self.assertNotIn(date(2021, 10, 12), holidays)
        # The day before
        self.assertIn(date(2021, 10, 11), holidays)

    def test_dia_malvinas_label(self):
        _, label = self.cal.get_malvinas_day(2020)
        self.assertEqual(
            label,
            "Día del Veterano y de los Caídos en la Guerra de Malvinas"
        )

    def test_dia_memoria_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        label_memoria = holidays[date(2020, 3, 24)]
        self.assertEqual(
            label_memoria,
            "Día Nacional de la Memoria por la Verdad y la Justicia"
        )

    def test_carnival_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        label_carnival = holidays[date(2020, 2, 25)]
        self.assertEqual(label_carnival, "Carnival")

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        label = holidays[date(2020, 5, 1)]
        self.assertEqual(label, "Día del Trabajador")

    def test_immaculate_conception_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        label = holidays[date(2020, 12, 8)]
        self.assertEqual(label, "Día de la Inmaculada Concepción de María")


class ChileTest(GenericCalendarTest):
    cal_class = Chile

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 3, 30), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 21), holidays)
        self.assertIn(date(2013, 6, 29), holidays)
        self.assertIn(date(2013, 7, 16), holidays)
        self.assertIn(date(2013, 8, 15), holidays)
        self.assertIn(date(2013, 9, 18), holidays)
        self.assertIn(date(2013, 9, 19), holidays)
        self.assertIn(date(2013, 9, 20), holidays)
        self.assertIn(date(2013, 10, 12), holidays)
        self.assertIn(date(2013, 10, 31), holidays)
        self.assertIn(date(2013, 11, 1), holidays)
        self.assertIn(date(2013, 12, 8), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 31), holidays)

    def test_holidays_2021(self):
        holidays = self.cal.holidays_set(2021)
        # Año Nuevo
        self.assertIn(date(2021, 1, 1), holidays)
        # Viernes Santo
        self.assertIn(date(2021, 4, 2), holidays)
        # Sábado Santo
        self.assertIn(date(2021, 4, 3), holidays)
        # Día Nacional del Trabajo
        self.assertIn(date(2021, 5, 1), holidays)
        # Día de las Glorias Navales
        self.assertIn(date(2021, 5, 21), holidays)
        # día nacional de los pueblos indígenas (June solstice)
        self.assertIn(date(2021, 6, 21), holidays)
        # San Pedro y San Pablo
        self.assertIn(date(2021, 6, 28), holidays)
        # Día de la Virgen del Carmen
        self.assertIn(date(2021, 7, 16), holidays)
        # Asunción de la Virgen
        self.assertIn(date(2021, 8, 15), holidays)
        # Additional Holiday
        self.assertIn(date(2021, 9, 17), holidays)
        # Independencia Nacional
        self.assertIn(date(2021, 9, 18), holidays)
        # Día de las Glorias del Ejército
        self.assertIn(date(2021, 9, 19), holidays)
        # Encuentro de Dos Mundos
        self.assertIn(date(2021, 10, 11), holidays)
        # Día de las Iglesias Evangélicas y Protestantes
        self.assertIn(date(2021, 10, 31), holidays)
        # Día de Todos los Santos
        self.assertIn(date(2021, 11, 1), holidays)
        # Inmaculada Concepción
        self.assertIn(date(2021, 12, 8), holidays)
        # Navidad
        self.assertIn(date(2021, 12, 25), holidays)
        # Feriado Bancario
        self.assertIn(date(2021, 12, 31), holidays)

    def test_indigenous_people_day(self):
        # Testing because variable nature of June solstice

        # approved in 2021
        holidays = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 6, 21), holidays)
        self.assertNotIn(date(2020, 6, 20), holidays)

        # fixed day in 2021
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 6, 21), holidays)

        # solstice 2022
        holidays = self.cal.holidays_set(2022)
        self.assertIn(date(2022, 6, 21), holidays)

        # solstice 2023
        holidays = self.cal.holidays_set(2023)
        self.assertIn(date(2023, 6, 21), holidays)

        # solstice 2023
        holidays = self.cal.holidays_set(2024)
        self.assertIn(date(2024, 6, 20), holidays)

    def test_reformation_day(self):
        holidays = self.cal.holidays_set(2012)
        self.assertNotIn(date(2012, 10, 31), holidays)
        self.assertIn(date(2012, 11, 2), holidays)

        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(date(2017, 10, 31), holidays)
        self.assertIn(date(2017, 10, 27), holidays)

    def test_national_bridge_days(self):
        # MON TUE
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 9, 18), holidays)
        self.assertIn(date(2017, 9, 19), holidays)

        # TUE WED
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 9, 17), holidays)
        self.assertIn(date(2018, 9, 18), holidays)
        self.assertIn(date(2018, 9, 19), holidays)
        self.assertNotIn(date(2018, 9, 20), holidays)

        # WED THU
        holidays = self.cal.holidays_set(2019)
        self.assertNotIn(date(2019, 9, 17), holidays)
        self.assertIn(date(2019, 9, 18), holidays)
        self.assertIn(date(2019, 9, 19), holidays)
        self.assertIn(date(2019, 9, 20), holidays)

        # THU FRI
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 9, 18), holidays)
        self.assertIn(date(2020, 9, 19), holidays)

        # FRI SAT
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 9, 17), holidays)
        self.assertIn(date(2015, 9, 18), holidays)
        self.assertIn(date(2015, 9, 19), holidays)

        # SUN MON
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 9, 18), holidays)
        self.assertIn(date(2016, 9, 19), holidays)
        self.assertNotIn(date(2016, 9, 20), holidays)

        # SAT SUN for additional day
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 9, 17), holidays)
        self.assertIn(date(2021, 9, 18), holidays)
        self.assertIn(date(2021, 9, 19), holidays)

    def test_columbus_day(self):
        # MON
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 10, 12), holidays)
        # TUE
        holidays = self.cal.holidays_set(2021)
        self.assertNotIn(date(2021, 10, 12), holidays)
        self.assertIn(date(2021, 10, 11), holidays)
        # WED
        holidays = self.cal.holidays_set(2016)
        self.assertNotIn(date(2016, 10, 12), holidays)
        self.assertIn(date(2016, 10, 10), holidays)
        # THU
        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(date(2017, 10, 12), holidays)
        self.assertIn(date(2017, 10, 9), holidays)
        # FRI
        holidays = self.cal.holidays_set(2018)
        self.assertNotIn(date(2018, 10, 12), holidays)
        self.assertIn(date(2018, 10, 15), holidays)

    def test_st_peter_and_st_paul_day(self):
        # MON
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 6, 29), holidays)
        # TUE
        holidays = self.cal.holidays_set(2021)
        self.assertNotIn(date(2021, 6, 29), holidays)
        self.assertIn(date(2021, 6, 28), holidays)
        # WED
        holidays = self.cal.holidays_set(2016)
        self.assertNotIn(date(2016, 6, 29), holidays)
        self.assertIn(date(2016, 6, 27), holidays)
        # THU
        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(date(2017, 6, 29), holidays)
        self.assertIn(date(2017, 6, 26), holidays)
        # FRI
        holidays = self.cal.holidays_set(2018)
        self.assertNotIn(date(2018, 6, 29), holidays)
        self.assertIn(date(2018, 7, 2), holidays)


class ColombiaTest(GenericCalendarTest):
    cal_class = Colombia

    def test_holidays_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)    # New year
        self.assertIn(date(2015, 1, 12), holidays)   # Epiphany (shifted)
        self.assertIn(date(2015, 3, 23), holidays)   # Saint Joseph
        self.assertIn(date(2015, 3, 29), holidays)   # Palm Sunday
        self.assertIn(date(2015, 4, 2), holidays)    # Holy Thursday
        self.assertIn(date(2015, 4, 3), holidays)    # Good Friday
        self.assertIn(date(2015, 4, 5), holidays)    # Easter (SUN)
        self.assertIn(date(2015, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2015, 5, 18), holidays)   # Ascension (shifted)
        self.assertIn(date(2015, 6, 8), holidays)    # Corpus Christi
        self.assertIn(date(2015, 6, 15), holidays)   # Sacred Heart
        self.assertIn(date(2015, 6, 29), holidays)   # St Peter & St Paul
        self.assertIn(date(2015, 7, 20), holidays)   # Independance Day
        self.assertIn(date(2015, 8, 7), holidays)    # Boyacá battle
        self.assertIn(date(2015, 8, 17), holidays)   # Assumption (shifted)
        self.assertIn(date(2015, 10, 12), holidays)  # Day of the Races
        self.assertIn(date(2015, 11, 2), holidays)   # All Saints (shifted)
        self.assertIn(date(2015, 11, 16), holidays)  # Cartagena independence
        self.assertIn(date(2015, 12, 8), holidays)   # Immaculate Conception
        self.assertIn(date(2015, 12, 25), holidays)  # XMas
        self.assertEqual(len(holidays), 20)

    def test_holidays_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)    # New year
        self.assertIn(date(2020, 1, 6), holidays)    # Epiphany
        self.assertIn(date(2020, 3, 23), holidays)   # Saint Joseph
        self.assertIn(date(2020, 4, 5), holidays)    # Palm Sunday
        self.assertIn(date(2020, 4, 9), holidays)    # Holy Thursday
        self.assertIn(date(2020, 4, 10), holidays)   # Good Friday
        self.assertIn(date(2020, 4, 12), holidays)   # Easter (SUN)
        self.assertIn(date(2020, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2020, 5, 25), holidays)   # Ascension (shifted)
        self.assertIn(date(2020, 6, 15), holidays)   # Corpus Christi
        self.assertIn(date(2020, 6, 22), holidays)   # Sacred Heart
        self.assertIn(date(2020, 6, 29), holidays)   # St Peter & St Paul
        self.assertIn(date(2020, 7, 20), holidays)   # Independance Day
        self.assertIn(date(2020, 8, 7), holidays)    # Boyacá battle
        self.assertIn(date(2020, 8, 17), holidays)   # Assumption (shifted)
        self.assertIn(date(2020, 10, 12), holidays)  # Day of the Races
        self.assertIn(date(2020, 11, 2), holidays)   # All Saints (shifted)
        self.assertIn(date(2020, 11, 16), holidays)  # Cartagena independence
        self.assertIn(date(2020, 12, 8), holidays)   # Immaculate Conception
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertEqual(len(holidays), 20)

    def test_epiphany_monday(self):
        # In 2020, Epiphany falls on MON
        epiphany_2020 = self.cal.get_epiphany(2020)
        self.assertEqual(epiphany_2020, date(2020, 1, 6))
        # In 2021, it does not, so it's shifted to the next MON
        epiphany_2021 = self.cal.get_epiphany(2021)
        self.assertEqual(epiphany_2021, date(2021, 1, 11))

    def test_saint_peter_and_saint_paul_monday(self):
        # In 2020, Saint Peter and Saint Paul falls on MON
        st_peter_paul_2020 = self.cal.get_saint_peter_and_saint_paul(2020)
        self.assertEqual(st_peter_paul_2020, date(2020, 6, 29))
        # In 2021, it does not, so it's shifted to the next MON
        st_peter_paul_2021 = self.cal.get_saint_peter_and_saint_paul(2021)
        self.assertEqual(st_peter_paul_2021, date(2021, 7, 5))

    def test_assumption_monday(self):
        # In 2021, Assumption falls on SUN, so it's shifted to MON
        assumption_2021 = self.cal.get_assumption(2021)
        self.assertEqual(assumption_2021, date(2021, 8, 16))
        # In 2022, Assumption falls on MON
        assumption_2022 = self.cal.get_assumption(2022)
        self.assertEqual(assumption_2022, date(2022, 8, 15))

    def test_day_of_the_races_monday(self):
        # In 2020, Day of the races and hispanity falls on MON
        day_races_2020 = self.cal.get_day_of_the_races(2020)
        self.assertEqual(day_races_2020, date(2020, 10, 12))
        # In 2021, It does not, so it's shifted to the next MON
        day_races_2021 = self.cal.get_day_of_the_races(2021)
        self.assertEqual(day_races_2021, date(2021, 10, 18))

    def test_all_saints_monday(self):
        # In 2021, The All Saints falls on MON
        all_saints_2021 = self.cal.get_all_saints(2021)
        self.assertEqual(all_saints_2021, date(2021, 11, 1))
        # In 2022, It does not, so it's shifted to the next MON
        all_saints_2022 = self.cal.get_all_saints(2022)
        self.assertEqual(all_saints_2022, date(2022, 11, 7))

    def test_cartagena_independence_monday(self):
        # In 2019, The Cartagena Independance falls on MON
        cartagena_2019 = self.cal.get_cartagena_independence(2019)
        self.assertEqual(cartagena_2019, date(2019, 11, 11))
        # In 2020, It does not, so it's shifted to the next MON
        cartagena_2020 = self.cal.get_cartagena_independence(2020)
        self.assertEqual(cartagena_2020, date(2020, 11, 16))


class MexicoTest(GenericCalendarTest):
    cal_class = Mexico

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 2, 4), holidays)  # Constitution day
        self.assertIn(date(2013, 3, 18), holidays)  # Benito Juárez's birthday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 9, 16), holidays)  # Independence day
        self.assertIn(date(2013, 11, 18), holidays)  # Revolution day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas

    def test_shift_to_monday(self):
        holidays = self.cal.holidays_set(2017)
        # New year on Sunday -> shift
        self.assertIn(date(2017, 1, 2), holidays)
        holidays = self.cal.holidays_set(2016)
        # XMas on sunday -> shift to monday
        self.assertIn(date(2016, 12, 26), holidays)
        # Same for Labour day
        self.assertIn(date(2016, 5, 2), holidays)

    def test_shift_to_friday(self):
        holidays = self.cal.holidays_set(2021)
        # January 1st 2022 is a saturday, so we shift to friday
        self.assertIn(date(2021, 12, 31), holidays)
        # Same for Labour day
        self.assertIn(date(2021, 4, 30), holidays)
        holidays = self.cal.holidays_set(2021)
        # December 25th, 2022 is a saturday, so we shift to friday
        self.assertIn(date(2021, 12, 24), holidays)


class PanamaTest(GenericCalendarTest):
    cal_class = Panama

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 1, 9), holidays)  # Martyrs day
        self.assertIn(date(2013, 2, 12), holidays)  # carnival tuesday
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 30), holidays)  # easter saturday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 11, 3), holidays)  # independence day
        self.assertIn(date(2013, 11, 5), holidays)  # colon day
        # Shout in Villa de los Santos
        self.assertIn(date(2013, 11, 10), holidays)
        self.assertIn(date(2013, 11, 28), holidays)  # Independence from spain
        self.assertIn(date(2013, 12, 8), holidays)  # mother day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas


class ParaguayTest(GenericCalendarTest):
    cal_class = Paraguay

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)
        self.assertIn(date(2019, 3, 1), holidays)  # Heroes day
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy thursday
        self.assertIn(date(2019, 4, 19), holidays)  # Good friday
        self.assertIn(date(2019, 5, 1), holidays)  # Labour day
        self.assertIn(date(2019, 5, 14), holidays)  # Independance day
        self.assertIn(date(2019, 6, 12), holidays)  # Chaco Armistice Day
        self.assertIn(date(2019, 8, 15), holidays)  # Founding of Asunción
        self.assertIn(date(2019, 9, 29), holidays)  # Boqueron Battle Victory
        self.assertIn(date(2019, 12, 8), holidays)  # Virgin of Caacupe
        self.assertIn(date(2019, 12, 25), holidays)  # XMas

    def test_holidays_2017(self):
        holidays = self.cal.holidays_set(2017)
        # In 2017, Heroes day has been moved to February 27th
        self.assertNotIn(date(2017, 3, 1), holidays)
        self.assertIn(date(2017, 2, 27), holidays)
        # Fundation of Asunción day: moved to August 14 for 2017
        self.assertNotIn(date(2017, 8, 15), holidays)
        self.assertIn(date(2017, 8, 14), holidays)
        # Boqueron Battle Victory Day: moved to October 2nd for 2017
        self.assertNotIn(date(2017, 9, 29), holidays)
        self.assertIn(date(2017, 10, 2), holidays)

    def test_immaculate_conception_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        label = holidays[date(2020, 12, 8)]
        self.assertEqual(label, "Virgin of Caacupé Day")


class BarbadosTest(GenericCalendarTest):
    cal_class = Barbados

    def test_holidays_2009(self):
        holidays = self.cal.holidays_set(2009)
        self.assertIn(date(2009, 1, 1), holidays)
        self.assertIn(date(2009, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2009, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2009, 4, 12), holidays)  # Easter Sunday
        self.assertIn(date(2009, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2009, 4, 28), holidays)  # National Heroes Day
        self.assertIn(date(2009, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2009, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2009, 8, 1), holidays)  # Emancipation Day
        self.assertIn(date(2009, 8, 3), holidays)  # Kabooment Day
        self.assertIn(date(2009, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2009, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2009, 12, 26), holidays)  # Boxing Day

    def test_holidays_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2016, 3, 25), holidays)  # Good Friday
        self.assertIn(date(2016, 3, 28), holidays)  # Easter Monday
        self.assertIn(date(2016, 4, 28), holidays)  # National Heroes Day
        self.assertIn(date(2016, 5, 2), holidays)  # Labour Day
        self.assertIn(date(2016, 5, 16), holidays)  # Whit Monday
        self.assertIn(date(2016, 8, 1), holidays)  # Kabooment Day
        self.assertIn(date(2016, 8, 2), holidays)  # Emancipation Day
        self.assertIn(date(2016, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2016, 12, 26), holidays)  # Boxing Day
        self.assertIn(date(2016, 12, 27), holidays)  # Public Holiday

    def test_holidays_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)
        self.assertIn(date(2018, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2018, 1, 22), holidays)  # Errol Barrow Day (shift)
        self.assertIn(date(2018, 3, 30), holidays)  # Good Friday
        self.assertIn(date(2018, 4, 1), holidays)  # Easter Sunday
        self.assertIn(date(2018, 4, 2), holidays)  # Easter Monday
        self.assertIn(date(2018, 4, 28), holidays)  # National Heroes Day
        self.assertIn(date(2018, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2018, 5, 21), holidays)  # Whit Monday
        self.assertIn(date(2018, 8, 1), holidays)  # Emancipation Day
        self.assertIn(date(2018, 8, 6), holidays)  # Kabooment Day
        self.assertIn(date(2018, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2018, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2018, 12, 26), holidays)  # Boxing Day

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)
        self.assertIn(date(2019, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2019, 4, 19), holidays)  # Good Friday
        self.assertIn(date(2019, 4, 21), holidays)  # Easter Sunday
        self.assertIn(date(2019, 4, 22), holidays)  # Easter Monday

        # National Heroes Day & shift
        self.assertIn(date(2019, 4, 28), holidays)
        self.assertIn(date(2019, 4, 29), holidays)  # shft'd

        self.assertIn(date(2019, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2019, 6, 10), holidays)  # Whit Monday
        self.assertIn(date(2019, 8, 1), holidays)  # Emancipation Day
        self.assertIn(date(2019, 8, 5), holidays)  # Kabooment Day
        self.assertIn(date(2019, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2019, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2019, 12, 26), holidays)  # Boxing Day

    def test_holidays_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)
        self.assertIn(date(2020, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday

        # National Heroes Day & shift
        self.assertIn(date(2020, 4, 28), holidays)

        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 8, 1), holidays)  # Emancipation Day
        self.assertIn(date(2020, 8, 3), holidays)  # Kabooment Day
        self.assertIn(date(2020, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2020, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2020, 12, 26), holidays)  # Boxing Day

    def test_holidays_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2021, 1, 4), holidays)  # Public Holiday
        self.assertIn(date(2021, 1, 5), holidays)  # Public Holiday
        self.assertIn(date(2021, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 4, 28), holidays)  # National Heroes Day

        self.assertIn(date(2021, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2021, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2021, 8, 2), holidays)  # Kabooment Day
        self.assertIn(date(2021, 8, 3), holidays)  # Emancipation Day
        self.assertIn(date(2021, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2021, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2021, 12, 27), holidays)  # Boxing Day
