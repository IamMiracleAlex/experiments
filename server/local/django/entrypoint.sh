#!/bin/sh


echo "Initializing postgres db..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "postgres database has initialized successfully"
fi


python manage.py migrate
python manage.py collectstatic --no-input

echo Starting the server.

python manage.py runserver

# exec "$@"