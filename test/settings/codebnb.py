# -*- coding: utf-8 -*-
import rollbar
from test.settings.base import *

DEBUG = True
THUMBNAIL_DEBUG = True

CLIENT_BASE_URL = 'http://test.codebnb.me'
BASE_URL = 'http://test-api.codebnb.me'
ALLOWED_HOSTS = ['*', ]

BASE_PATH = "/var/www/subdomains/codebnb/companify_api/public_html"

THIRD_PARTY_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + PROJECT_APPS


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'companify_user',
        'PASSWORD': 'hi48hc8wvntewczg9rk9v787qiye5iqx',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

SENDER_EMAIL = 'info@test.codebnb.me'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@dined.codebnb.me'
EMAIL_HOST_PASSWORD = 'e9fe03746b87bc87a03017cdc95a30ad'
EMAIL_PORT = 2525


ROLLBAR = {
    'access_token': '76ddfec65d1d410ca1e951d45b7798a4',
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}
rollbar.init(**ROLLBAR)
