====================
CrateDB on Azure IoT
====================


Architecture
============

This reference architecture enables high throughput ingestion and enrichment
of raw sensor data from a fleet of sensors. Once ingested into CrateDB, this
data can be used to perform complex analysis, to build real-time 
data-driven dashboards and reporting as well as feed your web or mobile application.

.. _figure_1:

.. figure:: /_assets/img/reference-architectures/cratedb-azure-iot.png
   :align: center


Integrations
============

This architecture makes use of the following integrations with CrateDB:

1. :ref:`azure-functions`
2. :ref:`cratedb-r`
3. :ref:`analysis`
