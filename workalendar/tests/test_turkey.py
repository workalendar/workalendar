# -*- coding: utf-8 -*-
from datetime import date

from workalendar.tests import GenericCalendarTest
from workalendar.europe.turkey import Turkey


class TurkeyTest(GenericCalendarTest):
    cal_class = Turkey

    def test_year_new_year_shift(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)
        self.assertIn(date(2012, 1, 2), holidays)
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertNotIn(date(2013, 1, 2), holidays)

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        # Fixed days section:
        # 1. New years Day
        self.assertIn(date(2014, 1, 1), holidays)
        # 2. National Sovereignty and Children's Day
        self.assertIn(date(2014, 4, 23), holidays)
        # 3. Labor and Solidarity Day
        self.assertIn(date(2014, 5, 1), holidays)
        # 4. Commemoration of Atatürk, Youth and Sports Day
        self.assertIn(date(2014, 5, 19), holidays)
        # 5. Democracy and National Unity Day
        self.assertIn(date(2014, 7, 15), holidays)
        # 6. Victory Day
        self.assertIn(date(2014, 8, 30), holidays)
        # 7. Republic Day
        self.assertIn(date(2014, 9, 29), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        # Fixed days section:
        # 1. New years Day
        self.assertIn(date(2015, 1, 1), holidays)
        # 2. National Sovereignty and Children's Day
        self.assertIn(date(2015, 4, 23), holidays)
        # 3. Labor and Solidarity Day
        self.assertIn(date(2015, 5, 1), holidays)
        # 4. Commemoration of Atatürk, Youth and Sports Day
        self.assertIn(date(2015, 5, 19), holidays)
        # 5. Democracy and National Unity Day
        self.assertIn(date(2015, 7, 15), holidays)
        # 6. Victory Day
        self.assertIn(date(2015, 8, 30), holidays)
        # 7. Republic Day
        self.assertIn(date(2015, 9, 29), holidays)

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        # Fixed days section:
        # 1. New years Day
        self.assertIn(date(2019, 1, 1), holidays)
        # 2. National Sovereignty and Children's Day
        self.assertIn(date(2019, 4, 23), holidays)
        # 3. Labor and Solidarity Day
        self.assertIn(date(2019, 5, 1), holidays)
        # 4. Commemoration of Atatürk, Youth and Sports Day
        self.assertIn(date(2019, 5, 19), holidays)
        # 5. Democracy and National Unity Day
        self.assertIn(date(2019, 7, 15), holidays)
        # 6. Victory Day
        self.assertIn(date(2019, 8, 30), holidays)
        # 7. Republic Day
        self.assertIn(date(2019, 9, 29), holidays)

        # Religious days
        # Ramadan Feast - 3 days
        self.assertIn(date(2019, 6, 4), holidays)
        self.assertIn(date(2019, 6, 5), holidays)
        self.assertIn(date(2019, 6, 6), holidays)
        # Ramadan Feast - 4 days
        self.assertIn(date(2019, 8, 11), holidays)
        self.assertIn(date(2019, 8, 12), holidays)
        self.assertIn(date(2019, 8, 13), holidays)
        self.assertIn(date(2019, 8, 14), holidays)
