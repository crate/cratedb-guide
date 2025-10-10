```{highlight} bash
```

(red-hat)=

(install-rpm)=

(install-redhat)=

(install-suse)=

# CrateDB on Red Hat, SUSE, and Derivates

Install CrateDB [RPM] packages using the [DNF], [YUM], or [ZYpp] package managers.

This installation method is suitable for RedHat Enterprise Linux (RHEL) and compatible
systems like Fedora, CentOS, Rocky Linux, AlmaLinux, AWS Linux, Oracle Linux, or
Scientific Linux. Installation also works on openSUSE and SUSE Linux Enterprise Server
(SLES) systems.

## Configure package repository

To register with the CrateDB package repository, create a file called `cratedb.repo`
in the `/etc/yum.repos.d/` directory for RedHat based distributions, or in the
`/etc/zypp/repos.d/` directory for OpenSuSE based distributions, containing:

```
[cratedb-ce-stable]
name=CrateDB RPM package repository - $basearch - Stable
baseurl=https://cdn.crate.io/downloads/yum/7/$basearch
enabled=0
gpgcheck=1
gpgkey=https://cdn.crate.io/downloads/yum/RPM-GPG-KEY-crate
autorefresh=1
type=rpm-md

[cratedb-ce-testing]
name=CrateDB RPM package repository - $basearch - Testing
baseurl=https://cdn.crate.io/downloads/yum/testing/7/$basearch
enabled=0
gpgcheck=1
gpgkey=https://cdn.crate.io/downloads/yum/RPM-GPG-KEY-crate
autorefresh=1
type=rpm-md
```

:::{NOTE}
The configured repository is disabled by default. This eliminates the
possibility of accidentally upgrading CrateDB when upgrading the rest
of the system. Each install or upgrade command must explicitly enable
the repository as indicated in the sample installation command below.
:::

CrateDB provides both *stable release* and *testing release* channels. You
can read more about the [release workflow].

## Install CrateDB

With everything set up, you can install CrateDB:

```
sudo dnf install --enablerepo=cratedb-ce-stable crate
```

:::{TIP}
On older Red Hat and CentOS installations, please use the `yum` command
instead of `dnf`. On SUSE based installations, please use the `zypper`
command.
:::

## Configure CrateDB

Please visit the {ref}`install-configure` documentation section to learn
about the location and meaning of CrateDB's configuration files.

## Trust signing key

In order to trust the package signing key upfront, before being prompted
to do it on the first installation of CrateDB, you can also import it
into your repository keyring, like that:

```
# Install prerequisites.
yum install sudo

# Import the public GPG key for verifying the package signatures.
sudo rpm --import https://cdn.crate.io/downloads/yum/RPM-GPG-KEY-crate
```

:::{include} _control-linux.md
:::

:::{include} _post-install.md
:::


[dnf]: https://en.wikipedia.org/wiki/DNF_(software)
[release workflow]: https://github.com/crate/crate/blob/master/devs/docs/release.rst
[rpm]: https://en.wikipedia.org/wiki/RPM_Package_Manager
[yum]: https://en.wikipedia.org/wiki/Yum_(software)
[zypp]: https://en.wikipedia.org/wiki/ZYpp
