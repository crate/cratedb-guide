(jmeter)=
# JMeter

```{div} .float-right .text-right
[![JMeter logo](https://jmeter.apache.org/images/logo.svg){height=60px loading=lazy}][Apache JMeter]
```
```{div} .clearfix
```

## About

[Apache JMeter] is an open‑source load‑testing tool for measuring functional
behavior and performance. It started with web apps and now supports many
protocols and back ends.

## Configure

Start with the official guide to building a [JMeter Database Test Plan].
Then add to your Test Plan:

- Thread Group
- JDBC Connection Configuration
- JDBC Request (your SQL)

Most defaults work out of the box.

Add the [PostgreSQL JDBC Driver] JAR to JMeter’s `./lib` folder.
Configure JDBC Connection Configuration with:

- JDBC URL: `jdbc:postgresql://YOUR_HOST:5432/crate?currentSchema=doc`
  - Append `&sslmode=require` if your cluster enforces TLS.
- Driver class: `org.postgresql.Driver`
- Username/Password: use a dedicated, least‑privileged user for load tests.
- Max connections: size ≥ total JMeter threads.


[Apache JMeter]: https://jmeter.apache.org/
[JMeter Database Test Plan]: https://jmeter.apache.org/usermanual/build-db-test-plan.html
[PostgreSQL JDBC Driver]: https://jdbc.postgresql.org
