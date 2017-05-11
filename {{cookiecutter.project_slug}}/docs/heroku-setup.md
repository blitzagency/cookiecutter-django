[Heroku CLI]: https://devcenter.heroku.com/articles/heroku-cli "Heroku CLI Homepage"
[AWS CLI]: http://docs.aws.amazon.com/cli/latest/userguide/installing.html "AWS CLI Install"

# Heroku Setup Guide

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

This document covers the setup for the automated version of a Heroku deploy process for this cookiecutter template. 

### How the deploy works

When a user runs the deploy target in the [__Makefile__](../Makefile)

1. Build static assets using Webpack (_this compile will break local assets until you recompile!_)
2. Spin up an instance of [__this docker container__](https://github.com/dinopetrone/docker-heroku)
3. Run __Fabric__ commands that:
    1. Deploys static media (`manage.py collectstatic`)
    2. Deploys maintenance pages
    3. Deploys source
    4. Migrates the DB
    5. Clears Django cache

### Some gotchas

1. The [__Procfile__](../Procfile) is located at the project root
2. This setup does not require an [__app.json__](https://devcenter.heroku.com/articles/app-json-schema)
3. [__app_info.json__](../django/app_info.json) configures the deploy scripts (It's worth looking at)
4. You may see `UserWarning: not reading /app/django/.env - it doesn't exist.` during the deploy, you can safely ignore this warning.
5. Things get weird for a minute when you've configured more than one remote; see [Managing Multiple Remotes](#managing-multiple-remotes)

## Setup

> Repeat this process for each hosted env.

1. [Create app](#1-create-app)
2. [Configure app](#2-configure-app)
3. [Create S3 bucket](#3-create-s3-bucket)
4. [Preflight](#4-preflight)
5. [Deploy](#5-deploy)

### 1. Create app

> Take a look at `django/app-info.json` for the `<app-name>` you'll need for this step (if the generated name has any underscores convert them into hyphens).

```bash
# -r, --remote
# This automatically names the heroku remote 
# (default remote name is heroku, which isn't that useful)
heroku create <app-name> -r <remote-name>
heroku addons:create heroku-postgresql:hobby-dev
```

### 2. Configure app

```bash
heroku config:set DJANGO_SETTINGS_MODULE=app.config.settings.prod
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set PYTHONPATH=/app/django/project:/app/django/project/vendor
heroku config:set USE_HTTPS_FOR_ASSETS=1

# This refers to the Django SECRET_KEY setting
# NOTE: Do not use existing SECRET_KEY(s) in env.dist or local.py
#       To generate one see Generate `SECRET_KEY` in the appendix
heroku config:set SECRET_KEY="<key>"

# If you do not have these ask a tech lead
heroku config:set AWS_ACCESS_KEY_ID="<key>"
heroku config:set AWS_SECRET_ACCESS_KEY="<key>"
```

### 3. Create S3 bucket

The S3 bucket will host our static assets. Follow this format when creating a bucket name: `com-<site-name>-<env-name>`, for example: `com-my-site-staging`.


First pull down a boilerplate CORS file setup for Heroku:

```bash
# Get a boilerplate cors.json to configure the s3 bucket
wget -O cors.json http://bit.ly/blitzherokus3cors
```

Now we can create the bucket:

```bash
# Create the bucket
aws s3api create-bucket --bucket <bucket-name>

# Add the CORS config file to the bucket permissions
# Yes you have to use the file:// protocol (/shrug...)
aws s3api put-bucket-cors  --bucket <bucket-name> --cors-configuration file://cors.json

# Let's set some related config
heroku config:set AWS_BUCKET_NAME=<bucket-name>
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

3. Open `django/app_info.json`
    + Double check that your `heroku_app_name`, `heroku_remote_name`, `branch_name` (this refers to your local branch), and `DJANGO_SETTINGS_MODULE` configs are all correct.

### 5. Deploy

```bash
# See: Makefile for exact script

# Kill your asset watch if it's running
# Re-run the watch __after__ deploy
make heroku.deploy ENV_NAME=<prod|staging|deploy>
```

> __Note:__ Grab your heroku email / password and wait for the Heroku login prompt.

After the deploy completes successfully, type `heroku go` to open the app in your default browser.

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

### Generate a `SECRET_KEY` value

Run:
```bash
make shell
python manage.py gen_secret_key

# Copy the output a value to the console
```

### Useful Heroku Buildpacks

* https://github.com/piotras/heroku-buildpack-gettext.git (required if you're using Django I81N)
* https://github.com/cyberdelia/heroku-geo-buildpack.git (required if you're using any Geo-Django features)
