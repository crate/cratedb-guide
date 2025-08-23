(example-applications)=
# Sample Applications


:::{rubric} Starter
:::

::::{grid} 3
:gutter: 2

:::{grid-item-card} JavaScript guestbook app
:link: https://github.com/crate/crate-sample-apps
A JavaScript guestbook app with several backend implementations.
+++
Each one is using a different client library to communicate with
CrateDB using HTTP. 
:::

:::{grid-item-card} Geospatial demo with CrateDB
:link: https://github.com/crate/devrel-shipping-forecast-geo-demo
Geospatial data demo application using CrateDB and the Express framework.
+++
Click on the map to drop a marker in the waters around the British Isles
then hit search to find out which Shipping Forecast region your marker is in.
:::

::::


:::{rubric} Advanced
:::

::::{grid} 3
:gutter: 2

:::{grid-item-card} CrateDB UK Offshore Wind Farms Data Workshop
:link: https://github.com/crate/cratedb-examples/tree/main/topic/multi-model
The workshop explores multimodel data modeling and queries with CrateDB.
+++
Acquire and import geographic data in WKT format and hourly wind farm
performance data in JSONL format from The Crown Estate which manages
the UK's offshore wind farms, and display them on a Leaflet map,
managed by CrateDB.
:::

:::{grid-item-card} CrateDB UK Offshore Wind Farms Data Demo
:link: https://github.com/crate/devrel-offshore-wind-farms-demo
Demo application that visualizes data in the UK Offshore wind
farms example dataset using CrateDB.
+++
Navigate the map widget to see the locations of individual wind farms, then
click on a marker to see details about that wind farm's performance.
Zoom in and drill down to locations and performance data of individual turbines.
:::

:::{grid-item-card} Planespotting with SDR and CrateDB
:link: https://github.com/crate/devrel-plane-spotting-with-cratedb
Plane Spotting with Software Defined Radio (SDR), CrateDB, and Node.js.
+++
Import data from the FlightAware API, then query the latest data for planes
that have a plane_id, callsign, altitude and position while have been updated
in the last 2 minutes.
:::

:::{grid-item-card} CrateDB GTFS / GTFS-RT Transit Data Demo
:link: https://github.com/crate/devrel-gtfs-transit
Capture GTFS and GTFS-RT data for storage and analysis with CrateDB.
+++
The demo application has a Python backend and a JavaScript/Leaflet
maps frontend. It uses GTFS (General Transit Feed Specification) and GTFS-RT
(the extra realtime feeds for GTFS) to store and analyze transit system route,
trip, stop and vehicle movement data stored in CrateDB.
:::

:::{grid-item-card} CrateDB RAG / Hybrid Search PDF Chatbot
:link: https://github.com/crate/devrel-pdf-rag-chatbot
A natural language chatbot powered by CrateDB using RAG techniques and data from PDF files.
+++
Source data / knowledge is extracted from text and images inside PDF documents,
then stored in CrateDB in plain text with a full-text index and vector embeddings.
Users can ask questions to the knowledge base using natural language.
:::

::::
