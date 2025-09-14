(balena-tutorial)=
# Deploying CrateDB on balena\.io

Balena is a complete set of tools for building, deploying and managing fleets of connected IoT devices. Balena provides infrastructure for fleet owners so they can focus on developing their applications and growing their fleets with as little friction as possible.

The tools are designed to work well together as a platform, but the user can also pick and choose the components you need for your project, and adapt them to your particular use case. In this short tutorial, we will show how you can integrate CrateDB as a component to [http://balena.io](http://balena.io) and run it on an ARM device such as Raspberry Pi 4 or x86 generic 64 bits device.

## Requirements

To deploy CrateDB on [http://balena.io](http://balena.io) and run it on IoT device you would need the following:

Hardware:
*   Raspberry Pi 4 or other ARM/x86 device
*   SD card
*   Power supply and WiFi

Software:
*   BalenaCloud account: please sign up [here](https://dashboard.balena-cloud.com/)
*   [BalenaEtcher](https://www.balena.io/etcher/)

## Deploy the code
There are two ways to deploy the code to a balenaCloud application: via [Balena Deploy](https://www.balena.io/docs/learn/deploy/deploy-with-balena-button/) and via [Balena CLI](https://www.balena.io/docs/reference/balena-cli/).

To use Balena Deploy just click on the deploy button below:

[![deploy-with-balena|331x66](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/aea351a7522cd74ffa5739b602868f77eadb77c3.png)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/mpous/crate-balena)

In this tutorial, we will show how to deploy CrateDB with Balena CLI. If you want to learn more please check the balena website [http://balena.io](http://balena.io).

Follow the next steps to create a new application and add a device:
1.  Click -> `Create Fleet`
    *   Put any name for your application
    *   Set Device type -> `Raspberry Pi 4`
    *   Set Application type -> `Starter`
    *   Click -> `Create new fleet`

2.  Open Fleet and Click -> `Add device`

    *   Set Device type -> `Raspberry Pi 4`
    *   Select the recommended version
    *   Set edition -> `Development` (recommended for first time users)
    *   Set Network Connection: `Wifi+Ethernet`
        *   Set your Wifi SSID
        *   Set your Wifi Password

Now, you can deploy the code to your device with the following steps:

1.  Login to balenaCloud account via CLI command: `balena login`

2.  Clone [this GitHub repository](https://github.com/mpous/crate-balena) to your local workspace

3.  Deploy the code to your device with: `balena push <application-name>`

Now your device is getting updated on balenaCloud and you are set up to run CrateDB on your Raspberry Pi!

![balenaCloud](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/8093d77b578e5847bc6927e33f277426dee90941.png "balenaCloud")

## Running CrateDB on Raspberry Pi

In balenaCloud click on your device, open `HostOS Terminal` and type:

`sysctl -w vm.max_map_count=212144`

This command increments `max_map_count` which is the maximum number of memory map areas a process may have of your container. It's by default 65536 as most of the applications need less than a thousand maps.

At this point, on the balenaCloud `Logs` component running CrateDB starts correctly. To start using CrateDB, in the Terminal window choose cratedb and then > Start terminal session:

![6bafe805-d24b-4da3-b138-b7d85a67fea7|501x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/a1707d53a3dc2858b9aa5ffc3023786c3d48ee1a.png){height=480}

At this point, we recommend installing Crash CLI to start working with CrateDB. The installation instructions on how to install Crash can be found {ref}`here <crate-crash:getting-started>`. To start Crash, use the following command:

`./crash`

Add `--verbose` in case you want to know more, or you get a connection error.

### Access to the Admin UI
Alternatively, you might want to access CrateDB Admin UI. Typing `"http://localhost:4200"` in your browser opens the Admin UI:

![Screenshot 2022-03-29 at 11.05.37|690x352](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/08b793f31ed21a49509dc3182cc1795e8b190474.jpeg)

Now, you are ready to explore CrateDB! Check our other tutorials for a successful start :slight_smile:
