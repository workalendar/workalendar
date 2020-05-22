from pyluach.dates import GregorianDate, HebrewDate

from ..core import Calendar, FRI, SAT
from ..registry_tools import iso_register


@iso_register("IL")
class Israel(Calendar):
    "Israel"

    WEEKEND_DAYS = (SAT, FRI)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)

        hebrew_date = GregorianDate(year=year, month=1, day=1).to_heb()
        jewish_year = hebrew_date.year

        holidays_hebrew_dates = [
            (HebrewDate(jewish_year, 6, 29), "Rosh Hashana Eve"),
            (HebrewDate(jewish_year + 1, 7, 1), "Rosh Hashana"),
            (HebrewDate(jewish_year + 1, 7, 2), "Rosh Hashana"),
            (HebrewDate(jewish_year + 1, 7, 9), "Yom Kippur Eve"),
            (HebrewDate(jewish_year + 1, 7, 10), "Yom Kippur"),
            (HebrewDate(jewish_year + 1, 7, 14), "Sukkot Eve"),
            (HebrewDate(jewish_year + 1, 7, 15), "Sukkot"),
            (HebrewDate(jewish_year + 1, 7, 21), "Shmini Atzeres Eve"),
            (HebrewDate(jewish_year + 1, 7, 22), "Shmini Atzeres"),
            (HebrewDate(jewish_year, 1, 14), "Pesach Eve"),
            (HebrewDate(jewish_year, 1, 15), "Pesach"),
            (HebrewDate(jewish_year, 1, 20), "7th of Pesach Eve"),
            (HebrewDate(jewish_year, 1, 21), "7th of Pesach"),
            (HebrewDate(jewish_year, 3, 5), "Shavout Eve"),
            (HebrewDate(jewish_year, 3, 6), "Shavout"),
        ]
        holidays_hebrew_dates += self.get_hebrew_independence_day(jewish_year)

        for holiday_hebrew_date, holiday_name in holidays_hebrew_dates:
            days.append((holiday_hebrew_date.to_pydate(), holiday_name))
        return days

    def get_hebrew_independence_day(self, jewish_year):
        """
        Returns the independence day eve and independence day dates
        according to the given hebrew year

        :param jewish_year: the specific hebrew year for calculating
                            the independence day dates
        :return: independence day dates
                 in the type of List[Tuple[HebrewDate, str]]
        """
        month = 2
        day = 5
        original_hebrew_independence_date = HebrewDate(jewish_year, month, day)
        if original_hebrew_independence_date.weekday() == 6:
            day = 4
        if original_hebrew_independence_date.weekday() == 7:
            day = 3
        if original_hebrew_independence_date.weekday() == 2:
            day = 6
        return [
            (HebrewDate(jewish_year, month, day - 1), "Independence Day Eve"),
            (HebrewDate(jewish_year, month, day), "Independence Day")
        ]
