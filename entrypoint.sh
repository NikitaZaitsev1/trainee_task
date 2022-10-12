#!/bin/sh

echo "Waiting for db..."


while ! nc -z db 5432; do
  sleep 0.1
done

echo "DB started"

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000