#-*- coding: utf-8 -*-
from datetime import timedelta, date
from workalendar.core import WesternCalendar
from workalendar.core import SUN
from workalendar.core import IslamicMixin, ChristianMixin


class AlgeriaCalendar(WesternCalendar, IslamicMixin):
    "Algeria calendar"
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_islamic_new_year = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (7, 5, "Independance Day"),
        (11, 1, "Anniversary of the revolution"),
    )

    ISLAMIC_HOLIDAYS = IslamicMixin.ISLAMIC_HOLIDAYS + (
        (1, 10, "Ashura"),
    )


class BeninCalendar(WesternCalendar, IslamicMixin, ChristianMixin):
    "Benin calendar"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
    # Islamic holidays
    include_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Tabaski"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 10, "Traditional Day"),
        (5, 1, "Labour Day"),
        (8, 1, "Independance Day"),
        (10, 26, "Armed Forces Day"),
        (11, 30, "National Day"),
    )


class IvoryCoastCalendar(WesternCalendar, ChristianMixin, IslamicMixin):
    "Ivory Coast"
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True
    include_day_after_prophet_birthday = True
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Feast of the Sacrifice"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (8, 7, "Independance Day"),
        (11, 15, "National Peace Day"),
    )


class MadagascarCalendar(WesternCalendar, ChristianMixin):
    "Madagascar"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 29, "Martyrs' Day"),
        (5, 1, "Labour Day"),
        (6, 26, "Independence Day"),
    )
    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True


class SaoTomeAndPrincipeCalendar(WesternCalendar, ChristianMixin):
    u"São Tomé and Príncipe"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 3, "Martyr's Day"),
        (5, 1, "Labour Day"),
        (7, 12, "Independance Day"),
        (9, 6, "Armed Forces Day"),
        (9, 30, "Agricultural Reform Day"),
        (12, 21, u"São Tomé Day"),
    )
    include_all_saints = True


class SouthAfricaCalendar(WesternCalendar, ChristianMixin):
    "South Africa calendar"
    include_good_friday = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (3, 21, 'Human Rights Day'),
        (4, 27, "Freedom Day"),
        (5, 1, "Workers Day"),
        (6, 16, "Youth Day"),
        (8, 9, "National Women Day"),
        (9, 24, "Heritage Day"),
        (12, 16, "Day of reconcilation"),
        (12, 26, "Day of good will"),
    )

    def get_family_day(self, year):
        return (self.get_good_friday(year), "Family Day")

    def get_variable_days(self, year):
        days = super(SouthAfricaCalendar, self).get_variable_days(year)
        days.append(self.get_family_day(year))
        # compute shifting days
        for month, day, label in self.FIXED_HOLIDAYS:
            holiday = date(year, month, day)
            if holiday.weekday() == SUN:
                days.append((
                    holiday + timedelta(days=1),
                    "%s substitute" % label
                ))
        return days
