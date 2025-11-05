(prometheus-jmx-exporter)=

# Prometheus JMX Exporter

The [Crate JMX HTTP Exporter] is a Prometheus exporter that consumes metrics
information from CrateDB's JMX collectors and exposes them via HTTP so they can
be scraped by Prometheus, and, for example, subsequently displayed in Grafana,
or processed into Alertmanager.

:::{rubric} Setup
:::

This is very simple, on each node run the following:

```shell
cd /usr/share/crate/lib
wget https://repo1.maven.org/maven2/io/crate/crate-jmx-exporter/1.2.0/crate-jmx-exporter-1.2.0.jar
nano /etc/default/crate
```

then uncomment the `CRATE_JAVA_OPTS` line and change its value to:

```shell
# Append to existing options (preserve other flags).
CRATE_JAVA_OPTS="${CRATE_JAVA_OPTS:-} -javaagent:/usr/share/crate/lib/crate-jmx-exporter-1.2.0.jar=8080"
```

and restart the crate daemon:

```bash
systemctl restart crate
```


[Crate JMX HTTP Exporter]: https://github.com/crate/jmx_exporter
