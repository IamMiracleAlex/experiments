#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input

echo Starting Gunicorn.

gunicorn mirapayments.wsgi:application --bind 0.0.0.0:8000 --workers 4