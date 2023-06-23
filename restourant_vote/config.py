import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = bool(os.environ.get('DEBUG'))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()

APP_PORT = os.environ.get('APP_PORT')

POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
