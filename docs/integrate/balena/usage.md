(balena-usage)=
# Deploying CrateDB on balena\.io

[Balena] provides a complete set of tools to build, deploy, and manage fleets of
connected IoT devices. It lets fleet owners focus on their applications and
growth with minimal friction.

The tools work well together as a platform, and you can also pick only the
components you need and adapt them to your use case. This usage guide
shows how to integrate CrateDB with Balena and run it on a Raspberry Pi 4
(ARM) or a generic x86_64 device.

## Requirements

To deploy CrateDB on Balena and run it on an IoT device, you need:

Hardware:
*   Raspberry Pi 4 or other ARM/x86 device
*   microSD card
*   Power supply and Wi‑Fi

Software:
*   balenaCloud account: [Create an account](https://dashboard.balena-cloud.com/)
*   [balenaEtcher](https://www.balena.io/etcher/)

## Deploy the code

There are two ways to deploy to a [balenaCloud] fleet: via [balena Deploy] or via
the [balena CLI].

To use balena Deploy, click the button:

[![Deploy with balena button](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/aea351a7522cd74ffa5739b602868f77eadb77c3.png)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/mpous/crate-balena)

This usage guide shows how to deploy CrateDB with the balena CLI. For details, see
[https://balena.io](https://balena.io).

Follow these steps to create a new fleet and add a device:
1.  Click `Create Fleet`
    *   Name your fleet
    *   Set Device type -> `Raspberry Pi 4`
    *   Set Application type -> `Starter`
    *   Click `Create new fleet`

2.  Open the fleet and click `Add device`

    *   Set Device type -> `Raspberry Pi 4`
    *   Select the recommended version
    *   Set edition -> `Development` (recommended for first‑time users)
    *   Set Network Connection: `Wi‑Fi + Ethernet`
        *   Set your Wi-Fi SSID
        *   Set your Wi-Fi password

You are ready to explore CrateDB. Check our other usage guides to continue.

1.  Log in to your balenaCloud account: `balena login`

2.  Clone the [code repository](https://github.com/mpous/crate-balena) to your workspace

3.  Deploy the code to your device with: `balena push <application-name>`

Now your device is getting updated on [balenaCloud] and you are set up to run
CrateDB on your Raspberry Pi.

![balenaCloud](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/8093d77b578e5847bc6927e33f277426dee90941.png "balenaCloud")

## Running CrateDB on Raspberry Pi

In balenaCloud, click your device, open `Host OS Terminal`, and run:

```shell
sysctl -w vm.max_map_count=262144
```

This command increases `vm.max_map_count` (the maximum number of VMAs per process).
The default is usually 65536. Set it to 262144 for CrateDB to start reliably with
memory‑mapped files.

:::{note}
This change is temporary and resets on reboot. To persist it on balenaOS,
configure it via a host sysctl drop‑in or an appropriate balena host
configuration/label.
:::

At this point, on the balenaCloud `Logs` component running CrateDB starts
correctly. To start using CrateDB, in the Terminal window choose `cratedb`
and then `Start terminal session`:

![Start a terminal session for CrateDB](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/a1707d53a3dc2858b9aa5ffc3023786c3d48ee1a.png){height=480}

## Use the CLI

At this point, we recommend installing Crash CLI to start working with CrateDB.
The installation instructions on how to install Crash can be found
{ref}`here <crate-crash:getting-started>`.

Start Crash with:
```shell
./crash
```

Add `--verbose` for more detail or when troubleshooting connection issues.

## Open the Admin UI

Alternatively, access the CrateDB Admin UI from your workstation:

* If you are in a terminal on the device or service container, open `http://localhost:4200`.
* From your workstation, use the device’s local IP (e.g., `http://<device-ip>:4200`)
  or enable a balena Public URL/port mapping as appropriate.

![CrateDB Admin UI](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/08b793f31ed21a49509dc3182cc1795e8b190474.jpeg)

Now, you are ready to explore CrateDB. Check our other usage guides for a
successful start.


[balena]: https://balena.io
[balena CLI]: https://www.balena.io/docs/reference/balena-cli/
[balenaCloud]: https://www.balena.io/cloud
[balena Deploy]: https://www.balena.io/docs/learn/deploy/deploy-with-balena-button/
