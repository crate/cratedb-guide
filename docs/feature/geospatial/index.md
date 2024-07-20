(geo)=
(geospatial)=
# Geospatial Data

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**CrateDB supports location data for efficiently storing and querying
geographic and spatial/geospatial data.**

:::{rubric} Overview
:::
CrateDB can be used as a database to conduct geospatial search operations
building upon the Prefix Tree and BKD-tree index structures of Apache Lucene.

:::{rubric} About
:::
CrateDB's GEO_POINT and GEO_SHAPE geographic data types represent points
or shapes in a 2D world.

:GEO_POINT:
    A geographic data type used to store latitude and longitude coordinates.
:GEO_SHAPE:
    A geographic data type used to store 2D shapes defined as GeoJSON geometry
    objects. It supports Point, MultiPoint, LineString, MultiLineString,
    Polygon, MultiPolygon, and GeometryCollection.
::::



::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- [](inv:crate-reference#data-types-geo-point)
- [](inv:crate-reference#data-types-geo-shape)
- [](inv:crate-reference#sql_dql_geo_search)

```{rubric} Related
```
- {ref}`sql`
- {ref}`query`

{tags-primary}`SQL`
{tags-primary}`Geospatial`
{tags-primary}`GeoJSON`
{tags-primary}`WKT`
::::

:::::


:::{rubric} Details
:::
When inserting spatial data, you can use [GeoJSON] or [WKT] formats.

- Geographic points can be inserted as a double precision array with longitude and
  latitude values, or by using a WKT string.
- Geographic shapes can be inserted as GeoJSON object literal or parameter as seen
  above and as WKT string.

Using spatial search, you can:

- Index points or other shapes.
- Filter search results by a bounding box, circle, donut, or other shape.
- Sort or boost scoring by distance between points, or relative area between rectangles.
- Generate a 2D grid of facet count numbers for heatmap generation or point-plotting.

:::{rubric} About Lucene
:::
CrateDB uses Lucene as a storage layer, so it inherits the implementation
and concepts of Lucene, in the same spirit like Solr and Elasticsearch.

- [Geospatial Indexing & Search at Scale with Lucene]
- [Geospatial Indexing with Apache Lucene and OpenSearch]
- [Apache Solr Spatial Search]

:::{div}
While Elasticsearch uses a [query DSL based on JSON], in CrateDB, you can work
with geospatial data using SQL.
:::


## Synopsis

Select data points by distance.

```sql
/**
 * Based on the location of the International Space Station,
 * this query returns the 10 closest capital cities from
 * the last known position.
**/

SELECT
  city AS "City Name",
  country AS "Country",
  DISTANCE(i.position, c.location)::LONG / 1000
    AS "Distance [km]"
FROM demo.iss i
CROSS JOIN demo.world_cities c
WHERE capital = 'primary'
  AND ts = (SELECT MAX(ts) FROM demo.iss)
ORDER BY 3 ASC
LIMIT 10;
```


## Usage

Using geographic search in CrateDB.

:::{rubric} Index Structure Type
:::
Computations on very complex polygons and geometry collections are exact but
very expensive. To provide fast queries even on complex shapes, CrateDB uses
a different approach to store, analyze and query geo shapes. The available
geo shape indexing strategies are based on two primary data structures: Prefix
and BKD trees, which are described below.

There are three geographic index types: `geohash` (default), `quadtree`, and
`bkdtree`, described in more detail at [](inv:crate-reference#type-geo_shape-index).

:::{rubric} Column Definition
:::
Learn how to define a `GEO_SHAPE` column, and how to adjust parameters of the
index structure in the documentation section about
[](inv:crate-reference#type-geo_shape-definition).

:::{rubric} `MATCH` predicate
:::
CrateDB's [MATCH predicate for geographical search] can be used to query
geographic indices for relations between geographical shapes and points.
It supports the **intersects**, **disjoint**, and **within** operations.


## Learn

Learn how to use CrateDB's geospatial data types through ORM adapters,
tutorials, or example applications.

:::{rubric} Examples and Tutorials
:::
- [Geospatial Queries with CrateDB]
- [Berlin and Geo Shapes in CrateDB]
- [Spatial data demo application using CrateDB and the Express framework]
- [Plane Spotting with Software Defined Radio (SDN), CrateDB and Node.js]

:::{rubric} Webinars
:::
- [CrateDB: Querying Multi-Model Heterogeneous Time-Series Data with SQL]

:::{rubric} Documentation
:::
- [SQLAlchemy Geopoint and Geoshape types]
- [Working with geospatial types in SQLAlchemy]

:::{rubric} In-Depth
:::
- [Geometric Shapes Indexing with BKD-trees]

:::{rubric} Testimonials
:::
- [GolfNow chooses CrateDB] for location analytics and commerce.
- [Spatially Health chooses CrateDB] for location analytics.


:::{seealso} **Product:**
[Multi-model Database] •
[Geospatial Database] •
[Geospatial Data Model] •
[Dynamic Database Schemas] •
[Nested Data Structure] •
[Relational Database]
:::


:::{todo}
- Improve "examples" sections.
- Better layout for "Learn" section.
:::


[Apache Solr Spatial Search]: https://solr.apache.org/guide/solr/latest/query-guide/spatial-search.html
[Berlin and Geo Shapes in CrateDB]: https://cratedb.com/blog/geo-shapes-in-cratedb
[CrateDB: Querying Multi-Model Heterogeneous Time-Series Data with SQL]: https://cratedb.com/resources/videos/unleashing-the-power-of-multi-model-data-querying-heterogeneous-time-series-data-with-sql-in-cratedb
[GeoJSON]: https://en.wikipedia.org/wiki/GeoJSON
[Geometric Shapes Indexing with BKD-trees]: https://cratedb.com/blog/geometric-shapes-indexing-with-bkd-trees
[Geospatial Indexing & Search at Scale with Lucene]: https://portal.ogc.org/files/?artifact_id=90337
[Geospatial Indexing with Apache Lucene and OpenSearch]: https://talks.osgeo.org/foss4g-2022/talk/KPQ97A/
[Geospatial Queries with CrateDB]: https://cratedb.com/blog/geospatial-queries-with-crate-data
[GolfNow chooses CrateDB]: https://cratedb.com/resources/videos/interview-golfnow-cratedb
[MATCH predicate for geographical search]: inv:crate-reference#sql_dql_geo_match
[Plane Spotting with Software Defined Radio (SDN), CrateDB and Node.js]: https://github.com/crate/devrel-plane-spotting-with-cratedb
[Spatial data demo application using CrateDB and the Express framework]: https://github.com/crate/devrel-shipping-forecast-geo-demo
[Spatially Health chooses CrateDB]: https://cratedb.com/customers/spatially-cratedb-location-analytics
[SQLAlchemy Geopoint and Geoshape types]: inv:sqlalchemy-cratedb#geopoint
[WKT]: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
[Working with geospatial types in SQLAlchemy]: https://cratedb.com/docs/sqlalchemy-cratedb/working-with-types.html#geospatial-types
