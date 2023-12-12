#!/bin/bash

python -m pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
python manage.py makemigrations
python manage.py migrate
python manage.py create_superuser
python manage.py collectstatic --noinput
gunicorn tree_menu.wsgi:application --bind 0.0.0.0:8080