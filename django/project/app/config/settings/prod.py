from os.path import join, normpath
from os import getenv
import dj_database_url
from os import environ
from .base import *


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost'),
}

DATABASES['default']['ENGINE'] = 'django_postgrespool'

DATABASE_POOL_ARGS = {
    'max_overflow': 7,
    'pool_size': 7,
    'recycle': 300,
}

# REDIS_HOST = getenv('REDISTOGO_URL', 'redis://localhost:6379')
# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# https://devcenter.heroku.com/articles/django-memcache#start-using-memcache
def get_cache():
    import os
    try:
        os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS']\
            .replace(',', ';')
        os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
        os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']

        return {
            'default': {
                'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
                'TIMEOUT': 500,
                'BINARY': True,
                'OPTIONS': {'tcp_nodelay': True}
            }
        }
    except:
        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
            }
        }

# uncomment this, and delete the next instance of CACHES to turn on memcachier
# which is a heroku plugin
# https://addons.heroku.com/memcachier?utm_campaign=category&utm_medium=dashboard&utm_source=addons
# CACHES = get_cache()
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# END CACHE CONFIGURATION


# TOOLBAR CONFIGURATION
# See:
# https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'gunicorn',
    'storages',
)

# See:
# https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)


# ALLOWED_HOSTS += ('example.com',)


# ######### LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'ratelimit': {
            '()': 'app.utils.error_ratelimit_filter.RateLimitFilter',
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(name)s %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'ratelimit'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'slack': {
            'level': 'ERROR',
            'class': 'app.project.apps.utils.log.SlackHandler',
            'formatter': 'verbose',
        },
    },

    'loggers': {
        '': {
            'handlers': ['slack', 'stream'],
            'level': 'WARNING',
            'propagate': False,
        },
        'sportlogos': {
            'handlers': ['slack', 'stream'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['slack', 'stream'],
            'level': 'WARNING',
            'propagate': False,
        },
        'z.pool': {
            'handlers': ['slack', 'stream'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django': {
            'handlers': ['slack', 'stream'],
            'propagate': False,
        },
    }
}
# ######### END LOGGING CONFIGURATION


# AWS settings
USE_HTTPS_FOR_ASSETS = False
AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID', '#####################')
AWS_SECRET_ACCESS_KEY = getenv(
    'AWS_SECRET_ACCESS_KEY', '########################################')
AWS_QUERYSTRING_AUTH = False
AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME = 'sportlogos-prod'
STATICFILES_STORAGE = 'app.utils.storage.OptimizedS3BotoStorage'
DEFAULT_FILE_STORAGE = "app.utils.storage.MediaRootS3BotoStorage"
ASSET_PROTOCOL = 'https' if USE_HTTPS_FOR_ASSETS else 'http'
STATIC_URL = '{}://{}.s3.amazonaws.com/'.format(
    ASSET_PROTOCOL, AWS_STORAGE_BUCKET_NAME)
MEDIA_URL = '{}://{}.s3.amazonaws.com/uploads/'.format(
    ASSET_PROTOCOL, AWS_STORAGE_BUCKET_NAME)


UPLOADCARE = {
    'pub_key': os.environ.get('UPLOADCARE_PUB_KEY',),
    'secret': os.environ.get('UPLOADCARE_SECRET_KEY',),
}


# Cloudfront
# STATIC_URL = "http://##############.cloudfront.net/"
# MEDIA_URL = "http://##############.cloudfront.net/uploads/"

# BOTO custom domain: cloudfront
# Note you do not need to include protocol or trailing slash
# AWS_S3_CUSTOM_DOMAIN = AWS_CLOUDFRONT_DOMAIN =
# "##############.cloudfront.net"


ASSET_VERSION = getenv("ASSET_VERSION")
if ASSET_VERSION:
    # set path of assets in s3 bucket, note this is '' by default
    AWS_LOCATION = '%s/' % ASSET_VERSION
    STATIC_URL += AWS_LOCATION

AWS_IS_GZIPPED = True

AWS_HEADERS = {
    'Cache-Control': 'max-age=31536000',
}

ALLOWED_HOSTS += ('.sportlogos.com', '.herokuapp.com', '*',)

SLACK_USER_NAME = 'Logger:PROD'
