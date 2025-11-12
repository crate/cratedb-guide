(amphp)=

# AMPHP PostgreSQL

:::{div} .float-right .text-right
[![PHP AMPHP CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml)
:::
:::{div} .clearfix
:::

The [AMPHP PostgreSQL driver], `amphp/postgres`, is an asynchronous
PostgreSQL client based on Amp.

:::{rubric} Synopsis
:::
```php
<?php
require 'vendor/autoload.php';

use Amp\Postgres\PostgresConfig;
use Amp\Postgres\PostgresConnectionPool;
use function Amp\async;
use function Amp\Future\await;

await(async(function () {
    $config = PostgresConfig::fromString("host=localhost user=crate");
    $pool = new PostgresConnectionPool($config);
    $statement = $pool->prepare("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3");
    $result = $statement->execute();
    foreach ($result as $row) {
        print_r($row);
    }
}));
?>
```
:::{rubric} Example
:::
- [Connect to CrateDB and CrateDB Cloud using AMPHP/PostgreSQL]


[AMPHP PostgreSQL driver]: https://github.com/amphp/postgres
[Connect to CrateDB and CrateDB Cloud using AMPHP/PostgreSQL]: https://github.com/crate/cratedb-examples/tree/main/by-language/php-amphp
