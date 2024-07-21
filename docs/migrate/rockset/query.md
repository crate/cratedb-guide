# Migrating queries from Rockset to CrateDB

## Introduction
As we work with more and more companies looking to migrate their workloads from
[Rockset] to CrateDB, we have built expertise on the details of what a [migration]
entails.

Both Rockset and CrateDB use SQL, so there is no need for your teams to
learn a new query language, there are however a few differences in the dialect. 

## First level columns
In Rockset, every record is entirely a JSON object, but in CrateDB tables have
first level columns which themselves can be of type [OBJECT].
If you are looking at migrating data from Rockset keeping changes to a minimum,
you can just define your tables with a single column of type `OBJECT`.
```sql
CREATE TABLE myschema.mytable (
	data OBJECT
);
```

## Accessing fields within objects
Rockset uses a dot notation for attribute access.
In CrateDB, a bracket notation is used instead, similar to what you would use in
Python for accessing dictionaries.
```sql
INSERT INTO myschema.mytable
VALUES('{"field1":1,"field2":"abc","field3":[1,2,3]}');

SELECT data['field2']
FROM myschema.mytable;
```

## Inspecting inferred schemas
After you load some JSON data into your database, you may want to check the schema
CrateDB has inferred automatically.
In Rockset, you would do this with the `DESCRIBE` command, in CrateDB you can use
`SHOW CREATE TABLE`.
```sql
SHOW CREATE TABLE myschema.mytable;
```

