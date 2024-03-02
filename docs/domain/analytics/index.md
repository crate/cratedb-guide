(analytics)=
# Raw-Data Analytics

**CrateDB provides real-time analytics on raw data.**

In domains of real-time analytics, where you absolutely must have access to all
the records, and can't live with any down-sampled variant, because records are
unique, and need to be accounted for within your analytics queries, you need a
storage system which manages all the data in its hot zone, to be available on
your fingertips.

With CrateDB, compatible to PostgreSQL, you can do all of that using plain SQL,
with excellent integration capabilities into commodity systems using standard
database access interfaces like ODBC or JDBC, and a proprietary HTTP interface
on top.


(bitmovin)=
## Bitmovin Insights

Multi tenant data analytics on top of billions of records.

:Industry:
    {tags-secondary}`Streaming Media` {tags-secondary}`Media Transcoding`
    {tags-secondary}`Broadcasting`

:Tags:
    {tags-primary}`Event Tracking` {tags-primary}`Customer Analytics`
    {tags-primary}`Multi Tenancy`


::::{info-card}

:::{grid-item}
:columns: 8

{material-outlined}`analytics;2em` &nbsp; **Bitmovin: Real-Time Analytics**

Bitmovin, as a leader in video codec algorithms and as a web-based video
stream broadcasting provider, produces billions of rows of data and stores
them in CrateDB, allowing their customers to do analytics on it.

Their product required to serve real-time analytics on very large and fast-moving
data, so they needed to find a performing database at the right cost.

- [Bitmovin: Improving the Streaming Experience with Real-Time Analytics]

The use-case of Bitmovin demonstrates why traditional databases weren't capable
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
