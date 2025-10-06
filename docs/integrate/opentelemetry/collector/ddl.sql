-- https://cratedb.com/docs/guide/integrate/opentelemetry/

CREATE TABLE IF NOT EXISTS "testdrive"."metrics" (
    "timestamp" TIMESTAMP,
    "labels_hash" TEXT,
    "labels" OBJECT(DYNAMIC),
    "value" DOUBLE,
    "valueRaw" LONG,
    "day__generated" TIMESTAMP GENERATED ALWAYS AS date_trunc('day', "timestamp"),
    PRIMARY KEY ("timestamp", "labels_hash", "day__generated")
)
PARTITIONED BY ("day__generated")
WITH ("number_of_replicas" = 0);
