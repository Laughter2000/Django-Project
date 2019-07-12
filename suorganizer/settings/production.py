# https://docs.djangoproject.com/en/1.8/topics/settings/
# https://docs.djangoproject.com/en/1.8/ref/settings/

import os

import dj_database_url

from .base import *

# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = 'l)zht&^pddidsyqe$+09%se1*ba2#b_q-!j0^v$(-3c-=-vmq4'


ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': dj_database_url.config(
		default='sqlite:///{}'.format(
			os.path.abspath(
				os.path.join(
					BASE_DIR, 'db.sqlite3'))),
	),

}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.django.CompressedManifestStaticFilesStorage'