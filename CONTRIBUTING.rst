=========================
Contribute to Workalendar
=========================

Use it (and test it)
====================

If you are using ``workalendar``, you are already contributing to it. As long
as you are able to check its result, compare the designated working days and
holidays to the reality, and make sure these are right,  it's fine.

If any of the computed holidays for the country / area your are using is
**wrong**, please report
`it using the Github issues <https://github.com/novapost/workalendar/issues>`_.


Adding new calendars
====================

Since ``workalendar`` is mainly built around configuration variables and generic
methods, it's not that difficult to add a calendar to our codebase. A few
**mandatory** steps should be observed:

1. Fork the repository and create a new branch named after the calendar you want to implement,
2. Add a test class to the workalendar test suite that checks holidays,
3. Implement the class using the core class APIs as much as possible. Test it until all tests pass.
4. Make a nice pull-request we'll be glad to review and merge when it's perfect.

.. note::

    Please respect the PEP8 convention, otherwise your PR won't be accepted.

Example
-------

Let's assume you want to include the holidays of the magic (fictional) kingdom
of "Zhraa", which has a few holidays of different kind.

For the sake of the example, it has the following specs:

* it's a Gregorian-based Calendar (i.e. the Western European / American one),
* even if the King is not versed into religions, the kingdom includes a few Christian holidays,
* even if you never knew about it, it is set in Oceania,

Here is a list of the holidays in *Zhraa*:

* January 1st, New year's Day,
* May 1st, Labour day,
* Easter Monday, which is variable (from march to may),
* The first monday in June, to celebrate the birth of the Founder of the Kingdom, Zhraa (nobody knows the exact day he was born, so this day was chosen as a convention),
* The birthday of the King, August 2nd.
* Christmas Day, Dec 25th.


Test-driven start
#################


Let's prepare the Zhraa class. In the ``workalendar/oceania.py`` file, add
a class like this::

    class Zhraa(WesternCalendar):
        pass


Now, we're building a test class. Edit the ``workalendar/tests/test_oceania.py``
file and add the following code::

    from workalendar.oceania import Zhraa
    # snip...

    class ZhraaTest(GenericCalendarTest):
        cal_class = Zhraa

        def test_year_2014(self):
            holidays = self.cal.holidays_set(2014)
            self.assertIn(date(2014, 1, 1), holidays)  # new year
            self.assertIn(date(2014, 5, 1), holidays)  # labour day
            self.assertIn(date(2014, 8, 2), holidays)  # king birthday
            self.assertIn(date(2014, 12, 25), holidays)  # Xmas
            # variable days
            self.assertIn(date(2014, 4, 21), holidays)  # easter monday
            self.assertIn(date(2014, 6, 2), holidays)  # First MON in June

of course, if you run the test using the ``make test`` command, this will fail.

With the ``WesternCalendar`` base class you have at least one holiday as a bonus:
the New year's day, which is commonly a holiday.

Add fixed days
##############

::

    class Zhraa(WesternCalendar):
        FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
            (5, 1, "Labour Day"),
            (8, 2, "King Birthday"),
        )

Now we've got 3 holidays out of 6.

Add religious holidays
######################

Using ChristianMixin as a base to our Zhraa class will instantly add Christmas
Day as a holiday. Now we can add Easter monday just by triggering the correct
flag.

::

    class Zhraa(WesternCalendar, ChristianMixin):
        include_easter_monday = True
        FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
            (5, 1, "Labour Day"),
            (8, 2, "King Birthday"),
        )

Almost there, 5 holidays out of 6.

Add variable "non-usual" holidays
#################################

There are many static methods that will grant you a clean access to variable
days computation. It's very easy to add days like the "Birthday of the Founder"::


    class Zhraa(WesternCalendar, ChristianMixin):
        include_easter_monday = True
        FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
            (5, 1, "Labour Day"),
            (8, 2, "King Birthday"),
        )

        def get_variable_days(self, year):
            # usual variable days
            days = super(Zhraa, self).get_variable_days(year)

            days.append(
                (Zhraa.get_nth_weekday_in_month(year, 6, MON),
                'Day of the Founder'),
            )
            return days

.. note::

    Please mind that the returned "variable_days" is a list of tuples. The first
    item being a date object (in the Python ``datetime.date`` sense) and the
    second one is the label string.


There you are. Commit, test, make sure it works for other years as well and
you're almost there.

We're planning to build a complete documentation for the other cases (special
holiday rules, other calendar types, other religions, etc). But with this
tutorial you're sorted for a lot of other calendars.


Other code contributions
========================

There are dozens of calendars all over the world. We'd appreciate you to
contribute to the core of the library by adding some new Mixins or Calendars.

Bear in mind that the code you'd provide **must** be tested using unittests
before you submit your pull-request.
