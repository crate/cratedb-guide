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
    'postgresql://crate:crate@localhost:5432/?sslmode=disable'
  );

  final result = await conn.execute("SELECT mountain, region, height FROM sys.summits ORDER BY height DESC LIMIT 3");
  print(result);

  await conn.close();
}
```

:::{include} ../_cratedb.md
:::
```shell
dart --disable-analytics
dart pub get
dart example.dart
```

:::{rubric} SSL connection
:::

Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```dart
final conn = await Connection.openFromUrl(
  'postgresql://admin:password@testcluster.cratedb.net:5432/?sslmode=require'
);
```


[postgres]: https://pub.dev/packages/postgres
