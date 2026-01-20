(debian)=
(ubuntu)=
(install-deb)=
(install-debian)=
(install-ubuntu)=

# CrateDB on Debian, Ubuntu, and Derivatives

:::{div} sd-text-muted
Install CrateDB [deb] packages using the [apt] package manager.
:::

This installation method is suitable for Debian systems and derivatives
like Ubuntu.

::::::{stepper}
:::::{step} Configure package repository
Configure your system to register with and trust packages from
the CrateDB package repository:

```shell
# Install prerequisites.
sudo apt update
sudo apt install --yes curl gnupg procps

# Import the public GPG key for verifying the package signatures.
curl -sS https://cdn.crate.io/downloads/debian/DEB-GPG-KEY-crate | \
    gpg --dearmor | sudo tee /usr/share/keyrings/cratedb.gpg >/dev/null

# Add CrateDB repository to Apt
echo "deb [signed-by=/usr/share/keyrings/cratedb.gpg] https://cdn.crate.io/downloads/debian/stable/ default main" | \
    sudo tee /etc/apt/sources.list.d/crate-stable.list
```

:::{NOTE}
CrateDB provides two repositories. A *stable* and a *testing* repository. To use
the testing repository, replace `stable` with `testing` in the command
above. You can read more about our [release workflow].
:::

Now, update the package sources:

```shell
sh$ sudo apt update
```

You should see a success message. This indicates that the CrateDB package
repository is correctly registered.
:::::

:::::{step} Install CrateDB
With everything set up, you can install CrateDB:

```shell
sh$ sudo apt install --yes crate
```

After the installation is finished, you can start the `crate` service:

```shell
sh$ sudo systemctl start crate
```

Once the service is up and running, you can access CrateDB by visiting:

```text
http://localhost:4200/
```
:::::

:::::{step} Configure CrateDB
Please visit the {ref}`install-configure` documentation section to learn
about the location and meaning of CrateDB's configuration files.
:::::
::::::

:::{include} _control-linux.md
:::

:::{include} _post-install.md
:::


[apt]: https://en.wikipedia.org/wiki/APT_(software)
[deb]: https://en.wikipedia.org/wiki/Deb_(file_format)
[release workflow]: https://github.com/crate/crate/blob/master/devs/docs/release.rst
