import os

from .base import *


DEBUG = True

SECRET_KEY = '0#1wxzxch=()01rkem8evr5y6jlje4w#v-%yct$n2&14b6pi6='

ALLOWED_HOSTS = ['*']

# Database

DATABASES_DEFAULT = 'mysql://root:root@mysql57:3306/ingemax_auditoria'

DATABASES = {
    'default': dj_database_url.config(default=DATABASES_DEFAULT)
}

# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.ancestor(1).child('media')

MEDIA_URL = '/media/'