(rsyslog-tutorial)=
# Storing server logs on CrateDB for fast search and aggregations

## Introduction

Did you know that CrateDB can be a great store for your server logs?

If you have been using log aggregation tools or even some of the most advanced commercial SIEM systems, you have probably experienced the same frustrations I have:

* timeouts when searching logs over long periods of time
* a complex and proprietary query syntax
* difficulties integrating queries on logs data into application monitoring dashboards

Storing server logs on CrateDB solves these problems, it allows to query the logs with standard SQL and from any tool supporting the PostgreSQL protocol; its unique indexing also makes full-text queries and aggregations super fast.
Let me show you an example.

## Setup

### CrateDB

First, we will need an instance of CrateDB, it may be best to have a dedicated cluster for this purpose, to separate the monitoring system from the systems being monitored, but for the purpose of this demo we can just have a single node cluster on a docker container:

```bash
sudo docker run -d --name cratedb --publish 4200:4200 --publish 5432:5432 --env CRATE_HEAP_SIZE=1g crate -Cdiscovery.type=single-node
```

Next, we need a table to store the logs, let's connect to `http://localhost:4200/#!/console` and run:

```sql
CREATE TABLE doc.systemevents (
	message TEXT
	,INDEX message_ft USING FULLTEXT(message)
	,facility INTEGER
	,fromhost TEXT
	,priority INTEGER
	,DeviceReportedTime TIMESTAMP
	,ReceivedAt TIMESTAMP
	,InfoUnitID INTEGER
	,SysLogTag TEXT	
	);
```
Tip: if you are on a headless system you can also run queries with {ref}`command-line tools <connect-cli>`.

Then we need an account for the logging system:

```sql
CREATE USER rsyslog WITH (PASSWORD='pwd123');
```

and we need to grant permissions on the table above:

```sql
GRANT DML ON TABLE doc.systemevents TO rsyslog;
```

### rsyslog

We will use [rsyslog](https://github.com/rsyslog/rsyslog) to send the logs to CrateDB, for this setup we need `rsyslog` v8.2202 or higher and the `ompgsql` module:

```bash
sudo add-apt-repository ppa:adiscon/v8-stable
sudo apt-get update
sudo apt-get install rsyslog
sudo debconf-set-selections <<< 'rsyslog-pgsql rsyslog-pgsql/dbconfig-install string false'
sudo apt-get install rsyslog-pgsql
```

Let's now configure it to use the account we created earlier:

```bash
echo 'module(load="ompgsql")' | sudo tee /etc/rsyslog.d/pgsql.conf
echo '*.* action(type="ompgsql" conninfo="postgresql://rsyslog:pwd123@localhost/doc")' | sudo tee -a /etc/rsyslog.d/pgsql.conf
sudo systemctl restart rsyslog
```

If you are interested in more advanced setups involving queuing for additional reliability in production scenarios, you can read more about available settings in the [rsyslog documentation](https://www.rsyslog.com/doc/v8-stable/tutorials/high_database_rate.html).

### MediaWiki

Now let's imagine that we want to run a container with [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) to host an intranet and we want all logs to go to CrateDB, we can just deploy this with:

```bash
sudo docker run --name mediawiki -p 80:80 -d --log-driver syslog --log-opt syslog-address=unixgram:///dev/log mediawiki
```

If we now point a web browser to port 80 at `http://localhost/`, you will see a new MediaWiki page.
Let's play around a bit to generate log entries, just click on "set up the wiki" and then once on Continue.
This will have generated entries in the `doc.systemevents` table with `syslogtag` matching the container id of the container running the site.


## Explore

We can now use the {ref}`crate-reference:predicates_match` to find the error messages we are interested in:

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

Let's now see which log sources created the most entries:

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

I hope you found this interesting. Please do not hesitate to let us know your thoughts in the [CrateDB Community](https://community.cratedb.com/).
