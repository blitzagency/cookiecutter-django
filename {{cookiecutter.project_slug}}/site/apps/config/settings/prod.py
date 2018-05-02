'''Production settings and globals.'''

from .base import *  # noqa F402


# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

ALLOWED_HOSTS += ('.herokuapp.com',)  # noqa F405
SECRET_KEY = env('SECRET_KEY')  # noqa F405

INSTALLED_APPS += (  # noqa F405
    'gunicorn',
    'storages',
)

DATABASES['default']['ENGINE'] = 'django_postgrespool'  # noqa F405
DATABASE_POOL_ARGS = {
    'max_overflow': 7,
    'pool_size': 7,
    'recycle': 300,
}


# Staticfiles
# =====================================

{% if cookiecutter.use_aws.lower() == 'y' -%}
DEFAULT_FILE_STORAGE = 'apps.utils.storage.MediaRootS3BotoStorage'
ASSET_PROTOCOL = 'https' if USE_HTTPS_FOR_ASSETS else 'http'  # noqa F405

# THIS IS VERY IMPORTANT TO MAKE COMPRESSOR WORK!!!!!!
ASSET_PORT = ':443' if USE_HTTPS_FOR_ASSETS else ''  # noqa F405

STATIC_URL = '{}://{}.s3.amazonaws.com{}/'.format(ASSET_PROTOCOL, AWS_STORAGE_BUCKET_NAME, ASSET_PORT)  # noqa F405
MEDIA_URL = '{}://{}.s3.amazonaws.com/uploads/'.format(ASSET_PROTOCOL, AWS_STORAGE_BUCKET_NAME)  # noqa F405

if ASSET_VERSION:  # noqa F405
    # set path of assets in s3 bucket, note this is '' by default
    AWS_LOCATION = '%s/' % ASSET_VERSION  # noqa F405
    STATIC_URL += AWS_LOCATION
{%- else -%}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
{%- endif %}

EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')  # noqa F405
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')  # noqa F405
EMAIL_PORT = env('EMAIL_PORT', default=587)  # noqa F405
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='your_email@example.com')  # noqa F405
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')  # noqa F405
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME  # noqa F405
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'ratelimit': {
            '()': 'apps.utils.error_ratelimit_filter.RateLimitFilter',
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
            'class': 'apps.utils.log.SlackHandler',
            'formatter': 'verbose',
        },
    },

    'loggers': {
        '': {
            'handlers': ['slack', 'stream', ],
            'level': LOG_LEVEL,  # noqa F405
            'propagate': False,
        },
        'django.db': {
            'handlers': ['slack', 'stream', ],
            'level': LOG_LEVEL,  # noqa F405
            'propagate': False,
        },
        'z.pool': {
            'handlers': ['slack', 'stream', ],
            'level': LOG_LEVEL,  # noqa F405
            'propagate': False,
        },
        'django': {
            'handlers': ['slack', 'stream', ],
            'propagate': False,
        },
    }
}

# -------------------------------------
# VENDOR CONFIGURATION
# -------------------------------------

AWS_HEADERS = {
    'Cache-Control': 'max-age=31536000',
}
