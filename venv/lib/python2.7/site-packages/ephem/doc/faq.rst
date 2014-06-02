
 >>> import ephem

**Q:**
 Why does an ``Observer`` not allow assignment to arbitrary attributes?
 I wanted to remember which of my friends lived in which cities,
 but attempting to set a ``friend`` attribute caused an exception:

 >>> boston = ephem.Observer()
 >>> boston.beer = 'Sam Adams'
 Traceback (most recent call last):
  ...
 AttributeError: 'Observer' object has no attribute 'beer'

**A:** 

 ``Observer`` objects restrict which of their attributes can be set
 to prevent users from misspelling attribute names.
 This means that users are immediately informed of their mistake
 when they attempt an assignment like::

  boston.longitude = '-71.0'

 If you need an ``Observer`` object
 that can remember additional attributes,
 simply create your own sub-class of ``Observer`` and use that instead:

 >>> class MyObserver(ephem.Observer):
 ...     pass
 >>> boston = MyObserver()
 >>> boston.friend = 'John Adams'
 >>> print boston.friend
 John Adams
