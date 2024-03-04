(analytics)=
# Raw-Data Analytics

**CrateDB provides real-time analytics on raw data stored for the long term**

In all domains of real-time analytics where you absolutely must have access to all
the records, and can't live with any down-sampled variants, because records are
unique, and need to be accounted for within your analytics queries.

If you find yourself in such a situation, you need a storage system which
manages all the high-volume data in its hot zone, to be available right on
your fingertips, for live querying. Batch jobs to roll up raw data into
analytical results are not an option, because users' queries are too
individual, so you need to run them on real data in real time.

With CrateDB, compatible to PostgreSQL, you can do all of that using plain SQL.
Other than integrating well with commodity systems using standard database
access interfaces like ODBC or JDBC, it provides a proprietary HTTP interface
on top.

:Tags:
  {tags-primary}`Analytics`
  {tags-primary}`Long Term Storage`

:Related:
  [](#document) •
  [](#geospatial) •
  [](#fulltext) •
  [](#timeseries) •
  [](#machine-learning)

:Product:
  [Real-time Analytics Database]


(bitmovin)=
## Bitmovin Insights

Multi tenant data analytics on top of billions of records.

> CrateDB enables use cases we couldn't satisfy with other
database systems, also with databases which are even stronger
focused on the time series domain.
>
> CrateDB is not your normal database!
>
> <small>-- Daniel Hölbling-Inzko, Director of Engineering Analytics, Bitmovin</small>

:Industry:
  {tags-secondary}`Broadcasting`
  {tags-secondary}`Media Transcoding`
  {tags-secondary}`Streaming Media`

:Tags:
  {tags-primary}`Event Tracking`
  {tags-primary}`Real-Time Analytics`
  {tags-primary}`Multi Tenancy`
  {tags-primary}`SaaS`

:Related:
  [CrateDB provides the backbone of Bitmovin's real-time video analytics platform] \
  [How Bitmovin uses CrateDB to monitor the biggest live video events]


::::{info-card}

:::{grid-item}
:columns: 8

{material-outlined}`analytics;2em` &nbsp; **Bitmovin: Real-Time Analytics**

Bitmovin, as a leader in video codec algorithms and as a web-based video
stream broadcasting provider, produces billions of rows of data and stores
them in CrateDB, allowing their customers to do analytics on it.

One of their product's subsystems, a video analytics component, required to
serve real-time analytics on very large and fast-moving data, so they needed
to find a performing database at the right cost.

- [Bitmovin: Improving the Streaming Experience with Real-Time Analytics]

The use-case of Bitmovin illustrates why traditional databases weren't capable
to deal with so many data records and keep them all available for querying in
real time.
:::

:::{grid-item} &nbsp;
:columns: 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/4BPApD0Piyc?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Date:** 14 Oct 2022 \
**Speakers:** Daniel Hölbling-Inzko, Georg Traar
:::

::::


[Bitmovin: Improving the Streaming Experience with Real-Time Analytics]: https://youtu.be/4BPApD0Piyc?feature=shared
[CrateDB provides the backbone of Bitmovin's real-time video analytics platform]: https://cratedb.com/customers/bitmovin
[How Bitmovin uses CrateDB to monitor the biggest live video events]: https://youtu.be/IR6hokaYv5g?feature=shared
[Real-time Analytics Database]: https://cratedb.com/solutions/real-time-analytics-database
