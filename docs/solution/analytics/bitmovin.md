(bitmovin)=
# Bitmovin insights

:::{div} sd-text-muted
Multi-tenant data analytics on top of billions of records.
:::

:::{rubric} About
:::

Bitmovin is a leading video streaming company that built the world’s
first commercial adaptive streaming player and deployed the first
software-defined encoding service that runs on any cloud platform.

The use-case of Bitmovin illustrates why traditional databases are
incapable of handling so many data records while keeping them all
available for querying in real time.

> CrateDB enables use cases we couldn't satisfy with other
> database systems, also with databases which are even stronger
> focused on the time series domain.
>
> CrateDB is not your normal database!
>
> <small>-- Daniel Hölbling‑Inzko, Director of Engineering Analytics, Bitmovin</small>

:::{rubric} See also
:::

:::{card} Bitmovin: Analyzing large volumes of video streaming events while reducing the cost of analytics
:link: https://cratedb.com/stories/bitmovin
:link-type: url
CrateDB forms the backbone of Bitmovin's real-time video analytics platform.

Bitmovin's database cluster includes 14 nodes, storing 140 terabytes worth
of structured data such as user events and user interactions.
The video analytics application adds around 2 billion new events per day,
with the largest tables comprising around 60 billion playback events in total. 
:::


:::::{info-card}

::::{grid-item}
:columns: 6

{material-outlined}`analytics;2em` &nbsp; **Real-time analytics on user events**

<iframe height="300" src="https://www.youtube-nocookie.com/embed/4BPApD0Piyc?si=J0w5yG56Ld4fIXfm" title="YouTube: Bitmovin Real-time Analytics on User Events" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<small>-- [Bitmovin: Improving the streaming experience with real-time analytics]</small>
::::

::::{grid-item}
:columns: 6

Bitmovin, as a leader in video codec algorithms and as a web-based video
stream broadcasting provider, produces billions of rows of data and stores
them in CrateDB, allowing their customers to do analytics on it.

One of their product's subsystems, a video analytics component, required to
serve real-time analytics on massive, fast-moving data, so they needed
to find a performing database at the right cost.

:::{article-info}
---
author: Daniel Hölbling‑Inzko, Georg Traar
date: October 14, 2022
read-time: 50 min watch
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
:::
::::

:::::


:::::{info-card}

::::{grid-item}
:columns: 6

{material-outlined}`video_camera_back;2em` &nbsp; **Live video broadcasting campaigns**

<iframe height="300" src="https://www.youtube-nocookie.com/embed/IR6hokaYv5g?si=J0w5yG56Ld4fIXfm" title="YouTube: Live Video Broadcasting with CrateDB" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<small>-- [How Bitmovin uses CrateDB to monitor the biggest live video events]</small>
::::

::::{grid-item}
:columns: 6

Bitmovin produces billions of rows of data and stores it in CrateDB.
In this talk, Daniel explains how Bitmovin uses CrateDB to monitor
the most significant live video events and especially which features
they are using to address their monitoring and scalability challenges.

Learn also about their typical queries and how the support from Crate\.io
helps them in their day-to-day data operations.

:::{article-info}
---
author: Daniel Hölbling‑Inzko
date: Nov 15, 2022
read-time: 35 min watch
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
:::
::::

:::::


:Industry:
  {tags-secondary}`Broadcasting`
  {tags-secondary}`Media Transcoding`
  {tags-secondary}`Streaming Media`

:Tags:
  {tags-primary}`Event Tracking`
  {tags-primary}`Real-Time Analytics`
  {tags-primary}`Multi Tenancy`
  {tags-primary}`SaaS`


[Bitmovin: Improving the streaming experience with real-time analytics]: https://youtu.be/4BPApD0Piyc?feature=shared
[How Bitmovin uses CrateDB to monitor the biggest live video events]: https://youtu.be/IR6hokaYv5g?feature=shared
