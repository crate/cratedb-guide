(pyviz)=
# PyViz

:::{include} /_include/links.md
:::

```{div} .float-right
[![hvPlot logo](https://hvplot.holoviz.org/_static/logo_horizontal.svg){height=60px loading=lazy}][hvPlot]
[![Datashader logo](https://datashader.org/_static/logo_horizontal.svg){height=60px loading=lazy}][Datashader]
```
```{div} .clearfix
```

The PyViz.org website is an open platform for helping users decide on the best
open-source (OSS) Python data visualization tools.

(hvplot)=
(datashader)=
## hvPlot and Datashader

:::::{grid}
:padding: 0

::::{grid-item}
:columns: auto 8 8 8

[hvPlot] is a familiar and high-level API for data exploration and visualization.
[Datashader] is a graphics pipeline system for creating
meaningful representations of large datasets quickly and flexibly.

It is used on behalf of the [hvPlot] package, which is based on [HoloViews], from the
family of [HoloViz] packages of the [PyViz] ecosystem.

With Datashader, you can "just plot" large datasets and explore them instantly, with no
parameter tweaking, magic numbers, subsampling, or approximation, up to the resolution
of the display.

[hvPlot] sources its power in the [HoloViz] ecosystem. With [HoloViews], you get the
ability to easily layout and overlay plots, with [Panel], you can get more interactive
control of your plots with widgets, with [DataShader], you can
visualize and interactively explore large-scale datasets, and with [GeoViews], you can
create geographic plots.
::::

::::{grid-item}
:columns: auto 4 4 4

[![Datashader map aggregation example][ds1]][ds1]

[![Datashader scatter/heat example][ds2]][ds2]

[ds1]: https://github.com/crate/crate-clients-tools/assets/453543/7f38dff6-04bc-429e-9d31-6beeb9289c4b
[ds2]: https://github.com/crate/crate-clients-tools/assets/453543/23561a87-fb4f-4154-9891-1b3068e40579

::::

:::::


## Learn

:::{include} /_include/card/timeseries-datashader.md
:::


:::{rubric} Webinars
:::

::::{info-card}

:::{grid-item}
:columns: 8

{material-outlined}`manage_history;2em` &nbsp; **Presentation about hvPlot and Panel at SciPy 2023**

_hvPlot and Panel: Visualize all your data easily, from notebooks to dashboards | SciPy 2023._
:::

:::{grid-item}
:columns: 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/eWpVUPHrCIA?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
:::

::::



[GeoViews]: https://geoviews.org/
[HoloViz]: https://holoviz.org/
[hvPlot]: https://hvplot.holoviz.org/
[Panel]: https://panel.holoviz.org/
[PyViz]: https://pyviz.org/
