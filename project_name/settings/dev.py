from os import environ
from os.path import normpath
from .base import *

#######################
# Debug configuration #
#######################

DEBUG = True

##########################
# Database configuration #
##########################

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'db.sqlite3')

INSTALLED_APPS += (
    'coverage',
    'debug_toolbar',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0')
