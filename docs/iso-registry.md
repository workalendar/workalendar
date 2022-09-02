# The ISO registry

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md) / [Class options](class-options.md) / [iCal Export](ical.md) / [Contributing](contributing.md)

As of version 3.0 (August/September 2018), we have introduced a global calendar registry for calendars related to a country or a region that belongs to the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) or the [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) for sub-regions (such as USA states, Australian territories or Canadian provinces and such).

## Iterate over the whole registry

```python
>>> from workalendar.registry import registry
>>> calendars = registry.get_calendars()  # This returns a dictionary
>>> for code, calendar_class in calendars.items():
...     print(f"`{code}` is code for {calendar_class.name!r}")
`AT` is code for 'Austria'
`BE` is code for 'Belgium'
`BG` is code for 'Bulgaria'
`HR` is code for 'Croatia'
`CY` is code for 'Cyprus'
`CZ` is code for 'Czech Republic'
`EE` is code for 'Estonia'
`DK` is code for 'Denmark'
`FI` is code for 'Finland'
`FR` is code for 'France'
... continued
```

The "private property" `registry.region_registry` is a `dict` object, with the ISO code as a key, and the calendar class as the value. As a "workalendar standard", **every** calendar in the registry has a `name` property (derived from the docstring), so you'd probably be able to build a user-friendly list of available calendars, for a dropdown list, for example.

**DEPRECATION WARNING**: As of version 9.0.0, the ``IsoRegistry.items()`` has been renamed into ``IsoRegistry.get_calendars()`` for all your queries in the registry.

## Retrieve a collection of regions

If you want the full dictionary of **countries**, you can use the ``get_calendars()`` method.

```python
>>> registry.get_calendars()
{'AT': <class 'workalendar.europe.austria.Austria'>,
 'BE': <class 'workalendar.europe.belgium.Belgium'>,
 'BG': <class 'workalendar.europe.bulgaria.Bulgaria'>,
 'KY': <class 'workalendar.europe.cayman_islands.CaymanIslands'>,
  # ... continued
}
```

Let's say you'd need only a subset of the ISO registry. For example, France, Switzerland and Canada calendars. You can use the method `get_calendars()` to filter only the calendars you want.

```python
>>> registry.get_calendars(['FR', 'CH', 'CA'])
{'FR': <class 'workalendar.europe.france.France'>,
 'CH': <class 'workalendar.europe.switzerland.Switzerland'>,
 'CA': <class 'workalendar.america.canada.Canada'>}
```

Also, if you want those regions **and** their subregions, you can use the `include_subregions` flag:

```python
>>> registry.get_calendars(['FR', 'CH', 'CA'], include_subregions=True)
{'FR': workalendar.europe.france.France,
 'CH': workalendar.europe.switzerland.Switzerland,
 'CH-AG': workalendar.europe.switzerland.Aargau,
 'CH-AI': workalendar.europe.switzerland.AppenzellInnerrhoden,
 'CH-AR': workalendar.europe.switzerland.AppenzellAusserrhoden,
 'CH-BE': workalendar.europe.switzerland.Bern,
 'CH-BL': workalendar.europe.switzerland.BaselLandschaft,
 'CH-BS': workalendar.europe.switzerland.BaselStadt,
 'CH-FR': workalendar.europe.switzerland.Fribourg,
 'CH-GE': workalendar.europe.switzerland.Geneva,
 'CH-GL': workalendar.europe.switzerland.Glarus,
 'CH-GR': workalendar.europe.switzerland.Graubunden,
 'CH-JU': workalendar.europe.switzerland.Jura,
 'CH-LU': workalendar.europe.switzerland.Luzern,
 'CH-NE': workalendar.europe.switzerland.Neuchatel,
 'CH-NW': workalendar.europe.switzerland.Nidwalden,
 'CH-OW': workalendar.europe.switzerland.Obwalden,
 'CH-SG': workalendar.europe.switzerland.StGallen,
 'CH-SH': workalendar.europe.switzerland.Schaffhausen,
 'CH-SO': workalendar.europe.switzerland.Solothurn,
 'CH-SZ': workalendar.europe.switzerland.Schwyz,
 'CH-TG': workalendar.europe.switzerland.Thurgau,
 'CH-TI': workalendar.europe.switzerland.Ticino,
 'CH-UR': workalendar.europe.switzerland.Uri,
 'CH-VD': workalendar.europe.switzerland.Vaud,
 'CH-VS': workalendar.europe.switzerland.Valais,
 'CH-ZG': workalendar.europe.switzerland.Zug,
 'CH-ZH': workalendar.europe.switzerland.Zurich,
 'CA': workalendar.america.canada.Canada,
 'CA-ON': workalendar.america.canada.Ontario,
 'CA-QC': workalendar.america.canada.Quebec,
 'CA-BC': workalendar.america.canada.BritishColumbia,
 'CA-AB': workalendar.america.canada.Alberta,
 'CA-SK': workalendar.america.canada.Saskatchewan,
 'CA-MB': workalendar.america.canada.Manitoba,
 'CA-NB': workalendar.america.canada.NewBrunswick,
 'CA-NS': workalendar.america.canada.NovaScotia,
 'CA-PE': workalendar.america.canada.PrinceEdwardIsland,
 'CA-NL': workalendar.america.canada.Newfoundland,
 'CA-YT': workalendar.america.canada.Yukon,
 'CA-NT': workalendar.america.canada.NorthwestTerritories,
 'CA-NU': workalendar.america.canada.Nunavut}
```

