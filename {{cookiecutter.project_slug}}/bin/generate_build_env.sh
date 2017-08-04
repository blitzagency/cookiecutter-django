#!/usr/bin/env bash

# -------------------------------------
# GENERATE BUILD ENV
# -------------------------------------

# See: https://sipb.mit.edu/doc/safe-shell/
set -eu -o pipefail


# Documentation
# =====================================

run_help() {
cat <<EOT
generate_build_env.sh (v0.0.1) - Aubrey Taylor - http://github.com/blitzagency

Generate a build env file.
NOTE: This assumes it's being run from the PROJECT / REPO ROOT

Usage: generate_build_env <registry> <env>

Arguments
    regisrty     The container registry, valid values include:
                 heroku.
    env          Environment name, possible values:
                 dev, staging, prod.

Options:
    -h, --help      Print this help message
EOT
}

# Logging
# =====================================

# Simple log to stdout functions
#
# Example:
# if ! true; then
#   log_error "Ack! Was not true!"
#
# More Colors:
# - https://github.com/c00kiemon5ter/dotfiles/blob/master/.shell.colors.tput

log_error() {
    # red
    printf "$(tput setaf 1)x %s$(tput sgr0)\n" "$@"
}

# Argv Handling
# =====================================

TARGET_DIR=./django

if [[ ! -d $TARGET_DIR ]]; then
    log_error "./django could not be found, are you running this from the project root?"
    run_help
    exit 1
fi

# $# is number of args
if [[ $# == 0 || "$1" =~ (--help|-h) ]]; then
    log_error "No valid arguments"
    run_help
    exit
fi

if [[ "$1" == "heroku" ]]; then

    if [[ $# < 2 ]]; then
        log_error "Expects an env name"
        run_help
        exit 1
    fi

    BUILD_ENV=$TARGET_DIR/env.build
    HEROKU_REMOTE="$2"

    # Let's make sure git is configured
    if ! git rev-parse HEAD; then
        log_error "Failed to get latest revision, are you sure this is a git repository?"
        exit 1
    fi

    # Let's make sure heroku is configured
    if ! heroku config; then
        log_error "Heroku is unavailable or not configured"
        exit 1
    fi

    # Empty file if it exists
    # -f in `rm -f ...` will fail silently if file does not exist
    rm -f $BUILD_ENV
    touch $BUILD_ENV

    # Redirect some local info into a file
    # ASSET_VERISON and AWS_* vars are used for collectstatic during `docker build`
    echo "ASSET_VERSION=$(git rev-parse HEAD)" >> $BUILD_ENV
    echo "SECRET_KEY=$(heroku config:get SECRET_KEY -r $HEROKU_REMOTE)" >> $BUILD_ENV
    echo "AWS_BUCKET_NAME=$(heroku config:get AWS_BUCKET_NAME -r $HEROKU_REMOTE)" >>  $BUILD_ENV
    echo "AWS_ACCESS_KEY_ID=$(heroku config:get AWS_ACCESS_KEY_ID -r $HEROKU_REMOTE)" >>  $BUILD_ENV
    echo "AWS_SECRET_ACCESS_KEY=$(heroku config:get AWS_SECRET_ACCESS_KEY -r $HEROKU_REMOTE)" >>  $BUILD_ENV
    exit
fi

# If we got here, nothing matched so run help str
run_help

unset run_help log_error
