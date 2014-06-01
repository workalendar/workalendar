
Newton's Method
===============

PyEphem comes with a simple implementation of Newton's Method,
named ``newton``.

    >>> from ephem import newton

Given a continuous function and two *x* coordinates
near which the function crosses zero,
it returns the *x* coordinate of the actual zero crossing.
For example,
if asked to find the zero-crossing of the ``sin()`` function
in the vicinity of the number three,
it returns a quite good appoximation of π (“pi”):

    >>> import math
    >>> n = newton(math.sin, 3.0, 3.1)
    >>> print n
    3.14159265359
