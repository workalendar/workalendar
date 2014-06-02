.. raw:: html

   <table class="triad" cellspacing="0"> <!-- for IE -->

   <tr class="cap">
   <td><img class="corner2" src="_static/corner2.png"/></td>
   <td><img class="corner2" src="_static/corner2.png"/></td>
   <td><img class="corner2" src="_static/corner2.png"/></td>
   </tr>

   <tr class="sites"><td>

   <p>This site is the PyEphem <b>home page</b></p>
   <img src="_static/pyephem-logo-short.png"/>
   <p>Simply <b>scroll down</b> to find:</p>
   <p>
     Installation Guide<br/>
     Documentation<br/>
     Data Sources<br/>
   </ul>

   <p>
     <i>Your contribution
     <br>
     supports PyEphem
     <br>
     development:</i>
   </p>
   <p>
     <iframe style="border: 0; margin: 0; padding: 0;"
             src="https://www.gittip.com/brandon-rhodes/widget.html"
             width="48pt" height="20pt"></iframe>
   </p>

   </td>
   <td>

   <p>Download PyEphem for Windows, Linux, or as source code,
   directly from the <b>Python Package Index</b>.</p>
   <img src="_static/python.png"/>
   <p>
     <a href="http://pypi.python.org/pypi/pyephem/"
      >PyPI PyEphem page</a>
     <br/>
     <br/>
     <a href="http://pypi.python.org/packages/2.7/p/pyephem/pyephem-3.7.5.2.win32-py2.7.exe"
      >Python 2.7 Windows installer</a>
     <br/>
     <a href="http://pypi.python.org/packages/2.6/p/pyephem/pyephem-3.7.5.2.win32-py2.6.exe"
      >Python 2.6 Windows installer</a>
     <br/>
     <br/>
     <a href="http://pypi.python.org/packages/source/p/pyephem/pyephem-3.7.5.2.tar.gz"
      >Source code (.tar.gz)</a><br/>
   </p>

   </td>
   <td>

   <p>
     Ask questions on <b>Stack Overflow</b>, or use our community support
     tools on <b>GitHub</b>!
   </p>
   <img src="_static/stackoverflow.png"/>
   <p>
     <a href="http://stackoverflow.com/questions/tagged/pyephem"
        >PyEphem Q&amp;A</a><br/>
     <a href="http://stackoverflow.com/questions/ask?tags=pyephem"
        >Ask a new question</a><br/>
   </p>
   <img src="_static/github.png"/>
   <p>
     <a href="https://github.com/brandon-rhodes/pyephem"
        >Code Repository</a><br/>
     <a href="https://github.com/brandon-rhodes/pyephem/issues?state=open"
        >Issue Tracker</a><br/>
   </p>

   </td></tr>

   <tr class="toe">
   <td></td>
   <td><img class="corner3" src="_static/corner3.png"/></td>
   <td><img class="corner3" src="_static/corner3.png"/></td>
   </tr>

   <tr class="mount">
   <td></td>
   </tr>

   <tr class="base">
   <td colspan=3>

   <div class="sideexample">

>>> import ephem

>>> mars = ephem.Mars()
>>> mars.compute()
>>> print mars.ra, mars.dec
6:05:56.34 23:23:40.0
>>> ephem.constellation(mars)
('Gem', 'Gemini')

>>> boston = ephem.Observer()
>>> boston.lat = '42.37'
>>> boston.lon = '-71.03'
>>> mars.compute(boston)
>>> print mars.az, mars.alt
37:55:48.9 -14:23:11.8

>>> boston.next_rising(mars)
2007/10/2 02:31:51
>>> print mars.az
56:52:52.1

>>> boston.next_transit(mars)
2007/10/2 10:07:47
>>> print mars.alt
71:02:16.3

.. raw:: html

   </div>

Welcome!
========

**PyEphem** provides scientific-grade astronomical computations
for the Python_ programming language.
Given a date and location on the Earth's surface,
it can compute the positions of the Sun and Moon,
of the planets and their moons,
and of any asteroids, comets, or earth satellites
whose orbital elements the user can provide.
Additional functions are provided to compute the angular separation
between two objects in the sky,
to determine the constellation in which an object lies,
and to find the times at which
an object rises, transits, and sets on a particular day.

.. _Python: http://www.python.org/

The numerical routines that lie behind PyEphem
are those from the wonderful XEphem_ astronomy application,
whose author, Elwood Downey, generously gave permission
for us to use them as the basis for PyEphem.

.. _XEphem: http://www.clearskyinstitute.com/xephem/

Installation
------------

Version **3.7.5.2** is the most recent release of PyEphem.
Consult the `change log`_ to see the new features!

.. _change log: CHANGELOG

The easiest way to install PyEphem on a Linux or Mac OS machine,
after making sure that “Python.h” and the other Python header files
are installed (which on Ubuntu requires the “python-dev” package),
is to use the pip_ command, like this:

.. _pip: http://pypi.python.org/pypi/pip
.. code-block:: bash

   $ pip install pyephem

Better yet,
you can use virtualenv_ to create a virtual environment,
and then run its ``pip`` instead of your system-wide one.
Then you will avoid having to gain administrator rights on your machine
before performing the installation.

If instead you want to download the Windows installer
or even the raw PyEphem source code,
you should visit the `PyEphem entry`_
at the Python Package Index,
or use the links at the top of this page.

.. _PyEphem entry: http://pypi.python.org/pypi/pyephem/
.. _virtualenv: http://pypi.python.org/pypi/virtualenv

Documentation
-------------

.. toctree::
   :maxdepth: 2

   quick
   tutorial
   catalogs
   CHANGELOG
   rise-set
   radec
   coordinates
   date
   angle
   examples
   newton
   reference

.. raw:: html

   </td></tr>

   </table>
