from datetime import date

from ..core import OrthodoxCalendar, MON, daterange, cleaned_date
from ..registry_tools import iso_register


@iso_register('RU')
class Russia(OrthodoxCalendar):
    'Russia'
    # Civil holidays
    include_labour_day = True

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (2, 23, "Defendence of the Fatherland"),
        (3, 8, "International Women's Day"),
        (5, 9, "Victory Day"),
        (6, 12, "National Day"),
        (11, 4, "Day of Unity"),
    )

    # Christian holidays
    include_christmas = False

    covid19_2020_start = date(2020, 3, 28)
    covid19_2020_end = date(2020, 4, 30)

    def get_fixed_holidays(self, year):

        if year >= 1992:
            self.labour_day_label = "The Day of Spring and Labour"
        else:
            self.labour_day_label = "International Workers' Day"

        days = super().get_fixed_holidays(year)

        if year >= 2005:
            days.extend([
                (date(year, 1, 3), "Third Day after New Year"),
                (date(year, 1, 4), "Fourth Day after New Year"),
                (date(year, 1, 5), "Fifth Day after New Year"),
                (date(year, 1, 6), "Sixth Day after New Year"),
                (date(year, 1, 8), "Eighth Day after New Year"),
            ])

        if year == 2020:
            index = 1
            for day in daterange(self.covid19_2020_start,
                                 self.covid19_2020_end):
                days.append(
                    (day, f"Non-Working Day (COVID-19) #{index}")
                )
                index += 1

            # Adding May extra days
            days.extend([
                (date(year, 5, 4), "May 4th, 2020 holiday"),
                (date(year, 5, 5), "Day of Spring and Labor"),
            ])

            # Extra COVID-19 in May
            days.extend([
                (date(year, 5, 6), "Covid-19 May #1"),
                (date(year, 5, 7), "Covid-19 May #2"),
                (date(year, 5, 8), "Covid-19 May #3"),
            ])

            # Constitution Vote Public Holiday
            days.append((date(year, 7, 1), "Constitution Vote Public Holiday"))
        elif year == 2021:
            days.extend([
                (date(year, 2, 22), "Day Before Defendence of the Fatherland"),
                (date(year, 11, 5), 'Day After Day of Unity'),
                (date(year, 12, 31), "New Year's Eve"),
            ])
        return days

    def get_calendar_holidays(self, year):
        holidays = super().get_calendar_holidays(year)
        shifts = []
        for day, label in holidays:
            if day.month == 1 and day.day in range(1, 9):
                continue
            # Add an exception for 2020 non-working days due to COVID-19
            if self.covid19_2020_start <= day <= self.covid19_2020_end:
                continue  # pragma: no cover
            if day.weekday() in self.get_weekend_days():
                shifts.append((
                    self.get_first_weekday_after(day, MON),
                    label + " shift"
                ))
        holidays.extend(shifts)
        return holidays

    def is_working_day(self, day,
                       extra_working_days=None, extra_holidays=None):
        day = cleaned_date(day)
        if day == date(2021, 2, 20):
            return True
        return super().is_working_day(
            day,
            extra_working_days=extra_working_days,
            extra_holidays=extra_holidays
        )
