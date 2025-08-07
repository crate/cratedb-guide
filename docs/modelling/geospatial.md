# Geospatial data

CrateDB supports **real-time geospatial analytics at scale**, enabling you to store, query, and analyze location-based data using standard SQL over two dedicated types: **GEO\_POINT** and **GEO\_SHAPE**. You can seamlessly combine spatial data with full-text, vector, JSON, or time-series in the same SQL queries.

## 1. Geospatial Data Types

### **GEO\_POINT**

* Stores a single location via latitude/longitude.
* Insert using either a coordinate array `[lon, lat]` or WKT string `'POINT (lon lat)'`.
* Must be declared explicitly; dynamic schema inference will not detect geo\_point type.

### **GEO\_SHAPE**

* Supports complex geometries (Point, LineString, Polygon, MultiPolygon, GeometryCollection) via GeoJSON or WKT.
* Indexed using geohash, quadtree, or BKD-tree, with configurable precision (e.g. `50m`) and error threshold

## 2. Table Schema Example

<pre class="language-sql"><code class="lang-sql"><strong>CREATE TABLE parcel_zones (
</strong>    zone_id INTEGER PRIMARY KEY,
<strong>    name VARCHAR,
</strong>    area GEO_SHAPE,
    centroid GEO_POINT
)
WITH (column_policy = 'dynamic');
</code></pre>

* Use `GEO_SHAPE` to define zones or service areas.
* `GEO_POINT` allows for simple referencing (e.g. store approximate center of zone).

## 3. Core Geospatial Functions

CrateDB provides key scalar functions for spatial operations:

* **`distance(geo_point1, geo_point2)`** – returns meters using the Haversine formula (e.g. compute distance between two points)
* **`within(shape1, shape2)`** – true if one geo object is fully contained within another
* **`intersects(shape1, shape2)`** – true if shapes overlap or touch anywhere
* **`latitude(geo_point)` / `longitude(geo_point)`** – extract individual coordinates
* **`geohash(geo_point)`** – compute a 12‑character geohash for the point
* **`area(geo_shape)`** – returns approximate area in square degrees; uses geodetic awareness

Note: More precise relational operations on shapes may bypass indexes and can be slower.

## 4. Spatial Queries & Indexing

CrateDB supports Lucene-based spatial indexing (Prefix Tree and BKD-tree structures) for efficient geospatial search. Use the `MATCH` predicate to leverage indices when filtering spatial data by bounding boxes, circles, polygons, etc.

**Example: Find nearby assets**

```sql
SELECT asset_id, DISTANCE(center_point, asset_location) AS dist
FROM assets
WHERE center_point = 'POINT(-1.234 51.050)'::GEO_POINT
ORDER BY dist
LIMIT 10;
```

**Example: Count incidents within service area**

```sql
SELECT area_id, count(*) AS incident_count
FROM incidents
WHERE within(incidents.location, service_areas.area)
GROUP BY area_id;
```

**Example: Which zones intersect a flight path**

```sql
SELECT zone_id, name
FROM flight_paths f
JOIN service_zones z
ON intersects(f.path_geom, z.area);
```

## 5. Real-World Examples: Chicago Use Cases

* **311 calls**: Each record includes `location` as `GEO_POINT`. Queries use `within()` to find calls near a polygon around O’Hare airport.
* **Community areas**: Polygon boundaries stored in `GEO_SHAPE`. Queries for intersections with arbitrary lines or polygons using `intersects()` return overlapping zones.
* **Taxi rides**: Pickup/drop off locations stored as geo points. Use `distance()` filter to compute trip distances and aggregate.

## 6. Architectural Strengths & Suitability

* Designed for **real-time geospatial tracking and analytics** (e.g. fleet tracking, mapping, location-layered apps).
* **Unified SQL platform**: spatial data can be combined with full-text search, JSON, vectors, time-series — in the same table or query.
* **High ingest and query throughput**, suitable for large-scale location-based workloads

## 7. Best Practices Checklist

<table><thead><tr><th>Topic</th><th width="254">Recommendation</th></tr></thead><tbody><tr><td>Data types</td><td>Declare <code>GEO_POINT</code>/<code>GEO_SHAPE</code> explicitly</td></tr><tr><td>Geometric formats</td><td>Use WKT or GeoJSON for insertions</td></tr><tr><td>Index tuning</td><td>Choose geohash/quadtree/BKD tree &#x26; adjust precision</td></tr><tr><td>Queries</td><td>Prefer <code>MATCH</code> for indexed filtering; use functions for precise checks</td></tr><tr><td>Joins &#x26; spatial filters</td><td>Use within/intersects to correlate spatial entities</td></tr><tr><td>Scale &#x26; performance</td><td>Index shapes, use distance/wwithin filters early</td></tr><tr><td>Mixed-model integration</td><td>Combine spatial with JSON, full-text, vector, time-series</td></tr></tbody></table>

## 8. Further Learning & Resources

* Official **Geospatial Search Guide** in CrateDB docs, detailing geospatial types, indexing, and MATCH predicate usage.
* CrateDB Academy **Hands-on: Geospatial Data** modules, with sample datasets (Chicago 311 calls, taxi rides, community zones) and example queries.
* CrateDB Blog: **Geospatial Queries with CrateDB** – outlines capabilities, limitations, and practical use cases (available since version 0.40

## 9. Summary

CrateDB provides robust support for geospatial modeling through clearly defined data types (`GEO_POINT`, `GEO_SHAPE`), powerful scalar functions (`distance`, `within`, `intersects`, `area`), and Lucene‑based indexing for fast queries. It excels in high‑volume, real‑time spatial analytics and integrates smoothly with multi-model use cases. Whether storing vehicle positions, mapping regions, or enabling spatial joins—CrateDB’s geospatial layer makes it easy, scalable, and extensible.
