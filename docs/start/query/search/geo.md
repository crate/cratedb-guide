# Geo search

CrateDB natively supports geospatial data types and spatial queries, allowing you to store, index, and efficiently query geographic data using SQL. Built on Apache Lucene, CrateDB offers powerful location-based search capabilities at scale.

## Overview

CrateDB enables geospatial search using **Lucene’s Prefix Tree** and **BKD Tree** indexing structures. With CrateDB, you can:

* Store and index geographic **points** and **shapes**
* Perform spatial queries using **bounding boxes**, **circles**, **donut shapes**, and more
* Filter, sort, or boost results by **distance**, **area**, or **spatial relationship**

You interact with geospatial data through SQL, combining ease of use with advanced capabilities.

## Geospatial Data Types

CrateDB supports two primary geospatial types:

### `GEO_POINT`

* Represents a single point using latitude and longitude.
* Can be inserted as:
  * An array: `[longitude, latitude]`
  * A WKT string (e.g. `'POINT (13.4050 52.5200)'`)

### `GEO_SHAPE`

* Represents more complex 2D shapes defined via GeoJSON or WKT formats.
* Supported geometry types:
  * `Point`, `MultiPoint`
  * `LineString`, `MultiLineString`
  * `Polygon`, `MultiPolygon`
  * `GeometryCollection`
* Insertable using:
  * A GeoJSON object
  * A WKT string

## Inserting Spatial Data

You can insert geospatial values using either **GeoJSON** or **WKT** formats.

**Examples**:

```sql
-- Inserting a point
INSERT INTO locations (name, coordinates)
VALUES ('Berlin', [13.4050, 52.5200]);

-- Inserting a shape (WKT format)
INSERT INTO parks (name, area)
VALUES ('Central Park', 'POLYGON ((...))');
```

## Querying Geospatial Data

CrateDB supports several SQL functions and predicates to work with geospatial data:

### Common Functions

| Function                               | Description                                          |
| -------------------------------------- | ---------------------------------------------------- |
| `distance(p1, p2)`                     | Computes the distance (in meters) between two points |
| `within(shape, region)`                | Checks if a shape is fully within another shape      |
| `intersects(shape1, shape2)`           | Checks if two shapes intersect                       |
| `area(shape)`                          | Returns the area of a given shape                    |
| `latitude(point)` / `longitude(point)` | Extracts lat/lon from a `GEO_POINT`                  |
| `geohash(point)`                       | Returns the geohash representation of a point        |

### MATCH Predicate

CrateDB provides a `MATCH` predicate for geospatial relationships:

```sql
sqlCopierModifier-- Find parks that intersect with a given region
SELECT name
FROM parks
WHERE MATCH(area) AGAINST('INTERSECTS POLYGON ((...))');
```

Supported relations: `INTERSECTS`, `DISJOINT`, `WITHIN`.

## Example: Finding Nearby Cities

The following query finds the 10 closest capital cities to the current location of the International Space Station:

```sql
SELECT
  city AS "City Name",
  country AS "Country",
  DISTANCE(i.position, c.location)::LONG / 1000 AS "Distance [km]"
FROM demo.iss i
CROSS JOIN demo.world_cities c
WHERE capital = 'primary'
  AND ts = (SELECT MAX(ts) FROM demo.iss)
ORDER BY 3 ASC
LIMIT 10;
```

## Indexing Strategies

CrateDB supports multiple indexing strategies for `GEO_SHAPE` columns:

| Index Type          | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| `geohash` (default) | Hash-based prefix tree for point-based queries               |
| `quadtree`          | Space-partitioning using recursive quadrant splits           |
| `bkdtree`           | Lucene BKD tree for efficient bounding box and range queries |

You can choose and configure the indexing method when defining your table schema.

### Performance Note

While CrateDB can perform **exact computations** on complex geometries (e.g. large polygons, geometry collections), these can be computationally expensive. Choose your index strategy carefully based on your query patterns.

## Defining a Geospatial Column

Here’s how to define a `GEO_SHAPE` column with a specific index:

```sql
CREATE TABLE regions (
  name TEXT,
  area GEO_SHAPE INDEX USING 'quadtree'
);
```

For full details, refer to the Geo Shape Column Definition section in the reference.
