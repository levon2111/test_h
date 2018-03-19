# -*- coding: utf-8 -*-
from test.settings.base import *

DEBUG = True
THUMBNAIL_DEBUG = True

BASE_URL = 'https://test.com/'
CLIENT_BASE_URL = 'https://companify_client.com/'
ALLOWED_HOSTS = ['*', ]

BASE_PATH = "/var/www/test"

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + PROJECT_APPS

STATIC_URL = 'https://test.com/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../collectstatic')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static"),
]

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
