(connect-dart)=

# Dart

:::{div} sd-text-muted
Connect to CrateDB from Dart applications.
:::

:::{rubric} About
:::

[postgres] is a library for connecting to and querying PostgreSQL databases.

:::{rubric} Synopsis
:::

`pubspec.yaml`
```yaml
name: cratedb_demo

dependencies:
  postgres: '^3.0.0'

environment:
  sdk: '^3.9.0'
```

`example.dart`
```dart
library;

import 'package:postgres/postgres.dart';

void main() async {

  final conn = await Connection.openFromUrl(
    'postgresql://crate:crate@localhost:5432/doc?sslmode=disable'
  );

  final result = await conn.execute("SELECT mountain, region, height FROM sys.summits ORDER BY height DESC LIMIT 3");
  print(result);

  await conn.close();
}

```
Start CrateDB using Docker or Podman, then compile and invoke example program.
```shell
docker run --rm --publish=5432:5432 crate -Cdiscovery.type=single-node
```
```shell
dart --disable-analytics
dart pub get
dart example.dart
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use the `sslmode=require`
parameter, and replace username, password, and hostname with values matching
your environment.
```dart
final conn = await Connection.openFromUrl(
  'postgresql://admin:password@testcluster.cratedb.net:5432/doc?sslmode=require'
);
```


[postgres]: https://pub.dev/packages/postgres
