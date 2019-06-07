# The ISO registry

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md)

As of version 3.0 (August/September 2018), we have introduced a global calendar registry for calendars related to a country or a region that belongs to the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) or the [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) for sub-regions (such as USA states, Australian territories or Canadian provinces and such).

## Iterate over the whole registry

```python
>>> from workalendar.registry import registry
>>> for code, calendar_class in registry.region_registry.items():
...     print(u"`{}` is code for '{}'".format(code, calendar_class.name))
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

The `registry.region_registry` is an `OrderedDict` object, with the ISO code as a key, and the calendar class as the value. As a "workalendar standard", **every** calendar in the registry has a `name` property (derived from the docstring), so you'd probably be able to build a user-friendly list of available calendars, for a dropdown list, for example.

**Deprecation Warning:** *Currently the registry returns `OrderedDict` objects when you're querying for regions or subregions. Expect that the next release will preferrably return plain'ol' `dict` objects. If your scripts rely on the order of the objects returned, you'll have to sort them yourself.*

## Retrieve a collection of regions

Let's say you'd need only a subset of the ISO registry. For example, France, Switzerland and Canada calendars. You can use the method `items()` to filter only the calendars you want.

```python
>>> registry.items(['FR', 'CH', 'CA'])
OrderedDict([('FR', workalendar.europe.france.France),
             ('CH', workalendar.europe.switzerland.Switzerland),
             ('CA', workalendar.america.canada.Canada)])
```

Also, if you want those regions **and** their subregions, you can use the `include_subregions` flag:

```python
>>> registry.items(['FR', 'CH', 'CA'], include_subregions=True)
OrderedDict([('FR', workalendar.europe.france.France),
             ('CH', workalendar.europe.switzerland.Switzerland),
             (u'CH-VD', workalendar.europe.switzerland.Vaud),
             ('CA', workalendar.america.canada.Canada),
             (u'CA-ON', workalendar.america.canada.Ontario),
             (u'CA-QC', workalendar.america.canada.Quebec),
             (u'CA-BC', workalendar.america.canada.BritishColumbia),
             (u'CA-AB', workalendar.america.canada.Alberta),
             (u'CA-SK', workalendar.america.canada.Saskatchewan),
             (u'CA-MB', workalendar.america.canada.Manitoba),
             (u'CA-NB', workalendar.america.canada.NewBrunswick),
             (u'CA-NS', workalendar.america.canada.NovaScotia),
             (u'CA-PE', workalendar.america.canada.PrinceEdwardIsland),
             (u'CA-NL', workalendar.america.canada.Newfoundland),
             (u'CA-YT', workalendar.america.canada.Yukon),
             (u'CA-NT', workalendar.america.canada.NorthwestTerritories),
             (u'CA-NU', workalendar.america.canada.Nunavut)])
```

*Note*: if any of the codes is unknown, this function won't raise an error.

## Select only one calendar

Let's say that we only know the ISO code for Switzerland (`CH`). If we want to compute holidays for Switzerland in 2018, we can do as follows:

```python
>>> registry.get_calendar_class('CH')
>>> CalendarClass = registry.get_calendar_class('CH')
>>> calendar = CalendarClass()
>>> calendar.holidays(2018)
[(datetime.date(2018, 1, 1), 'New year'),
 (datetime.date(2018, 1, 2), u"Berchtold's Day"),
 (datetime.date(2018, 3, 30), 'Good Friday'),
 (datetime.date(2018, 4, 1), 'Easter Sunday'),
 (datetime.date(2018, 4, 2), 'Easter Monday'),
 (datetime.date(2018, 5, 1), u'Labour Day'),
 (datetime.date(2018, 5, 10), 'Ascension Thursday'),
 (datetime.date(2018, 5, 20), 'Whit Sunday'),
 (datetime.date(2018, 5, 21), 'Whit Monday'),
 (datetime.date(2018, 8, 1), u'National Holiday'),
 (datetime.date(2018, 12, 25), 'Christmas Day'),
 (datetime.date(2018, 12, 26), 'Boxing Day')]
```

*Note*: this function would return `None` if the code is unknown.


## Select only sub-regions

As an example, the United States of America, or Australia and others are divided into "sub-regions" (states, provinces, territories, etc). There are usually Federal or State holidays, and variants depending on the region you're targeting.

```python
>>> registry.get_subregions('AU')
OrderedDict([(u'AU-ACT',
              workalendar.oceania.australia.AustralianCapitalTerritory),
             (u'AU-NSW', workalendar.oceania.australia.NewSouthWales),
             (u'AU-NT', workalendar.oceania.australia.NorthernTerritory),
             (u'AU-QLD', workalendar.oceania.australia.Queensland),
             (u'AU-SA', workalendar.oceania.australia.SouthAustralia),
             (u'AU-TAS', workalendar.oceania.australia.Tasmania),
             (u'AU-VIC', workalendar.oceania.australia.Victoria),
             (u'AU-WA', workalendar.oceania.australia.WesternAustralia)])
```

*Note*: this function will return an empty `OrderedDict` if the code is unknown.

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md)
