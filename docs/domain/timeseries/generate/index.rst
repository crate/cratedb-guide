.. _timeseries-generate:
.. _gen-ts:

=========================
Generate time series data
=========================

To work with time series data, you are going to need a source of time series
data. Fortunately, there are many ways to generate time series data, for
example by sampling system metrics on your workstation or server.

CrateDB is purpose-built for working with massive amounts of time series data,
like the type of data produced by smart sensors and other `Internet of Things`_
(IoT) devices.

This collection of tutorials will show you how to generate mock time series
data about the `International Space Station`_ (ISS) and write it to CrateDB
using the client of your choice.

.. rubric:: Table of contents

.. toctree::
   :maxdepth: 2
   :titlesonly:

   cli
   python
   node
   go

.. _International Space Station: https://www.nasa.gov/mission_pages/station/main/index.html
.. _Internet of Things: https://en.wikipedia.org/wiki/Internet_of_things
.. _system load: https://en.wikipedia.org/wiki/Load_(computing)
