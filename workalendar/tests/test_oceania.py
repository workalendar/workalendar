from datetime import date

from workalendar.tests import GenericCalendarTest
from workalendar.oceania import AustraliaCalendar
from workalendar.oceania import AustraliaCapitalTerritoryCalendar
from workalendar.oceania import AustraliaNewSouthWalesCalendar
from workalendar.oceania import AustraliaNorthernTerritoryCalendar


class AustraliaCalendarTest(GenericCalendarTest):
    cal_class = AustraliaCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 1, 26), holidays)
        self.assertIn(date(2013, 3, 29), holidays)  # Good Friday
        self.assertIn(date(2013, 4, 25), holidays)
        self.assertIn(date(2013, 12, 25), holidays)


class AustraliaCapitalTerritoryCalendarTest(AustraliaCalendarTest):
    cal_class = AustraliaCapitalTerritoryCalendar

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 11), holidays)
        self.assertIn(date(2013, 3, 30), holidays)  # Easter Saturday
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 9, 30), holidays)
        self.assertIn(date(2013, 10, 7), holidays)  # Labour day october
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day
        holidays = self.cal.holidays(2013)
        self.assertEquals(len(holidays), 12)


class AustraliaNewSouthWalesCalendarTest(AustraliaCalendarTest):
    cal_class = AustraliaNewSouthWalesCalendar

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 30), holidays)  # Good friday
        self.assertIn(date(2013, 3, 31), holidays)  # Easter Sunday
        self.assertIn(date(2013, 4, 1), holidays)  # Easter Monday
        self.assertIn(date(2013, 6, 10), holidays)  # Queen's Bday
        self.assertIn(date(2013, 10, 7), holidays)  # Labour day october
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day
        holidays = self.cal.holidays(2013)
        self.assertEquals(len(holidays), 11)


class AustraliaNorthernTerritoryCalendarTest(AustraliaCalendarTest):
    cal_class = AustraliaNorthernTerritoryCalendar

    def test_regional_specific_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 30), holidays)  # Easter Saturday
        self.assertIn(date(2013, 4, 1), holidays)  # Easter Monday
        self.assertIn(date(2013, 5, 6), holidays)  # May Day

