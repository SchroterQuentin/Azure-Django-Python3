from os import environ
from os.path import normpath
from .base import *


############################
# Allowed hosts & Security #
############################

ALLOWED_HOSTS = [

]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'ssl')

#######################
# Debug configuration #
#######################

DEBUG = False


##########################
# Database configuration #
##########################

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3' # Add 'postgresql_psycopg2',
# 'mysql', 'django.db.backends.postgresql_psycopg2' or 'oracle'.
DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'db.sqlite3')

##############
# Secret key #
##############

SECRET_KEY = environ.get("SECRET_KEY")
