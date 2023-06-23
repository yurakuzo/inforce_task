#!/bin/sh

# Wait for postgresql to start
while ! nc -z db 5432; do
    sleep 0.1
done

# Run migrations
python3 manage.py migrate

exec gunicorn --bind 0.0.0.0:${APP_PORT} restourant_vote.wsgi
