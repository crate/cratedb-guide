(example-applications)=
# Sample applications


:::{rubric} Starter
:::

::::{grid} 1 2 2 3
:gutter: 2

:::{grid-item-card} JavaScript guestbook
:link: https://github.com/crate/crate-sample-apps
:link-type: url
A JavaScript guestbook app with several backend implementations.
+++
Each application uses a different client library to communicate with CrateDB over HTTP.
:::

:::{grid-item-card} Geospatial data
:link: https://github.com/crate/devrel-shipping-forecast-geo-demo
:link-type: url
Geospatial data demo application using CrateDB and the Express.js framework.
+++
Select a point of interest on a map,
then drill up to the corresponding region.
:::

:::{grid-item-card} Assorted examples
:link: https://github.com/crate/cratedb-examples
:link-type: url
A collection of clear, concise examples about how to work with CrateDB.
+++
The repository includes a variety of executable code snippets
covering a wide range of clients and integrations.
:::

::::


:::{rubric} Advanced
:::

::::{grid} 1 2 2 3
:gutter: 2

:::{grid-item-card} UK offshore wind farms data » Workshop
:link: https://github.com/crate/cratedb-examples/tree/main/topic/multi-model
:link-type: url
The workshop explores multimodel data modeling and queries
with CrateDB and Leaflet.
+++
Acquire geographic data in WKT format and hourly performance data in JSONL
format about UK's offshore wind farm sites,
import them into CrateDB, and display them on map.
:::

:::{grid-item-card} UK offshore wind farms data » Demo
:link: https://github.com/crate/devrel-offshore-wind-farms-demo
:link-type: url
Demo application that visualizes data in the UK offshore wind farms
example dataset using CrateDB.
+++
Navigate the map widget to see the locations of wind farms, then drill
down into performance details about that wind farm and individual turbines.
:::

:::{grid-item-card} Planespotting with SDR
:link: https://github.com/crate/devrel-plane-spotting-with-cratedb
:link-type: url
Plane spotting with software-defined radio (SDR), CrateDB, and Node.js.
+++
Import data from the FlightAware API, then query the latest data for active
transmitting planes that has been updated within the last 2 minutes.
:::

:::{grid-item-card} GTFS / GTFS-RT transit data
:link: https://github.com/crate/devrel-gtfs-transit
:link-type: url
Store and analyze transit networks using a
a Python/JavaScript/Leaflet application and CrateDB.
+++
Store and analyze data about transit system routes,
trips, stops, and vehicle movements,
based on GTFS and GTFS‑RT data (General Transit Feed Specification).
:::

:::{grid-item-card} Hybrid-search PDF chatbot
:link: https://github.com/crate/devrel-pdf-rag-chatbot
:link-type: url
A natural language chatbot powered by CrateDB using RAG techniques and data from PDF files.
+++
Source data and knowledge are extracted from text and images inside PDF documents,
then stored in CrateDB as plain text with a full‑text index and vector embeddings.
Users can ask questions of the knowledge base using natural language.
:::

::::


:::{rubric} Community
:::

:::::{grid} 1 2 2 3
:gutter: 2

::::{grid-item-card}
:link: https://wetterdienst.readthedocs.io/en/latest/usage/python-api.html#export
:link-type: url
(weather-data-storage)=
:::{rubric} Store and analyze massive amounts of synoptic weather data
:::
Wetterdienst uses CrateDB for mass storage of weather data, allowing you to
query it efficiently. It provides access to data at more than ten canonical
sources of raw weather data from domestic weather agencies.
+++
**What's inside:**

{tags-primary}`Earth observations`
{tags-primary}`Metadata`
{tags-primary}`Sensor data`
{tags-primary}`Time series`

{tags-secondary}`pandas`
{tags-secondary}`Polars`
{tags-secondary}`SQL`
::::

:::::
