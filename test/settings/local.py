# -*- coding: utf-8 -*-
from test.settings.base import *

DEBUG = True
THUMBNAIL_DEBUG = True

# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'http://test-api.codebnb.me'
# CLIENT_BASE_URL = 'http://localhost:4200'
CLIENT_BASE_URL = 'http://test.codebnb.me'
ALLOWED_HOSTS = ['*', ]

BASE_PATH = "/var/www/test/"

THIRD_PARTY_APPS += [
    'debug_toolbar',
    'django_extensions',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + PROJECT_APPS


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'test_user',
        'PASSWORD': 'hi48hc8wvntewczg9rk9v787qiye5iqx',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

SENDER_EMAIL = 'info@test.codebnb.me'