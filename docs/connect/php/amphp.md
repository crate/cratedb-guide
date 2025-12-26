(amphp)=

# AMPHP PostgreSQL

:::{div} .float-right .text-right
[![PHP AMPHP CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml)
:::
:::{div} .clearfix
:::

The AMPHP PostgreSQL driver, `amphp/postgres`, is an asynchronous
PostgreSQL client based on Amp.


:::{rubric} Install
:::

```shell
composer require amphp/postgres
```

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

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://github.com/amphp/postgres
:link-type: url
:link-alt: amphp/postgres documentation
The full documentation for amphp/postgres.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/php-amphp
:link-type: url
:link-alt: amphp/postgres example
An executable example using the amphp/postgres driver.
::::

:::::
