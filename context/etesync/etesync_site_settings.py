import os

BASE_DIR = os.environ.get('BASE_DIR', '/etesync')

DEBUG = bool(os.environ.get('DEBUG', False))

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('DATA_DIR', os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}

ALLOWED_HOSTS = os.environ.get('DJANGO_HOSTS','*').split(',')

LANGUAGE_CODE = os.environ.get('DJANGO_LC','en-us')

USE_TZ = os.environ.get('USE_TZ', False)

TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

SECRET_FILE = os.environ.get('SECRET_FILE')
