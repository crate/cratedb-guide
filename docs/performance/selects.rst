.. _performance-select:

==================
Select Performance
==================

Aggregations and ``GROUP BY``
=============================

It is common to do ``GROUP BY`` queries for analytics purposes. For example,
you might select the ``avg``, ``max``, and ``min`` of some measurements over a
billion records and group them by device ID.

If you're running this query over a billion records and grouping by device ID,
you might have something like this::

   cr> SELECT
      device_id,
      max(value),
      avg(value),
      min(value)
   FROM
      measures
   GROUP BY
      device_id
   ORDER BY
      1 DESC;

   +-----------+------------+-------------------+------------+
   | device_id | max(value) |        avg(value) | min(value) |
   +-----------+------------+-------------------+------------+
   |         4 |      10000 | 5003.748816285036 |          0 |
   |         3 |      10000 | 5005.297395430482 |          0 |
   |         2 |      10000 | 5002.940588080021 |          0 |
   |         1 |      10000 | 5002.216030711031 |          0 |
   +-----------+------------+-------------------+------------+

By default, CrateDB processes all matching records. This may require a lot of
processing power, depending on the data set and the size of the CrateDB
cluster.

Some databases can limit the amount of records that are processed for
``GROUP BY`` operations (also known as `down-sampling`_) to improve performance
at the cost of less accurate results.

This exploits the fact that if your data set has a `normal distribution`_, it
is likely that the average over the whole data set is not much different from
the average over a subset of the data.

Aggregating 100,000 records instead of 10 or 100 million records can make a
huge difference in query response times.

For some analytics use-cases, this is an acceptable trade-off.

CrateDB users can emulate this down-sampling behaviour with a combination of
:ref:`LIMITs <crate-reference:sql-select-limit>` and
:ref:`sub-selects <crate-reference:sql-select-sub-select>`.
However, doing so involves costly data merges in
the query execution plan that reduce the parallelization (and thus performance)
of a distributed query.

A better way to emulate down-sampling is to filter on the ``_docid`` system
column using a :ref:`modulo (%) operation <crate-reference:arithmetic>`,
like this::

   cr> SELECT
      device_id,
      max(value),
      avg(value),
      min(value)
   FROM
      measures
   WHERE
      _docid % 10 = 0
   GROUP BY
      device_id
   ORDER BY
      1 DESC;

   +-----------+------------+--------------------+------------+
   | device_id | max(value) |         avg(value) | min(value) |
   +-----------+------------+--------------------+------------+
   |         4 |      10000 | 5013.052623224065  |          1 |
   |         3 |      10000 | 4999.1253575025175 |          0 |
   |         2 |      10000 | 5001.400379047543  |          0 |
   |         1 |      10000 | 5035.220951927276  |          0 |
   +-----------+------------+--------------------+------------+

You'll notice that the result has changed slightly, but is still fairly close
to the original result.

.. TIP::

    The ``% 10`` in this example was arbitrary and roughly translates to: "only
    consider every 10th row."

    The higher the number, the fewer records will match the query and the less
    accurate the result will be. Larger numbers trade accuracy for
    performance.

.. NOTE::

   The ``_docid`` system column exposes the internal document ID each document
   has within a `Lucene segment`_. The IDs are unique within a segment but not
   across segments or shards. This is good enough for a modulo sampling
   operation.

   Furthermore, the internal ID is already available and doesn't have to be
   read from the file system. This makes it an ideal candidate for modulo
   based sampling.


.. _downsampling-timestamp-binning:

Downsampling with ``DATE_BIN``
==============================

For improved downsampling using time-bucketing and resampling, the article
`resampling time series data with DATE_BIN`_ shares patterns how to
group records into time buckets and resample the values.

This technique will improve query performance by reducing the amount of data
needed to be transferred, by decreasing its granularity on the time dimension.
Most often, this is applied when querying live system metrics data using
visualization or dashboarding tools like Grafana and friends.

.. code-block:: sql

    SELECT ts_bin,
           battery_level,
           battery_status,
           battery_temperature
    FROM (
      SELECT DATE_BIN('5 minutes'::INTERVAL, "time", 0) AS ts_bin,
             battery_level,
             battery_status,
             battery_temperature,
             ROW_NUMBER() OVER (PARTITION BY DATE_BIN('5 minutes'::INTERVAL, "time", 0) ORDER BY "time" DESC) AS "row_number"
      FROM doc.sensor_readings
    ) x
    WHERE "row_number" = 1
    ORDER BY 1 ASC


.. _downsampling-lttb:

