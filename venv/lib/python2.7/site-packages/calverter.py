#!/usr/bin/env python
##   calverter.py
##
##   Copyright (C) 2008-2010 Mehdi Bayazee (Bayazee@Gmail.com)
##
##   Iranian (Jalali) calendar: 
##           http://en.wikipedia.org/wiki/Iranian_calendar
##   Islamic (Hijri) calendar:
##           http://en.wikipedia.org/wiki/Islamic_calendar
##   Gregorian calendar:
##           http://en.wikipedia.org/wiki/Gregorian_calendar
##
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2, or (at your option)
##   any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.


__author__ = "Mehdi Bayazee"
__copyright__ = "Copyright (C) 2008-2010 Mehdi Bayazee"

__version__ = "1.6.1"


GREGORIAN_EPOCH = 1721425.5
GREGORIAN_WEEKDAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

ISLAMIC_EPOCH = 1948439.5
ISLAMIC_WEEKDAYS = ("al-ahad", "al-'ithnayn", "ath-thalatha'", "al-arbia`aa'", "al-khamis", "al-jumu`a", "as-sabt")
          
JALALI_EPOCH = 1948320.5
JALALI_WEEKDAYS = ("Yekshanbeh", "Doshanbeh", "Seshhanbeh", "Chaharshanbeh", "Panjshanbeh", "Jomeh", "Shanbeh")

import math

