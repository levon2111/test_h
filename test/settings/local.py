# -*- coding: utf-8 -*-
from test.settings.base import *

DEBUG = True
THUMBNAIL_DEBUG = True

# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'https://demo-ticher.herokuapp.com/'
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
    'default': dj_database_url.config(
        default="postgres://zsiiagjgegwapv:fbcc173752b6366174ec1e413da13f3926dbd829f76ca607acb9b05e0877bc01@ec2-23-21-121-220.compute-1.amazonaws.com:5432/defp2enqgm72k8"
    )
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'test',
#         'USER': 'test_user',
#         'PASSWORD': 'hi48hc8wvntewczg9rk9v787qiye5iqx',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }
# }

SENDER_EMAIL = 'info@test.codebnb.me'


import django_heroku
django_heroku.settings(locals())