Downsampling with LTTB
======================

`Largest Triangle Three Buckets`_ is a downsampling method that tries to retain
visual similarity between the downsampled data and the original dataset using
considerably fewer data points.

The article about `advanced downsampling with the LTTB algorithm`_ explains how
to use LTTB with CrateDB. This technique is mostly used for the same purposes
like other downsampling procedures, where, in this case, retaining essential
details is important for proper visual graph analysis.

.. code-block:: sql

    WITH downsampleddata AS
      (SELECT lttb_with_parallel_arrays(
      array(SELECT n FROM demo ORDER BY n),
      array(SELECT reading FROM demo ORDER BY n), 100) AS lttb)
    SELECT unnest(lttb['0']) AS n,
           unnest(lttb['1']) AS reading
    FROM downsampleddata;


.. _rewrite-join-as-cte:

Rewrite JOINs as CTEs
=====================

The article about `using common table expressions to speed up queries`_ shares
a pattern you can use to replace JOINs with CTEs in your SQL queries, in order
to achieve consistent and faster execution times. Please note that what CTEs to
use depends on the profile of your data.

**Example**

.. code-block:: sql

    -- Uses JOINs

    SELECT SUM(quantity)
    FROM invoices
    JOIN invoice_items USING (invoice_number)
    JOIN products USING (product_id)
    WHERE product_description = 'super cool product'
    AND invoices.issue_date BETWEEN '2024-01-01' AND '2024-02-01';

.. code-block:: sql

    -- Uses CTEs

    WITH relevant_product_ids AS (
        SELECT product_id
        FROM products
        WHERE product_description = 'super cool product'
    ),
    relevant_invoice_lines AS (
        SELECT invoice_number, quantity
        FROM invoice_items
        WHERE invoice_items.product_id IN (SELECT relevant_product_ids.product_id FROM relevant_product_ids)
    ),
    relevant_invoices AS (
        SELECT invoice_number, issue_date
        FROM invoices
        WHERE invoices.invoice_number IN (SELECT relevant_invoice_lines.invoice_number FROM relevant_invoice_lines)
    )

    SELECT SUM(quantity)
    FROM relevant_invoices
    JOIN relevant_invoice_lines USING (invoice_number)
    WHERE relevant_invoices.issue_date BETWEEN '2024-01-01' AND '2024-02-01';


.. _retrieve-bulk-records-by-pks:

Retrieve individual records in bulk
===================================

The article about `retrieving records in bulk with a list of primary key values`_
shares a pattern you can use to retrieve a large number of individual records by
primary key, in order to achieve faster execution times.

Based on a very large table with a primary key made of multiple fields, and
given tens of thousands of values for these fields, we needed to retrieve all
specific records constrained by a composite primary key ``(machine_id,
sensor_type)`` in bulk.

When using a classic SQL statement, the ``WHERE`` clause easily gets too large
to be processed well, resulting in errors like ``statement is too large (stack
overflow while parsing)`` or just ``StackOverflowError[null]``.

By taking advantage of a system column called ``_id``, which exists on all
CrateDB tables, containing a compound string representation of all primary key
values of that record, and defining a staging table with primary key columns of
the same representation like the original table, you can use a sub-select to
retrieve multiple individual records from a large table efficiently.

.. code-block:: sql

    SELECT *
    FROM sensor_data
    WHERE _id IN (SELECT _id FROM relevant_pk_values);

The ``_id`` column contains a unique identifier for each record.
The useful characteristic here is that the value is deterministic: Two
individual records in different tables, with the same PK definition,
and the same PK values, will also have identical ``_id`` values.


.. _advanced downsampling with the LTTB algorithm: https://community.cratedb.com/t/advanced-downsampling-with-the-lttb-algorithm/1287
.. _down-sampling: https://web.archive.org/web/20240707050046/https://grisha.org/blog/2015/03/28/on-time-series/#downsampling
.. _Largest Triangle Three Buckets: https://github.com/sveinn-steinarsson/flot-downsample
.. _Lucene segment: https://stackoverflow.com/a/2705123
.. _normal distribution: https://en.wikipedia.org/wiki/Normal_distribution
.. _resampling time series data with DATE_BIN: https://community.cratedb.com/t/resampling-time-series-data-with-date-bin/1009
.. _retrieving records in bulk with a list of primary key values: https://community.cratedb.com/t/retrieving-records-in-bulk-with-a-list-of-primary-key-values/1721
.. _using common table expressions to speed up queries: https://community.cratedb.com/t/using-common-table-expressions-to-speed-up-queries/1719
