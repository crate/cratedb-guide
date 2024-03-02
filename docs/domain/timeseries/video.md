(timeseries-video)=
# Video Tutorials

Video tutorials about time series with CrateDB.


## Time Series Data and CrateDB

::::{info-card}

:::{grid-item} **A collection of videos about how CrateDB deals with time-series data**
:columns: 9

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=C5ayK8bqkhRYovjc&amp;list=PLDZqzXOGoWUKTZwR7zOY8s1sTvZOAa7cy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

-- [Time Series Data and CrateDB]

CrateDB simplifies the complexity of managing time-series data.
It provides a comprehensive solution for storing, querying, and extracting
insights from large-scale and high-volume time-series datasets.

Learn more about CrateDB and time-series data here:
https://cratedb.com/solutions/time-series-database
:::

:::{grid-item} &nbsp;
:columns: 3

{tags-secondary}`Introduction` \
{tags-primary}`Time Series` \
{tags-info}`21 Feb 2024`
:::

::::


## Importing and Exporting Data with CrateDB

::::{info-card}

:::{grid-item} **The basics of `COPY FROM` and `COPY TO`**
:columns: 9

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xDypaX37XZQ?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

-- [Importing and Exporting Data with CrateDB]

In this video tutorial, Rafaela will show you how to import JSON and CSV data
to CrateDB using the [`COPY FROM`] statement. Then, she will demonstrate how to
export data from CrateDB to a local file system, using the [`COPY TO`] statement.
Rafaela will use the [Quotes Dataset].

For more information about how to import and export
data from/into CrateDB, please refer to [](#timeseries-io).
:::

:::{grid-item} &nbsp;
:columns: 3

{tags-secondary}`Introduction` \
{tags-primary}`Import and Export` \
{tags-info}`8 Aug 2022`

Rafaela Sant'ana
:::

::::



## Analyzing Time Series Data with CrateDB

::::{info-card}

:::{grid-item} **From raw data to fast analysis in only three steps**
:columns: 9

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7biXPnG7dY4?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

-- [Time series data: From raw data to fast analysis in only three steps]

In this extensive video tutorial, Karyn and Niklas will show you how to use 
time-series data and data analysis to help businesses understand patterns,
trends, and causes over time.

On behalf of the webinar, Crate&#46;io's Solution Engineering team guides you
through the implementation steps of a time-series use case - from table layout
to querying.  

Our speakers will also show you how to find the right sharding and partitioning
strategy for your time-series data in CrateDB.
:::

:::{grid-item} &nbsp;
:columns: 3

{tags-secondary}`Extensive` \
{tags-primary}`Time Series` \
{tags-primary}`Modeling` \
{tags-primary}`Import and Export` \
{tags-primary}`Querying` \
{tags-info}`23 Feb 2023`

Karyn Azevedo, \
Niklas Schmidtmer
:::

::::


## CrateDB in Analytics Applications

::::{info-card}

:::{grid-item} **Real-time analytics on raw tracking data**
:columns: 9

Learn how Bitmovin leverages CrateDB to support real-time analytics on
top of tracking data from their video streaming broadcasting system.

- [](#bitmovin)
:::

:::{grid-item} &nbsp;
:columns: 3

{tags-secondary}`Extensive` \
{tags-primary}`Time Series` \
{tags-primary}`Tracking Analytics` \
{tags-info}`2022`

Daniel Hölbling-Inzko, \
Georg Traar
:::

::::


## CrateDB in Industrial Applications

::::{info-card}

:::{grid-item}
:columns: 9

**Industrial Analytics Platform, High-Speed Production Lines, and Logistics**

Learn how ABB, Rauch, and TGW leverage CrateDB to support their application
platforms, high-speed shop-floor production lines, and logistics databases
for warehouses around the world.

- [](#abb)
- [](#rauch)
- [](#tgw)
:::

:::{grid-item} &nbsp;
:columns: 3

{tags-secondary}`Extensive` \
{tags-primary}`Time Series` \
{tags-primary}`Industrial IoT` \
{tags-info}`2022/2023`

Alexander Mann, \
Arno Breuss, \
Christian Lutz, \
Georg Traar, \
Jan Weber, \
Marko Sommarberg
:::

::::



[`COPY FROM`]: inv:crate-reference#sql-copy-from
[`COPY TO`]: inv:crate-reference#sql-copy-to
[Importing and Exporting Data with CrateDB]: https://youtu.be/xDypaX37XZQ?feature=shared
[Quotes Dataset]: https://www.kaggle.com/datasets/manann/quotes-500k
[Time series data: From raw data to fast analysis in only three steps]: https://youtu.be/7biXPnG7dY4?feature=shared
[Time Series Data and CrateDB]: https://www.youtube.com/playlist?list=PLDZqzXOGoWUKTZwR7zOY8s1sTvZOAa7cy
