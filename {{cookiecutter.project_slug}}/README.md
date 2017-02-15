[Docker for Mac]: http://example.com/  "Download Docker for Mac"
[Docker for Windows]: http://example.com/  "Download Docker for Windows"
[BLITZ DockerHub]: https://hub.docker.com/u/blitzagency/ "BLITZ DockerHub"
[Node & Npm]: https://nodejs.org/en/download/ "Intsall Node"
[Homebrew]: http://brew.sh/ "Homebrew Homepage"

# Django Template

## Required

- Access to [BLITZ DockerHub]
- [Docker for Mac] __or__ [Docker for Windows]
- [Node & Npm]
    - Must be installed locally;
    - [OSX] `brew install node` (requires [Homebrew])

## Contribute

- [See CONTRIBUTING.md](./CONTRIBUTING.md)

## Setup

```bash
# From a terminal run
# After running this, you may need to fill out required settings
cp django/env.dist django/.env

make up
make init
make serve

# From another terminal run
make assets
```

> Site is available at <http://localhost:8000>, <http://docker.local:8000> (requires etc/hosts entry).

## Start

```bash
# From a terminal run
make up
make serve

# From another terminal run
make assets
```

> Site is available at <http://localhost:8000>, <http://docker.local:8000> (requires etc/hosts entry).

## Docker setup for windows:

Install [Docker for Windows]:

*__NOTE__: you must have Windows 10 Pro with Hyper-V enabled, otherwise you will
need to use docker-toolbox and another virtualization software like VMWare Fusion.*

*__NOTE 2__: you must have make installed on Windows, and ensure that you have an alias in your powershell profile that points to the proper make.exe.*

Syncing Files:
- After installed, right click the small docker icon in the system tray
- Choose settings
- Choose Shared Drives
- Click your C drive (or whatever drive your project is on)
- Click Apply
- Enter your credentials (if prompted)

Make sure you have an active dockerhub account

- cd into project root
- GitBash/Powershell Window:

```
$ docker login
$ make up
```

All other steps are the same as above after this point.

## Test

```bash
# Run Python / Django test suite
make test.py

# Run Javascript test suite
make test.js
```

## Automate

```bash
# To see latest help message run
make help
```