*Note*: if any of the codes is unknown, this function won't raise an error.

You can also get the full dict of all calendars registered in the ISO Registry with all the subregions using the following function call:

```python
>>> registry.get_calendars(include_subregions=True)
```

## Select only one calendar

Let's say that we only know the ISO code for Switzerland (`CH`). If we want to compute holidays for Switzerland in 2018, we can do as follows:

```python
>>> CalendarClass = registry.get('CH')
>>> calendar = CalendarClass()
>>> calendar.holidays(2018)
[(datetime.date(2018, 1, 1), 'New year'),
 (datetime.date(2018, 3, 30), 'Good Friday'),
 (datetime.date(2018, 4, 1), 'Easter Sunday'),
 (datetime.date(2018, 4, 2), 'Easter Monday'),
 (datetime.date(2018, 5, 10), 'Ascension Thursday'),
 (datetime.date(2018, 5, 20), 'Whit Sunday'),
 (datetime.date(2018, 5, 21), 'Whit Monday'),
 (datetime.date(2018, 8, 1), 'National Holiday'),
 (datetime.date(2018, 12, 25), 'Christmas Day'),
 (datetime.date(2018, 12, 26), 'Boxing Day')]
```

*Note*: this function would return `None` if the code is unknown.

**DEPRECATION WARNING**: As of version 10.0.0, the ``IsoRegistry.get_calendar_class()`` has been renamed into ``IsoRegistry.get()`` to retrieve a single calendar class out of the registry.


## Select only sub-regions

As an example, the United States of America, or Australia and others are divided into "sub-regions" (states, provinces, territories, etc). There are usually Federal or State holidays, and variants depending on the region you're targeting.

```python
>>> registry.get_subregions('AU')
{'AU-ACT': <class 'workalendar.oceania.australia.AustralianCapitalTerritory'>,
 'AU-NSW': <class 'workalendar.oceania.australia.NewSouthWales'>,
 'AU-NT': <class 'workalendar.oceania.australia.NorthernTerritory'>,
 'AU-QLD': <class 'workalendar.oceania.australia.Queensland'>,
 'AU-SA': <class 'workalendar.oceania.australia.SouthAustralia'>,
 'AU-TAS': <class 'workalendar.oceania.australia.Tasmania'>,
 'AU-VIC': <class 'workalendar.oceania.australia.Victoria'>,
 'AU-WA': <class 'workalendar.oceania.australia.WesternAustralia'>}
```

*Note*: this function will return an empty `dict` if the code is unknown.

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md) / [Class options](class-options.md) / [iCal Export](ical.md) / [Contributing](contributing.md)
