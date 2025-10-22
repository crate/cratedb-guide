(example-applications)=
# Sample Applications


:::{rubric} Starter
:::

::::{grid} 1 2 2 3
:gutter: 2

:::{grid-item-card} JavaScript guestbook app
:link: https://github.com/crate/crate-sample-apps
:link-type: url
A JavaScript guestbook app with several backend implementations.
+++
Each uses a different client library to communicate with CrateDB over HTTP.
:::

:::{grid-item-card} Geospatial demo with CrateDB
:link: https://github.com/crate/devrel-shipping-forecast-geo-demo
:link-type: url
Geospatial data demo application using CrateDB and the Express.js framework.
+++
Click on the map to drop a marker in the waters around the British Isles,
then select Search to see which Shipping Forecast region your marker is in.
:::

::::


:::{rubric} Advanced
:::

::::{grid} 1 2 2 3
:gutter: 2

:::{grid-item-card} CrateDB UK Offshore Wind Farms Data Workshop
:link: https://github.com/crate/cratedb-examples/tree/main/topic/multi-model
:link-type: url
The workshop explores multimodel data modeling and queries with CrateDB.
+++
Acquire geographic data in WKT format and hourly performance data in JSONL
from The Crown Estate (manager of the UK's offshore wind farm sites),
import them into CrateDB, and display them on a Leaflet map.
:::

:::{grid-item-card} CrateDB UK Offshore Wind Farms Data Demo
:link: https://github.com/crate/devrel-offshore-wind-farms-demo
:link-type: url
Demo application that visualizes data in the UK offshore wind farms
example dataset using CrateDB.
+++
Navigate the map widget to see the locations of individual wind farms, then
click on a marker to see details about that wind farm's performance.
Zoom in and drill down to locations and performance data of individual turbines.
:::

:::{grid-item-card} Planespotting with SDR and CrateDB
:link: https://github.com/crate/devrel-plane-spotting-with-cratedb
:link-type: url
Plane Spotting with Software Defined Radio (SDR), CrateDB, and Node.js.
+++
Import data from the FlightAware API, then query the latest data for planes
that have a plane_id, callsign, altitude, and position and have been updated
within the last 2 minutes.
:::

:::{grid-item-card} CrateDB GTFS / GTFS-RT Transit Data Demo
:link: https://github.com/crate/devrel-gtfs-transit
:link-type: url
Capture GTFS and GTFS-RT data for storage and analysis with CrateDB.
+++
The demo application has a Python backend and a JavaScript/Leaflet
maps frontend. It uses GTFS (General Transit Feed Specification) and GTFS‑RT
(the extra real-time feeds for GTFS) to store and analyze transit system route,
trip, stop, and vehicle‑movement data stored in CrateDB.
:::

:::{grid-item-card} CrateDB RAG / Hybrid Search PDF Chatbot
:link: https://github.com/crate/devrel-pdf-rag-chatbot
:link-type: url
A natural language chatbot powered by CrateDB using RAG techniques and data from PDF files.
+++
Source data and knowledge are extracted from text and images inside PDF documents,
then stored in CrateDB as plain text with a full‑text index and vector embeddings.
Users can ask questions of the knowledge base using natural language.
:::

::::
