(timeseries-generate)=

(gen-ts)=

# Generate time series data

To work with time series data, you are going to need a source of time series
data. Fortunately, there are many ways to generate time series data, for
example by sampling system metrics on your workstation or server.

CrateDB is purpose-built for working with massive amounts of time series data,
like the type of data produced by smart sensors and other [Internet of Things]
(IoT) devices.

This collection of tutorials will show you how to generate mock time series
data about the [International Space Station] (ISS) and write it to CrateDB
using the client of your choice.

```{eval-rst}
.. rubric:: Table of contents
```

```{toctree}
:maxdepth: 2
:titlesonly: true

cli
python
node
go
```

[international space station]: https://www.nasa.gov/mission_pages/station/main/index.html
[internet of things]: https://en.wikipedia.org/wiki/Internet_of_things
[system load]: https://en.wikipedia.org/wiki/Load_(computing)
