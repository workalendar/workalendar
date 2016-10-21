CHANGELOG
=========

1.8
---

Now tests are run using tox and releases are made automatically
using Travis-CI deployment framework.

Incorporate changes from workalendar 0.8.0:

- Fix Czech Republic calendar - as of 2016, Good Friday has become a holiday (#148).

Incorporate changes from workalendar 0.7.0:

- Easter Sunday is a Brandenburg federate state holiday (#143), thx @uvchik.
- Added Catalonia (#145), thx @ferranp.
- Use `find_packages()` to fetch package directories in `setup.py` (#141, #144).
- use py.test instead of nosetests for tests (#146).
- cleanup: remove unused ``swiss.py`` file (#147).

Incorporate changes from workalendar 0.6.1:

- Added Estonia, thx to @landler (#134),
- Europe-related modules being reorganized, thx to @Natim (#135),
- Fixed King / Queen's day in Netherlands, thx to @PeterJacob (#138),
- Added a pull-request template (#125),
- Added a Makefile for various dev-related tasks -- installs, running tests, uploading to PyPI... (#133).

1.7.1
-----

- #7: Avoid crashing on import when installed as zip package.

1.7
---

Incorporate changes from workalendar 0.5.0:

- A new holiday has appeared in Japan as of 2016 (#131), thx @suhara for the report.

Incorporate changes from workalendar 0.4.5:

- Added Slovenia, thx to @ratek1 (#124).
- Added Switzerland, thx to @sykaeh (#127).

1.6
---

- #6: Remove observance shift for Sweden.
- Use `jaraco skeleton <https://github.com/jaraco/skeleton>`_ to
  maintain the project structure, adding automatic releases
  from continuous integration and bundled documentation.

1.5
---

Incorporate changes from workalendar 0.4.3:

- Added Denmark (#117).
- Tiny fixes in the ``usa.py`` module (flake8 + typo) (#122)
- Added datetime to date conversion in is_holiday() (#118)
- Added function to get the holiday label by date (#120)
- Moved from `novapost` to the `novafloss` organization, handling FLOSS projects in People Doc Inc. (#116)
- Added Spain 2016 (#123)

Incorporate changes from workalendar 0.4.2:

- Added Luxembourg (#111)
- Added Netherlands (#113)
- Added Spain (#114)
- Bugfix: fixed the name of the Pentecost for Sweden (#115)

Incorporate changes from workalendar 0.4.1:

- Added Portugal, thx to @borfast (#110).

Incorporate changes from workalendar 0.4.0:

- Added Colombia calendar, thx to @spalac24
- Added Slovakia calendar, thx to @Adman
- Fixed the Boxing day & boxing day shift for Australia

1.4 (2015-04-14)
----------------

``Calendar.get_observed_date`` now allows ``observance_shift`` to be
a callable accepting the holiday and calendar and returning the observed
date. ``Holiday`` supplies a ``get_nearest_weekday`` method suitable for
locating the nearest weekday.

- #5: USA Independence Day now honors the nearest weekday model.

1.3 (2015-02-15)
----------------

Incorporate these fixes from Workalendar 0.3:

- ``delta`` argument for ``add_working_days()`` can be negative. added a
  ``sub_working_days()`` method that computes working days backwards.
- BUGFIX: Renaming Showa Day. "ō is not romji" #100 (thx @shinriyo)
- BUGFIX: Belgian National Day title #99 (thx @laulaz)

1.2.1 (2015-02-15)
------------------

Correct usage in example.

1.2 (2015-01-07)
----------------

Fixed issue #4 where Finland holidays were shifted but shouldn't have been.
Calendars and Holidays may now specify observance_shift=None to signal no
shift.

Package can now be tested with pytest-runner by invoking ``python setup.py
pytest``.

1.1.3 (2014-12-29)
------------------

Fix name of Finnish Independence Day.

1.1.2 (2014-11-07)
------------------

Fixed issues with packaging (disabled installation an zip egg and now use
setuptools always).

1.1 (2014-11-07)
----------------

UnitedKingdom Calendar now uses indicated/observed Holidays.

Includes these changes slated for workalendar 0.3:

- BUGFIX: shifting UK boxing day if Christmas day falls on a Friday (shit to
  next Monday) #95

1.0 (2014-09-21)
----------------

Initial release of Calendra based on Workalendar 0.2.

- Adds Holiday class per `Workalendar Pull Request #72
  <https://github.com/novapost/workalendar/pull/79>`_. Adds support for giving
  holidays a more rich description and better resolution of observed versus
  indicated holidays. See the pull request for detail on the motivation and
  implementation. See the usa.UnitedStates calendar for example usage.

Includes these changes slated for workalendar 0.3:

- Germany calendar added, thx to @rndusr
- Support building on systems where LANG=C (Ubuntu) #92
- little improvement to directly return a tested value.


0.2.0 (2014-07-15)
------------------

- How to contribute documentation,
- Added Belgium, European Central Bank, Sweden, every specific calendar in the
  United States of America, Canada.
- BUGFIX: fixed a corpus christi bug. This day used to be included in every
  ChristianMixin calendar, except noticed otherwise. Now it's not included by
  default and should be set to "True" when needed.


0.1 (2014-02-17)
----------------

- added LunarCalendar, including lunar month calculations
- added SouthKoreanCalendar, for a LunarCalendar proof of concept
- added Python3 support
- added Algeria, Australia, Brazil, Chile, Czech Republic, Finland,
  France Alsace-Moselle, Greece, Hungary, Iceland, Italy, Ivory Coast, Japan,
  Madagascar, Marshall Islands, Mexico, Northern Ireland, Norway, Panama,
  Poland, Qatar, South Africa, São Tomé, Taiwan, United Kingdom calendars.
- BACKWARDS INCOMPATIBILITY: calendar suffix for class names are now obsolete.
  e.g: to use the Japan calendar, simply import `workalendar.asia.Japan` instead
  of JapanCalendar.


v0.0.1 (2013-11-21)
-------------------

- First released version
- Core calendar classes, Western (European and North American)
  easter computations,
- United States federal days
- France legal holidays days
