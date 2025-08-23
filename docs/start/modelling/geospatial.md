# Geospatial data

CrateDB supports **real-time geospatial analytics at scale**, enabling you to store, query, and analyze 2D location-based data using standard SQL over two dedicated types: **GEO\_POINT** and **GEO\_SHAPE**. You can seamlessly combine spatial data with full-text, vector, JSON, or time-series in the same SQL queries.

## Geospatial Data Types

### **GEO\_POINT**

* Stores a single location via latitude/longitude.
* Insert using either a coordinate array `[lon, lat]` or Well-Known Text (WKT) string `'POINT (lon lat)'`.
* Must be declared explicitly; dynamic schema inference will not detect `geo_point` type.

### **GEO\_SHAPE**

* Supports complex geometries (Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, GeometryCollection) via GeoJSON or WKT.
* Indexed using geohash, quadtree, or BKD-tree, with configurable precision (e.g. `50m`) and error threshold. The indexes are described in the [reference manual](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/data-types.html#type-geo-shape-index).

## Table Schema Example

Let's define a table with country boarders and capital:

```sql
CREATE TABLE country (
   name text,
   country_code text primary key,
   shape geo_shape INDEX USING "geohash" WITH (precision='100m'),
   capital text,
   capital_location geo_point
) 
```

* Use `GEO_SHAPE` to define the border.
* `GEO_POINT` to define the location of the capital.

## Insert rows

We can populate the table with Austria:

```sql
INSERT INTO country (name, country_code, shape, capital, capital_location)
VALUES (
  'Austria',
  'at',
  
  ##{type='Polygon', coordinates=[
        [[16.979667, 48.123497], [16.903754, 47.714866],
        [16.340584, 47.712902], [16.534268, 47.496171],
        [16.202298, 46.852386], [16.011664, 46.683611],
        [15.137092, 46.658703], [14.632472, 46.431817],
        [13.806475, 46.509306], [12.376485, 46.767559],
        [12.153088, 47.115393], [11.164828, 46.941579],
        [11.048556, 46.751359], [10.442701, 46.893546],
        [9.932448, 46.920728], [9.47997, 47.10281],
        [9.632932, 47.347601], [9.594226, 47.525058],
        [9.896068, 47.580197], [10.402084, 47.302488],
        [10.544504, 47.566399], [11.426414, 47.523766],
        [12.141357, 47.703083], [12.62076, 47.672388],
        [12.932627, 47.467646], [13.025851, 47.637584],
        [12.884103, 48.289146], [13.243357, 48.416115],
        [13.595946, 48.877172], [14.338898, 48.555305],
        [14.901447, 48.964402], [15.253416, 49.039074],
        [16.029647, 48.733899], [16.499283, 48.785808],
        [16.960288, 48.596982], [16.879983, 48.470013],
        [16.979667, 48.123497]]
  ]},
  'Vienna',
  [16.372778, 48.209206]
);
```

## Core Geospatial Functions

CrateDB provides key scalar functions for spatial operations:

* **`distance(geo_point1, geo_point2)`** – returns meters using the Haversine formula (e.g. compute distance between two points)
* **`within(shape1, shape2)`** – true if one geo object is fully contained within another
* **`intersects(shape1, shape2)`** – true if shapes overlap or touch anywhere
* **`latitude(geo_point)` / `longitude(geo_point)`** – extract individual coordinates
* **`geohash(geo_point)`** – compute a 12‑character geohash for the point
* **`area(geo_shape)`** – returns approximate area in square degrees; uses geodetic awareness

Furthermore, it is possible to use the **match** predicate with geospatial data in queries.

Note: More precise relational operations on shapes may bypass indexes and can be slower.

## An example query

It is possible to find the distance to the capital of each country in the table:

```sql
SELECT distance(capital_location, [9.74, 47.41])/1000
FROM country;
```

## Real-World Examples: Chicago Use Cases

* **311 calls**: Each record includes `location` as `GEO_POINT`. Queries use `within()` to find calls near a polygon around O’Hare airport.
* **Community areas**: Polygon boundaries stored in `GEO_SHAPE`. Queries for intersections with arbitrary lines or polygons using `intersects()` return overlapping zones.
* **Taxi rides**: Pickup/drop off locations stored as geo points. Use `distance()` filter to compute trip distances and aggregate.

## Architectural Strengths & Suitability

* Designed for **real-time geospatial tracking and analytics** (e.g. fleet tracking, mapping, location-layered apps).
* **Unified SQL platform**: spatial data can be combined with full-text search, JSON, vectors, time-series — in the same table or query.
* **High ingest and query throughput**, suitable for large-scale location-based workloads

## Best Practices Checklist

<table><thead><tr><th>Topic</th><th width="254">Recommendation</th></tr></thead><tbody><tr><td>Data types</td><td>Declare <code>GEO_POINT</code>/<code>GEO_SHAPE</code> explicitly</td></tr><tr><td>Geometric formats</td><td>Use WKT or GeoJSON for insertions</td></tr><tr><td>Index tuning</td><td>Choose geohash/quadtree/BKD tree &#x26; adjust precision</td></tr><tr><td>Queries</td><td>Prefer <code>MATCH</code> for indexed filtering; use functions for precise checks</td></tr><tr><td>Joins &#x26; spatial filters</td><td>Use within/intersects to correlate spatial entities</td></tr><tr><td>Scale &#x26; performance</td><td>Index shapes, use distance/wwithin filters early</td></tr><tr><td>Mixed-model integration</td><td>Combine spatial with JSON, full-text, vector, time-series</td></tr></tbody></table>

## Further Learning & Resources

* Official **Geospatial Search Guide** in CrateDB docs, detailing geospatial types, indexing, and MATCH predicate usage.
* CrateDB Academy **Hands-on: Geospatial Data** modules, with sample datasets (Chicago 311 calls, taxi rides, community zones) and example queries.
* CrateDB Blog: **Geospatial Queries with CrateDB** – outlines capabilities, limitations, and practical use cases (available since version 0.40

## Summary

CrateDB provides robust support for geospatial modeling through clearly defined data types (`GEO_POINT`, `GEO_SHAPE`), powerful scalar functions (`distance`, `within`, `intersects`, `area`), and Lucene‑based indexing for fast queries. It excels in high‑volume, real‑time spatial analytics and integrates smoothly with multi-model use cases. Whether storing vehicle positions, mapping regions, or enabling spatial joins—CrateDB’s geospatial layer makes it easy, scalable, and extensible.
