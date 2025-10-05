(rsyslog-usage)=
# Store server logs on CrateDB for fast search and aggregations

## Introduction

CrateDB stores server logs efficiently and makes them easy to query.

Common pain points with traditional log stacks and SIEMs include:

* timeouts when searching across long time ranges
* proprietary, complex query syntaxes
* awkward integrations with application monitoring dashboards

CrateDB addresses these issues: query logs with standard SQL from any
PostgreSQL‑compatible tool, and use full‑text search and aggregations
backed by efficient indexes. The sections below walk through a minimal
setup.

## Setup

### CrateDB

First, start CrateDB. For production, use a dedicated cluster. For this demo, run a single‑node container:

```bash
sudo docker run -d --name cratedb -p 4200:4200 -p 5432:5432 -e CRATE_HEAP_SIZE=1g crate:latest
```

Next, create a table for logs. Open `http://localhost:4200/#!/console` or invoke `crash` and run:

```sql
CREATE TABLE doc.systemevents (
  message TEXT,
  INDEX message_ft USING FULLTEXT(message) WITH (analyzer = 'english'),
  facility INTEGER,
  fromhost TEXT,
  priority INTEGER,
  DeviceReportedTime TIMESTAMP,
  ReceivedAt TIMESTAMP,
  InfoUnitID INTEGER,
  SysLogTag TEXT
);
```
Tip: On headless systems, run queries with the {ref}`command-line tools <connect-cli>`.

Then we need an account for the logging system:

```sql
-- Use a strong secret; e.g. from a secret manager or env var.
CREATE USER rsyslog WITH (PASSWORD='pwd123');
```

and we need to grant permissions on the table above:

```sql
GRANT DML ON TABLE doc.systemevents TO rsyslog;
```

### rsyslog

We will use [rsyslog](https://github.com/rsyslog/rsyslog) to send the logs to CrateDB, for this setup we need `rsyslog` v8.2202 or higher and the `ompgsql` module:

```bash
sudo DEBIAN_FRONTEND=noninteractive apt install --yes software-properties-common
sudo add-apt-repository -y ppa:adiscon/v8-stable
sudo apt update --yes
sudo debconf-set-selections <<< 'rsyslog-pgsql rsyslog-pgsql/dbconfig-install string false'
sudo apt install --yes rsyslog rsyslog-pgsql
```

Let's now configure it to use the account we created earlier:

```bash
echo 'module(load="ompgsql")' | sudo tee /etc/rsyslog.d/pgsql.conf
echo '*.* action(type="ompgsql" conninfo="postgresql://rsyslog:pwd123@localhost/doc")' | sudo tee -a /etc/rsyslog.d/pgsql.conf
sudo chmod 640 /etc/rsyslog.d/pgsql.conf
sudo systemctl restart rsyslog
```

If you are interested in more advanced setups involving queuing for additional reliability in production scenarios, you can read more about available settings in the [rsyslog documentation](https://www.rsyslog.com/doc/v8-stable/tutorials/high_database_rate.html).

### MediaWiki

To generate logs, run a [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) container and forward its logs to rsyslog:

```bash
sudo docker run --name mediawiki -p 80:80 -d --log-driver syslog --log-opt syslog-address=unixgram:///dev/log mediawiki
```

Open `http://localhost/` to see the MediaWiki setup page.
Click “set up the wiki”, then “Continue” to generate log entries.
CrateDB now stores new rows in `doc.systemevents`, with `syslogtag` matching the container ID.


## Explore

Use {ref}`crate-reference:predicates_match` to find specific error messages:

```sql
SELECT devicereportedtime,message
FROM doc.systemevents
WHERE MATCH(message_ft, 'Could not reliably determine') USING PHRASE
ORDER BY 1 DESC;
```

```text
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| devicereportedtime | message                                                                                                                                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      1691510710000 | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.3. Set the 'ServerName' directive globally to suppress this message |
|      1691510710000 | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.3. Set the 'ServerName' directive globally to suppress this message |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

Show the top log sources by event count:

```sql
SELECT syslogtag,count(*)
FROM doc.systemevents
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
```

```text
+----------------------+----------+
| syslogtag            | count(*) |
+----------------------+----------+
| kernel:              |       23 |
| 083053ae8ea3[52134]: |       20 |
| systemd[1]:          |       15 |
| sudo:                |       10 |
| rsyslogd:            |        5 |
+----------------------+----------+
```

We hope this was useful. Share feedback and questions in the
[CrateDB Community](https://community.cratedb.com/).
