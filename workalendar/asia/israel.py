# -*- coding: utf-8 -*-
from __future__ import (absolute_import, unicode_literals)
from datetime import date, timedelta

from pyluach.dates import GregorianDate, HebrewDate

from ..core import Calendar, FRI, SAT
from ..registry import iso_register


@iso_register("IL")
class Israel(Calendar):
    "Israel"

    WEEKEND_DAYS = (SAT, FRI)

    def get_variable_days(self, year):
        days = super(Israel, self).get_variable_days(year)

        delta = timedelta(days=1)
        current_date = date(year, 1, 1)

        while current_date.year == year:
            hebrew_date = GregorianDate(
                year=current_date.year,
                month=current_date.month,
                day=current_date.day,
            ).to_heb()

            jewish_year = hebrew_date.year
            month = hebrew_date.month
            day = hebrew_date.day

            if month == 7:
                if day in {1, 2, 3}:
                    days.append((current_date, "Rosh Hashana"))
                elif day == 10:
                    days.append((current_date, "Yom Kippur"))
                elif day in range(15, 22):
                    days.append((current_date, "Sukkot"))
                elif day == 22:
                    days.append((current_date, "Shmini Atzeres"))
            elif month == 12 and not HebrewDate._is_leap(jewish_year):
                if day == 14:
                    days.append((current_date, "Purim"))
                if day == 15:
                    days.append((current_date, "Purim"))
                    days.append((current_date, "Shushan Purim"))
                elif day == 16:
                    days.append((current_date, "Shushan Purim"))
            elif month == 13:
                if day == 14:
                    days.append((current_date, "Purim"))
                elif day == 15:
                    days.append((current_date, "Purim"))
                    days.append((current_date, "Shushan Purim"))
                elif day == 16:
                    days.append((current_date, "Shushan Purim"))
            elif month == 1 and day in {15, 21}:
                days.append((current_date, "Pesach"))
            elif month == 2:
                if day == 5:
                    if hebrew_date.weekday() == 6:
                        days.append(
                            (
                                HebrewDate(jewish_year, month, 4).to_pydate(),
                                "Independence Day",
                            )
                        )
                    elif hebrew_date.weekday() == 7:
                        days.append(
                            (
                                HebrewDate(jewish_year, month, 3).to_pydate(),
                                "Independence Day",
                            )
                        )
                    elif hebrew_date.weekday() == 2:
                        days.append(
                            (
                                HebrewDate(jewish_year, month, 6).to_pydate(),
                                "Independence Day",
                            )
                        )
                    else:
                        days.append((current_date, "Independence Day"))
            elif month == 3 and day == 6:
                days.append((current_date, "Shavout"))

            current_date += delta

        return days
