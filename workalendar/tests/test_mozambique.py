from datetime import date

from . import GenericCalendarTest
from ..africa.mozambique import Mozambique


class MozambiqueTest(GenericCalendarTest):
    cal_class = Mozambique

    def test_year_new_year_shift(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)
        self.assertNotIn(date(2019, 1, 2), holidays)
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)
        self.assertNotIn(date(2020, 1, 2), holidays)

    def test_n_holidays(self):
        n_holidays = len(self.cal.holidays_set(2019))
        for holiday in self.cal.get_calendar_holidays(2020):
            print(holiday)
        assert n_holidays == 10

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        # Fixed days section:
        # 1. New Year's Day
        self.assertIn(date(2018, 1, 1), holidays)
        # 2. Mozambican Heroes' Day
        self.assertIn(date(2018, 2, 3), holidays)
        # 3. Mozambican Women's Day
        self.assertIn(date(2018, 4, 7), holidays)
        # 4. Good Friday
        self.assertIn(date(2018, 3, 30), holidays)
        # 5. Labour Day
        self.assertIn(date(2018, 5, 1), holidays)
        # 6. Independence Day
        self.assertIn(date(2018, 6, 25), holidays)
        # 7. Victory Day
        self.assertIn(date(2018, 9, 7), holidays)
        # 8. Armed Forces Day
        self.assertIn(date(2018, 9, 25), holidays)
        # 9. Peace And Reconciliation Day
        self.assertIn(date(2018, 10, 4), holidays)
        # 10. Christmas day
        self.assertIn(date(2018, 12, 25), holidays)

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        # Fixed days section:
        # 1. New Year's Day
        self.assertIn(date(2019, 1, 1), holidays)
        # 2. Mozambican Heroes' Day
        self.assertIn(date(2019, 2, 3), holidays)
        # 3. Mozambican Women's Day
        self.assertIn(date(2019, 4, 7), holidays)
        # 4. Good Friday
        self.assertIn(date(2019, 4, 19), holidays)
        # 5. Labour Day
        self.assertIn(date(2019, 5, 1), holidays)
        # 6. Independence Day
        self.assertIn(date(2019, 6, 25), holidays)
        # 7. Victory Day
        self.assertIn(date(2019, 9, 7), holidays)
        # 8. Armed Forces Day
        self.assertIn(date(2019, 9, 25), holidays)
        # 9. Peace And Reconciliation Day
        self.assertIn(date(2019, 10, 4), holidays)
        # 10. Christmas day
        self.assertIn(date(2019, 12, 25), holidays)

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        # Fixed days section:
        # 1. New Year's Day
        self.assertIn(date(2020, 1, 1), holidays)
        # 2. Mozambican Heroes' Day
        self.assertIn(date(2020, 2, 3), holidays)
        # 3. Mozambican Women's Day
        self.assertIn(date(2020, 4, 7), holidays)
        # 4. Good Friday
        self.assertIn(date(2020, 4, 10), holidays)
        # 5. Labour Day
        self.assertIn(date(2020, 5, 1), holidays)
        # 6. Independence Day
        self.assertIn(date(2020, 6, 25), holidays)
        # 7. Victory Day
        self.assertIn(date(2020, 9, 7), holidays)
        # 8. Armed Forces Day
        self.assertIn(date(2020, 9, 25), holidays)
        # 9. Peace And Reconciliation Day
        self.assertIn(date(2020, 10, 4), holidays)
        # 10. Christmas day
        self.assertIn(date(2020, 12, 25), holidays)

    def test_2020_new_years_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 1, 1)], "New year")

    def test_2020_heroes_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 2, 3)], "Mozambican Heroes' Day")

    def test_2020_women_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 4, 7)], "Mozambican Women's Day")

    def test_2020_good_friday_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 4, 10)], "Good Friday")

    def test_2020_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "Labour Day")

    def test_2020_independence_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 6, 25)], "Independence Day")

    def test_2020_victory_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 9, 7)], "Victory Day")

    def test_2020_armed_forces_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 9, 25)], "Armed Forces Day")

    def test_2020_peace_and_reconciliation_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 10, 4)], "Peace And Reconciliation Day")

    def test_2020_christmas_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 12, 25)], "Christmas Day")
