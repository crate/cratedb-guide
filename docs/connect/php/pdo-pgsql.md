(pdo-pgsql)=

# PostgreSQL PDO

:::{div} .float-right .text-right
[![PHP PDO CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml)
:::
:::{div} .clearfix
:::

[PDO_PGSQL] is a PHP-native driver that implements the PHP Data Objects (PDO)
interface, which enables access from PHP to PostgreSQL databases. 

:::{rubric} Synopsis
:::
```php
<?php
$connection = new PDO("pgsql:host=localhost;port=5432;user=crate");
$cursor = $connection->query("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3");
print_r($cursor->fetchAll(PDO::FETCH_ASSOC));
?>
```

:::{rubric} Example
:::
- [Use the PDO_PGSQL driver with CrateDB]


[PDO_PGSQL]: https://www.php.net/manual/en/ref.pdo-pgsql.php
[Use the PDO_PGSQL driver with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/by-language/php-pdo
