(model-geospatial)=
# Geospatial data

CrateDB supports **real-time geospatial analytics at scale**, enabling you to
store, query, and analyze 2D location-based data using standard SQL over two
dedicated types: **GEO\_POINT** and **GEO\_SHAPE**. You can seamlessly combine
spatial data with full-text, vector, JSON, or time-series in the same SQL
queries.

The strength of CrateDB's support for geospatial data includes:

* Designed for **real-time geospatial tracking and analytics** (e.g., fleet
  tracking, mapping, location-layered apps)
* **Unified SQL platform**: spatial data can be combined with full-text search,
  JSON, vectors, time-series — in the same table or query
* **High ingest and query throughput**, suitable for large-scale location-based
  workloads

## Geospatial Data Types

CrateDB has two geospatial data types:

### GEO_POINT

* Stores a single location via latitude/longitude.
* Insert using
  * coordinate array `[lon, lat]`
  * [Well-Known Text](https://libgeos.org/specifications/wkt/) (WKT) string
    `'POINT (lon lat)'`.
* Must be declared explicitly; dynamic schema inference will not detect
  `geo_point` type.

### GEO_SHAPE

* Represents more complex 2D shapes defined via GeoJSON or WKT formats.
* Supported geometry types:
  * `Point`, `MultiPoint`
  * `LineString`, `MultiLineString`
  * `Polygon`, `MultiPolygon`
  * `GeometryCollection`
* Indexed using geohash, quadtree, or BKD-tree, with configurable precision
  (e.g. `50m`) and error threshold. The indexes are described in the [reference
  manual](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/data-types.html#type-geo-shape-index).
  You can choose and configure the indexing method when defining your table
  schema.

## Defining a Geospatial Column

Here’s an example of how to define a `GEO_SHAPE` column with a specific index:

```sql
CREATE TABLE parks (
  name TEXT,
  area GEO_SHAPE INDEX USING quadtree WITH (precision = '50m')
);
```

## Inserting Geospatial Data

You can insert geospatial values using either **GeoJSON** or **WKT** formats.

```sql
-- Insert a shape (WKT format)
INSERT INTO parks (name, area)
VALUES ('My Park', 'POLYGON ((5 5, 30 5, 30 30, 5 30, 5 5))');
```

## Querying with spatial operations

For example, check whether a point lies within a park:

```sql
SELECT name FROM parks
WHERE within('POINT(10 10)'::geo_shape, area);
```

CrateDB provides key scalar functions for spatial operations such as distance(),
within(), intersects(), area(), geohash() and latitude()/longitude().

Furthermore, it is possible to use the **match** predicate with geospatial data
in queries.

See {ref}`Geo Search <crate-reference:sql_dql_geo_search>` for details.

## Further Learning & Resources

* Reference manual:
  * {ref}`Geo Search <crate-reference:sql_dql_geo_search>`
  * {ref}`Geo functions <crate-reference:scalar-geo>`: distance, within,
    intersects, latitude, longitude, geohash, area
* CrateDB Academy [**Hands-on: Geospatial
  Data**](https://cratedb.com/academy/fundamentals/data-modelling-with-cratedb/hands-on-geospatial-data)
  modules, with sample datasets (Chicago 311 calls, taxi rides, community zones)
  and example queries.
* CrateDB Blog: [**Geospatial Queries with
  CrateDB**](https://cratedb.com/blog/geospatial-queries-with-crate-data) –
  outlines capabilities, limitations, and practical use cases.
