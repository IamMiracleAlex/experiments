import dj_database_url
import django_heroku

from .base import *


ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bidnamic',
    }
}

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

django_heroku.settings(locals())