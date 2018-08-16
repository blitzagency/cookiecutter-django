#!/bin/sh

python manage.py migrate
python manage.py clear_cache
