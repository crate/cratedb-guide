(crate-dbal)=

# CrateDB DBAL

:::{div} .float-right .text-right
[![crate-dbal CI](https://github.com/crate/crate-dbal/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/crate-dbal/actions/workflows/tests.yml)
:::
:::{div} .clearfix
:::

DBAL is a PHP database abstraction layer that comes with database schema
introspection, schema management, and PDO support.
The `crate/crate-dbal` package implements this specification,
wrapping access to CrateDB's HTTP interface.

:::{rubric} Install
:::

```shell
composer require crate/crate-dbal
```

:::{rubric} Synopsis
:::

```php
<?php
require 'vendor/autoload.php';

$params = array(
    'driverClass' => 'Crate\DBAL\Driver\PDOCrate\Driver',
    'user' => 'admin',
    'password' => '<PASSWORD>',
    'host' => '<name-of-your-cluster>.cratedb.net',
    'port' => 4200
);

$connection = \Doctrine\DBAL\DriverManager::getConnection($params);
$sql = "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3";
$result = $connection->query($sql)->fetch();

print_r($result);
?>
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: crate-dbal:index
:link-type: ref
:link-alt: crate/crate-dbal documentation
The full documentation for crate/crate-dbal.
::::

:::::