class Calverter:
    """
    Converter Main Class
    """
     
    def __init__(self):
        self.J0000 = 1721424.5 # Julian date of Gregorian epoch: 0000-01-01
        self.J1970 = 2440587.5 # Julian date at Unix epoch: 1970-01-01
        self.JMJD  = 2400000.5 # Epoch of Modified Julian Date system
        self.J1900 = 2415020.5 # Epoch (day 1) of Excel 1900 date system (PC)
        self.J1904 = 2416480.5 # Epoch (day 0) of Excel 1904 date system (Mac)
          
        self.norm_leap = ("Normal year", "Leap year")
     
    def jwday(self, j):
        "Calculate day of week from Julian day"
          
        return int(math.floor((j + 1.5))) % 7     
     
    def weekday_before(self, weekday, jd):
        """
        Return Julian date of given weekday (0 = Sunday)
        in the seven days ending on jd.
        """
          
        return jd - self.jwday(jd - weekday)
     
    def search_weekday(self, weekday, jd, direction, offset):
        """
        Determine the Julian date for: 
     
        @param weekday: Day of week desired, 0 = Sunday
        @param jd: Julian date to begin search
        @param direction: 1 = next weekday, -1 = last weekday
        @param offset: Offset from jd to begin search
        """
                 
        return self.weekday_before(weekday, jd + (direction * offset))
     
    # Utility weekday functions, just wrappers for search_weekday
     
    def nearest_weekday(self, weekday, jd):
        return self.search_weekday(weekday, jd, 1, 3)
     
    def next_weekday(self, weekday, jd):
        return self.search_weekday(weekday, jd, 1, 7)
     
    def next_or_current_weekday(self, weekday, jd):
        return self.search_weekday(weekday, jd, 1, 6)
     
    def previous_weekday(self, weekday, jd):
        return self.search_weekday(weekday, jd, -1, 1)
     
    def previous_or_current_weekday(self, weekday, jd):
        return self.search_weekday(weekday, jd, 1, 0)
         
    def leap_gregorian(self, year):
        "Is a given year in the Gregorian calendar a leap year ?"
          
        return ((year % 4) == 0) and (not(((year % 100) == 0) and ((year % 400) != 0)))
     
    def gregorian_to_jd(self, year, month, day):
        "Determine Julian day number from Gregorian calendar date"
         
        tm = 0 if month <= 2 else (-1 if self.leap_gregorian(year) else -2)
             
        return (GREGORIAN_EPOCH - 1) + (365 * (year - 1)) + math.floor((year - 1) / 4) +  (-math.floor((year - 1) / 100)) + \
            math.floor((year - 1) / 400) + math.floor((((367 * month) - 362) / 12) + tm + day)
     
    def jd_to_gregorian(self, jd) :
        "Calculate Gregorian calendar date from Julian day"
     
        wjd = math.floor(jd - 0.5) + 0.5
        depoch = wjd - GREGORIAN_EPOCH
        quadricent = math.floor(depoch / 146097)
        dqc = depoch % 146097
        cent = math.floor(dqc / 36524)
        dcent = dqc % 36524
        quad = math.floor(dcent / 1461)
        dquad = dcent % 1461
        yindex = math.floor(dquad / 365)
        year = int((quadricent * 400) + (cent * 100) + (quad * 4) + yindex)
        if not((cent == 4) or (yindex == 4)) :
            year += 1
      
        yearday = wjd - self.gregorian_to_jd(year, 1, 1)
          
        leapadj = 0 if wjd < self.gregorian_to_jd(year, 3, 1) else (1 if self.leap_gregorian(year) else 2)
         
        month = int(math.floor((((yearday + leapadj) * 12) + 373) / 367))
        day = int(wjd - self.gregorian_to_jd(year, month, 1)) + 1
      
        return year, month, day
     
    def n_weeks(self, weekday, jd, nthweek):
         
        j = 7 * nthweek
        if nthweek > 0 :
            j += self.previous_weekday(weekday, jd)
        else :
            j += self.next_weekday(weekday, jd)
        return j
     
    def iso_to_julian(self, year, week, day):
        "Return Julian day of given ISO year, week, and day"
          
        return day + self.n_weeks(0, self.gregorian_to_jd(year - 1, 12, 28), week)
     
    def jd_to_iso(self, jd):
        "Return array of ISO (year, week, day) for Julian day"
          
        year = self.jd_to_gregorian(jd - 3)[0]
        if jd >= self.iso_to_julian(year + 1, 1, 1) :
            year += 1
         
        week = int(math.floor((jd - self.iso_to_julian(year, 1, 1)) / 7) + 1)
        day = self.jwday(jd)
        if day == 0 :
            day = 7
         
        return year, week, day
     
    def iso_day_to_julian(self, year, day):
        "Return Julian day of given ISO year, and day of year"
          
        return (day - 1) + self.gregorian_to_jd(year, 1, 1)
     
    def jd_to_iso_day(self, jd):
        "Return array of ISO (year, day_of_year) for Julian day"
          
        year = self.jd_to_gregorian(jd)[0]
        day = int(math.floor(jd - self.gregorian_to_jd(year, 1, 1))) + 1
        return year, day
     
    def pad(self, Str, howlong, padwith) :
        "Pad a string to a given length with a given fill character. "
          
        s = str(Str)
     
        while s.length < howlong :
            s = padwith + s
        return s
     
    def leap_islamic(self, year):
        "Is a given year a leap year in the Islamic calendar ?"
          
        return (((year * 11) + 14) % 30) < 11
     
    def islamic_to_jd(self, year, month, day):
        "Determine Julian day from Islamic date"
          
        return (day + math.ceil(29.5 * (month - 1)) + (year - 1) * 354 + \
            math.floor((3 + (11 * year)) / 30) + ISLAMIC_EPOCH) - 1
     
    def jd_to_islamic(self, jd):
        "Calculate Islamic date from Julian day"
         
        jd = math.floor(jd) + 0.5
        year = int(math.floor(((30 * (jd - ISLAMIC_EPOCH)) + 10646) / 10631))
        month = int(min(12, math.ceil((jd - (29 + self.islamic_to_jd(year, 1, 1))) / 29.5) + 1))
        day = int(jd - self.islamic_to_jd(year, month, 1)) + 1;
        return year, month, day
     
    def leap_jalali(self, year):
        "Is a given year a leap year in the Jalali calendar ?"
     
        return ((((((year - 474 if year > 0 else 473 ) % 2820) + 474) + 38) * 682) % 2816) < 682
     
    def jalali_to_jd(self, year, month, day):
        "Determine Julian day from Jalali date"
          
        epbase = year - 474 if year>=0 else 473
        epyear = 474 + (epbase % 2820)
                
        if month <= 7 :
            mm = (month - 1) * 31
        else:
            mm = ((month - 1) * 30) + 6
     
        return day + mm + math.floor(((epyear * 682) - 110) / 2816) + (epyear - 1) * 365 + \
            math.floor(epbase / 2820) * 1029983 + (JALALI_EPOCH - 1)
     
    def jd_to_jalali(self, jd):
        "Calculate Jalali date from Julian day"
     
        jd = math.floor(jd) + 0.5
        depoch = jd - self.jalali_to_jd(475, 1, 1)
        cycle = math.floor(depoch / 1029983)
        cyear = depoch % 1029983
        if cyear == 1029982 :
            ycycle = 2820
        else :
            aux1 = math.floor(cyear / 366)
            aux2 = cyear % 366
            ycycle = math.floor(((2134 * aux1) + (2816 * aux2) + 2815) / 1028522) + aux1 + 1
         
        year = int(ycycle + (2820 * cycle) + 474)
        if year <= 0 :
            year -= 1
         
        yday = (jd - self.jalali_to_jd(year, 1, 1)) + 1
        if yday <= 186:
            month = int(math.ceil(yday / 31))
        else:
            month = int(math.ceil((yday - 6) / 30))
             
        day = int(jd - self.jalali_to_jd(year, month, 1)) + 1
        return year, month, day
     
