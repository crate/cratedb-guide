(odbc-visualbasic)=

# ODBC with Visual Basic

:::{rubric} About
:::

Use ADODB to access data from your Visual Basic applications.

:::{rubric} Install
:::

:::{include} /connect/odbc/install-dropdown.md
:::

:::{rubric} Synopsis
:::

`example.vb`
```visualbasic
Dim cn as New ADODB.Connection
Dim rs as New ADODB.Recordset

'Connect to database
cn.Open "Dsn=<MyDataSourceName>;" & _
        "Server=localhost;" & _
        "Port=5432;" & _
        "Uid=crate;" & _
        "Pwd=crate;" & _
        "MaxVarcharSize=1073741824;"

'Invoke query
rs.Open "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 5", cn

'Display results
While Not rs.EOF
  Debug.Print rs!mountain & ": " & rs!height
  rs.MoveNext
Wend

'Clean up
rs.Close
cn.Close
```

:::{seealso}
Example: [psqlODBC with Visual Basic].
:::


[psqlODBC with Visual Basic]: https://odbc.postgresql.org/howto-vb.html