## Un-nesting arrays
Both Rockset and CrateDB provide an [UNNEST] function for un-nesting arrays.
In Rockset however you may have queries where `UNNEST` is used in a `CROSS JOIN`,
like in the [example with cars data in Rockset's documentation].
To achieve the same results in CrateDB, you can use `UNNEST` in the list of
columns you are selecting instead.
```sql
SELECT data['make'], UNNEST(data['models'])
FROM companies;
```

## Functions equivalence
You will find that a large number of functions work exactly in the same way in
Rockset and CrateDB. There are however some functions that exists under
different names.

We have compiled below a list of equivalences, and will come back and expand
this list as new functions come out in our work with prospects.

If there is anything in your queries for which you do not see an equivalence,
do not hesitate to reach out as chances are CrateDB has the same functionality
under a different name, or there may be a simple workaround for your use cases.


| Rockset function | CrateDB equivalent |
| ---      | ---       |
| ACOSH(x)| `LN(x + SQRT((x * x) - 1))`  |
| APPROX_DISTINCT(x[, e])| `hyperloglog_distinct`  |
| ARRAY_CONCAT(array1, array2, ...)| `array_cat`  |
| ARRAY_CONTAINS(array, element)| `element = ANY (array)`  |
| ARRAY_CREATE(val1, val2, ...)| `[val1, val2, ...]` or `_array(val1,val2, ...)`  |
| ARRAY_DISTINCT(array)| `array_unique`  |
| ARRAY_EXCEPT(array1, array2)| `array_unique(array_difference(array1, array2))` |
| ARRAY_FLATTEN(array)| `array_unnest`  |
| ARRAY_JOIN(array, delimiter, nullReplacement)| [`array_to_string`]  |
| ARRAY_MAP(function_name, array)| `(select array_agg(function_name(unnest)) from unnest(array))`  |
| ARRAY_REMOVE(array, val)| `array_difference(array,[val])`  |
| ARRAY_SHUFFLE(array)| `array(select unnest from unnest(array) ORDER BY random())`  |
| ARRAY_SORT(array)| `array(select unnest from unnest(array) ORDER BY unnest)`  |
| ARRAY_UNION(array1, array2)| `array_unique`  |
| ASINH(x)| `LN(x + SQRT((x * x) + 1))`   |
| ATANH(x)| `0.5*ln((1+x)/(1-x))`  |
| BITWISE_AND(x, y)| `x & y` |
| BITWISE_OR(x, y)| `x \| y`  |
| BITWISE_XOR(x, y)| `x # y`  |
| BOOL_AND(x)| `val1 AND val2 AND ... `  |
| BOOL_OR(x)| `val1 OR val2 OR ...`  |
| CARDINALITY(array)| `array_length(array,1)`  |
| COUNT_IF(x)| `COUNT(*) FILTER (WHERE x)`  |
| DATE_PARSE(string, format)| UDF: [`to_date`]   |
| DAYS(n)| `'n DAYS'::INTERVAL`  |
| EUCLIDEAN_DIST(array, array)| UDF: [`n_dimensional_distance`]  |
| EVERY(x)| `val1 AND val2 AND ... `  |
| FORMAT_DATE(format, date)| `date_format`  |
| FORMAT_DATETIME(format, datetime)| `date_format`  |
| FORMAT_TIME(format, time)| `date_format`  |
| FORMAT_TIMESTAMP(format, timestamp[, timezone]| `date_format`  |
| FROM_BASE64(s)| `decode(s, 'base64')`   |
| FROM_HEX(s)| `decode(s, 'hex')`  |
| HOURS(n)| `'n HOURS'::INTERVAL`  |
| HYPOT(x, y)| `SQRT(x*x+y*y)`  |
| IS DISTINCT FROM| `<>`  |
| JSON_FORMAT(x)| `x::TEXT`   |
| JSON_PARSE(x)| `x::OBJECT`  |
| KEYS(obj)| `object_keys(obj)`  |
| LOG(x)| `ln(x)`  |
| LOG10(x)| `log(x,10)`  |
| LOG2(x)| `log(x,2)`  |
| MILLISECONDS(n)| `AGE(n::LONG,0)`  |
| MINUTES(n)| `'n MINUTES'::INTERVAL`  |
| MONTHS(n)| `'n MONTHS'::INTERVAL`  |
| PARSE_DATE_ISO8601(string)| `date_trunc('day',string::TIMESTAMP)`  |
| PARSE_DATETIME_ISO8601(string)| `string::TIMESTAMP`  |
| POW(x, y)| `power(x,y)`  |
| RAND()| `random()`  |
| SEQUENCE(start, stop[, step])| `generate_series`  |
| SIGN(x)| See [^sign] for CrateDB <5.8  |
| ST_ASTEXT(geography)| See [](#ST_ASTEXT) for `POLYGON`s  |
| ST_GEOGFROMTEXT(well_known_text)| `well_known_text::geo_shape`  |
| ST_GEOGPOINT(longitude, latitude)| `[longitude, latitude]::geo_point`  |
| ST_INTERSECTS(geography_a, geography_b)| `intersects(geo_shape, geo_shape)`  |
| ST_X(point)| `longitude(point)`  |
| ST_Y(point)| `latitude(point)`  |
| TIME_BUCKET(interval, timestamp[, origin])| `date_bin`  |
| TIMESTAMP_SECONDS(n)| `(n::DOUBLE)::timestamp`  |
| TO_BASE64(b)| `encode(b, 'base64')`  |
| TO_HEX(b)| `encode(b, 'hex')`  |
| TRUNCATE(x)| `trunc(x)`   |
| TYPEOF(x)| `pg_typeof(x)`  |
| YEARS(n)| `'n YEARS'::INTERVAL`  |

[`array_to_string`]: https://cratedb.com/docs/crate/reference/en/latest/general/builtins/scalar-functions.html#array-to-string-anyarray-separator-null-string
[`n_dimensional_distance`]: https://community.cratedb.com/t/user-defined-function-collection/773
[`to_date`]: https://github.com/crate/crate/issues/9663#issuecomment-2178878930


## Appendix

(ST_ASTEXT)=
### ST_ASTEXT
CrateDB [user-defined function (UDF)] implementation of `ST_ASTEXT` function for polygons.
```text
CREATE FUNCTION ST_ASTEXT(geography geo_shape)
    RETURNS TEXT
    LANGUAGE JAVASCRIPT AS $$
    function st_astext(g) {
        return 'POLYGON(' + g.coordinates.map(r => '(' + r.map(p => p.join(' ')).join(', ') + ')').join(', ') + ')';
    }
    $$;
```


[^sign]: The `SIGN` function has been added in CrateDB 5.8 - in older versions use `IF(x<0,-1,IF(x=0,0,1))`.


[example with cars data in Rockset's documentation]: https://docs.rockset.com/documentation/reference/select#unnest
[migration]: https://cratedb.com/migrations/rockset
[OBJECT]: https://cratedb.com/docs/crate/reference/en/latest/general/ddl/data-types.html#objects
[Rockset]: https://rockset.com/
[UNNEST]: https://cratedb.com/docs/crate/reference/en/latest/general/builtins/table-functions.html#unnest-array-array
[user-defined function (UDF)]: https://cratedb-guide--53.org.readthedocs.build/feature/udf/
