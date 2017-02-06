NAME := $(shell basename $$PWD | sed -e s/[\\.-]//g)

init: reqs resetdb nodeinit

nodeinit:
	cd django/project/@static && npm install

reqs:
	-docker exec -it ${NAME}_django_1 easy_install pdbpp
	docker exec -it ${NAME}_django_1 pip install -U -r requirements/local.txt

resetdb: ## resets django db
	docker exec -it ${NAME}_django_1 ./manage.py reset_db --noinput
	docker exec -it ${NAME}_django_1 ./manage.py migrate
	docker exec -it ${NAME}_django_1 ./manage.py createsuperuser

serve:
	docker exec -it ${NAME}_django_1 ./manage.py runserver 0.0.0.0:8000

test: test-django

test-django:
	docker exec -it ${NAME}_django_1 ./manage.py test

assets: ## start npm build/watch
	cd django/project/@static && npm start

shell: ## start docker shell
	docker exec -it ${NAME}_django_1 /bin/bash

up:
	docker-compose -f ./docker-compose.yml up -d
