serve: ## run django dev server
	python manage.py runserver 0.0.0.0:8000

killall:
	@ps ax | grep '[m]anage.py runserver' | awk '{ print $$1 }' | xargs kill -9
