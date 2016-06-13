from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.asia import SouthKorea, Japan
from workalendar.asia import Qatar
from workalendar.asia import Taiwan


class SouthKoreaTest(GenericCalendarTest):

    cal_class = SouthKorea

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # new year
        self.assertIn(date(2013, 3, 1), holidays)    # Independence day
        self.assertIn(date(2013, 5, 5), holidays)    # children's day
        self.assertIn(date(2013, 6, 6), holidays)    # Memorial day
        self.assertIn(date(2013, 8, 15), holidays)   # Liberation day
        self.assertIn(date(2013, 10, 3), holidays)   # National Foundation Day
        self.assertIn(date(2013, 10, 9), holidays)   # Hangul Day
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas

        # Variable days
        self.assertIn(date(2013, 2, 9), holidays)
        self.assertIn(date(2013, 2, 10), holidays)
        self.assertIn(date(2013, 2, 11), holidays)
        self.assertIn(date(2013, 5, 17), holidays)
        self.assertIn(date(2013, 9, 18), holidays)
        self.assertIn(date(2013, 9, 19), holidays)
        self.assertIn(date(2013, 9, 20), holidays)


class JapanTest(GenericCalendarTest):

    cal_class = Japan

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # new year
        self.assertIn(date(2013, 2, 11), holidays)   # Foundation Day
        self.assertIn(date(2013, 3, 20), holidays)   # Vernal Equinox Day
        self.assertIn(date(2013, 4, 29), holidays)   # Showa Day
        self.assertIn(date(2013, 5, 3), holidays)  # Constitution Memorial Day
        self.assertIn(date(2013, 5, 4), holidays)    # Greenery Day
        self.assertIn(date(2013, 5, 5), holidays)    # Children's Day
        self.assertIn(date(2013, 9, 23), holidays)   # Autumnal Equinox Day
        self.assertIn(date(2013, 11, 3), holidays)   # Culture Day
        self.assertIn(date(2013, 11, 23), holidays)  # Labour Thanksgiving Day
        self.assertIn(date(2013, 12, 23), holidays)  # The Emperor's Birthday

        # Variable days
        self.assertIn(date(2013, 1, 14), holidays)   # Coming of Age Day
        self.assertIn(date(2013, 7, 15), holidays)   # Marine Day
        self.assertIn(date(2013, 9, 16), holidays)   # Respect-for-the-Aged Day
        self.assertIn(date(2013, 10, 14), holidays)  # Health and Sports Day

    def test_year_2016(self):
        # Before 2016, no Mountain Day
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(date(2014, 8, 11), holidays)   # Mountain Day
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 8, 11), holidays)   # Mountain Day
        # After 2016, yes
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 8, 11), holidays)   # Mountain Day
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 8, 11), holidays)   # Mountain Day


class QatarTest(GenericCalendarTest):
    cal_class = Qatar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 7, 9), holidays)  # start ramadan
        # warning, the official date was (2013, 8, 10)
        self.assertIn(date(2013, 8, 8), holidays)  # eid al fitr
        # The official date was (2013, 10, 14)
        self.assertIn(date(2013, 10, 15), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 16), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 17), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 18), holidays)  # eid al adha
        self.assertIn(date(2013, 12, 18), holidays)  # National Day


class TaiwanTest(GenericCalendarTest):

    cal_class = Taiwan

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # New Year
        self.assertIn(date(2013, 2, 9), holidays)    # Chinese new year's eve
        self.assertIn(date(2013, 2, 10), holidays)   # Chinese new year
        self.assertIn(date(2013, 2, 11), holidays)   # Spring Festival
        self.assertIn(date(2013, 2, 12), holidays)   # Spring Festival
        self.assertIn(date(2013, 2, 28), holidays)   # 228 Peace Memorial Day
        self.assertIn(date(2013, 4, 4), holidays)    # Children's Day
        self.assertIn(date(2013, 6, 12), holidays)   # Dragon Boat Festival
        self.assertIn(date(2013, 9, 19), holidays)   # Mid-Autumn Festival
        self.assertIn(date(2013, 10, 10), holidays)  # National Day

    def test_qingming_festival(self):
        self.assertIn(date(2001, 4, 5), self.cal.holidays_set(2001))
        self.assertIn(date(2002, 4, 5), self.cal.holidays_set(2002))
        self.assertIn(date(2005, 4, 5), self.cal.holidays_set(2005))
        self.assertIn(date(2006, 4, 5), self.cal.holidays_set(2006))
        self.assertIn(date(2007, 4, 5), self.cal.holidays_set(2007))
        self.assertIn(date(2008, 4, 4), self.cal.holidays_set(2008))
        self.assertIn(date(2010, 4, 5), self.cal.holidays_set(2010))
        self.assertIn(date(2011, 4, 5), self.cal.holidays_set(2011))
        self.assertIn(date(2012, 4, 4), self.cal.holidays_set(2012))
        self.assertIn(date(2013, 4, 4), self.cal.holidays_set(2013))
        self.assertIn(date(2014, 4, 4), self.cal.holidays_set(2014))
