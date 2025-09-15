(create-user)=
# Create User

This part of the documentation sheds some light on the topics of
[](inv:crate-reference#administration_user_management) and
[](inv:crate-reference#administration-privileges).


## Superuser Account

CrateDB ships with a superuser account called "`crate`", which has the
privileges to perform any action.

However, with the default configuration, this superuser can only access
CrateDB from the local machine CrateDB has been installed on. If you are
trying to connect from another machine, you are prompted to enter a
username and password.


## `CREATE USER` command

In order to create a user that can be used to authenticate from a remote
machine, first {ref}`install the CrateDB shell <crate-crash:getting-started>`
or {ref}`connect <connect>` with other tools on the same machine you installed
CrateDB on. Then, connect to CrateDB running on `localhost`.

While you can also perform the steps outlined below within
[](inv:crate-admin-ui:*:label#index) itself, the
walkthrough will outline how to do it using the
[](inv:crate-crash:*:label#index) on the command line.

Invoke Crash within the terminal of your choice.

```console
sh$ crash
```

Add your first user with a secure password to the database:

```sql
cr> CREATE USER username WITH (password = 'a_secret_password');
```

Grant all privileges to the newly created user:

```sql
cr> GRANT ALL PRIVILEGES TO username;
```

![image](/_assets/img/getting-started/create-user.png){width=640px}

Now try navigating to the [](inv:crate-admin-ui:*:label#index) in your
browser. In the URL below, please replace `cratedb.example.org` with
the host name or IP address of the machine CrateDB is running on, and
sign in with your newly created user account.

    http://cratedb.example.org:4200/

After creating the user and granting all privileges, you should be able
to continue with [the guided tour](#use), connecting to CrateDB from a
remote machine.
