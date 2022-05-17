Put.io Command Line Client
=

[![Build status](https://ci-central.openfunction.co/api/projects/status/p6kqvkte9o2m6qab?svg=true)](https://ci-central.openfunction.co/project/AppVeyor/pyputio-cli)
[![PyPI version](https://badge.fury.io/py/pyputio.svg)](https://badge.fury.io/py/pyputio)

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
`
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

To remove archives after download and extraction, set `PUTIO_CLEAN` to 1. 

Environment Reference
---

The following environment variables can be set to assist usage as well. Details on use of options follow in other sections

| Option            | Description                                                                                      | Value                          |
|-------------------|--------------------------------------------------------------------------------------------------|--------------------------------|
| PUTIO_CLEAN       | Removes archive after extraction                                                                 | IfPresent                      |
| PUTIO_DIR_CREATE  | Creates subdirectories if they do not exist in library path                                      | IfPresent                      |
| PUTIO_REPORT_TIME | Reports download and extract stats and info upon completion                                      | IfPresent                      |
| PUTIO_MANUAL_DL   | Downloads using shell rather than Python client                                                  | IfPresent                      |
| PUTIO_OUTPUT_MODE | Download/Extraction Detail verbosity                                                             | progress \|\| silent \|\| json |
| PUTIO_NOTIFY      | Push notifications (Requires PUSHOVER_TOKEN and PUSHOVER_USER)                                   | IfPresent                      |
| PUTIO_PLEX_UPDATE | Runs plex content scan upon completion (requires PLEX_SERVER_NAME, PLEX_USERNAME, PLEX_PASSWORD) | IfPresent                      |

Output Formats
---

Output format can be controlled using, either, the `-o` flag, or the `PUTIO_OUTPUT_MODE` environment variable, set to either default, `json` (which returns only a json object about the completed job), `progress` (which returns only the download progress), and `silent` (no output).

Integrations
---

The following are integrations available for this tool.

### Pushover

If you use [pushover](pushover.net), set `PUSHOVER_TOKEN` and `PUSHOVER_USER` in your environment, and to have completed jobs send a notification, set `--notify` to any value, or `PUTIO_NOTIFY` to any value. 

### Plex Media Server

Using the `PUTIO_PLEX_UPDATE` environment variable (set to anything not `None`), will trigger an update to your library to check for new content after downloading if the target directory from your `putio` run is mapped to a Plex library. Leaving `-s` off of your CLI command, or `library_subpath` unset in your config, or the `PUTIO_LIBRARY_SUBPATH` environment variable unset, at `putio` run time will show you your available Plex libraries, before showing you the local files in your `PUTIO_LIBRARY_PATH` content root. 

This requires that `PLEX_USERNAME`, `PLEX_PASSWORD`, and `PLEX_SERVER_NAME` (the friendly name that shows up in the UI for your server, not the hostname/IP of the server itself) be set in your environment.

If you just want to run an update, without a download, this package also installs `plex-scan`, which does not return anything after requesting the update from the Plex server.