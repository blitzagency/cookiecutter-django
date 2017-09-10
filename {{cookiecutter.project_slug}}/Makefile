# -------------------------------------
# MAKEFILE
# -------------------------------------

# Parse docker container name prefix from working dir
ifeq ($(OS),Windows_NT)
	NAME := $(notdir $(CURDIR))
	LOCATION := $(CURDIR)
else
	NAME := $(shell basename $$PWD | sed -e s/[-_\\.]//g)
	LOCATION := $(shell pwd -P)
endif

CONTAINER_NAME ?= "django"

# Project Commands
# =====================================

.DEFAULT_GOAL := help

.PHONY: up
up: ## Bring up all containers
	docker-compose -p ${NAME} up -d

.PHONY: init
init: envfile reqs.git reqs.py reqs.node init.django ## Initialize this project

.PHONY: serve
serve: ## Start development web server
	docker exec -it ${NAME}_django_1 python manage.py runserver 0.0.0.0:8000

.PHONY: assets
assets: ## Start static asset watch / compilation
	cd django/project/@static && npm start

.PHONY: envfile
envfile: ## copy over the .env file if it doesn't exist
	-cp -n django/env.dist django/.env

.PHONY: resetdb
resetdb: ## Reset Django / Postgres database
	docker exec -it ${NAME}_django_1 python manage.py reset_db --noinput

.PHONY: migrate
migrate: ## Runs Django makemigrations and migrate in a single command
	docker exec -it ${NAME}_django_1 python manage.py makemigrations
	docker exec -it ${NAME}_django_1 python manage.py migrate

.PHONY: po
po: ## Create / update po files
	docker exec -it ${NAME}_django_1 mkdir -p project/app/web/locale
	docker exec -it ${NAME}_django_1 python manage.py makemessages ${OPTS}

.PHONY: mo
mo: ## Compile all po -> mo files
	docker exec -it ${NAME}_django_1 python manage.py compilemessages ${OPTS}

.PHONY: shell
shell: ## Run a bash session on a container
	docker exec -it ${NAME}_django_1 /bin/bash

.PHONY: test.py
test.py: ## Run Python / Django test suite
	docker exec -it ${NAME}_django_1 pytest

.PHONY: test.js
test.js: ## Run Javascript test suite
	open http://localhost:3000
	cd django/project/\@static && npm test

.PHONY: reqs.git
reqs.git:
	-git submodule update --init --remote --recursive

.PHONY: reqs.py
reqs.py:
	docker exec -it ${NAME}_django_1 easy_install pdbpp
	docker exec -it ${NAME}_django_1 pip install -r requirements/local.txt

.PHONY: reqs.node
reqs.node:
	cd django/project/\@static && npm install

.PHONY: init.django
init.django: resetdb
	docker exec -it ${NAME}_django_1 python manage.py migrate
	docker exec -it ${NAME}_django_1 python manage.py createsuperuser

{% if cookiecutter.use_heroku.lower() == "y" %}
# Heroku Commands
# =====================================

ENV_NAME := dev
APP_NAME := {{cookiecutter.heroku_slug}}-$(ENV_NAME)

.PHONY: heroku.up
heroku.up: heroku.create heroku.s3 heroku.configure ## Create a Heroku app / remote for this project (see Usage)

# Create our Heroku app
.PHONY: heroku.create
heroku.create:
	heroku create ${APP_NAME} -r ${ENV_NAME}
	heroku addons:create heroku-postgresql:hobby-dev

# Set some boilerplate Heroku app configuration
.PHONY: heroku.configure
heroku.configure:
	heroku config:set DJANGO_SETINGS_MODULE=app.config.settings.prod
	heroku config:set SECRET_KEY=$$(docker exec -it ${NAME}_django_1 python manage.py gen_secret_key)
	heroku config:set USE_HTTPS_FOR_ASSETS=1
	heroku config:set AWS_BUCKET_NAME=${APP_NAME}
	@echo "NOTE: Be sure to set private credentials manually!"
	@echo "For example:"
	@echo "     - AWS_ACCESS_KEY_ID"
	@echo "     - AWS_SECRET_ACCESS_KEY"

# Create an S3 bucket for Heroku app static assets
# NOTE: Requires that the python aws cli is installed and that you're
# using the client's profile for the correct environment
# 	See: http://docs.aws.amazon.com/cli/latest/userguide/installing.html
.PHONY: heroku.s3
heroku.s3:
	wget -O cors.json http://bit.ly/blitzherokus3cors
	aws s3api create-bucket --bucket ${APP_NAME}
	aws s3api put-bucket-cors  --bucket ${APP_NAME} --cors-configuration file://cors.json
	-rm -rf cors.json

.PHONY: buildclean
buildclean:
	rm -rf django/.build

.PHONY: buildenv
buildenv: buildclean
	mkdir django/.build
	touch django/.build/.env
	echo "AWS_BUCKET_NAME=$$(heroku config:get AWS_BUCKET_NAME -a ${APP_NAME})" >>  django/.build/.env
	echo "AWS_ACCESS_KEY_ID=$$(heroku config:get AWS_ACCESS_KEY_ID -a ${APP_NAME})" >>  django/.build/.env
	echo "AWS_SECRET_ACCESS_KEY=$$(heroku config:get AWS_SECRET_ACCESS_KEY -a ${APP_NAME})" >>  django/.build/.env
	echo "SECRET_KEY=$$(heroku config:get SECRET_KEY -a ${APP_NAME})" >>  django/.build/.env
	# this is only here for reciept purposes
	echo "ASSET_VERSION=$$(git rev-parse HEAD)" >> django/.build/.env

# There's a lot going on here:
# 1. Generate a file called env.build for use during `docker build`
# 2. Build the new image based on docker/heroku/Dockerfile
# 3. Push the image to the heroku registry
# 4. Run migrate on the newly deployed / active container
.PHONY: heroku.deploy
heroku.deploy: heroku.assets buildenv
	docker build \
    --build-arg ASSET_VERSION=$$(git rev-parse HEAD) \
    . -f docker/heroku/Dockerfile -t registry.heroku.com/${APP_NAME}/web:latest
	docker push registry.heroku.com/${APP_NAME}/web
	# heroku run ./manage.py makemigrations -a ${APP_NAME}
	heroku run ./manage.py migrate -a ${APP_NAME}
	heroku run ./manage.py clear_cache -a ${APP_NAME}

# Exit if ENV_NAME does not match expected value
.PHONY: heroku.checkenv
heroku.checkenv:
	@if [[ ! $$ENV_NAME == "dev" ]]; then \
	if [[ ! $$ENV_NAME == "staging" ]]; then \
	if [[ ! $$ENV_NAME == "prod" ]]; then \
		echo "Invalid ENV_NAME=${ENV_NAME}, exiting..."; exit 1; \
	fi \
	fi \
	fi

# Build assets for the heroku deploy
# NOTE: You should cancel any active local asset watches
# 	and re-run them once the deploy is complete.
.PHONY: heroku.assets
heroku.assets:  ## Build Heroku assets (takes ENV_NAME=<env-name>, see help)
	-cd django/project/@static && \
		IS_HEROKU=1 VERSION=$$(git rev-parse HEAD) \
		USE_HTTPS_FOR_ASSETS=$$(heroku config:get USE_HTTPS_FOR_ASSETS -a ${APP_NAME}) \
		AWS_BUCKET_NAME=$$(heroku config:get AWS_BUCKET_NAME -a ${APP_NAME}) \
		npm run build

.PHONY: heroku.shell
heroku.shell: ## Get a session on the heroku container (takes ENV_NAME=<env-name>, see help)
	docker run --rm -w /usr/app/django \
		-v ${LOCATION}:/usr/app \
		--net ${NAME}_default \
		-e "DJANGO_SETTINGS_MODULE=app.config.settings.prod" \
		-e "PYTHONPATH=/usr/app/django/project:/usr/app/django/project/vendor" \
		-e "DEBUG=True" \
		-e "AWS_BUCKET_NAME=$$(heroku config:get AWS_BUCKET_NAME -a ${APP_NAME})" \
		-e "AWS_ACCESS_KEY_ID=$$(heroku config:get AWS_ACCESS_KEY_ID -a ${APP_NAME})" \
		-e "AWS_SECRET_ACCESS_KEY=$$(heroku config:get AWS_SECRET_ACCESS_KEY -a ${APP_NAME})" \
		-it dinopetrone/heroku:latest \
		/bin/bash
{% endif %}

# Makefile Documentation
# =====================================
# See: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.PHONY: help
help: help-commands help-usage help-examples ## This help dialog

.PHONY: help-commands
help-commands:
	@echo "\nCommands:"
	@grep -E '^[a-zA-Z._-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


# Update this target to add additional usage
.PHONY: help-usage
help-usage:
	@echo "\nUsage:"
	@echo "make <command> [Options...]"
	@echo "make shell"
	@echo "make po [OPTS=\"...\""]
	@echo "make mo [OPTS=\"...\""]
	@echo "make heroku.deploy ENV_NAME=<env-name>"
	@echo "make heroku.up HEROKU_REMOTE=<dev|staging|prod>"
	@echo "make heroku.deploy HEROKU_REMOTE=<dev|staging|prod>"

# Update this target to add additinoal examples
.PHONY: help-examples
help-examples:
	@echo "\nExamples:"
	@echo "make shell"
	@echo "make shell CONTAINER_NAME=postgres"
	@echo "make po OPTS=\"-l de -l es\""
	@echo "make po OPTS=\"-a\""
	@echo "make heroku.deploy ENV_NAME=dev"
	@echo "make heroku.up HEROKU_REMOTE=dev"
	@echo "make heroku.deploy HEROKU_REMOTE=dev"
	@echo ""

# Prompts Commands
# =====================================
# See: http://stackoverflow.com/a/14316012 (user confirmation snippet)

# Usage Example:
#
# .PHONY ask-message
# ask-messages:
# 	@echo "About to do a thing."
#
# .PHONY ask
# ask: ask-message confirm
# 	@echo "Did a thing!"
#

.PHONY: confirm
confirm:
	@while [ -z "$$CONTINUE" ]; do \
		read -r -p "Continue? [y/N] " CONTINUE; \
	done ; \
	if [ ! $$CONTINUE == "y" ]; then \
	if [ ! $$CONTINUE == "Y" ]; then \
		echo "Exiting." ; exit 1 ; \
	fi \
	fi
