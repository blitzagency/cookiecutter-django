[Docker for Mac]: http://example.com/  "Download Docker for Mac"
[Docker for Windows]: http://example.com/  "Download Docker for Windows"
[Docker Hub]: https://hub.docker.com/ "Docker Hub Homepage"
[BLITZ DockerHub]: https://hub.docker.com/u/blitzagency/ "BLITZ DockerHub"
[Node & Npm]: https://nodejs.org/en/download/ "Intsall Node"
[Homebrew]: http://brew.sh/ "Homebrew Homepage"

# {{ cookiecutter.project_name }}

## Required

- [Docker Hub] account
- [BLITZ DockerHub] Access
- [Docker for Mac] __or__ [Docker for Windows]
- [Node & Npm]
    - Must be installed locally;
    - [OSX] `brew install node` (requires [Homebrew])

## Contribute

- [See CONTRIBUTING.md](./CONTRIBUTING.md)

## Setup

> If you're running __Windows__, please first read [Initial Setup For Windows](./docs/windows-setup.md).

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
