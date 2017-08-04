[Heroku CLI]: https://devcenter.heroku.com/articles/heroku-cli "Heroku CLI Homepage"
[AWS CLI]: http://docs.aws.amazon.com/cli/latest/userguide/installing.html "AWS CLI Install"

# Heroku

## Learn

- [Heroku Dev Center](https://devcenter.heroku.com/)
- [AWS CLI Docs](http://docs.aws.amazon.com/cli/)

## Required

- Requirements from [README.md](../README.md)
- A Heroku Account & the [Heroku CLI]
- Access to BLITZ AWS & the [AWS CLI] 

> __See:__
> 
> - [Install Heroku CLI](#install-heroku-cli)
> - [Install AWS CLI](#install-aws-cli)

## Preamble

Our boilerplate automates both the creation of a Heroku app / remote and deployments to that remote via Docker containers. This document covers the full workflow from start to finish. 

### How the deploy works

The project __Makefile__ documents much of what's happening around creating a Heroku app and pre and post deploy actions. There's a lot going on there but what it essentially boils down to is this:

1. Build a new docker image using the __Dockerfile__ in __docker/heroku/__ (the Dockerfile also runs `manage.py collectstatic`).
2. Push new image to the Heroku regisry
3. Finally, run `manage.py migrate` on newly deploy container.

### Some gotchas

* You may see `UserWarning: not reading /app/django/.env - it doesn't exist.` during the deploy, you can safely ignore this warning.
* Managing multiple Heroku apps for one project doesn't seem straight forward at first. For some help see: [Managing Multiple Remotes](#managing-multiple-remotes)

## Setup

> Repeat this process for each hosted env.

1. [Setup Heroku For Docker](#1-setup-heroku-for-docker)
2. [Create app](#2-create-app)
3. [Configure private values](#3-configure-private-values)
4. [Preflight](#4-preflight)
5. [Deploy](#5-deploy)

### 1. Setup Heroku for Docker

> [See: Heroku Container Registry & Runtime](https://devcenter.heroku.com/articles/container-registry-and-runtime)

This step is _only necessary the first time you do this for any project_.

```bash
# 1. Install container registry plugin
heroku plugins:install heroku-container-registry

# 2. Log into registry
heroku container:login
```

### 2. Create app

This step is _only necessary when your desired Heroku app does not already exist_.

```bash
# `dev` here is the default value of the GIT_REMOTE option
# Some other values you might pass here are:
#   - dev
#   - staging
#   - prod
make heroku.up GIT_REMOTE=dev
```

### 3. Configure private values

This step is _only necessary when your desired Heroku app is not already configured_. Type `heroku config` to check.

```bash
# If you do not have these ask a tech lead
heroku config:set AWS_ACCESS_KEY_ID="<key>"
heroku config:set AWS_SECRET_ACCESS_KEY="<key>"
```

### 4. Preflight

Before we hit the button:

1. Login / Open AWS Console → S3:
    + Verify your bucket exists
    + Verify the CORS config is set 
        - "Permissions" → "CORS Configuration" (tab)

2. Double check Heroku
    + `heroku info` to print info about the app
    + `heroku config` to print set config values

### 5. Deploy

```bash
# See: Makefile for exact script
# Note: Kill the running `make asset` process, 
#       and re run `make assets` after deploy
make heroku.deploy GIT_REMOTE=dev
```

> After the deploy completes successfully, type `heroku open` to open the app in your default browser.

## Troubleshooting

To see Heroku help:

```bash
heroku help
heroku help TOPIC
heroku help TOPIC:COMMAND
```

To see Heroku app logs: 

```bash
heroku logs [-r, --remote <REMOTE_NAME>] [--tail]
```

To see app info:

```bash
heroku info [-r, --remote <REMOTE_NAME>]
```

To see app config:

```bash
heroku config [-r, --remote <REMOTE_NAME>]
```

To open app in browser:

```bash
heroku open [-r, --remote <REMOTE_NAME>]
```

## Appendix

### Install Heroku CLI

1. [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. `heroku login`

### Install AWS CLI

1. [Install AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
2. [Configure AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration)
    + You'll need your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
    + Our default region is `us-west-2`
    + Set default output to `json`

### Managing multiple Remotes

>  See [this reference](https://devcenter.heroku.com/articles/multiple-environments) for more info.

When a repo points to two Heroku remotes it can be confusing which remote Heroku commands will run against. Luckily Heroku provides a simple mechanism to point it at the desired remote / application.

If we want to run a command on a specific remote (app), we can pass the `-r` or `--remote` flag:

```bash
# This flag is compatible with most commands
# For example:
heroku config:set SOME_VAR=<some-value> --remote <remote-name> 
```

Typing `-r <remote-name>` can be a bit tiring, so we can configure Git to point Heroku to a default remote.

```bash
# NOTE: This config does not affect the deploy (currently);
# since that is happening remotely on a temporary docker container.
git config heroku.remote <remote-name>
```
