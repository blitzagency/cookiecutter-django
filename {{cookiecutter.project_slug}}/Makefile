NAME := $(shell basename $$PWD | sed -e s/[\\.-_]//g)
CONTAINER_NAME ?= "django"
LOCATION := $(shell pwd -P)

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
	@echo "resetdb"

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

.PHONY: heroku.prod.deploy
heroku.prod.deploy: heroku.build.prod ## Deploy to heroku (prod)
	docker run --rm -w /usr/app/django \
		-v ${LOCATION}:/usr/app \
		--net ${NAME}_default \
		-e "DJANGO_SETTINGS_MODULE=app.config.settings.prod" \
		-e "PYTHONPATH=/usr/app/django/project:/usr/app/django/project/vendor" \
		-e "DEBUG=true" \
		-it dinopetrone/heroku:latest \
		fab prod.deploy -f /usr/fabfile

.PHONY: heroku.staging.deploy
heroku.staging.deploy: heroku.build.prod ## Deploy to heroku (staging)
	docker run --rm -w /usr/app/django \
		-v ${LOCATION}:/usr/app \
		--net ${NAME}_default \
		-e "DJANGO_SETTINGS_MODULE=app.config.settings.prod" \
		-e "PYTHONPATH=/usr/app/django/project:/usr/app/django/project/vendor" \
		-e "DEBUG=true" \
		-it dinopetrone/heroku:latest \
		fab staging.deploy -f /usr/fabfile

.PHONY: heroku.build.prod
heroku.build.prod:
	cd django/project/@static && IS_HEROKU=1 VERSION=$$(git rev-parse HEAD) USE_HTTPS_FOR_ASSETS=$$(heroku config:get USE_HTTPS_FOR_ASSETS) AWS_BUCKET_NAME=$$(heroku config:get AWS_BUCKET_NAME) npm run build

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
	docker exec -it ${NAME}_django_1 ./manage.py migrate
	docker exec -it ${NAME}_django_1 ./manage.py createsuperuser

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
	@echo "make sh"
	@echo "make po [OPTS=\"...\""]
	@echo "make mo [OPTS=\"...\""]

# Update this target to add additinoal examples
.PHONY: help-examples
help-examples:
	@echo "\nExamples:"
	@echo "make sh"
	@echo "make sh CONTAINER_NAME=postgres"
	@echo "make po OPTS=\"-l de -l es\""
	@echo "make po OPTS=\"-a\""
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
