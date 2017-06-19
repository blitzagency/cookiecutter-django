# -------------------------------------
# DOCKERFILE
# -------------------------------------
# https://github.com/blitzagency/python-web
# https://hub.docker.com/r/blitzagency/python-web/

FROM blitzagency/python-web:3

# Build Args
# =====================================
# These are passed via the --build-arg flag during `docker build`
ARG ASSET_VERSION

# ENV Setup
# =====================================

# Single line form is preferred for caching
ENV PYTHONPATH=/usr/app/project:/usr/app/project/vendor \
    DJANGO_SETTINGS_MODULE=app.config.settings.prod

# File / Folder Setup
# ======================================

RUN mkdir -p /usr/app

# Install Dependencies
# =====================================

# Copy requirements before copying over all other files,
# preferred better caching, see:
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#add-or-copy
RUN mkdir -p /usr/app/requirements
COPY ./django/requirements/base.txt /usr/app/requirements/base.txt
COPY ./django/requirements/production.txt /usr/app/requirements/production.txt
COPY ./django/requirements.txt /usr/app
RUN pip install -r /usr/app/requirements.txt

# Asset Version
# =====================================
# Permanently embed ASSET_VERSION into container
# Separate from other ENV to avoid
# early / unintentional cache invalidation

ENV ASSET_VERSION=$ASSET_VERSION

# Copy Local Files
# =====================================
# Copy is (usually) preferred over Add, see:
#   https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#add-or-copy

COPY ./django/ /usr/app
WORKDIR /usr/app

# Copy env.build to .env temporarily for collect static
# NOTE: This overwrites any .env that may have been added from COPY above
RUN [ -f ./env.build ] || echo "Could not fine env.build"
RUN cp env.build .env

# Run Collect Static
# =====================================

RUN /usr/app/manage.py collectstatic --no-input

# We can get rid of .env now
# but leave env.build to keep as a build receipt.
RUN rm /usr/app/.env

# User Setup
# =====================================
# Recommended, run the image as non-root
# See: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#user

RUN adduser -D heroku
USER heroku

# Start the App
# =====================================
# CMD is required to run on Heroku
# $PORT is set by Heroku

CMD gunicorn app.config.wsgi --bind 0.0.0.0:$PORT -w 3 -k gevent
