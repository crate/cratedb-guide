(jmeter)=
# JMeter

```{div} .float-right .text-right
[![JMeter logo](https://jmeter.apache.org/images/logo.svg){height=60px loading=lazy}][Apache JMeter]
```
```{div} .clearfix
```

## About

[Apache JMeter] is an open-source application designed to load test functional behavior
and measure performance. It was originally designed for testing Web Applications but
has since expanded to other test functions. 

## Configure

Follow the documentation about building a [JMeter Database Test Plan],
this basically works out of the box.

Make sure you added the [PostgreSQL JDBC Driver] to your JMeter `./lib`
folder. Use default settings for your JDBC Connection Configuration
with Database URL `jdbc:postgresql://your.cratedb.cluster:5432/doc`,
JDBC Driver class `org.postgresql.Driver` and correct username and
password.


[Apache JMeter]: https://jmeter.apache.org/
[JMeter Database Test Plan]: https://jmeter.apache.org/usermanual/build-db-test-plan.html
[PostgreSQL JDBC Driver]: https://jdbc.postgresql.org
