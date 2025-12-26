(pdo-pgsql)=

# PostgreSQL PDO

:::{div} .float-right .text-right
[![PHP PDO CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml)
:::
:::{div} .clearfix
:::

PDO_PGSQL is a PHP-native driver that implements the PHP Data Objects (PDO)
interface, which enables access from PHP to PostgreSQL databases. 

:::{rubric} Install
:::

The module is mostly built into PHP itself.

:::{rubric} Synopsis
:::
```php
<?php
$connection = new PDO("pgsql:host=localhost;port=5432;user=crate");
$cursor = $connection->query("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3");
print_r($cursor->fetchAll(PDO::FETCH_ASSOC));
?>
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://www.php.net/manual/en/ref.pdo-pgsql.php
:link-type: url
:link-alt: PDO_PGSQL documentation
The full documentation for PDO_PGSQL.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/php-pdo
:link-type: url
:link-alt: PDO_PGSQL example
An executable example using the PDO_PGSQL driver.
::::

:::::
