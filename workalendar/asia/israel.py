from datetime import date, timedelta
from gettext import gettext as _

from pyluach.dates import GregorianDate, HebrewDate

from ..core import Calendar, FRI, SAT
from ..registry_tools import iso_register


@iso_register("IL")
class Israel(Calendar):
    "Israel"

    WEEKEND_DAYS = (SAT, FRI)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)

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
                if day == 1:
                    days.append((current_date - delta, _("Rosh Hashana Eve")))
                    days.append((current_date, _("Rosh Hashana")))
                    days.append((current_date + delta, _("Rosh Hashana")))
                elif day == 10:
                    days.append((current_date - delta, _("Yom Kippur Eve")))
                    days.append((current_date, _("Yom Kippur")))
                elif day == 15:
                    days.append((current_date - delta, _("Sukkot Eve")))
                    days.append((current_date, _("Sukkot")))
                elif day == 22:
                    days.append((
                        current_date - delta, _("Shmini Atzeres Eve"))
                    )
                    days.append((current_date, _("Shmini Atzeres")))
            elif month == 1:
                if day == 15:
                    days.append((current_date - delta, _("Pesach Eve")))
                    days.append((current_date, _("Pesach")))
                elif day == 21:
                    days.append((current_date - delta, _("7th of Pesach Eve")))
                    days.append((current_date, _("7th of Pesach")))
            elif month == 2:
                if day == 5:
                    independence_date = current_date
                    if hebrew_date.weekday() == 6:
                        independence_date = HebrewDate(
                            jewish_year, month, 4
                        ).to_pydate()
                    elif hebrew_date.weekday() == 7:
                        independence_date = HebrewDate(
                            jewish_year, month, 3
                        ).to_pydate()
                    elif hebrew_date.weekday() == 2:
                        independence_date = HebrewDate(
                            jewish_year, month, 6
                        ).to_pydate()
                    days.append(
                        (independence_date - delta, _("Independence Day Eve"))
                    )
                    days.append((independence_date, _("Independence Day")))
            elif month == 3 and day == 6:
                days.append((current_date - delta, _("Shavout Eve")))
                days.append((current_date, _("Shavout")))

            current_date += delta

        return days
