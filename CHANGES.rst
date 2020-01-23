v6.1.1
------

Fix version inference when installed from sdist.

v6.1.0
------

Incorporate changes from workalendar v8.0.0 (2020-01-10)

- **BREAKING CHANGE** Drop Support for Python 2 - EOL January 1st 2020 (#442).
- Added Ukraine calendar, by @apelloni.
- Small cleanup in the ``.travis.yml`` file, thx to @Natim.

- Changes in the ``registry.items()`` method API.
  - This method is aliased to ``get_calendars()``. In a near release, the ``items()`` method will change its purpose.
  - The ``get_calendars()`` method accepts an empty/missing ``region_codes`` argument to retrieve the full registry. Please see the [ISO Registry documentation](https://peopledoc.github.io/workalendar/iso-registry.html) for extensive usage docs (#403, #375).

Incorporate changes from workalendar v7.2.0 (2019-12-06)

New calendars

- Added Serbia calendar, by @apelloni (#435).
- Added Argentina calendar, by @ftatarli (#419).

Other changes

- Update China's public holidays for 2020, thx @nut-free (#429).
- Update Malaysia and Singapore for 2021 (Deepavali + Thaipusam) by @jack-pace (#432).
- Small refactorings on the Gevena (Switzerland) holiday class, thx to @cw-intellineers (#420).

Incorporate changes from workalendar v7.1.1 (2019-11-22)

- **Bugfix** for USA: Fixed incorrect implementation for Thanksgiving Friday, thx @deveshvar (#422).
- Fix Advanced usage documentation about Thanksgiving Day (#426).
- Added Geneva calendar by @cw-intellineers (#420).

Incorporate changes from workalendar v7.1.0 (2019-11-15)

New calendars

- Added 27 Brazil calendars -- thanks a lot to @luismalta & @mileo, (#409 & #415)

Enhancements

- Added compatibility with Python 3.8 (#406).
- Added an IBGE_REGISTER to reference IBGE (brazilian) calendars with related tests (#415).
- Improve ISO registry interface by raising an error when trying to register a non-Calendar class (#412).

Other changes

- Fixes and additions to some Brazil calendars ; again, thanks to @luismalta & @mileo, (#409 & #415)
- Fix Denmark, re-add Christmas Eve, which is widely treated as public holiday ; thx to @KidkArolis, (#414).
- Increase Malaysia coverage by adding tests for missing Deepavali & Thaipusam.
- Increase China coverage by adding tests for special extra-holidays & extra-working days cases.


v6.0.0
------

Require Python 3.6 or later.

v5.0.0
------

#11: Add support for ``__add__`` and ``__sub__`` for
``Holiday`` instances on Python 3.8 and later. Now adding
a timedelta to a ``Holiday`` returns another ``Holiday``.

Incorporate changes from workalendar v7.0.0 (2019-09-20)

- Drop `ephem` astronomical calculation library, in favor of `skyfield` and `skyfield-data` for providing minimal data files to enable computation (#302, #348). Many thanks to @GammaSagittarii for the tremendous help on finding the right way to compute Chinese Solar Terms. Also thanks to @antvig and @DainDwarf for testing the beta version (#398).

Incorporate changes from workalendar v6.0.1 (2019-09-17)

- Fix Turkey Republic Day (#399, thx to @mhmtozc & @Natim).

Incorporate changes from workalendar v6.0.0 (2019-08-02)

- **Deprecation Notice:** *The global ISO registry now returns plain `dict` objects from its various methods.*
- Global registry now returns plain built-in dicts (#375).
- Removed `EphemMixin` in favor of astronomical functions (#302).
- Added first day counting when computing working_days delta (#393), thx @Querdos.

Incorporate changes from workalendar v5.2.3 (2019-07-11)
- Fix Romania, make sure Easter and related holidays are calculated using the Orthodox calendar, thx to @KidkArolis (#389).


v4.0.0
------

Incorporate changes from workalendar v5.2.2. (2019-07-07)

- **Deprecation Warning:** *Currently the registry returns `OrderedDict` objects when you're querying for regions or subregions. Expect that the next major release will preferrably return plain'ol' `dict` objects. If your scripts rely on the order of the objects returned, you'll have to sort them yourself.*
- Fix Denmark, remove observances (remove Palm Sunday, Constitution Day, Christmas Eve and New Year's Eve) (#387, #386)

Incorporate changes from workalendar v5.2.1 (2019-07-05)

- Refactored the package building procedure, now linked to `make package` ; added a note about this target in the PR template (#366).
- Fixed United Kingom's 2020 holidays ; The Early May Bank Holiday has been moved to May 8th to commemorate the 75th anniversary of the end of WWII (#381).

Incorporate changes from workalendar v5.2.0 (2019-07-04)

- New Calendar

    - Added JapanBank by @raybuhr (#379, #369).

- Other changes

    - Added adjustments to 2019-2020 Japan calendar due to the coronation of a new emperor (#379).
    - Add a note about the fact that contributors should not change the version number in the changelog and/or the ``setup.py`` file (#380).

Incorporate changes from workalendar v5.1.1 (2019-06-27)

- Display missing lines in coverage report (#376).
- Add "Europe Day" for Luxembourg (#377).

Incorporate changes from workalendar v5.1.0 (2019-06-24)

- New Calendar

    - Added Turkey by @tayyipgoren (#371).

- Other changes

    - Change registry mechanism to avoid circular imports (#288).
    - Internal: Added a "Release" section to the Pull Request template.
    - Internal: Added advices on the Changelog entry in the Contributing document.
    - Bugfix: Fixing North Carolina shift rules when Christmas Day happens on Saturday (#232).
    - Documentation: rearrange country list in ``README.rst`` (sorting and fixing nested lists).
    - Documentation: Renamed and changed format of the "Contributing guidelines" document, now in Markdown (GFM variant), with a few fixes (#368).
    - Internal: remove coverage targets ; now coverage reports are displayed for each tox job, but they won't output classes with 100% coverage.

Incorporate changes from workalendar v5.0.3 (2019-06-07)

- Bugfix: Panama - Fixed incorrect independence from Spain date, thanks to @chopanpma (#361).

Incorporate changes from workalendar v5.0.2 (2019-06-03)

- Bugfix: Israel - Fixed incorrect Purim/Shushan Purim dates in jewish leap years, thx @orzarchi. This fix cancels the last (5.0.1) version, that will be deleted from PyPI.

Incorporate changes from workalendar v5.0.1 (2019-06-03)

- **WARNING** This version contains known bugs on Israel calendar. Please do not use it in production.

- Bugfix: Israel - Fixed incorrect Purim/Shushan Purim dates in jewish leap years, thx @orzarchi.

Incorporate changes from workalendar v5.0.0 (2019-05-24)

- Major Changes & fixes

    - Dropped Python 3.4 support (#352).
    - Added Malaysia Thaipusam days for the year 2019 & 2020 - thx @burlak for the bug report (#354).
    - Fixed Deepavali dates for the year 2018 ; confirmed fixed dates that were set in the past.

- Added calendars

    - Added Florida specific calendars: Florida Legal, Florida Circuit Courts, Miami-Dade (#216).

Incorporate changes from workalendar v4.4.0 (2019-05-17)

- **WARNING**: This release will be the last one to support Python 3.4, which has [reached its End of Life and has been retired](https://www.python.org/dev/peps/pep-0429/#release-schedule). Please upgrade.

- Added calendar

    - Added California specific calendars: California Education, Berkeley, San Francisco, West Hollywood (#215).

- Fixes

    - Added a few refactors and tests for Australia Capital Territory holiday named "Family & Community Day", that lasted from 2007 to 2017 (#25).
    - Added South African 2019 National Elections as holiday (#350), by @RichardOB.

Incorporate changes from workalendar v4.3.1 (2019-05-03)

- Bugfix: Update 2019 Labour Day Holidays for China as changed by government recently (2019-03-22), by @iamsk, and thanks to @ltyely for their patch (#345 & #347).

Incorporate changes from workalendar v4.3.0 (2019-03-15)

- New Calendar

    - Added Barbados by @ludsoft.

- Fixes

    - Added isolated tests for shifting mechanics in USA calendars - previously untested (#335).
    - Added Berlin specific holidays (#340).
    - Added several one-off public holidays to UK calendar (#336).

Incorporate changes from workalendar v4.2.0 (2019-02-21)

- New calendars

    - Added several US territories and other specific calendars:

        - American Samoa territory (#218).
        - Chicago, Illinois (#220).
        - Guam territory (#219).
        - Suffolk County, Massachusetts (#222).

    - Added Cayman Islands, British Overseas Territory (#328)

Incorporate changes from workalendar v4.1.0 (2019-02-07)

- New calendars

- **WARNING** Scotland (sub)calendars are highly experimental and because of their very puzzling rules, may be false. Please use them with care.

    - Added Scotland calendars, i.e. Scotland, Aberdeen, Angus, Arbroath, Ayr, Carnoustie & Monifieth, Clydebank, Dumfries & Galloway, Dundee, East Dunbartonshire, Edinburgh, Elgin, Falkirk, Fife, Galashiels, Glasgow, Hawick, Inverclyde, Inverness, Kilmarnock, Lochaber, Monifieth, North Lanarkshire, Paisley, Perth, Scottish Borders, South Lanarkshire, Stirling, and West Dunbartonshire (#31).

- Bugfixes

    - Fixed United Kingdom bank holiday for 2002 and 2012, thx @ludsoft (#315).
    - Fix a small flake8 issue with wrong indentation (#319).
    - Fix Russia "Day of Unity" date, set to November 4th, thx @alexitkes for the bug report (#317).

Incorporate changes from workalendar v4.0.0 (2019-01-24)

- Solved the incompatibility between `pandas` latest version and Python 3.4. Upgraded travis distro to Xenial/16.04 LTS (#307).
- Added instructions about the usage of the `iso_register` decorator in the pull-request template (#309).

- New Calendars

    - Added New Zealand, by @johnguant (#306).
    - Added Paraguay calendar, following the work of @reichert (#268).
    - Added China calendar, by @iamsk (#304).
    - Added Israel, by @armona, @tsehori (#281).

3.0
---

Incorporate changes from workalendar 3.2.1:

- Added DEEPAVALI days for 2019 and 2020, thx @pvalenti (#282).
- Fixed Germany Reformation Day miscalculation. Some German states include Reformation Day since the "beginning" ; in 2017, all states included Reformation Day as a holiday (500th anniversary of the Reformation) ; starting of 2018, 4 states added Reformation Day (#295).

Incorporate changes from workalendar 3.2.0:

- Removed dependency to `PyEphem`. This package was the "Python2-compatible" library to deal with the xephem system library. Now it's obsolete, so you don't need this dual-dependency handling, because `ephem` is compatible with Python 2 & Python 3 (#296).
- Raise an exception when trying to use unsupported date/datetime types. Workalendar now only supports stdlib `date` & `datetime` (sub)types. See the `basic documentation <https://peopledoc.github.io/workalendar/basic.html#standard-datetime-types-only-please>`_ for more details (#294).

Incorporate changes from workalendar 3.1.1:

- Fixed ISO 3166-1 code for the `Slovenia` calendar (#291, thx @john-sandall).

Incorporate changes from workalendar 3.1.0:

- Added support for Python 3.7 (#283).
- Fixed the `SouthAfrica` holidays calendar, taking into account the specs of holidays that vary over the periods. As a consequence, it cleaned up erroneous holidays that were duplicated in some years (#285). Thx to @surfer190 for his review & suggestions.
- Bugfix for South Africa: disabled the possibility to compute holidays prior to the year 1910.
- Renamed Madagascar test class name into `MadagascarTest` (#286).
- Separated the coverage jobs from the pure tests. Their report output was disturbing in development mode, you had to scroll your way up to find eventual failing tests (#289).

Incorporate changes from workalendar 3.0.0:

Large work on global registry: refs (#13), (#96), (#257) & (#284).

- Added Tests for Europe registry.
- Revamped and cleaned up Europe countries.
- Added the United States of America + States, American countries & sub-regions, African countries, Asian countries, Oceanian countries.
- The global registry usage is documented.
- Changed Canada namespace to `workalendar.america.canada`.
- You don't have to declare a `name` properties for Calendar classes. It will be deducted from the docstring.
- Changed the `registry.items()` mandatory argument name to `region_codes` for more readability.

Incorporate changes from workalendar 2.6.0:

- Added Angola, by @dvdmgl (#276)
- Portugal - removed carnival from Portuguese holidays, restored missing holidays (#275)
- Added All Souls Day to common (#274)
- Allow the `add_working_days()` function to be provided a datetime, and returning a `date` (#270).
- Added a `keep_datetime` option to keep the original type of the input argument for both ``add_working_days()`` and ``sub_working_days()`` functions (#270).
- Fixed usage examples of ``get_first_weekday_after()`` docstring + in code (calendars and tests) ; do not use magic values, use MON, TUE, etc (#271).
- Turned Changelog into a Markdown file (#272).
- Added basic usage documentation, hosted by Github pages.
- Added advanced usage documentation.

Incorporate changes from workalendar 2.5.0:

- Bugfix: deduplicate South Africa holidays that were emitted as duplicates (#265).
- Add the `get_working_days_delta` method to the core calendar class (#260).

Incorporate changes from workalendar 2.4.0:

- Added Lithuania, by @landler (#254).
- Added Russia, by @vanadium23 (#259).
- Fixed shifting ANZAC day for Australia states (#249).
- Renamed Australian state classes to actual state names(eg. AustraliaNewSouthWales to NewSouthWales).
- Update ACT holidays (#251).
- Fixing Federal Christmas Shift ; added a `include_veterans_day` flag to enable/disable Veteran's day on specific calendar - e.g. Mozilla's dedicated calendar (#242).
- **Deprecation:** Dropped support for Python 3.3 (#245).
- Fixed Travis-ci configuration for Python 3.5 and al (#252).
- First step iteration on the "global registry" feature. European countries are now part of a registry loaded in the ``workalendar.registry`` module. Please use with care at the moment (#248).
- Refactored Australia family and community day calculation (#244).

2.0
---

Incorporate changes from workalendar 2.1.0:

- Added Hong Kong, by @nedlowe (#235).
- Splitted `africa.py` file into an `africa/` module (#236).
- Added Alabama Counties - Baldwin County, Mobile County, Perry County. Refactored UnitedStates classes to have a parameter to include the "Mardi Gras" day (#214).
- Added brazilian calendar to consider working days for bank transactions, by @fvlima (#238).

Incorporate changes from workalendar 2.0.0:

- Major refactor in the USA module. Each State is now an independant module, all of the Mixins were removed, all the possible corrections have been made, following the main Wikipedia page, and cross-checking with official sources when it was possible (#171).
- Added District of Columbia in the USA module (#217).
- Run tests with Python3.6 in CI (#210)
- Small refactors / cleanups in the following calendars: Hungary, Iceland, Ireland, Latvia, Netherlands, Spain, Japan, Taiwan, Australia, Canada, USA (#209).
- Various refactors for the Asia module, essentially centered around a more convenient Chinese New Year computation toolset (#202).
- Refactoring the USA tests: using inheritance to test federal and state-based holidays using only one "Don't Repeat Yourself" codebase (#213).

Incorporate changes from workalendar 1.3.0:

- Added Singapore calendar, initiated by @nedlowe (#194 + #195).
- Added Malaysia, by @gregyhj (#201).
- Added Good Friday in the list of Hungarian holidays, as of the year 2017 (#203), thx to @mariusz-korzekwa for the bug report.
- Assigned a minimal setuptools version, to avoid naughty ``DistributionNotFound`` exceptions with obsolete versions (#74).
- Fixed a bug in Slovakia calendar, de-duplicated Christmas Day, that appeared twice (#205).
- Fixed important bugs in the calendars of the following Brazilian cities: Vitória, Vila Velha, Cariacica, Guarapari and Serra - thx to Fernanda Gonçalves Rodrigues, who confirmed this issue raised by @Skippern (#199).

Incorporate changes from workalendar 1.2.0:

- Moved all the calendar of countries on the american continent in their own modules (#188).
- Refactor base Calendar class get_weekend_days to use WEEKEND_DAYS more intelligently (#191 + #192).
- Many additions to the Brazil and various states / cities. Were added: Acre, Alagoas, Amapá, Amazonas, Bahia, Ceará, Distrito Federal, Espírito Santo State, Goiás, Maranhão, Mato Grosso, Mato Grosso do Sul, Pará, Paraíba, Pernambuco, Piauí, Rio de Janeiro, Rio Grande do Norte, Rio Grande do Sul, Rondônia, Roraima, Santa Catarina, São Paulo, Sergipe, Tocantins, City of Vitória, City of Vila Velha, City of Cariacica, City of Guarapari and City of Serra (#187).
- Added a ``good_friday_label`` class variable to ``ChristianMixin`` ; one can assign the right label to this holiday (#187).
- Added a ``ash_wednesday_label`` class variable to ``ChristianMixin`` ; one can assign the right label to this holiday (#187).

Incorporate changes from workalendar 1.1.0:

- Added Cyprus. thx @gregn610 (#174).
- Added Latvia. thx @gregn610 (#178).
- Added Malta. thx @gregn610 (#179).
- Added Romania. thx @gregn610 (#180).
- Added Canton of Vaud (Switzerland) - @brutasse (#182).
- Fixed January 2nd state holiday (#181).
- Fixed Saxony repentance day for the year 2016. thx @Natim (#168).
- Fixed Historical and one-off holidays for South Africa. thx @gregn610 (#173).
- Minor PEP8 fixes (#186).

Incorporate changes from workalendar 1.0.0:

- Add Ireland. thx @gregn610 (#152).
- Bugfix: New Year's Eve is not a holiday in Netherlands (#154).
- Add Austria.  thx @gregn610 (#153)
- Add Bulgaria. thx @gregn610 (#156)
- Add Croatia. thx @gregn610 (#157)

Incorporate changes from workalendar 0.8.1:

- Reformation Day is a national holiday in Germany, but only in 2017 (#150).

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

1.4
---

``Calendar.get_observed_date`` now allows ``observance_shift`` to be
a callable accepting the holiday and calendar and returning the observed
date. ``Holiday`` supplies a ``get_nearest_weekday`` method suitable for
locating the nearest weekday.

- #5: USA Independence Day now honors the nearest weekday model.

1.3
---

Incorporate these fixes from Workalendar 0.3:

- ``delta`` argument for ``add_working_days()`` can be negative. added a
  ``sub_working_days()`` method that computes working days backwards.
- BUGFIX: Renaming Showa Day. "ō is not romji" (#100) (thx @shinriyo)
- BUGFIX: Belgian National Day title (#99) (thx @laulaz)

1.2.1
-----

Correct usage in example.

1.2
---

Fixed issue #4 where Finland holidays were shifted but shouldn't have been.
Calendars and Holidays may now specify observance_shift=None to signal no
shift.

Package can now be tested with pytest-runner by invoking ``python setup.py
pytest``.

1.1.3
-----

Fix name of Finnish Independence Day.

1.1.2
-----

Fixed issues with packaging (disabled installation an zip egg and now use
setuptools always).

1.1
---

UnitedKingdom Calendar now uses indicated/observed Holidays.

Includes these changes slated for workalendar 0.3:

- BUGFIX: shifting UK boxing day if Christmas day falls on a Friday (shift to
  next Monday) (#95)

1.0
---

Initial release of Calendra based on Workalendar 0.2.

- Adds Holiday class per (#79). Adds support for giving
  holidays a more rich description and better resolution of observed versus
  indicated holidays. See the pull request for detail on the motivation and
  implementation. See the usa.UnitedStates calendar for example usage.

Includes these changes slated for workalendar 0.3:

- Germany calendar added, thx to @rndusr
- Support building on systems where LANG=C (Ubuntu) (#92)
- little improvement to directly return a tested value.
