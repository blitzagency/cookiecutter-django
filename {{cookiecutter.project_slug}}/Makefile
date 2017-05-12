# Parse docker container name prefix from working dir
ifeq ($(OS),Windows_NT)
	NAME := $(notdir $(CURDIR))
	LOCATION := $(CURDIR)
else
	NAME := $(shell basename $$PWD | sed -e s/[\\.-_]//g)
	LOCATION := $(shell pwd -P)
endif

CONTAINER_NAME ?= "django"

# -------------------------------------
# Project Commands
# -------------------------------------

.DEFAULT_GOAL := help

.PHONY: up
up: ## Bring up all containers
	docker-compose -p ${NAME} up -d

.PHONY: init
init: reqs.git reqs.py reqs.node init.django ## Initialize this project

.PHONY: serve
serve: ## Start development web server
	docker exec -it ${NAME}_django_1 python manage.py runserver 0.0.0.0:8000

.PHONY: assets
assets: ## Start static asset watch / compilation
	cd django/project/@static && npm start

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
# Heroku
# =====================================

# FAB_CMD_ suffix are lowercase on purpose to ease passing ENV option
FAB_CMD_dev := fab dev.deploy -f /usr/fabfile
FAB_CMD_staging := fab staging.deploy -f /usr/fabfile
FAB_CMD_prod := fab prod.deploy -f /usr/fabfile
ENV_NAME := dev

# Deploy to Heroku (takes ENV_NAME=<env-name>, see help)
# AWS_BUCKET_NAME is required for the `collectstatic` run
# (each env requires it's own s3 buicket, see docs/heroku-setup.md)
.PHONY: heroku.deploy
heroku.deploy: heroku.checkenv heroku.assets ## Deploy to Heroku (takes ENV_NAME=<env-name>, see help)
	docker run --rm -w /usr/app/django \
		-v ${LOCATION}:/usr/app \
		--net ${NAME}_default \
		-e "DJANGO_SETTINGS_MODULE=app.config.settings.prod" \
		-e "PYTHONPATH=/usr/app/django/project:/usr/app/django/project/vendor" \
		-e "DEBUG=True" \
		-e "AWS_BUCKET_NAME=$$(heroku config:get AWS_BUCKET_NAME -r ${ENV_NAME})" \
		-e "AWS_ACCESS_KEY_ID=$$(heroku config:get AWS_ACCESS_KEY_ID -r ${ENV_NAME})" \
		-e "AWS_SECRET_ACCESS_KEY=$$(heroku config:get AWS_SECRET_ACCESS_KEY -r ${ENV_NAME})" \
		-it dinopetrone/heroku:latest \
		$(FAB_CMD_$(ENV_NAME))

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

.PHONY: heroku.assets
heroku.assets:  ## Build Heroku assets (takes ENV_NAME=<env-name>, see help)
	cd django/project/@static && \
		IS_HEROKU=1 VERSION=$$(git rev-parse HEAD) \
		USE_HTTPS_FOR_ASSETS=$$(heroku config:get USE_HTTPS_FOR_ASSETS -r ${ENV_NAME}) \
		AWS_BUCKET_NAME=$$(heroku config:get AWS_BUCKET_NAME -r ${ENV_NAME}) \
		npm run build

.PHONY: heroku.shell
heroku.shell: ## Get a session on the heroku container (takes ENV_NAME=<env-name>, see help)
	docker run --rm -w /usr/app/django \
		-v ${LOCATION}:/usr/app \
		--net ${NAME}_default \
		-e "DJANGO_SETTINGS_MODULE=app.config.settings.prod" \
		-e "PYTHONPATH=/usr/app/django/project:/usr/app/django/project/vendor" \
		-e "DEBUG=True" \
		-e "AWS_BUCKET_NAME=$$(heroku config:get AWS_BUCKET_NAME -r ${ENV_NAME})" \
		-e "AWS_ACCESS_KEY_ID=$$(heroku config:get AWS_ACCESS_KEY_ID -r ${ENV_NAME})" \
		-e "AWS_SECRET_ACCESS_KEY=$$(heroku config:get AWS_SECRET_ACCESS_KEY -r ${ENV_NAME})" \
		-it dinopetrone/heroku:latest \
		/bin/bash

{% endif %}

# -------------------------------------
# Makefile Documentation
# -------------------------------------
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

# Update this target to add additinoal examples
.PHONY: help-examples
help-examples:
	@echo "\nExamples:"
	@echo "make shell"
	@echo "make shell CONTAINER_NAME=postgres"
	@echo "make po OPTS=\"-l de -l es\""
	@echo "make po OPTS=\"-a\""
	@echo "make heroku.deploy ENV_NAME=dev"
	@echo ""

# -------------------------------------
# Prompts
# -------------------------------------
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
