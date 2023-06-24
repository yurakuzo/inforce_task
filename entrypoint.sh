#!/bin/sh

# Wait for postgresql to start
while ! nc -z db 5432; do
    sleep 0.1
done

# Run migrations
python3 manage.py migrate

# Collecting static files, at least for admin and rest-api pages
python3 manage.py collectstatic --noinput

exec gunicorn --bind 0.0.0.0:${APP_PORT} restourant_vote.wsgi
