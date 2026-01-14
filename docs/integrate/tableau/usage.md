(tableau-usage)=
# Using CrateDB with Tableau

For using Tableau with CrateDB, install the latest PostgreSQL driver, as detailed in the steps below.

1. Download the Java 8 JDBC driver (e.g. `postgresql-42.7.1.jar` or newer) from https://jdbc.postgresql.org/download/. 
2. Move the downloaded `.jar`-file (e.g. `postgresql-42.7.1.jar`) into the Tableau Driver folder.
    > * **Windows**: `C:\Program Files\Tableau\Drivers`
    > * **Mac**: `~/Library/Tableau/Drivers`
    > * **Linux**: `/opt/tableau/tableau_driver/jdbc`
3. Open Tableau.
4. Create a `PostgreSQL` connection.

   ![image|454x500, 75%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/c/cf27bb4288737b66d2af620092f529f481dbe328.jpeg){height=500px}
5. Start using Tableau with CrateDB.

## Using Tableau with CrateDB 5.1 and earlier
::::{dropdown} **Details**

As of CrateDB 5.0.0 there are still some features missing to directly
use the default PostgreSQL Connector in CrateDB (e.g. `DECLARE CURSOR` support).
Therefore, it is best to use a `Other Databases (JDBC)` connection with the
latest PostgreSQL JDBC Driver. To improve the user experience Tableau allows
to customize connections using `.tdc` (Tableau Datasource Customization) files.

If we see significant demand, we might look into creating a custom Tableau Connector,
however we also expect CrateDB to be fully compatible with the default PostgreSQL
Connector soon.

## Customize CrateDB Connection

1. Download the [latest PostgreSQL JDBC Driver](https://jdbc.postgresql.org/download/)
2. Move the downloaded `.jar`-file (e.g. `postgresql-42.4.1.jar`) into the Tableau Driver folder
    > * **Windows**: `C:\Program Files\Tableau\Drivers`
    > * **Mac**: `~/Library/Tableau/Drivers`
    > * **Linux**: `/opt/tableau/tableau_driver/jdbc`
    >
    > *also see https://help.tableau.com/current/pro/desktop/en-us/examples_otherdatabases_jdbc.htm*
3. Create an empty [.tdc](https://help.tableau.com/current/pro/desktop/en-us/connect_customize.htm) (Tableau Datasource Customization) file e.g. `crate-jdbc.tdc`
4. Copy the following content into the file:
    ```xml
    <connection-customization class='genericjdbc' enabled='true' version='10.0'>
        <vendor name='genericjdbc' />
        <driver name='postgresql' />
        <customizations>
            <customization name='CAP_CONNECT_STORED_PROCEDURE' value='no'/>
            <customization name='CAP_CREATE_TEMP_TABLES' value='no'/>
            <customization name='CAP_FAST_METADATA' value='yes'/>
            <customization name="CAP_FORCE_COUNT_FOR_NUMBEROFRECORDS" value="yes"/>
            <customization name='CAP_JDBC_QUERY_ASYNC' value='yes'/>
            <customization name='CAP_JDBC_QUERY_CANCEL' value='yes'/>
            <customization name='CAP_QUERY_HAVING_REQUIRES_GROUP_BY' value='no'/>
            <customization name="CAP_QUERY_SUBQUERIES_WITH_TOP" value="yes"/>
            <customization name="CAP_QUERY_TOP_N" value="yes"/>
            <customization name='CAP_QUERY_TOPSTYLE_LIMIT' value='yes'/>
            <customization name='CAP_SELECT_INTO' value='no'/>
            <customization name='CAP_SUPPRESS_TEMP_TABLE_CHECKS' value='yes'/>
        </customizations>
    </connection-customization> 
    ```
5. Save the `.tdc-file` in your `Datasources` folder (e.g. `/Users/<username>/Documents/My Tableau Repository/Datasources/crate-jdbc.tdc`
6. Open Tableau
7. Create an `Other Databases (JDBC)` connection
    > **URL**: jdbc:postgresql://localhost:5432/doc
    > **Dialect**: PostgreSQL
    > **Username**: crate
    > **Password**:
8. Start using Tableau with CrateDB :)

::::
