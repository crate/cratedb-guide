# Control CrateDB on Linux

You can control the `crate` service with the `systemctl` utility program:

```
sudo systemctl COMMAND crate
```

Replace `COMMAND` with `start`, `stop`, `restart`, `status` and
so on.

# Notes

After the installation is finished, the `crate` service should be installed,
but may not be configured to start automatically. Use the following command to
start CrateDB:

```
sudo systemctl start crate
```

In order to make the service reboot-safe, invoke:

```
sudo systemctl enable crate
```
