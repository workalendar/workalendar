from datetime import date

from workalendar.tests import GenericCalendarTest
from workalendar.oceania import AustraliaCalendar
from workalendar.oceania import AustraliaCapitalTerritoryCalendar


class AustraliaCalendarTest(GenericCalendarTest):
    cal_class = AustraliaCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 4, 25), holidays)
        self.assertIn(date(2013, 12, 25), holidays)


class AustraliaCapitalTerritoryCalendarTest(AustraliaCalendarTest):
    cal_class = AustraliaCapitalTerritoryCalendar

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 11), holidays)
        self.assertIn(date(2013, 3, 30), holidays)
        self.assertIn(date(2013, 6, 10), holidays)
        self.assertIn(date(2013, 9, 30), holidays)
        self.assertIn(date(2013, 10, 7), holidays)
