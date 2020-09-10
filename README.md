Put.io Command Line Client
=

[![Build Status](https://cloud.drone.io/api/badges/jmarhee/pyputio-cli/status.svg)](https://cloud.drone.io/jmarhee/pyputio-cli)

This package installs the `putio` command-line client.

Setup
--

Clone this repo, and install:

```bash
pip3 install -e .
```

Either set environment variables:

```bash
export PUTIO_USER=your_user
export PUTIO_PASS="your_password"
export PUTIO_LIBRARY_PATH=/mnt/Plex
export PUTIO_LIBRARY_SUBPATH=Movies #i.e. (the name of the subdir: Movies, TV, etc.)
```

for example, or set `PUTIO_CONFIG_PATH` to the configuration in the following format:

```toml
[putio_config]
username = your_username
password = your_password
library_path = /mnt/Plex
```
and loading this configuration:

```bash
putio --config config.ini --url ""
```

or, using the command line flags to set these options credentials:

```bash
putio --username "" --password "" --library_path "/mnt/target" --library_subpath "Music" --url ""
```

and set `PUTIO_LIBRARY_SUBPATH`, or reply when prompted. If required values are not set using the above, you will be prompted for them. 

You can set `PUTIO_CLEAN` to any value to have it clean up the zip archives after the download attempt.

Usage
---

Once installed, run:

```bash
putio "URL"
```

using the "Zip and Download" option on the Put.io UI. 

If you wish to delete the zip archive after unarchiving is completed, set `PUTIO_CLEAN` to any value.
