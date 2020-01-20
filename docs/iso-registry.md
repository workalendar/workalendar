# The ISO registry

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md)

As of version 3.0 (August/September 2018), we have introduced a global calendar registry for calendars related to a country or a region that belongs to the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) or the [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) for sub-regions (such as USA states, Australian territories or Canadian provinces and such).

## Iterate over the whole registry

```python
>>> from workalendar.registry import registry
>>> calendars = registry.get_calendars()
>>> for code, calendar_class in calendars.items():
...     print("`{}` is code for '{}'".format(code, calendar_class.name))
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

**DEPRECATION WARNING**: the ``get_calendars`` method used to be named ``items()``. In a future release, it'll be deprecated and re-purposed. Please switch to using ``get_calendars()`` for all your queries in the registry.

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
{'CA': <class 'workalendar.america.canada.Canada'>,
 'CA-AB': <class 'workalendar.america.canada.Alberta'>,
 'CA-BC': <class 'workalendar.america.canada.BritishColumbia'>,
 'CA-MB': <class 'workalendar.america.canada.Manitoba'>,
 'CA-NB': <class 'workalendar.america.canada.NewBrunswick'>,
 'CA-NL': <class 'workalendar.america.canada.Newfoundland'>,
 'CA-NS': <class 'workalendar.america.canada.NovaScotia'>,
 'CA-NT': <class 'workalendar.america.canada.NorthwestTerritories'>,
 'CA-NU': <class 'workalendar.america.canada.Nunavut'>,
 'CA-ON': <class 'workalendar.america.canada.Ontario'>,
 'CA-PE': <class 'workalendar.america.canada.PrinceEdwardIsland'>,
 'CA-QC': <class 'workalendar.america.canada.Quebec'>,
 'CA-SK': <class 'workalendar.america.canada.Saskatchewan'>,
 'CA-YT': <class 'workalendar.america.canada.Yukon'>,
 'CH': <class 'workalendar.europe.switzerland.Switzerland'>,
 'CH-VD': <class 'workalendar.europe.switzerland.Vaud'>,
 'CH-GE': <class 'workalendar.europe.switzerland.Geneva'>,
 'FR': <class 'workalendar.europe.france.France'>}
```

*Note*: if any of the codes is unknown, this function won't raise an error.

You can also get the full dict of all calendars registered in the ISO Registry with all the subregions using the following function call:

```python
>>> registry.get_calendars(include_subregions=True)
```

## Select only one calendar

Let's say that we only know the ISO code for Switzerland (`CH`). If we want to compute holidays for Switzerland in 2018, we can do as follows:

```python
>>> registry.get_calendar_class('CH')
>>> CalendarClass = registry.get_calendar_class('CH')
>>> calendar = CalendarClass()
>>> calendar.holidays(2018)
[(datetime.date(2018, 1, 1), 'New year'),
 (datetime.date(2018, 1, 2), "Berchtold's Day"),
 (datetime.date(2018, 3, 30), 'Good Friday'),
 (datetime.date(2018, 4, 1), 'Easter Sunday'),
 (datetime.date(2018, 4, 2), 'Easter Monday'),
 (datetime.date(2018, 5, 1), 'Labour Day'),
 (datetime.date(2018, 5, 10), 'Ascension Thursday'),
 (datetime.date(2018, 5, 20), 'Whit Sunday'),
 (datetime.date(2018, 5, 21), 'Whit Monday'),
 (datetime.date(2018, 8, 1), 'National Holiday'),
 (datetime.date(2018, 12, 25), 'Christmas Day'),
 (datetime.date(2018, 12, 26), 'Boxing Day')]
```

*Note*: this function would return `None` if the code is unknown.


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

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md)
