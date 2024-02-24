==================
Select performance
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



.. _down-sampling: https://grisha.org/blog/2015/03/28/on-time-series/#downsampling
.. _Lucene segment: https://stackoverflow.com/a/2705123
.. _normal distribution: https://en.wikipedia.org/wiki/Normal_distribution
.. _using common table expressions to speed up queries: https://community.cratedb.com/t/using-common-table-expressions-to-speed-up-queries/1719
